
user=[{'id': 1000, 'name': 'aromal', 'email': 'a@','phone': 920712, 'password': 'asdf','room':[]}]
def register():
        print('Registration Page')
        if len(user)==0:
            id=1000
        else:
            id=user[-1]['id']+1
        email=str(input('enter your email :'))
        f=0
        for i in user:
            if i['email']==email:
                f=1
            print('email already exists enter another one')
            register()
        if f==0:
            name=str(input('enter your name : '))
            phone=int(input('enter your number : '))
            password=input('enter the password : ')
            print('Registration Succesfull email id is your username')
            user.append({'id':id,'name':name,'email':email,'phone':phone,'password':password,'room':[]})

def login():
        usern=str(input('Enter Username : '))
        passw=input('Enter password : ')
        f=0
        u=''
        if usern=='admin' and passw=='admin':
            f=1
        for i in user:
            if usern==i['email'] and passw==i['password']:
                f=2
            u=i
        return f,u
def add_room():
    type=input("enter the type")
    room_no=input("enter the room no")
    ac=input('enter room is ac')
    non_ac=input('enter room is non ac')



def delete_rooms():
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
def view_room():
        print('BOOK DETAILS')
        print("{:<5}{:<10}{:<10}{:<10}".format('ID','BOOKNAME','PRICE','STOCK'))
        print('_'*30)
        for i in lib:
            print("{:<5}{:<10}{:<10}{:<10}".format(i['id'],i['name'],i['price'],i['stock']))



    

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
                1.view profile
                2.update profile
                3.view rooms
                4.book rooms
                5.Logout''')
                c=int(input('enter your choice : '))
                if c==1:
                    view_profile(u)
                elif c==2:
                    update_profile(u)
                elif c==2==3:
                    view_rooms(u)
                elif c==4:
                    book_room(u) 
                elif c==5:
                    break
                else:
                    print('invalid choice')
    elif f==2:
            while True:
                print('''
                    1.view user
                    2.add rooms
                    3.remove rooms
                    4.logout''')
                c1=int(input('enter your choice : '))
                if c1==1:
                    view_user()
                elif c1==2:
                    addrooms()
                elif c1==3:
                    remove_rooms()
                elif c1==4:
                    break
                else:
                    print('invalid choice')
                
                
    

   
       