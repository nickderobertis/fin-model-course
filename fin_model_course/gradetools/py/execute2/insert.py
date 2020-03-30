from dataclasses import dataclass
from typing import Sequence

@dataclass
class InsertConfig:
    insert_lines: Sequence[str]
    position: int = 0


def insert_lines_in_source(source: str, insert_configs: Sequence[InsertConfig]) -> str:
    source_lines = source.split('\n')
    lines_inserted = 0
    for config in insert_configs:
        to_insert = reversed(config.insert_lines)
        insert_position = config.position + lines_inserted  # adjust for previous inserts
        for line in to_insert:
            source_lines.insert(insert_position, line)
            lines_inserted += 1
    new_source = '\n'.join(source_lines)
    return new_source