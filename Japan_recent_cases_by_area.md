# 全国の感染状況の推移2（直近12週間・日次・地域別：陽性数）
データ元:  
厚生労働省「新型コロナウィルス感染症について」の[オープンデータ](https://www.mhlw.go.jp/stf/covid-19/open-data.html)で公開されている下記の3つのファイル：
- [新規陽性者数の推移（日別）](https://covid19.mhlw.go.jp/public/opendata/newly_confirmed_cases_daily.csv)
- [死亡者数（累積）](https://covid19.mhlw.go.jp/public/opendata/deaths_cumulative_daily.csv)
- [重症者数の推移](https://covid19.mhlw.go.jp/public/opendata/severe_cases_daily.csv)

から日本全国および県別の新規陽性数，新規死亡者数，重症者数を取得し，直近12週間の7日間移動平均(重症者数は実数）を地域別にプロット． 人数が大きくなれば対数プロットに切り替える．
## <a name="nc">新規陽性者数</a>
<a href="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-recent-cases_by_area.png"><img src="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-recent-cases_by_area.png" alt="Japan CoVid-19 recent daily cases" width="800" /></a>
## <a name="nd">新規死亡者数</a>
<a href="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-recent-deaths_by_area.png"><img src="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-recent-deaths_by_area.png" alt="Japan CoVid-19 recent daily death" width="800" /></a>
## 入院者数
<a href="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-recent-hospitalized_by_area.png"><img src="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-recent-hospitalized_by_area.png" alt="Japan CoVid-19 recent daily death" width="800" /></a>
## <a name="sc">重症者数</a>
<a href="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-recent-severe_cases_by_area.png"><img src="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-recent-severe_cases_by_area.png" alt="Japan CoVid-19 recent severe cases" width="800" /></a>
