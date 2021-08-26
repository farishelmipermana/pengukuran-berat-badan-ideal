print("Selamat datang, disini anda akan menemukan berat badan ideal anda")
print("=" * 50)
print("Hitung berat badan ideal")

# Pria: Berat badan ideal (kg) = [tinggi badan (cm) – 100] – [(tinggi badan (cm) – 100) x 10%]

# Wanita: Berat badan ideal (kg) = [tinggi badan (cm) – 100] – [(tinggi badan (cm) – 100) x 15%]

nama = input("Nama kamu siapa? : ")
kelamin = input ("kelamin (l/p)? : ")

laki = ["l"]
perempuan = ["p"]

print("="*50)

if kelamin in laki:

    tb = int(input("tinggi badan kamu berapa? (dalam cm): "))
    bb = int(input("masukkan berat badan kamu (dalam kg): "))
    rumus = ((tb-100)-((tb-100)*10/100))
    print(nama, ", tinggi badan kamu ", tb, "cm")
    print("berat badan idealmu ", rumus)

    if (bb>rumus):

        print("berat badanmu melebihi normal, \n ayo turunkan berat badanmu!")
        rencana = str(input("apa rencanamu dalam menurunkan berat badan? : "))
        lama = int(input("berapa lama anda akan menurunkan berat badan? (dalam hitungan hari): "))

        if (lama>360):
            print("Kamu terlalu lama menurunkan berat badanmu sebesar", bb, "kg. Terkait ", rencana, "sudah sangat baik!")
        else:
            print(rencana, " sudah sangat baik!" )




    elif (bb==rumus):
        print("selamat! berat badanmu ideal! \n ayo pertahankan berat badan idealmu!")
    
    else:
        
        print("kamu kurus banget yaa! \n ayo perbanyak makan!")
        rencana = str(input("apa rencanamu dalam menaikan berat badan? : "))
        lama = int(input("berapa lama anda akan menaikan berat badan? (dalam hitungan hari): "))

        if (lama>360):
            print("Kamu terlalu lama menaikan berat badanmu sebesar", bb, "kg. Terkait ", rencana, "sudah sangat baik!")
        else:
            print(rencana, " sudah sangat baik!" )

    



elif kelamin in perempuan:

    tb = int(input("tinggi badan kamu berapa? (dalam cm): "))
    bb = int(input("masukkan berat badan kamu (dalam kg): "))
    rumus = ((tb-100)-((tb-100)*15/100))
    print(nama, ", tinggi badan kamu ", tb, "cm")
    print("berat badan idealmu ", rumus)

    if (bb>rumus):

        print("berat badanmu melebihi normal, \n ayo turunkan berat badanmu!")
        rencana = str(input("apa rencanamu dalam menurunkan berat badan? : "))
        lama = int(input("berapa lama anda akan menurunkan berat badan? (dalam hitungan hari): "))

        if (lama>360):
            print("Kamu terlalu lama menurunkan berat badanmu sebesar", bb, "kg. Terkait ", rencana, "sudah sangat baik!")
        else:
            print(rencana, " sudah sangat baik!" )




    elif (bb==rumus):
        print("selamat! berat badanmu ideal! \n ayo pertahankan berat badan idealmu!")
    
    else:
        
        print("kamu kurus banget yaa! \n ayo perbanyak makan!")
        rencana = str(input("apa rencanamu dalam menaikan berat badan? : "))
        lama = int(input("berapa lama anda akan menaikan berat badan? (dalam hitungan hari): "))

        if (lama>360):
            print("Kamu terlalu lama menaikan berat badanmu sebesar", bb, "kg. Terkait ", rencana, "sudah sangat baik!")
        else:
            print(rencana, " sudah sangat baik!" )

else:
    pass