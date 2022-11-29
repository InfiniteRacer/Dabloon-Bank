import time

items = []

def openacc():
    
    global name
    
    name=input("Whats your full name? ")
    print("")
    print("Hello " +name+ "!")
    print("")
    
    openacc2()
    
def openacc2():
    
    global balance

    balance=input("What is your starting balance? ")
    print("Please confirm that the amount is " +balance+ " Dabloons?")
    print("")
    
    openacc3()
    
def openacc3():
    
    check1=input("y/n? ")
    
    if check1 == 'y':
        print("Done! We are now preparing your account with us.")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(1)
        print("Done!")
        mainstartupvariation()
    elif check1 == 'n':
        print("That is fine! Please try again.")
        print("")
        openacc2()
    else:
        print("Invalid input")
        print("")
        openacc3()
        
def mainstartupvariation():
    
    print("")
    print("Welcome to the main menu " +name+ "!")
    print("More features will be added in later versions!")
    print("")
    
    menu()  
        
def main():
    print("")
    print("Welcome back " +name+ "!")
    print("More features will be added in later versions!")
    print("")
    
    menu()
    
def menu():    

    print("Enter '1' to view balance.")
    print("Enter '2' to add Dabloons.")
    print("Enter '3' to minus Dabloons.")
    print("Enter '4' to add existing assets to list.")
    print("Enter '5' to view purchased assets.")
    print("Enter 'laws' to view the laws with transactions.")
    print("Enter 'cancel' to cancel account.")
    
    print("")
    
    choicemenu=input("Enter Choice: ")
    
    if choicemenu == '1':
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        balancecheck()
    elif choicemenu == '2':
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        add()
    elif choicemenu == '3':
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        minus()
    elif choicemenu == '4':
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        addassets()
    elif choicemenu == '5':
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        viewassets()
    elif choicemenu == 'laws':
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        laws()
    elif choicemenu == 'cancel':
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(1)
        print("Done! We are sorry to see you go...")
        exit()
    else:
        print("Invalid Input! Try again...")
        print("")
        menu()
        
def balancecheck():
    
    print("")
    
    print("Your current balance is:")
    
    print(balance, " Dabloons")
    
    print("")
    
    time.sleep(2)
    
    main()
    
def add():
    
    global balance
    global moneyadd
    global maxamtlaw
    
    maxamtlaw = 101
    
    print("")
    
    moneyadd=input("How much would you like to add into your account? ")
    
    if int(moneyadd) < int(maxamtlaw):
        
        print("")
        
        balance = int(balance) + int(moneyadd)
        
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(1)
        
        print("Your current balance is: ")
        
        print(str(balance))
        
        time.sleep(2)
        print("")
        main()
        
    elif int(moneyadd) > int(maxamtlaw):
        
        print("")
        
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(1)
        print("")
        
        print("Can not complete transaction! According to law - 100 Dabloons MAX per transaction.")
        
        time.sleep(2)
        
        print("")
        
        main()
    
def minus():
    
    global balance
    global moneyminus
    
    print("")
    
    print("Enter '1' for withdraw.")
    print("Enter '2' for purchase.")
    typeofpurch=input("Enter option here: ")
    
    if typeofpurch == '1':
        moneyminus=input("How much would you like to take away from your account? ")
        
        if int(moneyminus) > int(balance):
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(1)
            print("")
            print("Can not complete transaction! Invalid amount in account")
            print("")
            time.sleep(2)
            main()
        elif int(moneyminus) < int(balance):
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(1)
            
            balance = int(balance) - int(moneyminus)
            
            print("Transaction complete!")
            
            print("")
            
            print("Your balance is now: ")
            
            print(str(balance))
            
            time.sleep(2)
            print("")
            main()
            
    elif typeofpurch == '2':
        
        itemaddacc=input("Please state the name of the purchase: ")
        
        moneyminus=input("How much does this purchase cost? ")
        
        if int(moneyminus) > int(balance):
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(1)
            print("")
            print("Can not complete transaction! Invalid amount in account")
            print("")
            time.sleep(2)
            main()
        elif int(moneyminus) < int(balance):
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(1)
            
            balance = int(balance) - int(moneyminus)
            
            items.append(itemaddacc)
            
            print("Transaction complete!")
            
            print("")
            
            print("Your balance is now: ")
            
            print(str(balance))
            
            time.sleep(2)
            print("")
            main()
    else:
        print("Invalid input. Try again...")
        print("")
        minus()
        
def addassets():
    
    listitemadd=input("Please state the name of your asset: (ONE AT A TIME) ")
    
    items.append(listitemadd)
    
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(1)
    
    print("Done!")
    
    time.sleep(1)
    
    main()
    
def viewassets():
    
    print("The current assets registered are listed below:")
    
    time.sleep(2)
    
    print(items)
    
    time.sleep(2)
    
    main()
    
def laws():

    print("The current laws are listed below:")
    
    print("")
    
    print("NO MORE than 100 dabloons per withdraw.")
    print("Do NOT add fake money into account. Always verify it first.")
    print("Do NOT use a fake name.")
    
    time.sleep(4)
    
    main()
        
print("Welcome to Dabloon Bank.")
print("Open an account with us below!")
print("")

openacc()
