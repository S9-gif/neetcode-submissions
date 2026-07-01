class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count=dict()    #window içindeki frekansları aktif olarak tutacak hash table
        max_freq=0      #Görülen en yüksek frekans
        L=0
        result=0


        for R in range(len(s)):


            count[s[R]] = count.get(s[R], 0) + 1        #Burda dşct 'e append mi yoksa add mi kullanmalıyım bilemedim==> get kullan koçum
            max_freq=max(max_freq,count [s[R]])

            if (R - L + 1) - max_freq > k:  #Hala hakkım varsa devam et demek gibi
    
                count[s[L]] -= 1
                L+=1

            result = max(result, R - L + 1)
        return result

             














'''




PROBLEM:
Büyük ingilizce harflerden oluşan s stringi ve k tam sayısı veriliyor.Sorunun istediği seçilen
k kadar harf değiştirerek en uzun ardışık parçanın uzunluğunu elde etmeye çalışıyoruz.


Sliding window ile arama yapıp her en iyi length i güncelleyeceğiz.




'''


