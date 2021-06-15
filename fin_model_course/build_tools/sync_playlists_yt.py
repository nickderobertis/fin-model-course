"""
Sync the playlists for lecture videos. Ensures there is one
per lecture series and that the lectures from that
series are added to the playlist.

Sample usage:

python -m build_tools.sync_playlists_yt
"""
from build_tools import yt_api
from lectures.config import get_lecture_groups

if __name__ == "__main__":
    youtube = yt_api.get_authenticated_service()
    existing_playlists = yt_api.get_all_playlists(youtube=youtube)

    lecture_groups = get_lecture_groups()
    for lg in lecture_groups:
        lg.update_youtube_playlist(existing_playlists=existing_playlists, youtube=youtube)

