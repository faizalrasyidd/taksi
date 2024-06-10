import os 
os.system("cls")

# buat taksi bisa mulai bekerja
#taksi bisa menerima jarak yang akan ditempuh
#harga taksi per-1km = 5000 ribu rupiah / 100 meter = 500 rupiah

def tarif(jarak):
     #jarak dalam satuan meter
     harga = jarak * 5
     return harga

  
def jalan():
     pendapatan = 0
     while True:
          print("1 . Ambil orderan")
          print("2 . Cancel orderan")
          print("3. Selesai")
          user = int(input("Masukkan pilihan anda\t: "))
          if user == 1:
               jarak = int(input("Masukkan jarak(meter)\t: "))
               penumpang = tarif(jarak)
               pendapatan += penumpang
               print("Telah Sampai Tujuan")
               print(f"Tarif yang harus dibayar :{penumpang}")
               print(f"Pendapatan anda saat ini! {pendapatan} Semangatt!")
          elif user == 2:
               print("Silahkan menunggu orderan selanjutnya! ")
          elif user == 3:
               print("Selamat beristirahat...")
               print(f"Pendapatan anda hari ini! {pendapatan} Semangatt!")
               break

print("Mulai jalan?")
driver = str(input("Y/N\t: ")).lower()
if driver != "y":
     exit()
elif driver == "y":
     jalan()
   
#    DONE GAK BANG
