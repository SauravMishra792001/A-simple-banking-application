
balance=0
kyc_document ={}
def check_balance():
    print(f"your current balance is: {balance}")
    print("============")


def deposit(amount):
    global balance
    if amount >0:
        balance += amount
    else:
        print("deposit Amount can't be less than zero")
        print("=============")



def withdraw(amount):
    global balance
    if amount <=0:
        print("Amount can't be negative or less than zero")
        print("============")
    elif amount >balance:
     print("Cannot withdraw :Infufficient balance")
     print("============")
    else:
        balance -= amount


def kyc(docs):
    global kyc_document
    kyc_document.update(docs)


def check_kyc():
    if len(kyc_document)==0:
        print("kyc not done")
    else:
        for doc in kyc_document:
            print(f"{doc} : {kyc_document[doc]}")
        print("============")


def update_kyc(docs):
    global kyc_document
    kyc_document.update(docs)


if __name__=="__main__":
    print("============")
    print("welcome to your apna bank!!")
    print("============")
    print()

    while True:
        print("1.Check your balance")
        print("2.Deposit an account")
        print("3.Check KYC")
        print("4.Update KYC")
        print("5.Withdraw an amount")
        print("6.Quit")
        choice=input("Enter a choice(1-6)")
        print("============")
        if choice =='1':
            check_balance()
        elif choice =='2':
            amt=float(input("Enter the amount to deposit : "))
            deposit(amt)
            print(f"your current balance is: {balance}"   )
        elif choice =='3':
            amt = float(input("Enter the amount to withdraw : "))
            withdraw(amt)
            print(f"Amount {amt} withrawn successfully")
        elif choice =='4':
            check_kyc()
        elif choice =='5':
            kyc_docs={}
            n_documents = int(input("Enter the number of documnent you want to add : "))
            for i in range(n_documents):
                key = input("Enter the document type: ")
                value = input("Enter the document number : ")
                kyc_docs[key]=value
            update_kyc(kyc_docs)
            print("KYC updated")
        elif choice =='6':
            print("Quit ,have a nice day")
            break
        else:
            print("Invalid choice!!! Re try.")
            print("============")
        print()
        print("Thank you for using our apna bank!")

