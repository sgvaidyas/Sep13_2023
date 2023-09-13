'''
Program:
To demonstrate the CRUD operations in a list
'''
contacts = []
while True:
    ch  = int(input("1 CREATE 2 DISPLAY 3 UPDATE 4 DELETE 5 EXIT"))
    match ch:
        case 1:
            d = {}
            d['name'] = input("enter the name")
            d['phone'] = int(input("enter the phone num"))
            d['email'] = input("enter the email")
            contacts.append(d)
            print("A new contact is created!")
        case 2:
            if len(contacts)>0:
                print("_____DISPLAY ALL CONTACT______________")
                for x in contacts:
                    print("NAME  = ",x['name'])
                    print("PHONE = ", x['phone'])
                    print("EMAIL = ", x['email'])
                    #print("*".center(40,'-'))
                    print("*".center(40,'-'))
            else:
                print("No contacts present")
        case 3:
            searchname = input("Enter the search name = ").strip().casefold()
            for x in contacts:
                if x['name'].strip().casefold() == searchname:
                    print("-----Match found -----")
                    update = int(input("1 Phone 2 Email 3 Do nothing"))
                    if update==1:
                        x['phone'] = int(input("Enter the phone num ="))
                    elif update == 2:
                        x['email'] = input("Enter the email =")
                    elif update ==3:
                        print("No changes")
                    else:
                        print("invalid choice")
                    break
            else:
                print("no such data found")
        case 4:
            searchname = input("Enter the search name = ").strip().casefold()
            ind =0
            for x in contacts:
                if x['name'].strip().casefold() == searchname:
                    print("-----Match found -----")
                    delch = int(input("1 Delete 2 Do nothing"))
                    if delch == 1:
                        contacts.pop(ind)
                    elif delch == 2:
                        print("No changes")
                    else:
                        print("invalid choice")
                    break
                ind=ind+1
            else:
                print("The record doesnt exist")
        case 5:
            break
        case _:
            print("invalid choice")

