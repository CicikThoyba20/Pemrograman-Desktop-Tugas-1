kondisi=True
coba=0
while kondisi:
        username=input("masukan username=")
        password=input("masukan password=")
        if username=="sate" and password=="ayam":
                print("welcome")
                kondisi=False
        else:
                print("username atau password anda salah")
                coba+=1
                if coba>3:
                        print("anda salah memasukan lebih dari 3 kali")
                        break
