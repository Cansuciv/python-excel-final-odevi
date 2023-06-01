#adminlerin kullanıcı adları ve şifreleri
adminler= {"admin1":["admin1", "sifre123"],
           "admin2":["admin2", "sifre321"]}


# Admin giriş ekranı için fonksiyon yazımı
def admin_girisi():
    while True:
        print("Lütfen admin girişi için admin kullanıcı adınızı ve şifrenizi giriniz.\n")
        admin_adi = input("Admin Kullanıcı Adı: ")
        admin_sifresi = input("Admin Şifre: ")

        if admin_adi not in adminler or admin_sifresi not in adminler[admin_adi][1]:
            print("Hatalı şifre veya kullanıcı adı. Tekrar deneyin!\n")
        else:
            print("Admin girişi başarıyla yapılmıştır.\n")
            break
        
# menü ekranı
def kullanici_girisi():
    menu=["1-Sisteme üye ol","2-Sisteme giriş yap","3-Şifremi unuttum"]
    print(menu[0])
    print(menu[1])
    print(menu[2])
    
    
   
        


GirisMetni=(""""Uygulamaya hoş geldiniz Bu uygulama, deprem anında ve depremden sonrasında
size yardım etmek için vardır. Deprem sırasında depreme yakalandığınız yeri ve
sağlık durumunuzu girerek yardım çağırabilirsiniz. Depremden sonra ise maddi ve manevi yardım için başvurular 
yapabilirsiniz. \n""")
print(GirisMetni)

while True:
    # admin olarak mı kullanıcı olarak mı giriş yapılacağının seçimi
    giris = input("Sisteme admin olarak mı giriş yapmak istiyorsunuz kullanıcı olarak mı giriş yapmak istiyorsunuz (admin/kullanıcı): ")
    
    #kullanıcı ekranı........................................................
    if giris.lower()=="kullanıcı":
        print("-KULLANICI GİRİŞİ-\n\n\n")
        kullanici_girisi()
             
        secim=int(input("Lütfen yapmak istediğiniz seçeneği giriniz:"))
        #üye olma menüsü(ad-soay, tel no, tc no, adres , şifre vb. girişi  yapılır)
        if secim==1:
            print("-SİSTEME ÜYE OL-\n")
            ad_soyad=input("Adınızı ve soyadınızı giriniz:")
            kullanici_adi=input("Kullanıcı adı giriniz:")
            while True: #tel no da sadece rakam girişi yapma
                tel_no=input("Telefon numaranızı giriniz:")
                if tel_no.isdecimal():
                    break
                else:
                    print("Hatıl giriş yaptınız. Lütfen sadece rakam giriniz.\n")
                        
            e_posta=input("Lütfen e-posta adresinizi giriniz:")
                
            while True: #tc no da sadece rakam girişi yapma
                tc_no=input("TC numaranızı giriniz:")
                if tc_no.isdecimal():
                    break
                else:
                    print("Hatıl giriş yaptınız. Lütfen sadece rakam giriniz.\n")
                        
            adres=input("Lütfen adresinizi giriniz:")
            sifre=input("Lütfen bir şifre giriniz:")
            print("\nSİSTEME ÜYE OLUNDU!!! \n\n")
               
                
        #sisteme giriş yapma ekranı
        elif secim==2:
            print("-SİSTEME GİRİŞ YAP-\n")               
            #eposta adresiyle giriş yapma
            e_posta=input("Lütfen e-posta adresinizi giriniz:")
            sifre=input("Lütfen şifrenizi giriniz:")
            print("\nSİSTEME GİRİŞ YAPILDI!!! \n\n")
                  
                
        #şifremi unuttum ile tel no ya da eposta adresiyle şifer değiştirme
        elif secim==3:
            print("-ŞİFREMİ UNUTTUM-\n")
            sifremi_unuttum=input(""""Şifrenizi unuttunuz ve değiştirmek mi istiyorsunuz? Şİfrenizi telefon numarası
ile değiştirmek için 4'e, e-posta dresi ile değiştirmek için 5'ye basınız:""")
            #tel no ile şifre değiştirme. telefona gelen kodu girerek yeni şifre oluşturma
            if sifremi_unuttum=="4":
                while True: #tel no da sadece rakam girişi yapma
                    tel_no=input("Telefon numaranızı giriniz:")
                    if tel_no.isdecimal():
                        break
                    else:
                        print("Hatıl giriş yaptınız. Lütfen sadece rakam giriniz.")   
                    
                kod=input("Telefonunuza gelen kodu giriniz:")
                yeni_sifre=input("Yeni şifrenizi giriniz:")
                print("\nŞİFRENİZ DEĞİŞTİRİLDİ!!! \n\n")
                    
            #eposta ile şifre değiştirme. epostaya gelen kodu girerek yeni şifre oluşturma
            elif sifremi_unuttum=="5":
                e_posta=input("Lütfen e-posta adresinizi giriniz:")
                kod=input("E-posta adresinize gelen kodu giriniz:")
                yeni_sifre=input("Yeni şifrenizi giriniz:")
                print("\nŞİFRENİZ DEĞİŞTİRİLDİ!!! \n\n")
                    
            else:
                print("Geçersiz seçim yaptınız. Lütfen tekrar deneyin.\n")   
                
    
        #seçim2 ile deprem sırasında ve sonrasında bilgi alımı
        secim2=input("deprem sırasındaki işlemler için 1'e depremden sonraki işlemler için 2'ye basınız")
        if secim2=="1":
            adres=input("Merhaba!!! Adresiniz sisteme kayıtlı mı? (Evetse 'E'ye, hayirsa 'H'ye basiniz) \n")
            if adres.upper()=="E":
                print("Adresiniz kayıtlıdır. Devam edebilirsiniz.\n")
            else:
                adres=input("Adresinizi giriniz: \n")
    
            apartman_adi=input("Apartman adını giriniz: \n")
            kat_no=input("Kat numarasını giriniz: \n")
            daire_no=input("Daire numaranızı giriniz: \n")
            oda=input("Hangi odada olduğunuzu giriniz: \n")
            yakin_tel_no=int(input("Yakın bir tanıdığınızın telefon numarasını giriniz:"))
            saglik_durumu=input("Lütfen sağlık durumunuz hakkında bize birkaç bilgi veriniz:")
            yaninizda_biri_var_mi=input("yaninizda biri var mi? (Evetse 'E'ye, Hayirsa 'H'ye basiniz)")
            if yaninizda_biri_var_mi.upper()=="E":
                yaninizdaki_kisinin_saglik_durumu = input("Yanınızdaki kişinin sağlık durumunu nedir?: ")
            
            print(adres)
            print(apartman_adi)
            print(kat_no)
            print(daire_no)
            print(oda)
            print(yakin_tel_no)
            print(saglik_durumu)
            print(yaninizda_biri_var_mi)
            print(yaninizdaki_kisinin_saglik_durumu)
            print("Bilgileriniz alınmıştır ve ilgili yerlere iletilmiştir.")
            
            
        if secim2=="2":
            ev_hasar_durumu = input("Evinizin hasar durumu: ")
            yardim_kurumlari=("AFAD","YEŞİLAY", "KIZILAY", "AHBAP")
            print(yardim_kurumlari)
            yardim_kurum_sec=input("Yardım almak istediğiniz kurumları seçiniz:")
            yardim_tipi=input("nasıl bir yardım almak istediğinizi giriniz:")
            su_anki_adresiniz=input("Şu anda yaşadığınız yerin adresini giriniz:")
            print("Yardım talebiniz başarıyla gerçekleşmiştir.\n")
            
            
        Cikis=input("\nSistemden çıkmak için '1'e basınız.\n")
        if Cikis=="1":
            break
        else:
            continue        
    
    
    #admin ekranı.............................................................
    elif giris.lower() == "admin":
        print("-ADMİN GİRİŞİ-\n\n\n")
        admin_girisi()
        
        
        import pandas as pd
        # Excel dosyasını okur
        df=pd.read_excel("kullanici-bilgileri.xlsx")
        print(df)
        
        #kullanıcı bilgilerinde value değerleri sırası ile ad soyad, tel no, e posta, tc, adres, şifre ve eski şifre dir  
        bilgiler = {
        "ahmetS": ["Ahmet Saka", "1548452", "AhmetS@gmail.com", "2145855254", "dknsfkjfewrebjk", "Ahmet123Saka", "Yok"],
        "mehmetK": ["Mehmet Kara", "12454521", "MehmetK@gmail.com", "1548715", "fsgrsghkdshg", "Mehmet1542", "Mehmeterjkds54"],
        "AyşeS": ["Ayşe Sel", "1541555", "AyseS@gmail.com", "564819198", "dsgsdfdlakszflsaf", "Aysesel185", "Ayse154778"],
        "FatmaY": ["Fatma Yak", "52357378", "FatmaY@gmail.com", "687687868", "dsgrhtfjdfgj", "Fatma123Fatma13", "123Fatma123"],
        "GülA": ["Gül Ak", "533873873", "GülAk@gmail.com", "054686868", "fjdfgjfgjgfjd", "GülAKakGÜL154882", "Yok"]
        }
        
        
        while True:
            kullanici_adi_gir = input("Erişmek istediğiniz kullanıcının bilgileri için kullanıcı adı giriniz: ")
            if kullanici_adi_gir in bilgiler.keys():
                kullanici_bilgileri = bilgiler[kullanici_adi_gir]
                print("Adı Soyadı:", kullanici_bilgileri[0])
                print("Telefon Numarası:", kullanici_bilgileri[1])
                print("E-posta Adresi:", kullanici_bilgileri[2])
                print("TC Numarası:", kullanici_bilgileri[3])
                print("Adres:", kullanici_bilgileri[4])
                print("Şifre:", kullanici_bilgileri[5])
                print("Eski Şifre:", kullanici_bilgileri[6])
            else:
                print("Girdiğiniz kullanıcı adına sahip bir kullanıcı bulunamadı.\n")
        
            Cikis=input("\nSistemden çıkmak için '1'e basınız.\n")
            if Cikis=="1":
                break
            else:
                continue
     
    
    
    #geçersiz seçim ekranı....................................................
    else:
        print("Geçersiz giriş seçimi yaptınız. lütfen tekrardan deneyiniz!!!\n")
        
    