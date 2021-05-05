"""
    https://youtu.be/5vofEMqMyGk
    https://github.com/sharebook-kr/book-cryptocurrency/blob/master/ch07/07_13.py

"""

import pyupbit
import numpy as np

# OHLCV(Open, High, Low, Close, Volume)로 당일 시가, 고가, 저가, 종가, 거래량에 대한 데이터
df = pyupbit.get_ohlcv("KRW-BTC", count=7)
#print(df)

# range(변동폭 * k) --> (고가-저가) * k값
df['range'] = (df['high'] - df['low']) * 0.5

# target(매수가), range 컬럼을 한칸씩 밑으로 내림
df['target'] = df['open'] + df['range'].shift(1)
#print(df)

# 수수료
# fee = 0.0032
fee = 0.0

# ror(수익율), np.where(조건문, 참, 거짓)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'] - fee,
                     1)

# 누적 곱 계산 --> 누적 수익률
df['hpr'] = df['ror'].cumprod()

# Draw Down 계산 (누적 최대값과 현재 hpr 차이 / 누적 최대값 * 100)
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

# Max Draw Down
print("MDD(%): ", df['dd'].max())

# 엑셀로 출력
#df.to_excel("dd.xlsx")
