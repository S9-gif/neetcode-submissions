class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        prevhash_table={} #val=index

        for i ,n in enumerate(nums): #enumerate hem indeksi hem değeri aynı anda verir.

            tamamlayıcı=target-n

            if tamamlayıcı in prevhash_table:
                return [prevhash_table[tamamlayıcı],i]

            
            prevhash_table[n] = i#tamamlayıcı elemanını key value değer olarak hash table a ekledim burda elemanı() ile eleman indisini[]ile aldım
        return

                

solution=Solution()

print(solution.twoSum(nums=(1,2,3,1,23,2),target=3))












'''
PROBLEM:
Verilen tam sayı dizisinden farklı iki sayını toplamı target olarak 
belirlenen sayıya eşit olmalı eşitlik sağlanıyorsa i ve j ellemanlarının
indekslerini döndür.


*Topics olarak hash table verilmiş
*Şöyle yapabilirim for döngüsü ile bir elemanı alırım daha sonra ikinci
bir içi içe for döngüsü ile alınan ilk eleman için tek tek diğer liste 
elemanları ile toplama yapıp target değere eşit mi?diye sorarım *Bu noktada problemimiz aynı sayı da olmaması bunun için de target değeri
veren ikililerin hepsini farketmeksizin bir yere koyar bu ikililer eşit mi
diye sorgularım bi de.ama bu 
durum için algoritma verimli olmaz daha akıllı bir algoritma olmalı.



*Elimde for döngüüs ile tuttuğum eleman için şunu sorabiliirim bu elemanın
target için tamamlayıcısı hash table da var mı 

*En hızlı şekilde tek bir cevap bulabilmemiz yeterli bu nedenle 
olabşldiğince hızlı arama yapabilmek adına target -nums[i]= fark
diyorum ve bu bulunan farkın hash_map de olup olmadığına bakıyorum
eğer varsa cevap bulunur yoksa mevcut dizi elemanını indisi ile birlikte
hash_map'e ekliyorum ik belki ilerki elemanlar için araştırdığımda
tamamlayıcı bu eleman olur ve hash_map'de direkt bulunduğu için yine hızlı
bir şekilde cevabı yazabiliirm.
*Aslında bu algoritma aramasını istatistikten birikimli dağılım fonksiyonunun
olasılık aramasına benzetebiliriz.





*********ÇÖZÜM*********

Diziyi tek bir döngüyle geziyoruz. Her eleman için target - n 
ile tamamlayıcısını hesaplıyoruz. Bu tamamlayıcı daha önce görüldüyse 
prevhash_table'da bulunur ve indeksleri döndürürüz. Görülmediyse mevcut
elemanı indeksiyle birlikte hash table'a ekleyip devam ediyoruz — 
ileride başka bir eleman bu elemanı tamamlayıcı olarak arayabilir.

ALgoritma her elemanı bir kere tarar ve hash map maksimum n elemanı tutabilir
Time:
O(n)
Storage:
O(n)




*Yalan yok problem akşama kaldığı için hem odak olarak düşüktüm hem de enerji olarak
ama bunlar bahane değil en yakın zamanda dönüp işimi daha iyi yapıcam
'''







