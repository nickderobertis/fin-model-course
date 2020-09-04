RST_HEADER_LEVELS = ['#', '*', '=', '-', '^', '"']


def header_rst(category: str, level: int) -> str:
    try:
        header_char = RST_HEADER_LEVELS[level - 1]
    except IndexError as e:
        raise ValueError(f'Invalid header level {level}') from e

    return '\n' + category + '\n' + header_char * (len(category) + 3) + '\n'