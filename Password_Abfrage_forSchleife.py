password = input("Wie lautet ihr Password?")
password_erlaubt = ["@q12345678",
                    "@w12345678",
                    "@e12345678",
                    "@r12345678",
                    "@t12345678",
                    "@z12345678",
                    "@i12345678",
                    "1234567890",]


special_Char = False
letter = False
digit = False
passwordOK = False



if password in password_erlaubt:
    if len(password) >= 10:
        #i = 0

        for zeichen in password:
            if zeichen.isdigit():
                digit = True
            elif zeichen.isalpha():
                letter = True
            else:
                special_Char = True


            '''while len(password) > i:
                if password[i].isdigit():
                    print("zahl")
                    digit = True

                elif password[i].isalpha():
                    print("buchstabe")
                    letter = True

                else:
                    print("Sonderzeichen")
                    special_Char = True

                i = i + 1'''

    else:
        print("Ungültiges Password!")

else:
    print("Falsche Passwortkombination!")

if digit == True and letter == True and special_Char == True:
    passwordOK = True
    print("Password OK")

else:
    print("Bitte geben sie eine Gültiges Passwort ein")

#return passwordOK
