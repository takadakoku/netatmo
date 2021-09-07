#! /usr/bin/env python3

import netatmo
import requests
# fetch data using ~/.netatmorc credentials
netatmo.fetch()

# credentials as parameters
ws = netatmo.WeatherStation( {
        'client_id': 'ここにclient_id',
        'client_secret': 'ここにclient_secret',
        'username': 'アカウントのユーザーネーム',
        'password': 'アカウントのパスワード',
        'device': 'MACアドレス' } )
ws.get_data()
rainfall_amount = ws.devices[0]["modules"][1]["dashboard_data"]["sum_rain_1"]
rainfall_amount = rainfall_amount

file = open("rain.conf", "r")
limit = float(file.read())

if rainfall_amount < limit:
	import requests

	# 発行されたトークン
	ACCESS_TOKEN = "LINE APIのアクセストークン"

	headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

	data = {
	    "message": f"降水量が{limit}mmを下回りました。"
            "160.251.43.41/netatmo/stop_rain_down.php"
	}

	requests.post(
	    "https://notify-api.line.me/api/notify",
	    headers=headers,
	    data=data,
	)

