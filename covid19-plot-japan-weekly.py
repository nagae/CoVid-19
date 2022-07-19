import numpy as np
import pandas as pd
import datetime as dt
from itertools import product
from matplotlib  import pyplot as plt
import japanize_matplotlib

path = 'data/CoVid19-Japan-weekly_patients_by_age.csv'
df = pd.read_csv(path, header=[0,1], index_col=0, parse_dates=[0])
df = df.sort_index(ascending=True)

fig, ax = plt.subplots(4,2,figsize=(12*2,9*4))
ax0, ax1, ax2, ax3, ax4, ax5, ax6, ax7 = ax[0,0], ax[0,1], ax[1,0], ax[1,1], ax[2,0], ax[2,1], ax[3,0], ax[3,1]
# 1行目
df["陽性者数"].loc[:,:"80歳以上"].diff().plot(kind='bar', stacked="True",ax=ax0)
ax0.set_xticklabels(df.index.strftime("%y-%m-%d").to_list())
ax0.set_title("a) 新規陽性者数(一週間あたり)")
df["死亡者数"].loc[:,:"80歳以上"].diff().plot(kind='bar', stacked="True", ax=ax1)
ax1.set_xticklabels(df.index.strftime("%y-%m-%d").to_list())
ax1.set_title("b) 新規死亡者数(一週間あたり)")
df1 = df["死亡者数"].loc[:,"合計"].diff().dropna()
ylim1 = df1[df1.index!=dt.datetime(2021,9,28)].max()
ax1.set_ylim((0,ylim1))
# 2行目
df["入院者数"].loc[:,:"不明等"].plot(kind='bar', stacked="True", ax=ax2)
ax2.set_xticklabels(df.index.strftime("%y-%m-%d").to_list())
ax2.set_title("c) 入院者数")
df["重症者数"].loc[:,:"不明等"].plot(kind='bar', stacked="True", ax=ax3)
ax3.set_xticklabels(df.index.strftime("%y-%m-%d").to_list())
ax3.set_title("d) 重症者数")
# 3行目
(df["入院者数"].loc[:,:"80歳以上"].cumsum()/df["陽性者数"].loc[:,:"80歳以上"]).plot(ax=ax4, xticks=df.index, rot=90)
ax4.set_xticklabels(df.index.strftime("%y-%m-%d").to_list())
ax4.set_title("e) 累積陽性者数あたりの述べ入院者数(人×週)")
ax4.set_xlim(df.index[0], df.index[-1])
(df["重症者数"].loc[:,:"80歳以上"].cumsum()/df["陽性者数"].loc[:,:"80歳以上"]).plot(ax=ax5, xticks=df.index, rot=90)
ax5.set_xticklabels(df.index.strftime("%y-%m-%d").to_list())
ax5.set_title("f) 累積陽性者数あたりの述べ重症者数(人×週)")
ax5.set_xlim(df.index[0], df.index[-1])
# 4行目
#(df["重症者数"].loc[:,:"80歳以上"]/df["入院者数"].loc[:,:"80歳以上"]).plot(ax=ax6, xticks=df.index, rot=90)
#ax6.set_xticklabels(df.index.strftime("%y-%m-%d").to_list())
#ax6.set_title("g) 入院者数に対する重症者数の比率")
#ax6.legend(loc="upper left")
#ax6.grid(axis='y')
#ax6.set_ylim((0,0.04))
#ax6.set_xlim(df.index[0], df.index[-1])

cases_reg=df["陽性者数"].loc[:,:"80歳以上"]/1e6
(df["死亡者数"].loc[:,:"80歳以上"]/cases_reg).plot(ax=ax6, xticks=df.index, rot=90)
ax6.set_xticklabels(df.index.strftime("%y-%m-%d").to_list())
ax6.set_title("g) 総陽性者100万人あたりの総死亡者数")
ax6.legend(loc="upper left")
ax6.grid(axis='y')
ax6.set_yscale('log')
ax6.set_yticklabels(["{:d}".format(int(n)) for n in ax6.get_yticks()])
ax6.set_xlim(df.index[0], df.index[-1])
#print(np.array(ax6.get_yticks()))
#print(ax6.get_yticklabels())

nc=df["陽性者数"].loc[:,:"80歳以上"][::-1].diff().dropna().astype(int).cumsum()[::-1]
nd=df["死亡者数"].loc[:,:"80歳以上"][::-1].diff().dropna().astype(int).cumsum()[::-1]
(nd/nc*1e6).plot(ax=ax7, xticks=df.index, rot=90)
ax7.set_xticklabels(df.index.strftime("%y-%m-%d").to_list())
ax7.set_title("h) 当該日以降の累積陽性者100万人あたりの累積死亡者数")
ax7.set_yscale('log')
ax7.grid(axis='y')
ax7.set_yticklabels(["{:d}".format(int(n)) for n in ax6.get_yticks()])
ax7.legend(loc='upper left')
ax7.set_xlim(df.index[0], df.index[-1])

fig.savefig("fig/CoVid19-Japan-patients_by_age.png", bbox_inches='tight')
print("Wrote: fig/CoVid19-Japan-patients_by_age.png")
#plt.show()
