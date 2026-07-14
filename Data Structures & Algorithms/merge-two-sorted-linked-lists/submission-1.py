'''2-Merge Two Sorted Linked Lists'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        curr1=list1
        curr2=list2

        dummy=ListNode()    #Burda birnevi bir liste oluşturacağım.
        tail=dummy  #Oluşturduğumuz listenin son elemanını takip edecek

        while curr1 and curr2: #İki listeden birinde bile elaman none olmadığı sürece while döngüsü sürmeli

            if curr1.val == curr2.val:
                
                #curr1 i mevcut eleman yap ve curr1 i bir sonrak node a geçir,curr2 kalsın

                tail.next=curr1
                curr1=curr1.next
                tail=tail.next

            elif curr1.val > curr2.val:

                #curr2 i mevcut eleman yap ve curr2 i bir sonrak node a geçir,curr1 kalsın büyük olduğu için çünkü küçükten büyüğe sıralıyoruz.

                tail.next=curr2
                curr2=curr2.next
                tail=tail.next


            else:
                #Karşılaştırma sonucu küçük olarak görülen curr ü nasıl ekleyeceğim?Galiba başka bir değişkene daha ihtiyacım var.
                #Bu noktada problemin en başında bulunan list node sınıfından yararlanacağım list node ilk elemanı 0 ve nexti none olan bir head objesi
                #Burayı ekstra değişkenim olarak kullanabilirim.Geçici değişken gibi

                tail.next=curr1                
                curr1=curr1.next
                tail=tail.next

        if curr1:
            tail.next = curr1       #Burda önemli bir bug çözüyoruz.Merge edilen iki ilsteden biri bitince while döngüsü de bitecek bu durumda bitmeyen hala elemanları olan bir liste olabilir 
                                    #ve bize bu liste bilindiği üzere sıralı olarak verilmişti. zaten bizim yapacağımız da bu kalan elemanları dummy e eklemek olacak.
        if curr2:
            tail.next = curr2


        return dummy.next














'''

PROBLEM:

İki adet sıralanmış linked list'in head'i yani girişi bize veriliyor.Bizden istenen iki linked list'i
yine sıralı biçimde birleştirmek.


--------------------------------------------------

*Elimdeki değişkenler list1 ve list2 adında head değişkenleri bunlar başlangıç noktaları.
*Yapabileceğimiz şey iki liste için iki tane current olsun.Bu curr değerleri karşılaştıralım küçük 
olan curr değeri mevcut liste elemanı yapalım(Bu noktayı koda nasıl dökerim acaba?) daha sonra eklenen
curr için next nodüle geçilir.next nodül ile önceki sorguda curr olan değer karşılaştırılacak ve küçük
olan eklenecek.Böyle böyle  iki curr da kalmayana kadar devam.Sonra çıktı(çıktıyı head ile döndüürcem ama
kodda nasıl yapıcam)



*********ÇÖZÜM*********  


Çözüm için yukarıda düşündüğümüz şekilde uyguladık.Uygulamam verimlilik açısından daha iyi yazılabilirdi
fakat sorunu çözmektedir.Linked list olduğu için yer tutucuyu da o yipte aldık ilgli eklemeleri bu 
dummy isimli linked list haline getirdik de diyeblilirz.






'''

