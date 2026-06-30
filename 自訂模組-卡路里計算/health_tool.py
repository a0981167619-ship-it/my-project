def bmi(weight,height):
    weight=float(input('請輸入體重:'))
    height=float(input('請輸入身高:'))
    BMI=weight/(height/100)**2
    return BMI
def status(BMI):
    if BMI<18.5:
        print('過輕')
    elif 18.5<BMI<24.9:
        print('正常')
    else:
        print('過重')
    