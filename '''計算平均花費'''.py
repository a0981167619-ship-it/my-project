'''計算平均花費'''
import sys
average=sys.argv[1:]
average=[int(x) for x in average]
total=sum(average)
answer=total/len(average)
print('平均花費為:',answer)