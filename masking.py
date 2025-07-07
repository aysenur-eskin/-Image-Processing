from PIL import Image
import numpy as np
import os

#iki resmi aç
dental_xray = Image.open(r'C:\Users\DELL\Desktop\202213171807-Ayşenur Eskin\Ek\Fig0234(a)(dental_xray).jpg')
dental_xray_mask = Image.open(r'C:\Users\DELL\Desktop\202213171807-Ayşenur Eskin\Ek\Fig0234(b)(dental_xray_mask).jpg')


if os.path.exists(r'C:\Users\DELL\Desktop\202213171807-Ayşenur Eskin\Ek\Fig0234(a)(dental_xray).jpg') and os.path.exists(r'C:\Users\DELL\Desktop\202213171807-Ayşenur Eskin\Ek\Fig0234(b)(dental_xray_mask).jpg'):
    print("Dosyalar bulundu!")
else:
    print("Dosyalar bulunamadı!")

# iki resimi birbiriyle çarpa
def resim_carpimi(resim_a, resim_b):
    #önce numpy dizisine çevir
    dental_xray = np.array(resim_a)
    dental_xray_mask_np = np.array(resim_b)
    
     #iki resmi çarpıyorum
    masked_resim_np = np.clip(dental_xray * dental_xray_mask_np, 0, 255)
    
    # maskelenmiş resmi geri döndür
    return Image.fromarray(masked_resim_np.astype(np.uint8))

# fonksiyonu çağır
cikis_dental_xray = resim_carpimi(dental_xray, dental_xray_mask)

# resmi kaydettt
cikis_dental_xray.save(r'C:\Users\DELL\Desktop\202213171807-Ayşenur Eskin\Ek\Fig0230(c)(dental_xray_masked).jpg')
