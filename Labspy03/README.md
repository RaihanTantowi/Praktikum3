# Praktikum3
## Tugas Pertemuan 7 - Bahasa Pemrograman

### 1. File latihan1.py
**Program sederhana untuk menentukan bilangan terbesar dari dua bilangan yang diinputkan**

* **CODINGAN:**
```
 print("Tampilkan n bilangan acak yang lebih kecil dari 0.5")

 jumlah = int(input("Masukan jumlah n: "))
 import random
 for i in range(jumlah):
     print("data ke", i+1,"=",(random.uniform(0.1,0.5)))
```

* **Penjelasan alur program:**

  print("Menampilkan n bilangan acak yang lebih kecil dari 0.5") 
- itu hanya perintah untuk menamilkan judul saja
  jumlah = int(input("Masukan jumlah n: )) 
  Adalah perinntah untuk menginputkan nilai n tersebut
  import random
  Adalah perintah untuk menginportkan built-in random yang telah tersedia di python
  for in range (jumlah): 
  Adalah perintah untuk, i sebagai integer dalam baris jumlah
  print ("data ke",i+1,"=",(random.uniform(0.1,0.5))) 
-  Adalah perintah untuk menampilkan hasil yang telah di input dengan ketentuan random uniform mulai dari nilai 0.1 sampai 0.5


* **Hasil output program:**

![Gambar 2](screenshoot/ss1.png)