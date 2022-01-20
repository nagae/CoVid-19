# -*- coding: utf-8 -*-
import pandas as pd
import datetime as dt
from itertools import product
all_patients_fname = "CoVid19-Miyagi-all_patients"
daily_patients_fname = "CoVid19-Miyagi-daily_patients_by_age"
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
today = dt.date.today()-dt.timedelta(days=1)
today_str = today.strftime("%Y%m%d")
orig_df.to_csv("data/resources/{}-{}_0900.csv".format(all_patients_fname, today_str), encoding='utf-8')
orig_df.to_csv("data/{}.csv".format(all_patients_fname), encoding='utf-8')

# 最近の患者データ
ages = ["10歳未満", "10代", "20代", "30代", "40代", "50代", "60代", "70代", "80代", "90歳以上"]
states = ["入院中", "入院調整中", "療養中", "合計"]
mult_cols = pd.MultiIndex.from_tuples(product(ages, states))
df = orig_df[orig_df["患者_療養状況"] != "退院等"]
new_row_df = pd.DataFrame(df.groupby(["患者_年代", "患者_療養状況"]).count()["公表_年月日"]).T
rdf = pd.DataFrame(columns=mult_cols, index = [today])
for c in mult_cols:
    if c in new_row_df:
        rdf.iloc[0][c] = new_row_df.iloc[0][c]
    else:
        rdf.iloc[0][c] = 0
sum_df = rdf.T.groupby(level=0).sum()
for age in ages:
    rdf.iloc[0][age, "合計"] = sum_df.loc[age].values[0]
daily_df_url = 'data/{}.csv'.format(daily_patients_fname)
daily_df = pd.read_csv(daily_df_url, header=[0,1], index_col=0)
if today.strftime("%Y-%m-%d") not in daily_df.index:
    updated_df = pd.concat([rdf, daily_df])
    updated_df.to_csv('data/{}.csv'.format(daily_patients_fname))
    print("Wrote:\ndata/{}.csv".format(daily_patients_fname))
