# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
            curr=head#head ile başlıyoorum
            prev=None#Bir tane değişken atamamı sağlayacak prev değer
            while curr:

                next_node=curr.next     
                curr.next=prev

                prev = curr
                curr = next_node


            return prev



        




                #Son elemanın yeni head olması gerekli

                










'''

PROBLEM:

Tek yönlü birbirine bağlanmış bir linked list cerilmiş bizden istenen bu listeyi ters çevirmemiz.

Linked list'ler her eleman için elemanın kendisini bir de sonraki elemana bağlanan bir yapıya sahiptir.
İkinci bilgi listenin diğer elemanına bağlanmak için saklanan bir bilgi gibidir.

Head-->Data-Next-->Data-Next-->Data-Next    şeklinde bir yapıdır.Bunu ters çevirmek için son eleman
head olarak tanımlanmalı ve bağlantılar 1 den 2 ye 3 e değil de 3 ten bire olacak şekilde güncellenmeli
Bunun için her liste elemanının next değerini saklayıp bunu kendisinden önceki listeye yönlemdirmemiz 
gerekli

Linked list ler bir class yapısı ile oluşturulur ve takip edilmesi gereken üç bilgiye sahipti 
data(value),prev(ikililerde),next.



*********ÇÖZÜM*********

Çözüm aşamasında teoride çok takıldım.Biraz daha düz bir mantık ile her liste elemanının next 
'ini prev değere atadım ve bir sonraki elemana geçtim









'''