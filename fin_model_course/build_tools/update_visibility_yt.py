"""
Update the visibility for lecture video(s).

Note: This script was added to change the lab exercise
solutions from unlisted to public. If teaching at a university
again, can expand this to set the visibility based on
models using publishAt as well

Sample usages:

All videos:
python -m build_tools.update_visibility_yt

Single video:
python -m build_tools.update_visibility_yt --video-id=<VIDEO_ID>
"""

import argparse

from build_tools import yt_api
from lectures.lab_exercises.main import get_lab_exercises_lecture

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--video-id", help="ID of video to update.")
    args = parser.parse_args()

    youtube = yt_api.get_authenticated_service()

    lecture_groups = [get_lab_exercises_lecture()]
    for lg in lecture_groups:
        for lect in lg.lectures:
            if (args.video_id and lect.youtube_id == args.video_id) or not args.video_id:
                print(f'Making lecture {lect.youtube_id} - {lect.title} visible')
                yt_api.update_video_visibility(
                    lect.youtube_id,
                    yt_api.VideoVisibility.PUBLIC,
                    youtube=youtube,
                    print_output=False
                )

