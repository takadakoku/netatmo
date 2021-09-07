#! /usr/bin/env python3

import netatmo
import requests
# fetch data using ~/.netatmorc credentials
netatmo.fetch()

# credentials as parameters
ws = netatmo.WeatherStation( {
        'client_id': '60cc6422d6d93f4a332ba9f3',
        'client_secret': '0ihaipiUDdl89vVIxDrEvvTUI2pEOUvfOBa',
        'username': 'charon@toyocom.jp',
        'password': 'Higesan3+',
        'device': '70:ee:50:63:fb:a8' } )
ws.get_data()
rainfall_amount = ws.devices[0]["modules"][1]["dashboard_data"]["sum_rain_1"]

limit = 0.5


if rainfall_amount > limit:
	import requests

	# 発行されたトークン
	ACCESS_TOKEN = "1eN0evClmso8DeWgFF3XAspdisBa9MzYRa3bWJDobId"

	headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

	data = {
	    "message": f"1時間の降水量は{rainfall_amount}です。"
	}

	requests.post(
	    "https://notify-api.line.me/api/notify",
	    headers=headers,
	    data=data,
	)

