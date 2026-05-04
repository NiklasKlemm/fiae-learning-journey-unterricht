from Password_Abfrage import password_abfrage

zugriff = password_abfrage()

if zugriff:
    print("Zugriff gewährt")
else:
    print("Zugriff verweigert")
