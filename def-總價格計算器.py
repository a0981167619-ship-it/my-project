def total_price(price,rate,tax=5,shipping=50):
    price=int(input('請輸入商品原價:'))
    #若有折扣
    rate=int(input('請輸入折扣:'))
    #稅率
    tax=int(input('請輸入稅率:'))
    shipping=int(input('請輸入運費:'))

    #折扣後價格
    price_after_discount=price*(1-rate/100)
    print('折扣後價格為:',price_after_discount)

    #加上稅金
    price_with_tax=price_after_discount*(1+tax/100)
    print('加上稅金後為:',price_with_tax)

    #加上運費

    final_price=price_with_tax+shipping

    print('總價格為:',final_price)

print(total_price(500,10,8,30))