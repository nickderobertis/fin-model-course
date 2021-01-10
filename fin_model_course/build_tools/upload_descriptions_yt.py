"""
Update the description for a lecture video. Will not update the
description if it already matches (by checking checked-in metadata,
not by checking YouTube). After running this script, gen_metadata
should be run to record the update in the repo.

Note: This is not currently run in the CI/CD process as it requires
a manual authorization in the browser. Be sure to run this locally
after adding new lectures.


Sample usages:

All videos:
python -m build_tools.upload_descriptions_yt

Single video:
python -m build_tools.upload_descriptions_yt --video-id=<VIDEO_ID>
"""

import argparse

from build_tools import yt_api
from lectures.config import get_lecture_groups

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--video-id", help="ID of video to update.")
    args = parser.parse_args()

    youtube = yt_api.get_authenticated_service()

    lecture_groups = get_lecture_groups()
    for lg in lecture_groups:
        for lect in lg.lectures:
            if (args.video_id and lect.youtube_id == args.video_id) or not args.video_id:
                try:
                    lect.upload_youtube_description(youtube=youtube)
                except yt_api.YouTubeDescriptionIsCurrentException as e:
                    print(str(e))

