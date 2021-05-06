"""
    잔고 조회
"""

import os
import configparser
import pyupbit

config_filename = "config.ini"
current_path = os.path.dirname(__file__)            # 현재 파일의 위치 반환

config = configparser.ConfigParser()
config.read(os.path.join(current_path,config_filename))

# c = config.items("CONNECT")
# print(c)

access = config.get("UPBIT", "access_key")
secret = config.get("UPBIT", "secret_key")
print("access key: ", access)
print("secret key: ", secret)


# 로그인
# access = ""          # 본인 값으로 변경
# secret = ""          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

# 잔고조회
print("XRP\t", upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print("BTC\t", upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print("QTCON\t", upbit.get_balance("KRW-QTCON"))     # KRW-XRP 조회
print("KRW\t", upbit.get_balance("KRW"))         # 보유 현금 조회

