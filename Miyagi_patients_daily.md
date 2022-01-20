# 宮城県の感染状況の推移（日次・年代別：患者数・入院数）
データ元:  
宮城県の[新型コロナウイルス感染症対策サイト](https://www.pref.miyagi.jp/site/covid-19/02.html)で公開されている[新型コロナウイルス感染症患者状況一覧表 [Excelファイル]　](https://www.pref.miyagi.jp/pdf/covid19/m-covid-kanja.xlsx)の「患者状況一覧(HP掲載)」シート．

各日について，欠番ではない全ての患者のうち「患者_療養状況」が「退院等」になっていないデータを年代別および「療養中」「入院調整中」「入院中」の別に集計．

上記データは毎日更新される（過去のデータは未公開）ので，「魚拓」を[ここ](https://github.com/nagae/CoVid-19/tree/main/data/resources)に保管すると同時に，[日次データ](https://github.com/nagae/CoVid-19/blob/main/data/CoVid19-Miyagi-daily_patients_by_age.csv)として記録したものを可視化している．

備考:
1. 2021年11月21日〜2022年1月17日までのデータは欠損（後日充填するかもしれないが)．
2. 9月21日以前のデータは[（非公式）宮城県新型コロナウイルス感染症対策サイト](https://github.com/code4shiogama/covid19-miyagi)のものを利用させていただいている． 完全な日次データではないため，ところどころ横軸の時系列が飛んでいることに注意（例えば，2021年9月17日から20日， 2021年7月30日から8月3日など)．

## 各日で報告されている年代別の患者数
- 上図: 全ての患者について，年代別に「療養中(淡)」「入院調整中(中濃)」「入院中(濃)」として積み上げた棒グラフ． 
- 下図: 入院中の患者を年代別に積み上げた棒グラフ．

<a href="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Miyagi-patients_by_age.png"><img src="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Miyagi-patients_by_age.png" alt="Miyagi by age" width="800"/></a>

## 各日で報告されている患者の年代別構成比率
上で作成したグラフの年代別の構成比率をプロットしたもの．
<a href="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Miyagi-patients_by_age_rate.png"><img src="https://github.com/nagae/CoVid-19/raw/main/fig/CoVid19-Miyagi-patients_by_age_rate.png" alt="Miyagi age rate" width="800"/></a>

