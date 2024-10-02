
user=[{'id': 1000, 'name': 'aromal', 'email': 'a@','phone': 920712, 'password': 'asdf','room':[]}]
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
                    add_rooms()
                elif c1==3:
                    remove_rooms()
                elif c1==4:
                    break
                else:
                    print('invalid choice')
                
                
    

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
        user.append({'id':id,'name':name,'email':email,'phone':phone,'password':password,'book':[]})

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
       