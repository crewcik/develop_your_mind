import random
import time

print("1: Sayı hatırlatma oyunu\n2: Kelime hatırlatma oyunu")
tercih = int(input("Seçim: "))
print("Bu oyun Crew.dev tarafından kodlandı.")

def sayi_hafizasi_oyunu():
    print("Sayı Hatırlama Oyununa Hoş Geldiniz!")
    print("Her turda bir sayı dizisi gösterilecek, doğru sırayla hatırlamaya çalışın.")
    
    tur = 1
    while True:
        sayi_dizisi = [random.randint(0, 9) for _ in range(3 + tur)]
        
        print(f"Tur {tur}:")
        print(" ".join(map(str, sayi_dizisi)))
        
        time.sleep(5)
        print("\033[H\033[J")
        
        cevap = input("Sayı dizisini sırayla girin (aralarına boşluk koyun): ")
        kullanici_dizisi = list(map(int, cevap.split()))
        
        if kullanici_dizisi == sayi_dizisi:
            print("Doğru! Bir sonraki tura geçiyorsunuz.")
            tur += 1
        else:
            print(f"Yanlış! Oyun bitti. Toplamda {tur - 1} tur tamamladınız.")
            print(f"Doğru cevap {sayi_dizisi}")
            break

kelimeler = [
    "elma", "masa", "kitap", "bilgisayar", "telefon", "araba", "yazılım", 
    "kalem", "çiçek", "ağaç", "kedi", "köpek", "okul", "pencere", "çanta", "crew", "ben", "sen", "onlar", "tamam", "baba", "anne",
    "gitmek", "gelmek", "can", "canlılar", "göz", "görmek", "duymak", "ağlamak", "zihin", "geliştirmek", "tahmin", 
    "canlanmak", "görünmez", "cambaz", "sinema", "korku", "komedi", "anımsamak", "bu", "kod", "crew", "tarafından", "kodlandı"
]

def kelime_hatirlama_oyunu():
    print("Kelime Hatırlama Oyununa Hoş Geldiniz!")
    print("Her turda gösterilen kelimeleri doğru sırayla hatırlayın.")
    
    tur = 1
    while True:
        kelime_dizisi = random.sample(kelimeler, 3 + tur)
        
        print(f"Tur {tur}:")
        print(", ".join(kelime_dizisi))
        
        time.sleep(5)
        print("\033[H\033[J")  
        
        cevap = input("Kelimeleri sırayla girin (aralarına boşluk koyun): ")
        kullanici_dizisi = cevap.split()
        
        if kullanici_dizisi == kelime_dizisi:
            print("Doğru! Bir sonraki tura geçiyorsunuz.")
            tur += 1
        else:
            print(f"Yanlış! Oyun bitti. Toplamda {tur - 1} tur tamamladınız.")
            print(f"Doğru cevap: {kelime_dizisi}")
            break

if tercih == 1:
    sayi_hafizasi_oyunu()
elif tercih == 2:
    kelime_hatirlama_oyunu()
else:
    print('Geçersiz tercih.')
