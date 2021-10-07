
# 全国の感染状況の推移2（週次・年代別：患者数・死亡数・入院数・重症数）
## 注意 (2021.10.04)
**[2021年9月28日24時現在の発表](https://www.mhlw.go.jp/content/10906000/000837754.pdf)では，その[前週の発表](https://www.mhlw.go.jp/content/10906000/000835194.pdf)に比べて，死亡数が14,462人から17,409人へと大きく変化しています． ただし， 下記の理由から， これは *集計上の問題(集計遅れや集計方法の変更など)* であり， 突然多くの方が亡くなったことを意味しているものではないと思われます．：**
1. [「新型コロナウィルス感染症について/オープンデータ」](https://www.mhlw.go.jp/stf/covid-19/open-data.html)で報告されている，各都道府県の発表件数を積み上げた[日次データ](https://nagae.github.io/CoVid-19/Japan_cases_daily.html)では，こうした死亡数の急増は観測されていない．
2. [9月22日時点での発表](https://www.mhlw.go.jp/content/10906000/000835194.pdf)までは， 国内発生動向(速報値)における死亡数が[ 「新型コロナウィルス感染症について/オープンデータ/死亡者数（累積）」](https://covid19.mhlw.go.jp/public/opendata/deaths_cumulative_daily.csv)での報告数に比べて少なかった． (例えば， 9/22 での国内発生動向(速報値)の死亡数は 14,462名だが，オープンデータでは17,312名）．

## グラフの見方
データ元:  
厚生労働省 「新型コロナウイルス感染症について」の「[国内の発生状況など](https://www.mhlw.go.jp/stf/covid-19/kokunainohasseijoukyou.html)」および「[報道発表資料](https://www.mhlw.go.jp/stf/houdou/index.html)」「[新型コロナウイルス感染症に関する報道発表資料](https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000121431_00086.html)」で公開されている「新型コロナウイルス感染症の国内発生動向(例えば, [9/22 18時時点](https://www.mhlw.go.jp/content/10906000/000835194.pdf))」．

上記データはPDFとして毎週更新されている（過去データは「[報道発表資料](https://www.mhlw.go.jp/stf/houdou/index.html)」「[新型コロナウイルス感染症に関する報道発表資料](https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000121431_00086.html)」内に残っている）ので，各週について，年代別に
- 陽性者
- 死亡者
- 入院者
- 重症者
をPDFファイルから手入力したものを[こちら](https://github.com/nagae/CoVid-19/blob/main/data/CoVid19-Japan-weekly_patients_by_age.csv)に保存． ただし，年代について「不明」「調査中」あるいは「非公表」となっているものは総じて「不明等」とした．

以下の8つのグラフを出力している：
- 1段目:  
  - a) 新規陽性者数(1週間あたり)
  - b) 新規死亡者数(1週間あたり)
- 2段目：  
  - c) 入院者数
  - d)重症者数
- 3段目：  
  - e) 累積陽性者数あたりの述べ入院者数(*1)
  - f) 累積陽性者数あたりの述べ重症者数(*1)
  
  *1 ほぼ毎週報告される入院者/重症者を，当該週まで単純に合計したもの． 同じ患者が2週にわたって入院している場合は2名としてカウントされるので，累積入院者/重症者ではないことに注意．  
- 4段目：  
  - g) 入院者数に対する重症者の比率
  - h) 累積陽性者あたりの累積死亡者数(≒感染死亡率)


<a href="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-patients_by_age.png"><img src="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Japan-patients_by_age.png" alt="Japan CoVid-19 patients by age" width="800" /></a>
