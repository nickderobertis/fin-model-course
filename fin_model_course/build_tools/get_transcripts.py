import json
import os
from pathlib import Path
from typing import List

from pydantic import BaseModel
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

from build_tools.config import TRANSCRIPTS_FOLDER

if not os.path.exists(TRANSCRIPTS_FOLDER):
    os.makedirs(TRANSCRIPTS_FOLDER)


class TranscriptEntry(BaseModel):
    text: str
    start: float
    duration: float

    @property
    def hhmmss(self) -> str:
        seconds = self.start
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60

        return "%d:%02d:%02d" % (hour, minutes, seconds)

    @property
    def mmss(self) -> str:
        seconds = self.start
        minutes = seconds // 60
        seconds %= 60

        return "%02d:%02d" % (minutes, seconds)

    def to_html(self, include_hours: bool = False) -> str:
        if include_hours:
            timestamp = self.hhmmss
        else:
            timestamp = self.mmss
        return f'\t\t<li class="transcript-entry"><span class="transcript-timestamp">{timestamp}: </span>{self.text}</li>'


class Transcript(BaseModel):
    entries: List[TranscriptEntry]

    @property
    def max_start(self) -> float:
        return max([entry.start for entry in self.entries])

    def to_html(self) -> str:
        if self.max_start >= (60 * 60):
            include_hours = True
        else:
            include_hours = False

        entry_html = '\n'.join([entry.to_html(include_hours=include_hours) for entry in self.entries])
        return f'<div class="transcript"><ul class="transcript-entries">\n{entry_html}\n\t</ul></div>'


def get_all_transcripts(
    retreive_from_cache: bool = True,
    store_in_cache: bool = True,
    cache_folder: Path = TRANSCRIPTS_FOLDER,
) -> List[Transcript]:
    from lectures.config import get_lecture_groups

    lecture_groups = get_lecture_groups()
    transcripts: List[Transcript] = []
    for lg in lecture_groups:
        for lecture in lg.lectures:
            yt_id = lecture.youtube_id
            if not yt_id:
                print(
                    f"Skipping getting transcript for lecture {lecture.title} as has no YouTube ID"
                )
                continue
            try:
                transcript = get_transcript(
                    yt_id,
                    retreive_from_cache=retreive_from_cache,
                    store_in_cache=store_in_cache,
                    cache_folder=cache_folder,
                )
            except TranscriptsDisabled as e:
                print(e)
                continue
            transcripts.append(transcript)
    return transcripts


def get_transcript(
    youtube_id: str,
    retreive_from_cache: bool = True,
    store_in_cache: bool = True,
    cache_folder: Path = TRANSCRIPTS_FOLDER,
) -> Transcript:
    file_path = cache_folder / f"{youtube_id}.json"
    if retreive_from_cache and os.path.exists(file_path):
        transcript_raw = json.loads(file_path.read_text())
        print(f"Loading transcript for {youtube_id} from cache")
        transcript = Transcript(entries=transcript_raw["entries"])
    else:
        print(f"Fetching transcript for {youtube_id} from YouTube")
        transcript = _get_transcript(youtube_id)

    if store_in_cache:
        transcript_raw = transcript.dict()
        file_path.write_text(json.dumps(transcript_raw, indent=2))

    return transcript


def _get_transcript(youtube_id: str) -> Transcript:
    raw = YouTubeTranscriptApi.get_transcript(video_id=youtube_id)
    return Transcript(entries=raw)


if __name__ == "__main__":
    transcripts = get_all_transcripts()
