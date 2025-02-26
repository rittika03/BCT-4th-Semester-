from prettytable import PrettyTable 
table=PrettyTable()
l = []
def signIn():
    email=input("Enter your email: ")
    password=input("Enter your password: ")
    n=len(l)
    for i in range(n):
        if l[i]['email']!=email:
            print(l[i])
            print(f"{email} is not registered, please signUp first.")
            return
        elif email.endswith(".com")!=True:
            print(f"Wrong  email entered please Try Again")
            return
        else:
            if(l[i]['password']!=password):
                print("Incorrect password.")
                return
            else:
                print("Login successfull.")
                return
def signUp():
    database = {}
    email=input("Enter your email: ")
    password=input("Enter your password: ")
    database["email"] = email
    database["password"] = password
   if email.endswith(".com")==True:
        l.append(database)
        print("Signup successfull.")
    else:
        print(f"Wrong  email entered please Try Again")
    return
def show():
    table.field_names=(["EMAIL","PASSWORD"])
    n=len(l)
    for i in range(n):
        e=l[i]['email']
        p=l[i]['password']
        table.add_row([e,p])
    print(table)
def main():
    while True:
        key=int(input('''\nEnter 1 for signup...
                      \nEnter 2 for signin...
                      \nEnter 3 to exit...
                      \nEnter 4 to show database'''))
        if(key==3):
            break
        elif(key==1):
            signUp()
        elif(key==2):
            signIn()
        elif(key==4):
            show()
        else:
            print("Please enter a valid parameter.")
main()
