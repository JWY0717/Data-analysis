import pandas as pd

df = pd.read_csv('./data/성별_임금_및_근로시간.csv', encoding='cp949')
#print(df)

# df에 몇 개의 자료가 들어갔는지 확인!
#print(len(df))              # 14
print(df.columns)     # Index (['시점', '항목', '전체근로자', '전체근로자.1', '전체근로자.2', '전체근로자(특수형태포함)'.....

# 데이터의 모양 확인  행 == 14개 ,,,,, 열 == 17개
# print(df.shape)  # (14, 17)

df2 = df[[]]

# 처음 자료만 출력
#print(df.head())

# 마지막 자료만 출력
#print(df.tail())

#print(df.전체근로자)

