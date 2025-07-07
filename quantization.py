from PIL import Image
import numpy as np
import os

giris_resim_a = Image.open(r'C:\Users\DELL\Desktop\202213171807-Ayşenur Eskin\Ek\Fig0224(a).jpg')


if os.path.exists(r'C:\Users\DELL\Desktop\202213171807-Ayşenur Eskin\Ek\Fig0224(a).jpg'):
    print("Dosya bulundu!")
else:
    print("Dosya bulunamadı!")

# Resmin yoğunluğunu düşüren fonksiyonum 
def yogunluk_dusurme(resim_a):
    
    resim_a_np = np.array(resim_a) # Resmi NumPy dizisine çevir
    
    
    resim_a_np = (resim_a_np // 16) * 16 #renk yoğunluğunu düşür
    
    # tekrar resim yap
    return Image.fromarray(resim_a_np)





# yoğrunluğu düşür
cikis_resim_a = yogunluk_dusurme(giris_resim_a)

cikis_resim_a.save(r'C:\Users\DELL\Desktop\202213171807-Ayşenur Eskin\Ek\Fig0224(e)-4-bit.jpg')
