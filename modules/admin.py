from data import *

lib=[{'id': 1, 'name': 'aa', 'price': 20, 'stock': 2},{'id': 2, 'name': 'ab', 'price': 200, 'stock': 2}]


def add_bk():
    id=int(input('enter the id '))
    name=str(input('enter name'))
    price=int(input('enter the price'))
    stock=int(input('enter the stock'))
    lib.append({'id':id,'name':name,'price':price,'stock':stock,})

def view_bk():
        print('BOOK DETAILS')
        print("{:<5}{:<10}{:<10}{:<10}".format('ID','BOOKNAME','PRICE','STOCK'))
        print('_'*35)
        for i in lib:
            print("{:<5}{:<10}{:<10}{:<10}".format(i['id'],i['name'],i['price'],i['stock']))

def update_bk():
    id=int(input('enter the id : '))
    f=0
    for i in lib:
        if i['id']==id:
            price=int(input('enter the price : '))
            stock=int(input('enter the stock : '))
            i['price']=price
            i['stock']=stock
            print('Details Updated')
            f=1
    if f==0:
        print('invalid id')

def delete_bk():
    id=int(input('enter the id : '))
    f=0
    for i in lib:
        if i['id']==id:
            lib.remove(i)
            print('data deleted')
            f=1
    if f==0:
        print('Invalid id')

def view_usr():
    print('USERS DETAILS')
    print("{:<10}{:<15}{:<15}{:<15}".format('ID','NAME','EMAIL','PHONE'))
    print('_'*55)
    for i in user:
        print("{:<10}{:<15}{:<15}{:<15}".format(i['id'],i['name'],i['email'],i['phone']))

def view_pro(u):
    print('NAME : ',u['name'])
    print('ID : ',u['id'])
    print('Email : ',u['email'])
    print('Phone : ',u['phone'])
    print('Password : ',u['password'])
    print('Books : ',u['book'])



def update_usr(u):
    phone=int(input('enter your number : '))
    password=input('enter new password')
    u['phone']=phone
    u['password']=password
    print('updated')

def rent(u):
    id=int(input('enter the id : '))
    f=0
    for i in lib:
        if i['id']==id:
            f=1
            i['stock']-=1
            u['book'].append(id)
            print('book added')
    if f==0:
        print('invalid ID')

def return_bk(u):
    id=int(input('enter the id : '))
    f=0
    for i in lib:
        if i['id']==id and id in u['book']:
            f=1
            i['stock']+=1
            u['book'].remove(id)
            print('book removed')
    if f==0:
        print('invalid ID')
def books_in_hand(u):
    print(u['book'])