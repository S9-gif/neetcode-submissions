class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #Sliding window kullanacağım için soldan ve sağdan işaretleyiciler oluşturuyorum.

        L= 0 #s stringinin birinci indeksi
        max_len=0
        liste_set=set() 
        #İlgili L ve R güncellemelerini while içinde yapıcam


        '''
        s stringinin ilk indeksinden başlayarak L ve R imleçlerinde R yi kaydırarak arama yapıcam.L 
        başlangıç R ise gezinen olacak.Gezen R imleci için her elemanda bir öncekiler ile aynı mı sorusunu
        sorucam gördüğüm her r elemanını set e ekliyeceğim ve her dilimi incelerken o dilim için özel bir
        set aramsı yapacağım.
        '''

        for R in range(len(s)):
            # s[R] pencerede zaten varsa, L'yi duplicate'in BİR SONRASINA kadar ilerletip
            # set'ten geride kalan karakterleri çıkarıyoruz
            while s[R] in liste_set:
                liste_set.remove(s[L])
                L += 1

            # Artık s[R] pencerede yok, ekleyebiliriz
            liste_set.add(s[R])

            # Mevcut pencere boyutu (R - L + 1) en uzun olanı geçtiyse güncelle
            max_len = max(max_len, R - L + 1)

        return max_len
                    
                        
                









        
        '''

Problem:
String için alınan substring yani bir dilimin hem olabildiğince uzun hem de tekrar eden eleman olmaması
istenmektedir.
Bunun için fark etmeksizin  en uzun dilimleri alıp daha sonra tekrar eden karakter kontrolü yapabilirim
AMA ya bu aldığım en uzunların(ne de olsa sadece uzun olup olmaması önemli alırken bu substring leri)
hepsinde tekrar eden karakter varsa ve ben ideali atladıysam ne yaparız.


s = "zxyzxyz" karakteri için en uzun sondaki xyz seçilmiş mesela

topic olarak da hash table (saklamak için) ,sting ve sliding window(bulmak için) verilmiş

İstenen zaman ve alan O(n) dir.Her eleman için


Sliding window'u şöyle kullanabilriz soldan ilk iki elemana imleçlerimizi yerleştirerek başlarız 
daha sonra sağdakini kaudırırız.Ta ki L ile aynı ya da duplicate bir elamana denk gelene kadar(Burda
aynı elemana denk gelip gelmediğini nasıl anlıycaz?) Bu nokta çözüm için kritik==> önceki gördüklein
ile aynı mı şeklinde bir soru sorabiliriz R imleci için





*********ÇÖZÜM**********


Valla yalan yok kafam allak bullak oldu iki gün sonunda pek kafama yatmaması üzerine çözümü izledim
ve üstüne claude dan yardım istedim ama hala mantık olarak kafama yatmadı ama yine de ben aklımda 
kalanları yazayım.



Yaptığımız sliding window yöntemi,yani sol imleç ve sağ imleçten sağdaki imleç bir duplicate ile
karşılaşana kadar devam eder karşılaşınca soldan L imlecinden silinme işlemi yapılır.




        '''