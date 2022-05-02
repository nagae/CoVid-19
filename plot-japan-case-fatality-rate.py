# ある日以降の陽性数に対する死亡数をプロットする
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt, dates as mdates
import japanize_matplotlib
import datetime as dt

# 厚労省CSVを読込む
# 新規感染者
nc_day = pd.read_csv('https://covid19.mhlw.go.jp/public/opendata/newly_confirmed_cases_daily.csv')
nc_day["Date"] = pd.to_datetime(nc_day["Date"])
nc_day = nc_day.set_index("Date")
# 新規累積死亡者
nd_day = pd.read_csv("https://covid19.mhlw.go.jp/public/opendata/deaths_cumulative_daily.csv")
nd_day["Date"] = pd.to_datetime(nd_day["Date"])
nd_day = nd_day.set_index("Date").diff().dropna()
# 逆累積感染死亡率
tc = nc_day[::-1].cumsum()[::-1]["ALL"]
td = nd_day[::-1].cumsum()[::-1]["ALL"]
p = (td/tc).dropna() # 感染死亡率
z = 1.96
v = p*(1-p)/tc.loc[p.index]
lb = p-z*np.sqrt(v)
ub = p+z*np.sqrt(v)
fig, ax = plt.subplots(1,1,figsize=(8,6))
ax.fill_between(lb.index, lb*1e3, ub*1e3, color='green', alpha=0.3, label="95%CI")
ax.plot(p*1e3, lw=3)
ax.legend()
ax.set_ylabel("death per 1000 cases")
ax.set_title("ある日以降の陽性者1000人あたりの死亡数")
ax.grid(axis='y')
fig.savefig('fig/CoVid19-Japan-case_fatility_rate.png', bbox_inches='tight')

