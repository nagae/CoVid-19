import pandas as pd
import datetime as dt
all_patients_fname = "CoVid19-Miyagi-all_patients"
orig_df_url = "https://covid19.pref.miyagi.jp/data/patients-utf8.csv"
orig_df = pd.read_csv(orig_df_url, index_col=0)
orig_df = orig_df[orig_df["公表_年月日"] != "欠番"]
def to_dt(x):
    if x not in ["調査中", "非公表", "不明"]:
        return pd.to_datetime(x)
    else:
        return x
for col in ["公表_年月日", "患者_発症日", "患者_陽性判明日"]:
    orig_df[col].apply(to_dt)
today = dt.date.today()
today_str = today.strftime("%Y-%m-%d")
orig_df.to_csv("data/resources/{}-{}.csv".format(all_patients_fname, today_str), encoding='utf-8')
