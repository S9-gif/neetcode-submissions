class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_alan=0
        mevcut_alan=0


        L=0     #L pointer'ı birinci indeksten başlar
        R=len(heights)-1    #R pointer'ı sonuncu indeksten başlar

        while L<R: #Yani indeksleri birbirinden farklı olduğu sürece
            
            boy=0 #Boy her döngüde sıfırlansa sorun olmaz herhalde ama if döngüsünde kaynaklanabilecek bir değişken hatasının önüne geçebilir.
            en=R-L  #İndekslere göre her döngüde en hesaplanır
            
            if heights[L]<heights[R]:   #Kısa olan boya göre boy seçilir (Burda hata olabilir)
                boy=heights[L]
                L+=1
            else:                       #Kısa olan boya göre boy seçilir (Burda hata olabilir)
                boy=heights[R]          #BUrda heights[R]ile boy değerini almam gerekiyor olabilir.
                R-=1

            mevcut_alan=boy*en

            if mevcut_alan>max_alan:
                max_alan=mevcut_alan   

        return max_alan         











        '''
PROBLEM:
heights adında int veriler içeren bir liste verilecek.Bu listedeki elemanlar indekslerine göre 
bulundukları indeksin bar uzunluğunu vermekte.Bizden istenen seçilen iki bar için iki bar arasına 
sığabilecek en fazla su hazmini bulmamız istenmekte.

Yani iki ba birbirinden olabildiğince uzak(yani alanın taban boyu uzun) ve barların olabildiğince 
uzun seçilmesi en azından kısa alt sınırın uzun seçilmesi gerekli.

*Tek tek alan hesaplayarak mı ilerleyeceğim?
tek tek hesaplama işleminde hint 1 de O(n^2) zamanlı bir çözüm oluruş daha iyi bir çözüm buşmalıyız
*İki alanı karşılaştırmak yerine greedy mantığı ile her seferinde en iyiyiy bulursak güncellesek
*Bunun için iki tane sayaç mantıklı değişken tanımşadım bunlar her adımda güncellenecek
de neye göre gümcelliyeceğiz kafada oturtamadım.
*İki bar arasına doldurulabilecek en fazla su için seçilen iki bardan kısa olan ya da eşit ise barın
boyu ve barlar arası mesafenin büyük olması gerekli kısacası en ideali bar ikilisi ve barlar arası 
mesafeye sahip olan kombinasyonu arıyoruz.
*Şununla başlayalım,elde ettiğim iki bar uzunluğu ve mevcut uzaklıklarını kullnarak alan hesaplayan
birformül bulalım
*İlk mevcut uzunluk 5 ikincisi 6 diyelim indeksler arası fark yani barların birbirine uzaklığı da 9 
olsun 5,6 olan bar uzunluklarından biri diğerinden farklı ise küçük olan uzunluğu alıcam.Çünkü su 
maksimum oraya kadar dolabilir.if i<j i boy olur,i>j için j boy olur.
Ama O(n) süreli bir alhoritma istediğimiz için tek for döngüsü ile gezmelyim(neyse orayı hallederiz)
daha sonra bu boyu indeksler arası uzaklıkla çarparak mevcut alan blunur



*Olabilir iki bar arasını da bir birim olarak kabul edebiliriz.
two pointers konu başlığı altında bulunduğumuz için sağdan ve soldan barları tarayarak gidebilirz 
belki aynı zamanda greedy diye bir başlık da var.









        '''