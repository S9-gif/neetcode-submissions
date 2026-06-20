class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums=sorted(nums)
        set1=set()
    
        for i in range(len(nums)):

            L=i+1
            R=len(nums)-1
            while L<R:
                if nums[L]+nums[R]+nums[i]==0:
                    set1.add(tuple(sorted((nums[i], nums[L], nums[R]))))
                    
                    L += 1
                    R -= 1

                elif nums[L]+nums[R]+nums[i]>0:
                    R -= 1
 

                elif nums[L]+nums[R]+nums[i]<0:
                    L += 1
        return list(set1)







        '''
        liste=set()
        
        for i in range(0,len(nums)):        

            for j in range(i+1,len(nums)): #İlk döngü i seçtikten sonra ikinci for döngüsünün i den farklı bir değer seçmesi gerekli bunun için range ile sınır belirtilebilinir belki?
                           #j for i in nums: içinde bir döngü olduğu için büyül ihtimalle i den farklı ilk değeri seçecektir.Bu da bizim için iyi bir şey. 
                for k in range(j+1,len(nums)):

                    if nums[i]+nums[j]+nums[k]==0:

                        liste.add(tuple(sorted((nums[i], nums[j], nums[k]))))
                    #Bu kullanım doğru mu acaba?Koşula uyan üçlüleri listenin içine eklemeye çalışıyorum.
                   # continue#Bu continue ifadesi en sonki döngüyü devam ettirir di mi for k in nums yani
                    


        return [list(a) for a in liste]


        '''

        '''
PROBLEM:
Verilen karışık int tipindeki listeden toplamı sıfır olan üç sayı döndürülecektir.
Dödürülen üçlü sayılar  birebir aynı olmamalıdır.

Üç tane değişken için listede üç tane for döngüsü ile gezinirim.Bu sayede her kombinasyonu denemiş 
olurum.Uygun kombinasyonları da boş bir listeye eklerim.Hiç uygun yoksa bu boş liste döner.


*Şimdi şöyle ki bu ilk düşündüğüm ve yaptığım çözüm doğru fakat O(n^3) sürede çalışıyor ve ben bunu 
kodu debug ettikten sonra fark ettim ki çok acı.Bizim two pointers algoritması kullanarak maksimum
O(n^2) hızında daha verimli bir algoritma yazmamız gerekli.

Two pointers da yani tek fro döngüsü ile elamn i seçicem daha sonra seçilen i için sort 
edilmiş listenin sağından geziberek bu i değeri için toplamı sıfır veren diğer iki değeri arıycam
bu sayede sadece i için for döngüsü kullanılacak






        '''