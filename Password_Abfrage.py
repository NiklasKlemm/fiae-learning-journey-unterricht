def password_abfrage():

    password = input("Wie lautet ihr Password?")
    password_erlaubt = ["@q12345678",
                        "@w12345678",
                        "@e12345678",
                        "@r12345678",
                        "@t12345678",
                        "@z12345678",
                        "@i12345678",
                        "1234567890"]


    special_char = False
    letter = False
    digit = False
    password_ok = False



    if password in password_erlaubt:
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

