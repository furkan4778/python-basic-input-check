#Değişkenler
isim = input ("İsminizi giriniz: ")
soyisim = input ("Soyisminizi giriniz: ")
yas = int (input ("Yaşınızı giriniz: "))


#İsim Sorma
if len(isim) > 10:
    print ("İsminiz 10 karakterden uzun lütfen başka isim giriniz.")

elif len(isim) <= 3:
    print     ("İsminiz 3 karakterden kısa lütfen başka isim giriniz.")


#Soyisim Sorma
if len(soyisim) > 10:
    print ("Soyisminiz 10 karakterden uzun lütfen başka isim giriniz.")

elif len(soyisim) <= 3:
    print     ("Soyisminiz 3 karakterden kısa lütfen başka isim giriniz.")
    

#Yaş Sormaa
if yas < 18:
    print ("Yaşınız 18 den az olduğundan giriş yapamassınız. ")

elif yas >= 18:
    print     (f"Teşşekürler {isim} {soyisim} giriş ypabilirsiniz:)")
    

