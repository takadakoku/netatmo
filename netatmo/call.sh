#!/bin/bash
cd /var/www/html/netatmo/
python3 rain_up.py
python3 rain_down.py
python3 temperature_up.py
python3 temperature_down.py

