try:
    a=2
    b=int(input('請輸入一整數:'))
    print(a/b)

except SyntaxError:
    print('Error--語法錯誤')
except NameError:
    print('Error--未宣告變數')
except TypeError:
    print('Error--類型錯誤')
except ZeroDivisionError:
    print('Error--除0錯誤')
except IndexError:
    print('Error--指定索引錯誤')
except NotImplementedError:
    print('Error--尚未實作的方法')
except ValueError:
    print('Error--無效的參數')
except SyntaxWarning:
    print('Warning--可疑語法錯誤')
except DeprecationWarning:
    print('Warning--已棄用的特徵')

finally:
    print('ღ--執行結束')