
def mask_sensitive_info(info,info_type):
    if info_type == int:
        info = str(info)
        last_four = info[-4:]
        # print(last_four)
        
        mask_info = info[:-4]
        # print(mask_info
        masked_info = ""
        for i in mask_info:
            masked_info +=  "*"
        masked_info += last_four
        print(masked_info)
    
    elif info_type == str:
        username, domain = info.split("@")
        masked_username = username[0] + "*"*(len(username)-2) + username[-1]
        
        print(masked_username + '@' + domain)
        
print('What do you want to mask: \n1)credit card \n2)email')
choice = int(input('Enter your choice: '))

try:
    match choice:
        case 1:
            credit_card = int(input('Enter your credit card number: '))
            mask_sensitive_info(credit_card,int)
        case 2:
            email = str(input('Enter your email address: '))
            mask_sensitive_info(email,str)


except  ValueError as e:
    print("Invalid input")
    
finally:
    print("Thank you for using the mask_sensitive_info function")

