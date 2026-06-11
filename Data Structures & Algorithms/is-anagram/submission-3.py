class Solution:
    def isAnagram(self, s: str, t: str) ->bool:
        

       
        s=sorted(list(s))
        t=sorted(list(t))

        if s==t:
            return True
        
        
        return False

        #Listeye çevirdikten sonra sıralayabilirim 
        #Şuanda elimde sıralı stringler var bunlardan for döngüsü ile bişyler yapıcaz bakalım


        #Harf frekansını nasıl sayıcam?
        #Acaba demetleri kullanabilir miyim?-->bence hayır en azından frekans saymak için değil yani

        


solution=Solution()

print(solution.isAnagram(s="seco",t="oces"))













'''
Problem: İki tane string vericez sisteme ve bu verilen iki kelime için
anagram olup olmadıklarını kontrol edicez.

*Anagramlıkk kontrolu için kelimenin harflerini tek tek gezip eşit 
frekanslarda harf bulunduğunu teyit etmeliyiz

*Belki ilk örnekte özdüğümüz gibi set veri tipini kullanabiliriz.
*Algoritmayı temel yazarız gerekirse daha akıllı bir hale getiririz.
*İki tane set kursak sonra bu setleri alfabetik sırada karşılaştırsak olabilir
ama yine de harflerin frekanslarına da ihtiyacımız var 
*O zaman bir yandan her yeni harf tutulacak bir yandan da sayılacak.
*Çözümün O(nlogn+mlogn) olması gerekli n ve m farklı iki stringin uzunluğu
*Önce uzunluk karşılaştırarak direkt iki anagram kelime eşit uzunlukta olması
gerektiği için ,değillerse direk False döndğrebiliriz.
*Hint 1 için sort işlemi yapabileceğimizi söylüyor.




ÇÖZÜM:

İki kelimenin analığı için iki kelimede de aynı frekansta aynı harflerin bulunması gerekir
 biz de her iki kelimeyi String tip ipinden alıp önce bir listeye çevirdik
 Daha sonra kelimenin harfleri listenin elemanlarına dönüştü bu listenin
 Elemanlarını sıralarsak ve bu iki String kelime eğer ki Anagramsa t ve s'nin
 Liste olarak birebir aynı olması gerekir

 * aslında ilk başta hedeflediim kelimeleri listeledikkten sonra harfleri frekanslarına göre saymaktı
 Yani bir hash map oluşturup bu ikisini karşılaştırmaktı ama bu birazcık daha zahmetli geldi
 O yüzden iki listeyi karşılaştırmayı tercih ettim keza daha akıllı bir algoritmama burada yazılan.

* aynı zamanda Python'da bulunan counter fonksiyonu ile de tek satırda
Stringlerin frekanslarını sayıp karşılaştıran yani yapmayı düşündüğümüz 
hashmap in kısa yolu olan bu fonksiyonlarda tek satırda yapabilirdik.

**************Diğer Çözüm**************


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Uzunluklar farklıysa zaten anagram olamaz, direkt False döndür
        if len(s) != len(t):
            return False

        # Her string için boş birer hashmap oluşturuyoruz
        # Key: harf, Value: o harfin kaç kez geçtiği
        countS, countT = {}, {}

        # Her iki stringi aynı anda geziyoruz
        for i in range(len(s)):
            # s'deki mevcut harfin frekansını 1 artır
            # .get(s[i], 0) → harf daha önce yoksa 0'dan başlat, varsa üstüne ekle
            countS[s[i]] = 1 + countS.get(s[i], 0)

            # Aynısını t için yapıyoruz
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # countS'teki her harfi countT ile karşılaştır
        for c in countS:
            # countT'de o harf hiç yoksa .get(c, 0) → 0 döndürür
            # Frekanslar eşit değilse anagram değildir
            if countS[c] != countT.get(c, 0):
                return False

        # Tüm harflerin frekansları eşitse anagramdır
        return True



'''






