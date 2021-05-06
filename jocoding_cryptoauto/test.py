import pyupbit


# 로그인
access = "RUuBBKBiuMN6QJCaw5mJYzCxnB7N9E8RBGXsnxkS"          # 본인 값으로 변경
secret = "x6savsHIaZvvSZV77MSbW53UhjiztzxYSxJJ3NS9"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

# 잔고조회
print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회

