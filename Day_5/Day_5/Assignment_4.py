num = [10,-5,0,7,-3,4,-2]

check = map(lambda x: "Positive" if x>0 else("negative" if x<0 else"zero"),num)

print(num)
print(list(check))