"""
    자동 매매 (Upbit)
    QTCON
    https://github.com/youtube-jocoding/pyupbit-autotrade/blob/main/bitcoinAutoTradeWithSlack.py
"""

import os
import time
import datetime
import requests
import configparser
import pyupbit

# Slack 메세지 보내기
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel, "text": text}
    )

# 변동성 돌파 전략으로 매수 목표가 조회
def get_target_price(ticker, k):
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

# 시작 시간 조회
def get_start_time(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

# 15일 이동 평균선 조회
def get_ma15(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="day", count=15)
    ma15 = df['close'].rolling(15).mean().iloc[-1]
    return ma15

# 잔고 조회
def get_balance(coin):
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == coin:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0

# 현재가 조회
def get_current_price(ticker):
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]


# 로그인
config_filename = "config.ini"
current_path = os.path.dirname(__file__)

config = configparser.ConfigParser()
config.read(os.path.join(current_path,config_filename))

access = config.get("UPBIT", "access_key")
secret = config.get("UPBIT", "secret_key")
# print("access key: ", access)
# print("secret key: ", secret)
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 시작 메세지 슬랙 전송
myToken = config.get("SLACK", "token")
post_message(myToken,"#coin", "autotrade start")

c= "KRW-QTCON"

while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time(c)
        end_time = start_time + datetime.timedelta(days=1)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price(c, 0.5)
            ma15 = get_ma15(c)
            current_price = get_current_price(c)
            print("target_price: ", target_price, " / current_price ", current_price)
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order(c, krw*0.9995)
                    post_message(myToken,"#coin", c + " buy : " +str(buy_result))
        else:
            crp = get_balance(c)
            if crp > 58:
                sell_result = upbit.sell_market_order(c, crp*0.9995)
                post_message(myToken,"#coin", c + " sell : " +str(sell_result))
        time.sleep(1)
    except Exception as e:
        print(e)
        post_message(myToken,"#coin", e)
        time.sleep(1)


# 잔고조회
# print("XRP\t", upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
# print("BTC\t", upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
# print("QTCON\t", upbit.get_balance("KRW-QTCON"))     # KRW-XRP 조회
# print("KRW\t", upbit.get_balance("KRW"))         # 보유 현금 조회








slack_token = config.get("SLACK", "token")
post_message(slack_token, "#coin", "HelloWorld")


