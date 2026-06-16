class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        liste = [1] * len(nums)
        # -->[0,0,0,0] şeklinde bir dizi oluşturmuş oldum işlemlerimi buraya ekliycem.
        #liste[0] = diğer elemanlar çarğımı
        i = 0

        while i < len(nums):

            for j in list(range(0, i)) + list(range(i+1, len(nums))):
                
                liste[i] *= nums[j]

            i = i + 1

        return liste


                

                

















        """
PROBLEM:
Verilen nums dizisi için her eleman için kendisi hariç diğer tüm sayıların çarpımını döndürücez
Yani dizinin birinci elemanı için karşılık gelecek değer birinci eleman hariç diğer tüm elemanların 
çarpımı.




* i̇ki tane for döngüsüyle i. İndeks hariç diğer elemanlara ulaşabilirim fakat burdaki sorun
Her j elemanının çarpımını birikimli olarak eklememiz gerektiği.





        """
