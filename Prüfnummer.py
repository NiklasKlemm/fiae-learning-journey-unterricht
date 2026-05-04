kreditkarten_nr = input("Kredikartennummer?")
#8282828277
#0123456789

for i in range(0, len(kreditkarten_nr), 2):

    ziffer = kreditkarten_nr[i]
    verdopplung = int(ziffer) * 2
    print(verdopplung)

    quersumme =  verdopplung // 10 + verdopplung % 10
    print(quersumme)






            #verdopplung[0] + verdopplung[1])
    #print(quersumme)



    #print(ziffer)
    #print(verdopplung)

#quersumme = verdopplung





    #kreditkarten_nr * 2

#print(ord("a"))

#print len(kreditkarten_nr)