#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import datetime as dt
from itertools import product
import re
# 新しいデータを取得
url = "https://www.kantei.go.jp/jp/content/nenreikaikyubetsu-vaccination_data.xlsx"
#df_ratio = pd.read_excel(url, sheet_name="様式", header=3, index_col=0).iloc[:2,:]
latest_date = pd.read_excel(url, sheet_name="様式", header=None, index_col=None).iat[2,11]
df_num = pd.read_excel(url, sheet_name="様式", header=8, index_col=0).iloc[:3,:].astype(int)
latest_dt = dt.datetime(dt.datetime.today().year, *np.array(re.search("(\d+)月(\d+)日", latest_date).groups()).astype(int))
latest_dt_str = latest_dt.strftime("%Y/%m/%d")
ndf = pd.DataFrame(df_num.values.T.reshape(1,df_num.values.size),columns=pd.MultiIndex.from_tuples(product(df_num.columns,df_num.index)), index=[latest_dt_str]).astype(int)
# 既存のデータを取得
data_fname = "data/CoVid19-Japan-vaccine_by_age.csv"
orig_df = pd.read_csv(data_fname, index_col=0, header=[0,1])
# 新データの日付が既存データに含まれていなかったら，データを追加してファイルを更新
if latest_dt_str not in orig_df.index:
    df = pd.concat([ndf, orig_df])
    df.to_csv(data_fname)
