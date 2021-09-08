# 雨量通知システム

2021年5月に某工事会社に雨量計とこのシステムをセットで貸すために開発しました。

雨量計はNetatmo Weather Stationを使用しました。(下記参照)

https://www.netatmo.com/en-eu/weather/weatherstation

簡単な概要としては、一時間辺りの降水量が設定値を超えるとラインに通知するというものです。

後半で各ファイルごとに詳しく説明しています。



## 使用したAPI

・LINE API

https://notify-bot.line.me/doc/ja/

・Netatmo API

https://dev.netatmo.com/apidocumentation/weather

## 使用したライブラリ

・lnetatmo

https://github.com/philippelt/netatmo-api-python









## 主要ファイル

・call.sh

・setting.php

雨量をブラウザからで設定する時に使うファイルです。ここで設定された雨量値はrain.confに書き込まれます。

・rain.conf

ここに書き込まれた値をpythonファイルに渡し設定値を超えているか、下回ったかなど判定しLINEに通知をします。

・rain_up.py

このシステムを使う時に最初に動くファイルです。雨量が設定値を超えていればstop_rain_up.phpのURLとともにラインに通知します。

・stop_rain_up.php


・rain_down.py

・stop_rain_down.php

# 説明

あらかじめrain_down.pyのパーミッションを111にしておきCronを使い定期的にcall.shを実行します。

