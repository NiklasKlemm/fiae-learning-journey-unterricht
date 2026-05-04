def password_abfrage2():

    user = input("Wie lautet ihr Benutzername?")
    password = input("Wie lautet ihr Password?")

    user_daten = {"test1": "@q12345678",}


    special_char = False
    letter = False
    digit = False
    password_ok = False



    if user in user_daten:
        if password == user_daten[user]:
            if len(password) >= 10:
                i = 0
                while len(password) > i:
                    if password[i].isdigit():
                        print("zahl")
                        digit = True

                    elif password[i].isalpha():
                        print("buchstabe")
                        letter = True

                    else:
                        print("Sonderzeichen")
                        special_char = True

                    i = i + 1

            else:
                print("Ungültiges Password!")

        else:
            print("Falsche Passwortkombination!")

        if digit == True and letter == True and special_char == True:
            password_ok = True
            print("Password OK")

        else:
            print("Bitte geben sie eine Gültiges Passwort ein")

        return password_ok

zugriff = password_abfrage2()

if zugriff:
    print("Zugriff gewährt")
else:
    print("Zugriff verweigert")

