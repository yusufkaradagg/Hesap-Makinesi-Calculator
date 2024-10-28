from tkinter import *

# Bu fonksiyon, bir sayıyı veya karakteri giriş alanına ekler.
# This function appends a number or character to the entry field.
def yaz(x):
    s = len(giris.get())  # Mevcut giriş uzunluğunu alır / Gets the current input length
    giris.insert(s, str(x))  # Yeni karakteri giriş alanına ekler / Inserts new character to the entry field

# İşlem tipi ve ilk sayıyı saklamak için global değişkenler
# Global variables to store the operation type and the first number
hesap = 5
s1 = 0

# Bu fonksiyon, hangi işlemin seçildiğini ayarlar ve ilk sayıyı saklar.
# This function sets which operation is selected and stores the first number.
def islemler(x):
    global hesap
    hesap = x  # İşlem tipini saklar (0=Toplama, 1=Çıkarma, 2=Çarpma, 3=Bölme)
    # Stores the operation type (0=Addition, 1=Subtraction, 2=Multiplication, 3=Division)
    global s1
    s1 = float(giris.get())  # İlk sayıyı alır ve kaydeder / Gets and saves the first number
    print(hesap)  # Seçilen işlemi yazdırır / Prints selected operation
    print(s1)  # İlk sayıyı yazdırır / Prints first number
    giris.delete(0, 'end')  # Giriş alanını temizler / Clears the entry field

# İkinci sayıyı saklamak için bir değişken
# Variable to store the second number
s2 = 0

# Bu fonksiyon, sonucu hesaplar ve gösterir.
# This function calculates and displays the result.
def hesapla():
    global s2
    s2 = float(giris.get())  # İkinci sayıyı alır / Gets the second number
    print(s2)  # İkinci sayıyı yazdırır / Prints second number
    global hesap
    sonuc = 0  # Sonucu saklamak için bir değişken / Variable to store the result
    if hesap == 0:
        sonuc = s1 + s2  # Toplama işlemi / Addition operation
    elif hesap == 1:
        sonuc = s1 - s2  # Çıkarma işlemi / Subtraction operation
    elif hesap == 2:
        sonuc = s1 * s2  # Çarpma işlemi / Multiplication operation
    elif hesap == 3:
        sonuc = s1 / s2  # Bölme işlemi / Division operation
    giris.delete(0, 'end')  # Giriş alanını temizler / Clears the entry field
    giris.insert(0, str(sonuc))  # Sonucu giriş alanına yazar / Writes the result in the entry field

# Ana pencereyi oluşturur
# Creates the main window
pencere = Tk()
pencere.geometry("250x300")  # Pencere boyutunu ayarlar / Sets the window size

# Giriş alanını oluşturur
# Creates the entry field
giris = Entry(font="Verdana 14 bold", width=15, justify=RIGHT)
giris.place(x=20, y=20)

# Sayı butonlarını oluşturur ve saklar
# Creates and stores number buttons
b = []
for i in range(1, 10):
    b.append(Button(text=str(i), font="Verdana 14 bold", command=lambda x=i: yaz(x)))

# Sayı butonlarını 3x3 bir ızgarada yerleştirir
# Places number buttons in a 3x3 grid
sayac = 0
for i in range(0, 3):
    for j in range(0, 3):
        b[sayac].place(x=20 + j * 50, y=50 + i * 50)
        sayac += 1

# İşlem butonlarını oluşturur ve saklar
# Creates and stores operation buttons
islem = []
for i in range(0, 4):
    islem.append(Button(font="Verdana 14 bold", width=2, command=lambda x=i: islemler(x)))

# İşlem butonlarının metnini ayarlar
# Sets the text of operation buttons
islem[0]['text'] = "+"
islem[1]['text'] = "-"
islem[2]['text'] = "*"
islem[3]['text'] = "/"

# İşlem butonlarını dikey olarak yerleştirir
# Places operation buttons vertically
for i in range(0, 4):
    islem[i].place(x=170, y=50 + 50 * i)

# "0" butonunu ekler
# Adds the "0" button
sb = Button(text="0", font="Verdana 14 bold", command=lambda x=0: yaz(x))
sb.place(x=20, y=200)

# Ondalık nokta butonunu ekler
# Adds the decimal point button
nb = Button(text=".", font="Verdana 14 bold", width=2, command=lambda x=".": yaz(x))
nb.place(x=70, y=200)

# Eşittir butonunu ekler ve hesaplama yapar
# Adds the equal button and performs the calculation
eb = Button(text="=", fg="RED", font="Verdana 14 bold", command=hesapla)
eb.place(x=120, y=200)

# Ana döngüyü başlatır
# Starts the main loop
pencere.mainloop()
