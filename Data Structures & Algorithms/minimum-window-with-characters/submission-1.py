    

'''4-Minimum Window Substring'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        from collections import Counter

        need = Counter(t)       # {'A':1, 'B':1, 'C':1}
        window = {}

        required = len(need)    # kaç farklı karakter karşılanmalı
        formed = 0              # şu an kaç farklı karakter karşılandı

        left = 0
        min_len = float("inf")
        result = ""

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            # Bu karakter t'de gerekiyor mu ve yeterince var mı?
            if char in need and window[char] == need[char]:
                formed += 1

            # Tüm karakterler karşılandıysa → pencereyi daralt
            while formed == required:
                # Sonucu güncelle
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]

                # Sol karakteri çıkar
                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                left += 1

        return result




        '''
PROBLEM:

Veirlen s ve t stringleri için t stringi s içinde rsatgele olarak bulunabilmektedir.Sorudunun
isteği t nin karakterlerinin bulunduğu en kısa parçayı çıktı vermemiz.Bunun için hash table ve 
sliding windowu birlikte iki kez kullanacağız.Asıl kilit nokta iki hash table ı nasıl kullandığımızdır.
Kullanım özeti şu şekildedir.Bir adet t harfleri için ne ile uğraştığımızı neyi aradığımızı bilmemizi
sağlayan t hash table'ı var;bir de s için kontrol hash table ı var.Yapılan şey her imleç hareketinde
önceden buluğumuz t hash mapi ile güncelledidğimiz s hash table 'ını karşılaştırmamızdır.Bu karşı-
laştırmayı da sayaç benzeri bir işlem ile yapıyoruz.Misal t deki giderilmesi gereken elemanlar yani
need kısmı 3 kısıt olsun,s'i sliding window ile tararken karşılanan her kısıt için have adındaki değişken
bir arttırılır.have ile need değişkenleri eşit olduğunda kısıtlara uyulan bir pencere bulunmuş demektir.
Algoritmanın pratikte yaptığı budur.Aynı şekilde daha kısa dilimleri bulabilmek adına bu have listesi
azaltılacak şekilde de güncellenebilir.Bu nokta da da idealliği yani result kontrolünü de length lere 
bakarak yapıyoruz.


Bu algoritma sorusunu çözemedim kodu claude ile yazdım mantığını solutions ile öğrendim.



        '''