def main():
    # membuat judul program
    print("="*86)
    print('Program sederhana untuk menentukan bilangan terbesar dari dua bilangan yang diinputkan')
    print("="*86)
    # menentukan input user
    a = int(input("masukan bilangan pertama: "))
    b = int(input("masukan bilangan kedua: "))
 
     # Menentukan Nilai Bilangan  dengan if else
    if a > b:
        maks = a
    else:
        maks = b
    # mencetak nilai maksimum
    print('Nilai Terbesar adalah %d' % maks)
 
if __name__ == '__main__':
    main()