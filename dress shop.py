 

          
shop=[]
id=1000
while True:
    print('''
 
          
1.Add products
2.View products
3.Update products
4.delect products
5.search products
6.exit
''')
    ch=int(input('Enter your choice: '))
    if ch==1:
        cat=str(input('Enter category of product: '))
        pname=str(input('Enter the name of product: '))
        price=int(input('Enter the price of product: '))
        stock=int(input('Enter the stock of product'))
        id+=1
        pid=id
        shop.append({'cat':cat,'pname':pname,'pid':pid,'price':price,'stock':stock})

    elif ch==2:
        for i in shop:
            print(i)

    elif ch==3:
        pid=int(input('Enter the id of product: '))
        f=0
        for i in shop:
            
            if i['pid']==pid:
                nstock=int(input('enter new stocks of product: '))
                nprice=int(input('enter new price: '))
                i['stock']=nstock
                i['price']=nprice
                f=1
        if f==0:
            print('invalid id')

    elif ch==4:
        pid=int(input('Enter the id of product: '))
        f=0
        for i in shop:
            
            if i['pid']==pid:
                shop.remove(i)
                f=1
        if f==0:
            print('invalid id')
    elif ch==5:
        
        pid=int(input('Enter the id of product: '))
        f=0
        for i in shop:
            if i['pid']==pid:
                print(i)
                f=1
        if f==0:
            print('invalid id')
    elif ch==6:
                                          
            break
    else:
        print('invalid choice')
        