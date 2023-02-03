# DataBase (Dictionary)
UserNames = {"Admin": "Admin",
"m17z": "m17z123"
}

###########################################

print("="*40)
print(" "*10 + "Hello To The Website" + " "*10)
print("="*40)
haveAnAcc = input("Hello, Do you have an account? (Y,N) ") #Ask the visitor if he had an acc in the database.
YesAnswer = ["Yes", "Y"]
NoAnswer = ["No", "N"]

tries = 3

if haveAnAcc not in YesAnswer or NoAnswer:
    print("Please Choose Yes or No.")

while haveAnAcc.strip().capitalize() in YesAnswer:
    username = input("Okay, please type your username: ")
    password = input("Now your password: ")
    if UserNames.get(username) == password and tries > 0:
        print("You succesfully login.\nWelcom")
        break
    elif UserNames.get(username) != password:
        print("The usename or password is wrong, please try again.")
        tries -= 1
        if UserNames.get(username) != password and tries == 0:
            print("You tries 3 times wrong, please re-open the file.")
            break
        else:
            continue
    else:
        print("ERROR")
while haveAnAcc.strip().capitalize() in NoAnswer:
    signup = input("Do you wanna make an account? (Y,N) ")
    signup = signup.strip().capitalize()
    if signup in YesAnswer:
        NewUser = input("Type the username you want to use: ")
        NewUser = NewUser.strip()
        if NewUser in UserNames:
            print("The username have been used, Try Again ...")
            continue
        elif NewUser not in UserNames:
            NewEmail = input("Your Email: ")
            NewEmail = NewEmail.strip()
            NewPass = input("the password: ")
            confirmPass = input("Confirm the password: ")
            NewPass = NewPass.strip()
            confirmPass = confirmPass.strip()
            if NewPass == confirmPass:
                print(f"Now you have an account has a username {NewUser}, Please Reopen the file to sign-in.")
                UserNames.setdefault(f"{NewUser}", f"{NewPass}")
                break
            else:
                print("Please make sure that the password is confirmed.")
                continue
    elif signup in NoAnswer:
        print("Okay sir, We are happy to see you here again <3")
        break
    else:
        print("SOMTHING WRONG WITH YOUR ANSWER")
        continue
