s1 = {'apple','mango','grapes','banana'}
s2 = {'apple','gobi','bhindi','aloo'}
s3 = {'apple','wheat','bajri','jawari'}
s4 = s1.intersection(s2.intersection((s3)))
print(s4)

s6 = {'apple','mango','grapes','banana'}
s7 = {'apple','gobi','bhindi','aloo'}
s8 = {'apple','wheat','bajri','jawari'}
s5 = s6.symmetric_difference(s7)
s9 = s5.symmetric_difference(s8)
print(s9)

s10 = {'apple','mango','grapes','banana'}
s20 = {'apple','gobi','bhindi','aloo'}
s30 = {'apple','wheat','bajri','jawari'}
s40 = s10.difference(s20.difference(s30))

print(s40 )
