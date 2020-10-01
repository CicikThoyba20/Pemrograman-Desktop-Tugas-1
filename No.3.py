tinggi=int(input("masukkan tinggi badan anda(cm):"))
berat=int(input("masukkan berat badan anda(kg):"))
c=tinggi/100.00
d=(berat/(c*c))
print(("Hasil=="),d)
if d<18.5:
    print("berat badan kurang")
elif d>18.5 and d<22.9:
    print("berat badan normal")
elif d>23 and d<29.9:
    print("berat badan berlebih")
else :
    print("obesitas")


