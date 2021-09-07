
#! /usr/bin/env python3

import netatmo

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
print(ws.devices)
