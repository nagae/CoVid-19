# 全国の感染状況の推移2（直近12週間・日次・地域別：陽性・死亡・入院・重症者・実効再生産数）
データ元:  
厚生労働省「新型コロナウィルス感染症について」の[オープンデータ](https://www.mhlw.go.jp/stf/covid-19/open-data.html)および[療養状況等及び入院患者受入病床数等に関する調査について](https://www.mhlw.go.jp/stf/seisakunitsuite/newpage_00023.html)
から日本全国および県別の新規陽性数，新規死亡者数，入院者数，重症者数を取得し，直近12週間の7日間移動平均(入院者数，重症者数は実数）を地域別にプロット． 人数が大きくなれば対数プロットに切り替える．

実効再生産数は，[国立感染症研究所](https://www.niid.go.jp/niid/ja/2019-ncov/2502-idsc/iasr-in/10465-496d04.html)で提案されている以下の式で計算した：
「t日の実効再生産数」=「(t-6)日〜t日の7日間新規感染者数」÷「(t-11)日〜(t-5)日の7日間新規感染者数」

## <a name="nc">新規陽性者数</a>
[[新規陽性者数]](#nc)|[[新規死亡者数]](#nd)|[[入院者数]](#hs)|[[重症者数]](#sc)|[[実効再生産数]](#rt)
<a href="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-recent-cases_by_area.png"><img src="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-recent-cases_by_area.png" alt="Japan CoVid-19 recent daily cases" width="800" /></a>

## <a name="nd">新規死亡者数</a>
[[新規陽性者数]](#nc)|[[新規死亡者数]](#nd)|[[入院者数]](#hs)|[[重症者数]](#sc)|[[実効再生産数]](#rt)
<a href="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-recent-deaths_by_area.png"><img src="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-recent-deaths_by_area.png" alt="Japan CoVid-19 recent daily death" width="800" /></a>

## <a name="hs">入院者数</a>
[[新規陽性者数]](#nc)|[[新規死亡者数]](#nd)|[[入院者数]](#hs)|[[重症者数]](#sc)|[[実効再生産数]](#rt)
<a href="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-recent-hospitalized_by_area.png"><img src="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-recent-hospitalized_by_area.png" alt="Japan CoVid-19 recent daily death" width="800" /></a>

## <a name="sc">重症者数</a>
[[新規陽性者数]](#nc)|[[新規死亡者数]](#nd)|[[入院者数]](#hs)|[[重症者数]](#sc)|[[実効再生産数]](#rt)
<a href="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-recent-severe_cases_by_area.png"><img src="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-recent-severe_cases_by_area.png" alt="Japan CoVid-19 recent severe cases" width="800" /></a>

## <a name="rt">実効再生産数</a>
[[新規陽性者数]](#nc)|[[新規死亡者数]](#nd)|[[入院者数]](#hs)|[[重症者数]](#sc)|[[実効再生産数]](#rt)
<a href="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-recent-Rt_by_area.png"><img src="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-recent-Rt_by_area.png" alt="Japan CoVid-19 recent Rt" width="800" /></a>
