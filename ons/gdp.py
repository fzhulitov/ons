import pandas as pd
from io import StringIO

import ons

def get_gdp() -> pd.Series:
    jresp = ons.request_data.get_data_frame()
    df = pd.read_csv(StringIO(jresp), engine='python', encoding='utf-8',
                     usecols=["V4_1", "Time", "nuts", "sic-unofficial", "GrowthRate"],
                     dtype={"V4_1": float},
                     parse_dates=["Time"],
                     )
    dfuk = df[df['nuts'] == 'UK0']
    dfukat = dfuk[dfuk['sic-unofficial'] == 'A--T']
    dfukatgr = dfukat[dfukat['GrowthRate'] == 'Quarterly index']
    df = dfukatgr.iloc[:, [0, 1]]
    df.rename(columns={df.columns[1]: "date"}, inplace=True)
    df.rename(columns={df.columns[0]: "GDP"}, inplace=True)
    df.set_index("date", inplace=True)
    df.sort_index(ascending=True, inplace=True)
    s = df.squeeze()

    return s
