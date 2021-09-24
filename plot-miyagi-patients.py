import numpy as np
import pandas as pd
import datetime as dt
from itertools import product
from matplotlib  import pyplot as plt
import japanize_matplotlib
df_url = "https://raw.githubusercontent.com/nagae/CoVid-19/main/data/CoVid19-Miyagi-daily_patients_by_age.csv"
df = pd.read_csv(df_url, header=[0,1], index_col=0)
df = df.set_index(pd.to_datetime(df.index))
latest_date = df.index[0]
latest_date_str = latest_date.strftime("%Y-%m-%d")
ages = ["10歳未満", "10代", "20代", "30代", "40代", "50代", "60代", "70代", "80代", "90歳以上"]
age_label = ["10-", "10代", "20代", "30代", "40代", "50代", "60代", "70代", "80代", "90+"]

########################################
fig, ax = plt.subplots(2,1,figsize=(18,12*2))
# 最初のグラフ
colors1 = []
for i in range(10):
    colors1 += ['C{}'.format(i)]*3
plot_df = df.T.loc[product(ages, ["入院中", "入院調整中", "療養中"])].fillna(0).astype(int).T[-1::-1]
plot_df.plot(kind='bar', stacked='True', ax=ax[0], color=colors1)
ax[0].set_title("宮城県-年代別患者数　(各年代について，色の薄い順に療養中，入院調整中,入院中)")
ax[0].grid(axis='y', zorder=1)
alphas = [1.0,0.75,0.5]
for pid,p in enumerate(ax[0].patches):
    p.set_alpha( alphas[ pid//len(plot_df) % 3])
h,l = ax[0].get_legend_handles_labels()
ax[0].legend(h[::3],age_label,loc="upper left")
ax[0].set_xticklabels(plot_df.index.strftime("%y-%m-%d").to_list())

# 2つめのグラフ
colors2 = []
for i in range(10):
    colors2 += ['C{}'.format(i)]
plot_df = df.T.loc[product(ages, ["入院中"])].fillna(0).astype(int).T[-1::-1]
ax[1].set_title("宮城県-年代別入院者数")
plot_df.plot(kind='bar', stacked='True', ax=ax[1], color=colors2)
ax[1].grid(axis='y', zorder=1)
h,l = ax[1].get_legend_handles_labels()
ax[1].legend(h,age_label,loc="upper left")
ax[1].set_xticklabels(plot_df.index.strftime("%y-%m-%d").to_list())


# グラフの保存
plt.savefig("fig/CoVid19-Miyagi-patients_by_age.png", bbox_inches="tight")

########################################
fig, ax = plt.subplots(2,1,figsize=(18,12*2))
# 最初のグラフ
colors1 = []
for i in range(10):
    colors1 += ['C{}'.format(i)]*3
colors2 = []
for i in range(10):
    colors2 += ['C{}'.format(i)]

# 3つめのグラフ
plot_df = df.T.loc[product(ages, ["入院中", "入院調整中", "療養中"])].fillna(0).astype(int).T[-1::-1]
plot_df.apply(lambda x: x/x.sum(), axis=1).plot(kind="bar",stacked="True",ax=ax[0],color=colors1)
ax[0].set_title("宮城県-患者の年代別比率 　(各年代について，色の薄い順に療養中，入院調整中,入院中)")
ax[0].grid(axis='y', zorder=1)
alphas = [1.0,0.75,0.5]
for pid,p in enumerate(ax[0].patches):
    p.set_alpha( alphas[ pid//len(plot_df) % 3])
h,l = ax[0].get_legend_handles_labels()
ax[0].legend(h[::3],age_label,loc="center left")
ax[0].set_xticklabels(plot_df.index.strftime("%y-%m-%d").to_list())

# 4つめのグラフ
plot_df = df.T.loc[product(ages, ["入院中"])].fillna(0).astype(int).T[-1::-1]
plot_df.apply(lambda x: x/x.sum(), axis=1).plot(kind="bar",stacked="True",ax=ax[1],color=colors2)
ax[1].set_title("宮城県-入院者の年代別比率")
ax[1].grid(axis='y', zorder=1)
h,l = ax[1].get_legend_handles_labels()
ax[1].legend(h, age_label, loc="center left")
ax[1].set_xticklabels(plot_df.index.strftime("%y-%m-%d").to_list())

# グラフの保存
plt.savefig("fig/CoVid19-Miyagi-patients_by_age_rate.png", bbox_inches="tight")
