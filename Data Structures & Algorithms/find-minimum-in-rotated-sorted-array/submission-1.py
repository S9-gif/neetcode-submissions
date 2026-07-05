'''1-Find Minimum in Rotated Sorted Array'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l,r=0,len(nums)-1       #Sol ve sağ imleçler



        while l<r:

            mid=(l + r) // 2     #Burda neden direkt olarak açıklığı r-l ile hesaplayıp bunun ortasını almadık?
                                                #Ortanca konumu böyle bulamaz mıydım?



            if nums[mid]>nums[r]:       #Kırılma noktası sağda kalıyor demek bu yüzden sağa yönelicez l pointer sağa çekilmeli

                l=mid+1

            else:  #Kırılma noktası solda kalıyor demek bu yüzden sola yönelicez r pointer sola çekilmeli

                r=mid


        return nums[l] #Bunun gibi bir şey yapabilir miyim?



















'''


Problemimiz eşsiz elemanlardan oluşan ve döngüye uğramış bir liste için kırılma noktasını bulmamızı 
istiyor.


*********ÇÖZÜM*********

Verilen eşsiz elemanlardan oluşan ve döngüye sokulmuş listemiz için kırılma noktası aramaktayız.
Bunun için binary search ile arama alanımızı daraltalaeak ilerlemeyi tecih ettik.l ve r imleçlerimizi
yerleştirdik ve l<r olduğu sürece döngüye soktuk.Döngümüzde bu imleçleri güncelleyerek ilerleyeceğiz.
Daha sonra kırılma noktaısnın listede nerede kaldığını hesaplayabilmek için yön belirlememiz gerekti
.Biz de bunu için mid değeri bulduk ve bu mid değer için sol ve sağ imleçte anormallik aradık.Anor
mall,k olan tarafta kırılma noktamız olduğunu bildik ve o alana doğru imleçlerimizi daralttık.


En son daralamayacak noktaya geldiğinde çıktıyı verdik.






'''













