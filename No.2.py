print("1.Persegi")
print("2.persegi panjang")
print("3.segitiga")
print("4.lingkaran")
print("5.trapesium")
print("6.belah ketupat")
pilih=int(input("masukan angka pilihan="))
if pilih==1:
    s=float(input("masukan panjang sisi="))
    luas=s**2
    keliling=4*s
    print("luas persegi=",luas)
    print("keliling persegi",keliling)
elif pilih==2:
    panjang=float(input("masukan panjang="))
    lebar=float(input("masukan lebar="))
    luas=panjang*lebar
    keliling=2*(panjang+lebar)
    print("luas persegi panjang=",luas)
    print("keliling persegi panjang=",keliling)
elif pilih==3:
    alas=float(input("masukan alas="))
    tinggi=float(input("masukan tinggi="))
    luas=0.5*alas*tinggi
    print("luas segitiga",luas)
    a=float(input("Masukan sisi 1="))
    b=float(input("Masukan sisi 2="))
    c=float(input("Masukan sisi 3="))
    kel = a + b + c
    print("keliling segitiga =",kel)
elif pilih==4:
    phi=3.14
    jari=float(input("masukan jari-jari="))
    luas=phi*jari*jari
    keliling=2*phi*jari
    print("luas lingkaran",luas)
    print("keliling lingkaran",keliling)
elif pilih==5:
    a=float(input("masukan panjang sisi="))
    b=float(input("masukan panjang sisi bawah="))
    c=float(input("masukan tinggi="))
    luas=(((a+b)/2)*c)
    print("luas trapesium",luas)
    a=float(input("Masukan sisi 1="))
    b=float(input("Masukan sisi 2="))
    c=float(input("Masukan sisi 3="))
    d=float(input("Masukan sisi 4="))
    kel = a+b+c+d
    print("keliling trapesium =",kel)
elif pilih==6:
    d1=float(input("masukan diagonal 1="))
    d2=float(input("masukan diagonal 2="))
    luas=((d1*d2)/2)
    keliling=(0.5*d1*d1)+(0.5*d2*d2)
    print("luas belah ketupat=",luas)
    print("keliling belah ketupat",keliling)
else:
    print("bangun datar tidak ada")
    
