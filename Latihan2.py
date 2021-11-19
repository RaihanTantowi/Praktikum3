#Judul Program
print('='*70)
print ('Program untuk mengurutkan bilangan dari yang terkecil hingga terbesar')
print('='*70)

#Input 
def pengulangan():
    print ('Masukkan 3 bilangan yang diinginkan!')
    a=int(input('Masukan Bilangan 1 = '))
    b=int(input('Masukan Bilangan 2 = '))
    c=int(input('Masukan Bilangan 3 = '))

#Kondisi
    if a<b and a<c:
        if b<c:
            
#Output 
            print(a, b, c)
        else:
            print(a, c, b)
    elif b<a and b<c:
        if a<c:
            print(b, a, c)
        else:
            print(b, c, a)
    else:
        if a<b:
            print(c, a, b)
        else:
            print(c, b, a)

    print('')
    print('Ingin mencoba lagi? (ya/tidak)')
    x=input()
    if x=='ya':
        return pengulangan()
    if x=='tidak':
        print('='*45)
        print('Terima kasih telah menggunakan program ini :)')
        print('='*45)
pengulangan()