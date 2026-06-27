class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        min_price=float('inf')      #Görülen en ucuz  kağıt
        max_profit=0                #En iyi karın saklanacağı değişken


        for i in range(len(prices)):

            if prices[i]<min_price:
                min_price=prices[i]

            else:
               m = prices[i]-min_price
               if m>max_profit:
                    max_profit=m
        return max_profit


            #Problem şuda bizden istenen çözüm O(n) sürede çözümlü olmalıdır ama minimum seçilen 
            #değer için sonraki günleri hesaplamam gerektiği için ikinci bir for döngüsü kullanmam 
            #gerekiyor bu da bildiğim kadarıyla tek değişkende iki kez işlem demek yani=(n^2)
            








        '''
PROBLEM:
integer verilen bir liste var ,bu listedeki değerler indekslerinin bulunduğu günkü borsa değeridir.
Şöyle ki bizden istenen bir borsa kağıdı alım satım algoritması yazmamız.Bu nedenle amaç en ucuz günden alıp 
o günden sonraki en pahalı günde satmak.Karlı satış yapılamayacak ise yani fiyat sürekli düştüyse de
bu durumda da maksimum karı sıfır olarak belirtmeli ve kar satışı yapmamalıyız.
*Biz analiz hazırlıyoruz her minimum alınan kağıt için olası kar hesaplıyoruz ve çıktı olarak en iyi
karı gösteriyoruz.

*Anlamadığım şey şu ucuz olduğunu neyr göre belirliyoruz ve seçiyoruz.maksimum karı neye göre 
seçiyoruz ki satalım.
Önce şunu bulmalıyız Alım için bugün gördüğüm değer en düşük gördüğüm değer mi evet 
Bulunan her düşük değer için(öncekinden) alınsaydı ileriki günlerde nasıl bir kar ortaya koyabilirdi
sorusuna cevap arıyoruz.

*Mesela ilk gün geldim 10 şuana kadar gödrüğüm en küçük değer o yüzden tuttum.sonra biri gördüm 
ikinci gün (1.indeks için) satım yapılsaydı gün 1 için alınandan için bir potansiyel kar hesaplıyorum
kenara atıyorum.ikinic gün daha önekilerden daha ucuz bunu saklıyorum.İlerliyorum sağa doğru ve
bu tuttuğum minimum alış değeri için en iyi artışa bakıyorum potansiyel karım en büyük olunca satıyorum.





*********ÇÖZÜM*********

Yaptığımız gerçek zamanlı bir iş gibi görünse de aslında her gün için potamsiyel kar hesanı yapmaktayız.
Bunun için basit bir şekilde her değerde for döngüsü ile gezdim ve görülen en küçük değer ise sakladım
.Saklanan bu minimum değer için bir kar hesaplaması yaptık.





        '''