def main():
    # membuat judul program
    print("="*89)
    print("Program sederhana untuk menentukan bilangan terbesar dari ketiga bilangan yang diinputkan")
    print("="*89)
    # input dari user
    a = int(input('masukan bilangan ke-1: '))
    b = int(input('masukan bilangan ke-2: '))
    c = int(input('masukan bilangan ke-3: '))
 
    # menentukan nilai bilangan
    maks = a
    if b > maks:
        maks = b
    if c > maks:
        maks = c
 
    # cetak hasil
    print('bilangan terbesar adalah: %d' % maks)
 
if __name__=='__main__':
    main()