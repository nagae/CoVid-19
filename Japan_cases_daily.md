# 全国の感染状況の推移1（日次・県別：陽性数・死亡数・入院数・重症数）
データ元:厚生労働省[「新型コロナウィルス感染症について」](https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000164708_00001.html)
1. [オープンデータ](https://www.mhlw.go.jp/stf/covid-19/open-data.html)
2. [療養状況等及び入院患者受入病床数等に関する調査について](https://www.mhlw.go.jp/stf/seisakunitsuite/newpage_00023.html)を整理した下記サイト:  
[CoVid-19 JAPAN新型コロナウィルス対策ダッシュボード](https://www.stopcovid19.jp/data/covid19japan_beds/all.csv)

- 新規陽性者数：[1] [新規陽性者数の推移（日別）](https://covid19.mhlw.go.jp/public/opendata/newly_confirmed_cases_daily.csv)
- 累積死亡者数：[1] [死亡者数（累積）](https://covid19.mhlw.go.jp/public/opendata/deaths_cumulative_daily.csv)
- 患者数：[1] [入院治療等を要する者等推移](https://covid19.mhlw.go.jp/public/opendata/requiring_inpatient_care_etc_daily.csv)
- 重症者数：[1] [重症者数の推移](https://covid19.mhlw.go.jp/public/opendata/severe_cases_daily.csv)
- 入院者数：[2] [入院者数](https://www.stopcovid19.jp/data/covid19japan_beds/all.csv)

日本全体および各県について，以下を片対数プロット：
- 累積陽性者数(青実線, 新規陽性数の累和として計算)
- 累積死亡者数(橙実線)
- 新規死亡者数(青領域，7日間移動平均)
- 新規死亡者数(橙領域，累積死亡数の差分の7日間移動平均)
- 患者数(緑点線，「累積陽性数」と「退院もしくは療養解除となった者」の差)
- 入院者数(赤点線)
- 重症者数(紫点線)

下記に注意：
- 県別グラフは，縦軸のスケールを最大の累積陽性数に合わせてある． 
- どのグラフも，縦軸の最小値を (1=10^0) としているため， 7日間平均などで1を下回っていると，見かけ上の数値がプロットされない．
- 入院者数は週次のため，直近の数日について表示されないことがある．

## 直近16週間
[[直近16週間](#直近16週間)][[全期間](#全期間)]

<a href="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-cases_by_pref-0-recent.png"><img src="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-cases_by_pref-0-recent.png" alt="Japan CoVid-19 daily situation" width="800" /></a>
<a href="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-cases_by_pref-1-recent.png"><img src="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-cases_by_pref-1-recent.png" alt="Japan CoVid-19 daily situation" width="800" /></a>
<a href="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-cases_by_pref-2-recent.png"><img src="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-cases_by_pref-2-recent.png" alt="Japan CoVid-19 daily situation" width="800" /></a>
<a href="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-cases_by_pref-3-recent.png"><img src="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-cases_by_pref-3-recent.png" alt="Japan CoVid-19 daily situation" width="800" /></a>

## 全期間
[[直近16週間](#直近16週間)][[全期間](#全期間)]

<a href="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-cases_by_pref-0.png"><img src="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-cases_by_pref-0.png" alt="Japan CoVid-19 daily situation" width="800" /></a>
<a href="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-cases_by_pref-1.png"><img src="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-cases_by_pref-1.png" alt="Japan CoVid-19 daily situation" width="800" /></a>
<a href="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-cases_by_pref-2.png"><img src="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-cases_by_pref-2.png" alt="Japan CoVid-19 daily situation" width="800" /></a>
<a href="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-cases_by_pref-3.png"><img src="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-cases_by_pref-3.png" alt="Japan CoVid-19 daily situation" width="800" /></a>
