from PIL import Image
import numpy as np
import os

#resmi al
giris_kidney = Image.open(r'C:\Users\DELL\Desktop\202213171807-Ayşenur Eskin\Ek\Fig0239(c)(kidney).jpg')

if os.path.exists(r'C:\Users\DELL\Desktop\202213171807-Ayşenur Eskin\Ek\Fig0239(c)(kidney).jpg'):
    print("Dosya bulundu!")
else:
    print("Dosya bulunamadı!")

# bulanıklık fonksiyonumu tanımladım
def yerel_bulaniklik(resim_c, komsuluk_boyutu=41):
    
    resim_c_np = np.array(resim_c)
    
    
    yukseklik, genislik = resim_c_np.shape #resmi yeniden boyutlandır
    
    
    yeni_resim_np = np.zeros_like(resim_c_np) #yeni resim dizisi
    
    
    yaricap = komsuluk_boyutu // 2
    
    
    for i in range(yaricap, yukseklik - yaricap):
        for j in range(yaricap, genislik - yaricap):
            
            komsuluk = resim_c_np[i - yaricap:i + yaricap + 1, j - yaricap:j + yaricap + 1]
            
            
            ortalama = np.mean(komsuluk)
            
            
            yeni_resim_np[i, j] = ortalama
    
    # resmi geri döndür
    return Image.fromarray(np.uint8(yeni_resim_np))


# resmi bulanıklaştır
cikis_resim_a = yerel_bulaniklik(giris_kidney)


cikis_resim_a.save(r'C:\Users\DELL\Desktop\202213171807-Ayşenur Eskin\Ek\Fig0239(d)(kidney)_blur.jpg')
