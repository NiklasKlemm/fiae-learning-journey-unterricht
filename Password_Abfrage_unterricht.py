password = input("Wie lautet ihr Password?")

special_char = False
letter = False
digit = False
password_ok = False

zahl = 0

if len(password) >= 10:
    i = 0
    while len(password) > i:
        if password[i].isdigit():
            print("zahl")
            zahl = zahl +1
            digit = True

        elif password[i].isalpha():
            print("buchstabe")
            letter = True

        else:
            print("Sonderzeichen")
            special_char = True

        i = i + 1

        print("Zahlen", zahl)

if digit == True and letter == True and special_char == True:
    password_ok = True
    print("password ist ok")


else:
    print("Ungültiges Passwort")