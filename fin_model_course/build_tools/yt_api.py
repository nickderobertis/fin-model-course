import sys
from enum import Enum
from pathlib import Path
from typing import Optional, Sequence, TypedDict, List

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow


# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# the {{ Google Cloud Console }} at
# {{ https://cloud.google.com/console }}.
# Please ensure that you have enabled the YouTube Data API for your project.
# For more information about using OAuth2 to access the YouTube Data API, see:
#   https://developers.google.com/youtube/v3/guides/authentication
# For more information about the client_secrets.json file format, see:
#   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
CLIENT_SECRETS_FILE = Path(__file__).parent / "client_secret.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account.
SCOPES = ["https://www.googleapis.com/auth/youtube"]
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"


class YouTubeDescriptionIsCurrentException(Exception):
    pass


class YouTubeIDDoesNotExistException(Exception):
    pass


class YouTubePlaylistExistsException(Exception):
    pass


def get_authenticated_service():
    """
    Authorize the request and store authorization credentials.
    :return: YouTube api object
    """
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)


class VideoVisibility(str, Enum):
    PUBLIC = 'public'
    UNLISTED = 'unlisted'
    PRIVATE = 'private'


class VideoSnippet(TypedDict):
    title: str
    description: str
    tags: List[str]


class VideoStatus(TypedDict):
    privacyStatus: VideoVisibility


class VideoResponse(TypedDict):
    snippet: Optional[VideoSnippet]
    status: Optional[VideoStatus]


class VideosListResponse(TypedDict):
    items: List[VideoResponse]


def _get_video_response(video_id: str, part: str, youtube: Optional = None) -> VideosListResponse:
    if youtube is None:
        youtube = get_authenticated_service()

    # Call the API's videos.list method to retrieve the video resource.
    videos_list_response: VideosListResponse = (
        youtube.videos().list(id=video_id, part=part).execute()
    )

    # If the response does not contain an array of 'items' then the video was
    # not found.
    if not videos_list_response["items"]:
        raise YouTubeIDDoesNotExistException('Video "%s" was not found.' % video_id)

    return videos_list_response


def update_video_description(video_id: str, title: Optional[str] = None, description: Optional[str] = None,
                             tags: Optional[Sequence[str]] = None, youtube: Optional = None,
                             print_output: bool = True):
    if youtube is None:
        youtube = get_authenticated_service()

    videos_list_response = _get_video_response(video_id, 'snippet', youtube=youtube)

    # Since the request specified a video ID, the response only contains one
    # video resource. This code extracts the snippet from that resource.
    videos_list_snippet: VideoSnippet = videos_list_response["items"][0]["snippet"]

    # Set video title, description, default language if specified in args.
    if title:
        videos_list_snippet["title"] = title
    if description:
        videos_list_snippet["description"] = description

    # Preserve any tags already associated with the video. If the video does
    # not have any tags, create a new array. Append the provided tag to the
    # list of tags associated with the video.
    if "tags" not in videos_list_snippet:
        videos_list_snippet["tags"] = []
    if tags:
        videos_list_snippet["tags"] = list(tags)

    # Update the video resource by calling the videos.update() method.
    videos_update_response = (
        youtube.videos()
        .update(
            part="snippet", body=dict(snippet=videos_list_snippet, id=video_id)
        )
        .execute()
    )

    if print_output:
        print(
            "The updated video metadata is:\n"
            + "Title: "
            + videos_update_response["snippet"]["title"]
            + "\n"
        )
        if "description" in videos_update_response['snippet'] and videos_update_response["snippet"]["description"]:
            print("Description: " + videos_update_response["snippet"]["description"] + "\n")
        if 'tags' in videos_update_response["snippet"] and videos_update_response["snippet"]["tags"]:
            print("Tags: " + ",".join(videos_update_response["snippet"]["tags"]) + "\n")


def update_video_visibility(video_id: str, visibility: VideoVisibility, youtube: Optional = None,
                            print_output: bool = True):
    if youtube is None:
        youtube = get_authenticated_service()

    videos_list_response = _get_video_response(video_id, 'status', youtube=youtube)

    # Since the request specified a video ID, the response only contains one
    # video resource. This code extracts the snippet from that resource.
    video_status: VideoStatus = videos_list_response["items"][0]["status"]

    video_status['privacyStatus'] = visibility.value

    # Update the video resource by calling the videos.update() method.
    videos_update_response = (
        youtube.videos()
        .update(
            part="status", body=dict(status=video_status, id=video_id)
        )
        .execute()
    )

    if print_output:
        print(videos_update_response)


class PlaylistSnippet(TypedDict):
    title: str
    description: str


class PlaylistResponse(TypedDict):
    id: str
    snippet: PlaylistSnippet


class PlaylistListResponse(TypedDict):
    items: List[PlaylistResponse]


def add_playlist(title: str, description: str, visibility: VideoVisibility = VideoVisibility.PUBLIC,
                 youtube: Optional = None, print_output: bool = True):
    if youtube is None:
        youtube = get_authenticated_service()

    body = dict(
        snippet=dict(
            title=title,
            description=description
        ),
        status=dict(
            privacyStatus=visibility.value
        )
    )

    playlists_insert_response = youtube.playlists().insert(
        part='snippet,status',
        body=body
    ).execute()

    if print_output:
        print('New playlist ID: %s' % playlists_insert_response['id'])


def get_all_playlists(youtube: Optional = None, print_output: bool = True) -> PlaylistListResponse:
    if youtube is None:
        youtube = get_authenticated_service()

    response: PlaylistListResponse = youtube.playlists().list(
        part="snippet,contentDetails",
        maxResults=25,
        mine=True
    ).execute()

    if print_output:
        print(f'Got {len(response["items"])} playlists:')
        for playlist in response['items']:
            print(playlist['snippet']['title'])

    return response


def add_playlist_if_needed(
    title: str, description: str, visibility: VideoVisibility = VideoVisibility.PUBLIC,
    existing_playlists: Optional[PlaylistListResponse] = None,
    youtube: Optional = None, print_output: bool = True
):
    if youtube is None:
        youtube = get_authenticated_service()

    if existing_playlists is None:
        existing_playlists = get_all_playlists(youtube=youtube, print_output=print_output)

    for playlist in existing_playlists['items']:
        match_title = playlist['snippet']['title']
        if match_title == title:
            raise YouTubePlaylistExistsException(title)

    add_playlist(title, description, visibility=visibility, youtube=youtube, print_output=print_output)
