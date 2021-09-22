#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import datetime as dt
url = "https://www.pref.miyagi.jp/pdf/covid19/m-covid-kanja.xlsx"
df = pd.read_excel(url, sheet_name="患者状況一覧（HP掲載）", index_col=0)
last_update = pd.to_datetime(df.iloc[0,:].index[-1])
last_update = dt.datetime(last_update.year, last_update.month, last_update.day, 9, 0, 0)
last_update_str = last_update.strftime("%Y%m%d_%H%M")
df.columns = df.iloc[1,:]
df.index.name=""
df = df[2:]
df = df[df["公表_年月日"] != "欠番"]
def to_dt(x):
    if x not in ["調査中", "非公表", "不明"]:
        return pd.to_datetime(x)
    else:
        return x
for col in ["公表_年月日", "患者_発症日", "陽性判明_年月日"]:
    df[col].apply(to_dt)
df.to_csv("data/resources/CoVid19-Miyagi-patients-{}.csv".format(last_update_str), encoding='utf-8')
df.to_csv("data/CoVid19-Miyagi-patients.csv", encoding='utf-8')
