from typing import Union

import pandas as pd
from pandas.io.formats.style import Styler


def get_df_from_df_or_styler(df_or_sty: Union[pd.DataFrame, Styler]) -> pd.DataFrame:
    if isinstance(df_or_sty, Styler):
        return df_or_sty.data
    if isinstance(df_or_sty, pd.DataFrame):
        return df_or_sty

    raise ValueError(f'got inproper type, should be DataFrame or Styler, got {type(df_or_sty)}')