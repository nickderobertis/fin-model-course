import sys
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


def get_authenticated_service():
    """
    Authorize the request and store authorization credentials.
    :return: YouTube api object
    """
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)


class VideosSnippet(TypedDict):
    title: str
    description: str
    tags: List[str]


class VideoResponse(TypedDict):
    snippet: VideosSnippet


class VideosListResponse(TypedDict):
    items: List[VideoResponse]


def update_video(video_id: str, title: Optional[str] = None, description: Optional[str] = None,
                 tags: Optional[Sequence[str]] = None, youtube: Optional = None):
    if youtube is None:
        youtube = get_authenticated_service()

    # Call the API's videos.list method to retrieve the video resource.
    videos_list_response: VideosListResponse = (
        youtube.videos().list(id=video_id, part="snippet").execute()
    )

    # If the response does not contain an array of 'items' then the video was
    # not found.
    if not videos_list_response["items"]:
        print('Video "%s" was not found.' % video_id)
        sys.exit(1)

    # Since the request specified a video ID, the response only contains one
    # video resource. This code extracts the snippet from that resource.
    videos_list_snippet: VideosSnippet = videos_list_response["items"][0]["snippet"]

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


