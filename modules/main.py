from registration import*
from admin import *
from data import *

while True:
    print('''
    1.Register as User
    2.Login
    3.EXIT''')
    
    c=int(input('enter your choice : '))
    if c==1:
        register()
    elif c==2:
        f,u=login()
        if f==1:
            while True:
                print('''
                1.Add book
                2.View Book
                3.Update Book Details
                4.Delete book
                5.View Users
                6.Logout''')

                c1=int(input('enter your choice : '))
                if c1==1:
                    add_bk()
                elif c1==2:
                    view_bk()
                elif c1==3:
                    update_bk()
                elif c1==4:
                    delete_bk()
                elif c1==5:
                    view_usr()
                elif c1==6:
                    break
                else:
                    print('invalid Choice')
        elif f==2:
            while True:
                print('''
                    1.view profile
                    2.view book
                    3.update profile
                    4.Rent a book
                    5.Return a book
                    6.book in hand
                    7.logout''')
                c1=int(input('enter your choice : '))
                if c1==1:
                    view_pro(u)
                elif c1==2:
                    view_bk()
                elif c1==3:
                    update_usr(u)
                elif c1==4:
                    rent(u)
                elif c1==5:
                    return_bk(u)
                elif c1==6:
                    books_in_hand(u)
                elif c1==7:
                    break
                else:
                    print('invalid option')
        else:
            print('invalid username or password')
    elif c==3:
        break
    else:
        print('Invalid Choice')