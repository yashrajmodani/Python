import pandas as pd

data = pd.Series([10,20,30,40,10,20,40])

print("average rank")
# print(data.rank(method='average'))
print(data.rank(method = 'average'))

print("\nMin rank")
print(data.rank(method='min'))

print("\nMax rank")
print(data.rank(method='max'))

print("\nFirst rank")
print(data.rank(method='first'))

print("\nDense rank")
print(data.rank(method='dense'))
