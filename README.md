# 雨量通知システム

2021年5月に某工事会社に雨量計とこのシステムをセットで貸すために開発しました。

雨量計はNetatmo Weather Stationを使用しました。(下記参照)

https://www.netatmo.com/en-eu/weather/weatherstation

APIはLINE API, Netatmo APIを使用しています。(下記参照)

LINE API =>

Netatmo API => https://dev.netatmo.com/apidocumentation/weather

システムの簡単な概要としては、一時間辺りの降水量が設定雨量を超えるとラインに通知するというものです。後半で詳しく説明しています。



# 主要なファイル

・setting.php

・stop_rain_down.php

・stop_rain_up.php

・rain_down.py

・rain_up.py

・rain.conf

・call.sh

# 説明


setting.phpで任意の雨量値を設定する→
