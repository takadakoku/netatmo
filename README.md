# 雨量通知システム

2021年5月に某工事会社に雨量計とこのシステムをセットで貸すために開発しました。

雨量計はNetatmo Weather Stationを使用しました。(下記参照)

https://www.netatmo.com/en-eu/weather/weatherstation

システムの簡単な説明としては、一時間辺りの降水量が設定値を超えるとラインに通知するというものです。

後半で各ファイルごとに詳しく説明しています。



## 使用したAPI

・LINE API

https://notify-bot.line.me/doc/ja/

・Netatmo API

https://dev.netatmo.com/apidocumentation/weather

## 使用したライブラリ

・lnetatmo

https://github.com/philippelt/netatmo-api-python


## 実行環境

Linux Ubuntu 18.04

## 概要

Cronなどを使い定期的にcall.shを実行します。

setting.phpで設定した値を雨量が超えるとLINEに通知が来ます。

メッセージに記載されているURLをクリックすると通知が止まります。

雨が治まり雨量が設定値を下回るとLINEに通知が来ます。

メッセージに記載されているURLをクリックすると通知が止まります。

## 主要ファイル

#### call.sh

rain_up.pyとrain_down.pyを同時に実行するためのコマンドが書かれたファイルです。

#### setting.php

雨量をブラウザからで設定する時に使うファイルです。ここで設定された雨量値はrain.confに書き込まれます。

#### rain.conf

ここに書き込まれた値をそれぞれのpythonファイルに渡し設定値を超えているか、下回ったかなど判定しLINEに通知をします。

#### rain_up.py (rwxrwxrwx)
              
このシステムを使う時、最初に動くファイルです。雨量が設定値を超えていればstop_rain_up.phpのURLとともにラインに通知します。

#### stop_rain_up.php

アクセスするとrain_up.pyのパーミッションが(---x--x--x)になり通知が止まります。

同時にrain_down.pyのパーミッションが(rwxrwxrwx)になります。

#### rain_down.py (---x--x--x)

雨量が設定値を下回るとLINEに通知します。

#### stop_rain_down.php

アクセスするとrain_down.pyのパーミッションが(---x--x--x)になり通知が止まります。

同時にrain_up.pyのパーミッションが(rwxrwxrwx)になります。

