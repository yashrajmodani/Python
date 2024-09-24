dict = {'a':1,'b':2,"'c":3}

ans = {value:key for key,value in dict.items()}

print(ans)