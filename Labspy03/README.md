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
```
   -print("Menampilkan n bilangan acak yang lebih kecil dari 0.5") 
   itu merupakan perintah untuk menampilkan sebuah input dari judul program
   -jumlah = int(input("Masukan jumlah n: )) 
   Adalah perinntah untuk menginputkan nilai n tersebut
   -import random
   Adalah perintah untuk menginportkan built-in random yang telah tersedia di python
   -for in range (jumlah): 
   Adalah perintah untuk, i sebagai integer dalam baris jumlah
   -print ("data ke",i+1,"=",(random.uniform(0.1,0.5))) 
   Adalah perintah untuk menampilkan hasil yang telah di input dengan ketentuan random uniform mulai dari nilai 0.1 sampai 0.5
```

* **Hasil output program:**

![Gambar 1](screenshoot/ss1.png)

### 2. File latihan2.py
**Program sederhana untuk menampilkan bilangan terbesar dari n buah data yang diinputkan**

* **CODINGAN:**
```
 print("Menampilkan bilangan terbesar dari n buah data yang diinput")

 max = 0
 while True:
     a = int(input("Masukkan Bilangan: "))
     if max < a:
         max = a
     if a ==0:
         break
 print("Bilangan Terbesar Adalah: ", max)
 ```

 * **Penjelasan alur program:**
```
   -print("Menampilkan bilangan terbesar dari n buah data yang diinput") 
   itu merupakan perintah untuk menampilkan sebuah input dari judul program
   -a = int(input("Masukkan Bilangan: "))
   Adalah perinntah untuk menginputkan bilangan
   -if max < a:
         max = a
   ini adalah  max kurang dari nilai a, maka max sama dengan a
   -if a ==0:
         break 
   Adalah perintah untuk berhenti dari program yang sedang berjalan, dengaan mengetik angka 0
   -print("Bilangan Terbesar Adalah: ", max)
   Adalah perintah untuk menampilkan hasil yang terbesar dari sebuah bilangan yang diinputkan
```

* **Hasil output program:**

![Gambar 2](screenshoot/ss2.png)

### 3. File program1.py
**Program sederhana untuk menampilkan bilangan terbesar dari n buah data yang diinputkan**