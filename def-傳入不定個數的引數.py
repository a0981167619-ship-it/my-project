"""傳入不定個數的引數--*元組回傳"""
def AP_number(*genuine):
    answer=0
    for num in genuine:
        answer+=num*num
    return answer
    
answer1=AP_number(3)
print('3*3=',answer1)
answer2=AP_number(2,3)
print('2*2+3*3=',answer2)
answer3=AP_number(7,10,15)
print('7*7+10*10+15*15',answer3)
answer4=AP_number(4,5)
print('4*4+5*5',answer4)

def number(*num1):
    answer=0
    for num in num1:
        answer=num**num
    return answer
answer1=number(2)
print('2**2=',answer1)
answer2=number(10)
print('10**10=',answer2)
answer3=number(89,56)
print('89**89+56**56=',answer3)
        

