class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        


        mevcut_dizi_length=1
        en_uzun_length=0


        sirali=list(set())

        sorted_nums = sorted(nums)       

        for i in sorted_nums:

            if i not in sirali:
                sirali.append(i)
            #Bu noktada elimde temiz bir dizi olacaktır.

        for j in sirali:

            if j+1 in sirali:
                mevcut_dizi_length=mevcut_dizi_length+1
            
            elif en_uzun_length<=mevcut_dizi_length:

                en_uzun_length=mevcut_dizi_length
                mevcut_dizi_length=1

        return en_uzun_length



            









        """
PROBLEM:
Rastgele sayılardan ve sıradan oluşan int tipindeki nums listesi var elimizde.İstenen bu listede
ki en uzun ardışık sayı dizisinin uzunluğudur(ardışık sayı dizisi için her elemanın önceki elemandan 1 büyük olması gerekli).
En uzun ardışık dizi kaç sayıdan oluşuyor?

Topic olarak tahmin ettiğim üzere hash table var.Ekstra olarak union find adında bir ds var.
union table kümeleme yapmaya yarar.



Bir kere mutlaka hash table kullanacağız.
Her döngü ile aldıpım sayıyı bir önceki ile karşılaştırabilirim.
ama bu karşılaştırma neye göre olacak eğer mesela [1,23,3] şeklinde bir liste varda birden sonra iyi
23>1 dedim ama sonraki 3 için napıcam halbuki 1 ve üç asıl ardışık.Bu noktada listeyi sort etmek en 
mantıklısı.Bu durumda da aynı sayılar olabilir.Bunu da set ile çözebilirim her sayıdan bir tane olur.
Bu adımları takip ederek mesela [1,2,2,3,6,75,5] şeklindeki listeyi sort edip sete ekleyince
-->[1,2,3,5,6,75] şeklinde bir liste döndürmüş olurum.

İdeal listeme oluştum

Bu noktada ardışık sırayı istediğim için union find ı kullanıcam.Misal aramaya başladık:
[1,2,3,45,60,61,62,63,64] şeklinde bir dizi var.Görüldüğü üzere iki tane ardışık sayı dizisi var .
Benim yapmam gereken bu iki ardışık diziyi gruplamak ve bunlardan uzunluğu daha büyük olan kümeyi döndürmem.
bbu noktada hash table işin içine giriyor olabailir:

{1,2,3}:lengt=3
{60,61,62,63,64}:lengt=5

karşılaştırmayı burdan yapabilrim ya da mümkünse direkt kümeleri karşılaştırırım ama pek mümkün değil gibi







        """