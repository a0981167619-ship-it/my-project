"""字串方法"""
x='If possible, I will go'
print("原字首:",x)
print("首字元大寫,其餘字元小寫:",x.capitalize())
print("全部大寫:",x.lower())
print("全部小寫:",x.upper())
print("每個單字首字大寫,其餘小寫:",x.title())
print("判斷是否所有字元皆為小寫:",x.islower())
print("判斷是否所有字元皆為大寫:",x.isupper())
print("判斷首字元是否為大寫:",x.istitle())
print("判斷字串是否僅由字母/數字組成:",x.isalnum())#是為True 否為False
print("判斷是否僅由字母組成:",x.isalpha())
print("判斷是否僅由數字組成:",x.isdigit())
print("判斷字串是否僅由空格組成:",x.isspace())