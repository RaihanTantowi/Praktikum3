print("="*58)
print("Program menampikan bilangan acak yang lebih kecil dari 0.5")
print("="*58)
jumlah = int(input("Masukan jumlah n : "))
import random
for i in range(jumlah):
    print("data ke",i+1,"=>",(random.uniform(0.1,0.5)))
    