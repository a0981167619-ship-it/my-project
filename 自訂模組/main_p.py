import bank_module
m=bank_module.deposit(1000,500)
print('目前餘額為{0}元'.format(m))
d=bank_module.withdraw(1500,300)
print('目前餘額為{0}元'.format(d))
r=bank_module.withdraw(1200,1500)
print('目前餘額為%s元'%(r))
