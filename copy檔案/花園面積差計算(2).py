import math
fgarden=int(input('請輸入前院的寬:'))
fgarden1=int(input('請輸入前院的長:'))
ans=fgarden*fgarden1
bf=int(input('請輸入後院面積的長:'))
bf1=int(input('請輸入後院面積的寬:'))
result=bf*bf1

sol=ans-result
print('兩院面積差為:',math.fabs(sol))