'''2-Prerequisites'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            # Sol yarı sıralı mı?
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # Sağ yarı sıralı
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1






            











'''


PROBLEM:

Verilen ve yine döngüye tabi tutulmuş ,eşsiz elemanlardan oluşan bir dizi için bizlere target değer
veriliyor.İstenen target değer dizide varsa indeksini döndürmek yoksa -1 döndürmek.
Ve bunu binary search ile O(logn) sürede yapmamız isteniyor.



Bu döngüye tabi tutulmuş dizi aslında yine sıralı olacaktır he ne kadar sırası bozulmuş olsa da
misal[3,4,5,6,1,2] şeklindei bir dizi için hedef değer 1 olsun.Binary searvh ile ararken yine bir mid
indeks kullanabilir ve bu mid indekse göre arama yönümü belirleyebilirim.


*********ÇÖZÜM*********


Aslında iki binary search sorusu birbirinin aynısı.Sadece bu seferseçtiğim yarının sıralı olup olmadığı
kontrolünü sağladım bunu da target değeri atlamamak için 
yaptım, o yüzden bir iki değişken değiştirmesi il aynı 
soruyu yazdık.Zaten binary search için de farklı bir soru tipi yok anladığım kadarıyla.





'''











