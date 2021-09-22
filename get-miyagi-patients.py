#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import datetime as dt
url = "https://www.pref.miyagi.jp/pdf/covid19/m-covid-kanja.xlsx"
all_patients_fname = "CoVid19-Miyagi-all_patients.csv"
daily_patients_fname = "CoVid19-Miyagi-daily_patients_by_age.csv"

df = pd.read_excel(url, sheet_name="患者状況一覧（HP掲載）", index_col=0)
last_update = pd.to_datetime(df.iloc[0,:].index[-1])
last_update = dt.datetime(last_update.year, last_update.month, last_update.day, 9, 0, 0)
last_update_str = last_update.strftime("%Y%m%d_%H%M")
df.columns = df.iloc[1,:]
df.index.name=last_update.strftime("%Y/%m/%d %H:%M")
df = df[2:]
df = df[df["公表_年月日"] != "欠番"]
def to_dt(x):
    if x not in ["調査中", "非公表", "不明"]:
        return pd.to_datetime(x)
    else:
        return x
for col in ["公表_年月日", "患者_発症日", "陽性判明_年月日"]:
    df[col].apply(to_dt)
df.to_csv("data/resources/{}-{}.csv".format(all_patients_fname, last_update_str), encoding='utf-8')
df.to_csv("data/{}".format(all_patients_fname), encoding='utf-8')

# もともとの日次年代別データ
df_url = 'https://raw.githubusercontent.com/nagae/CoVid-19/main/data/{}'.format(daily_patients_fname)
df = pd.read_csv(df_url, header=[0,1], index_col=0)
df = df.set_index(pd.to_datetime(df.index))

# 最近の患者データ
ages = ["10歳未満", "10代", "20代", "30代", "40代", "50代", "60代", "70代", "80代", "90歳以上"]
states = ["入院中", "入院調整中", "療養中", "合計"]
mult_cols = pd.MultiIndex.from_tuples(product(ages, states))
all_patients_df_url = 'https://raw.githubusercontent.com/nagae/CoVid-19/main/data/{}'.format(all_patients_fname)
all_patients_df = pd.read_csv(all_patients_df_url, index_col = 0, header=0)
latest_dt = pd.to_datetime(patient_df.index.name) # 最近の患者データの更新日
latest_dt = dt.datetime(latest_dt.year, last_dt.month, last_dt.day)

# 最近のデータがもともとのデータに反映されていない場合
if latest_dt not in df.index:
    new_row_df = pd.DataFrame(patient_df[ patient_df["患者_療養状況"] != "退院等"].groupby(["患者_年代", "患者_療養状況"]).count()["公表_年月日"]).T
    rdf = pd.DataFrame(columns=mult_cols, index = [latest_dt])
    for c in mult_cols:
        if c in new_row_df.columns:
            rdf.iloc[0][c] = new_row_df.iloc[0][c]
        else:
            rdf.iloc[0][c] = 0
    sum_df = rdf.T.groupby(level=0).sum()
    for age in ages:
        rdf.iloc[0][age, "合計"] = sum_df.loc[age].values[0]
    updated_df = pd.concat([rdf, df])
    updated_df.to_csv('data/{}'.format(daily_patients_fname))
