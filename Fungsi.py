"""
TODO:
Buatlah sebuah fungsi bernama "minimal" dengan ketentuan berikut.
- Menerima dua buah argumen berupa number, yaitu a dan b.
- Mengembalikan nilai terkecil antara a atau b.
- Bila nilai keduanya sama, kembalikan dengan nilai a.
"""

# TODO: Silakan buat kode Anda di bawah ini.
def minimal(a, b):
    if(a<b):
        return a
    elif(a>b):
        return b
    else:
        return a
        
print(minimal(1,2))
print(minimal(3,2))
print(minimal(2,2))