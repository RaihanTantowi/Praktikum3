# Praktikum3
## Tugas Pertemuan 7 - Bahasa Pemrograman

### 1. File program latihan1 (Lab 2 perulangan)
**Program sederhana untuk menentukan bilangan terbesar dari dua bilangan yang diinputkan**

**CODINGAN**

![Gambar 1](screenshoot/ss1.png)
```
 #Membuat judul program 
 print("="*86)
 print("Program sederhana untuk menentukan bilangan terbesar dari dua bilangan yang diinputkan")
 print("="*86)
 bil1=int(input("Masukan bilangan pertama= "))
 bil2=int(input("Masukan bilangan kedua= "))

 #Nilai Terbesar
 if (bil1>bil2):
     print("Hasil bilangan terbesarnya adalah= ",bil1)
 elif (bil2>bil1):
    print("Hasil bilangan terbesarnya adalah= ",bil2)
```