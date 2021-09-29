# 全国の感染状況の推移1</br>（日次・県別：陽性数・死亡数・入院数・重症数）
データ元:  
厚生労働省「新型コロナウィルス感染症について」の[オープンデータ](https://www.mhlw.go.jp/stf/covid-19/open-data.html)で公開されている下記の4つのファイル：
- [新規陽性者数の推移（日別）](https://covid19.mhlw.go.jp/public/opendata/newly_confirmed_cases_daily.csv)
- [死亡者数（累積）](https://covid19.mhlw.go.jp/public/opendata/deaths_cumulative_daily.csv)
- [入院治療等を要する者等推移](https://covid19.mhlw.go.jp/public/opendata/requiring_inpatient_care_etc_daily.csv)
- [重症者数の推移](https://covid19.mhlw.go.jp/public/opendata/severe_cases_daily.csv)

から新規陽性数，累積死亡数，入院治療等を要する者(入院数), 重症者数を取得し，県ごとに集計．

日本全体および各県について，以下を片対数プロット：
- 累積陽性数(青実線, 新規陽性数の累和として計算)
- 累積死亡数(橙実線)
- 新規死亡数(青領域，7日間移動平均)
- 新規死亡数(橙領域，累積死亡数の差分の7日間移動平均)
- 入院数(緑点線)
- 重症数(紫点線)

下記に注意：
- 県別グラフは，縦軸のスケールを最大の累積陽性数に合わせてある． 
- どのグラフも，縦軸の最小値を (1=10^0) としているため， 新規死亡数の7日間平均が1を下回っていると，見かけ上の新規死亡数がプロットされない．

<a href="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-cases_by_pref-0.png"><img src="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-cases_by_pref-0.png" alt="Japan CoVid-19 daily situation" width="800" /></a>
<a href="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-cases_by_pref-1.png"><img src="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-cases_by_pref-1.png" alt="Japan CoVid-19 daily situation" width="800" /></a>
<a href="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-cases_by_pref-2.png"><img src="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-cases_by_pref-2.png" alt="Japan CoVid-19 daily situation" width="800" /></a>
<a href="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-cases_by_pref-3.png"><img src="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-cases_by_pref-3.png" alt="Japan CoVid-19 daily situation" width="800" /></a>
