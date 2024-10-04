
print('1.addition :\n')
print('2.multiplication :\n')
print('3.division:\n')
print('4.subtration:\n')

operation_sign=int(input("input the operation sign of your choice:\n"))
first_number= int(input("enter first number of your choice:\n"))
second_number= int(input("enter second number of your choice:\n"))
results=0
if operation_sign ==1:
    results=first_number+ second_number
    print('\n' ,results)
elif operation_sign==2:
    results= first_number*second_number
    print('\n' ,results)
elif operation_sign==3:
    result= first_number/second_number
    print('\n' ,results)
elif operation_sign==4:
    results= first_number-second_number
    print('\n' ,results)
else:
    print("invalid operation_sign")





    

