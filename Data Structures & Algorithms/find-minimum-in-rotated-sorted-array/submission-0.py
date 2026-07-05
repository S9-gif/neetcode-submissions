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







'''













