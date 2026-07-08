'''2-Prerequisites'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[l]<=nums[mid]:      #   Sol yarı için
                if target<nums[l] or target> nums[mid]:     #target değer sol imleçten küçük veya target mid değerden büyük yani target değer sol yarı ile uyuşmuyor ise arama için sol yarı daraltılır.
                    l=mid+1

                else:                                       #Sol yarı için böyle bir durum yoksa sağdan kısılır.

                    r=mid-1

            else:

                if target>nums[r] or target<nums[mid]:          #Aynı mantıktaki işlemleri sağ yarı için de yaparım.
                    r=mid-1

                else:
                    l=mid+1

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

Şöyle bir durumla karşılaşabilriz. [3,4,5,6,7,0,1,2,3] listesi için hedef 1 olsun mid değer ilk durumda
7 olacaktır 7 mid değeri için target 1 ,7 değerinden küçüktür ama sola yarıdaki tüm değerler de 
aslında 1 gibi 7 den küçük .Dizinin sol parçası için target ile mid ve l pointer uyuşmuyorsa bu l 
pointer'ı daraltmamız anlamına gelmekte.Aynı kontrolü sağ için de yaptık.





Aslında problemde anlaşılmayacak bir şey yok önceki problemde olduğu gibi düşündüğüm için çıkmaza girdim.

'''











