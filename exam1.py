class Telefon:
    def __init__(self, marka, model, narx):
        self.marka = marka
        self.model = model
        self.narx = narx
    
    def telefonni_tekshirish(self):
        yaxshi_markalar = ["Samsung", "Apple", "Google", "OnePlus"]
        if self.marka in yaxshi_markalar:
            return "Bu yaxshi telefon"
        else:
            return "Bu telefon unchalik yaxshi emas"
    
    def __str__(self):
      
        return "Marka: {}\nModel: {}\nNarx: {}\nTekshirish: {}".format(
            self.marka, self.model, self.narx, self.telefonni_tekshirish()
        )

telefon1 = Telefon("Apple", "iPhone 13", 1500000)


print(telefon1)

class Telefon():
    def init(self,nomi,xotirasi,rangi,modeli,ogirligi):
        self.nomi=nomi
        self.xotirasi=xotirasi
        self.rangi=rangi
        self.modeli=modeli
        self.ogirligi=ogirligi
        
        
    def get_info(self):
        return self.nomi,self.xotirasi,self.rangi,self.modeli,self.ogirligi
    
    def get_nomi(self):
        return self.nomi
    
    def get_xotirasi(self):
        return self.xotirasi
    
    def get_rangi(self):
        return self.rangi
    
    
d=Telefon("iphone","512","oq","15 pro max","0,5 kg")
f=Telefon("samsung","256","qora","24 ultra","0,6 kg") 
g=Telefon("xiaomi","128","kok","14 pr","03 kg")
h=Telefon("iphone","512","oq","16 pro","0,7 kg")

print(d.get_info())
print(f.get_nomi())
print(g.get_xotirasi())
print(h.get_rangi())

class Product():
    def init(self,tami,ogirligi,sroki,uzunligi,kompaniyasi,kattaligi,sifati,rangi):
        self.tami=tami
        self.ogirligi=ogirligi
        self.sroki=sroki
        self.uzunligi=uzunligi
        self.kompaniyasi=kompaniyasi
        self.kattaligi=kattaligi
        self.sifati=sifati
        self.rangi=rangi
        
    def get_info(self):
        return self.tami,self.ogirligi.self.sroki,self.uzunligi,self.kompaniyasi,self.kattaligi,self.sifati,self.rangi
    
    def get_tami(self):
        return self.tami
    
    def get_ogirligi(self):
        return self.ogirligi
    
    
class Product2(Product):
    
    
    def get_tami1(self):
        return self.tami
    
    def get_ogirligi1(self):
        return self.ogirligi
    
    def get_sroki1(self):
        return self.sroki
    
    
b=Product2("daxshat","1kg","xoxlagancha","1x1","pepsi","katta","sifatli","sariq")    
b1=Product2("daxshat","2kg","2yil","3x3","cola","ortancha","sifatsiz","qora") 
b2=Product2("daxshat","3kg","1yil","2x2","sprite","kichik","chdasa boladi","kok") 


print(b.get_tami1())
print(b1.get_ogirligi1())
print(b2.get_sroki1())


class Parta():
    def init(self,ogirligi,materiali,uzunligi,oyoqlari,kattaligi):
        self.ogirligi=ogirligi
        self.materiali=materiali
        self.uzunligi=uzunligi
        self.oyoqlari=oyoqlari
        self.kattaligi=kattaligi
        
    def get_info(self):
        return self.ogirligi.self.materiali,self.uzunligi,self.oyoqlari,self.kattaligi
    
    def get_ogirligi(self):
        return self.oggirligi
    
    def get_materiali(self):
        return self.materiali
    
    
    
    
class Parta2(Parta):
    
    
    def get_ogirligi(self):
        return self.ogirligi
    
    def get_materiali(self):
        return self.materiali
    
    def get_uzunligi(self):
        return self.uzunligi
    


   
class Parta3(Parta):

    def get_uzunligi(self):
        return self.uzunligi
    
    def get_kattaligi(self):
        return self.kattaligi
    
    def get_materiali(self):
        return self.materiali
    
    
    
b=Parta3("3kg","zor","xoxlagancha","4ta","katta")    
b1=Parta3("ogir","zormas","2x2","4ta","katta") 
b2=Parta3("ogirmas","zor","3x3","5ta","kichik") 


print(b.get_uzunligi())
print(b1.get_kattaligi())
print(b2.get_materiali())


class User:
    def init(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, entered_password):
        
        if entered_password == self.password:
            return "parol notogri"
        else:
            return "parol notogri"

a=User("shoxa_dev","2009")

print(a.check_password("shoxa_devv"))
print(a.check_password("2008"))

class Magazin:
    def init(self, nomi,turi,mahsulotlar_soni,joylashuvi,narx):
        self.nomi=nomi
        self.turi=turi
        self.mahsulotlar_soni=mahsulotlar_soni
        self.joylashuvi=joylashuvi
        self.narx=narx
    
    def narxni_tekshirish(self):
        if self.narx > 10000:
            return "Orta"
        else:
            return "Past"
    
    def str(self):
        return f"Magazin: {self.nomi}\nTuri: {self.turi}\nMahsulotlar soni: {self.mahsulotlar_soni}\nJoylashuvi: {self.joylashuvi}\nNarx: {self.narx}\nNarx holati: {self.narxni_tekshirish()}"

magazin1 = Magazin("yuksalish sp", "Supermarket", 50000, "samarqand, araqzavod", 15000)


print(magazin1)

class Telefon:
    def init(self, marka, model, narx):
        self.marka = marka
        self.model = model
        self.narx = narx
    
    def telefonni_tekshirish(self):
        yaxshi_markalar = ["Samsung", "Apple", "Google", "OnePlus"]
        if self.marka in yaxshi_markalar:
            return "Bu yaxshi telefon"
        else:
            return "Bu telefon unchalik yaxshi emas"
    
    def str(self):
      
        return "Marka: {}\nModel: {}\nNarx: {}\nTekshirish: {}".format(
            self.marka, self.model, self.narx, self.telefonni_tekshirish()
        )

telefon1 = Telefon("Apple", "iPhone 13", 1500000)


print(telefon1)

