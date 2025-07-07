from PIL import Image
import numpy as np
import os

# resmin boyutlarını değiştirecek bir fonksiyon 
def en_yakin_komsu_enterpolasyonu(resim_a, son_genislik, son_yukseklik):
    # resmin il başkati genişlik ve yüksekliğini aldım
    ilk_genislik, ilk_yukseklik = resim_a.size
    
    #piksellerinden np dizisi oluştur
    new_resim_a = np.zeros((son_yukseklik, son_genislik, 3), dtype=np.uint8)
    
    for i in range(son_yukseklik):  
        for j in range(son_genislik):  
            
            # yeni pikselin hangi orijinal piksele karşılık geldiğini hesapla
            orig_x = int(i * ilk_yukseklik / son_yukseklik)  
            orig_y = int(j * ilk_genislik / son_genislik)    
            
            # Yeni resimdeki pikselin rengini, orijinal resimdeki ilgili pikselden alıyorum.
            new_resim_a[i, j] = resim_a.getpixel((orig_y, orig_x))
    
    # NumPy dizisini tekrar bir resme çevir
    return Image.fromarray(new_resim_a)


#resmi aç
giris_resim_a = Image.open(r'C:\Users\DELL\Desktop\202213171807-Ayşenur Eskin\Ek\Fig0223(a)-930.jpg')

if os.path.exists(r'C:\Users\DELL\Desktop\202213171807-Ayşenur Eskin\Ek\Fig0223(a)-930.jpg'):
    print("Dosya bulundu!")
else:
    print("Dosya bulunamadı!")

son_genislik = 166
son_yukseklik = 165

#enterpolasyonla değiştirme kısmı
cikis_resim_a = en_yakin_komsu_enterpolasyonu(giris_resim_a, son_genislik, son_yukseklik)

#kaydet
cikis_resim_a.save(r'C:\Users\DELL\Desktop\202213171807-Ayşenur Eskin\Ek\Fig0223(d)-72.jpg')
