#!/bin/bash

wget -O xray.zip https://github.com/XTLS/Xray-core/releases/download/v24.9.19/Xray-linux-64.zip
unzip ./xray.zip
chmod +x ./xray
wget -O config.json https://gist.githubusercontent.com/efrancis74/a07162d05beba30ce061ed898a3e3642/raw/config.json
sleep 5
nohup ./xray -c ./config.json >/dev/null 2>&1 &	
sleep 10
nohup streamlit run main.py --server.port 5000 >/dev/null 2>&1 &
