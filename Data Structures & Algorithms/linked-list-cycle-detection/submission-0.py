# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        visited=set()

        curr=head

        while curr is not None:

            visited.add(curr)    
            curr=curr.next

            if curr in visited:
                
                return True
                
        return False
            









'''
PROBLEM:
Verilen linked list içinde bir cycle varsa true döndürmemiz isteniyor.


*Problemde gezinirken cycle olup olmağığını kontrol etmemiz isteniyor.
*Peki bir iç döngü cycle 'ın varlığını nasıl kontrol ederiz.
*Verilen örnekte hem birin hem de dördün next node'u aynı liste elemanını göstermekte.Yani verilen 
listede en az iki tane aynı next node varsa bu listede cycle vardır.

*Ama iki tane next node'u karşılaştırmak pek doğru değil gibi.Bunun yerine şunu düşünebilriz:cycle için
daha önce gördüğüm elemanları görmeye başlamam lazım mesela burdaki örnekte 2'yi gördüm bir daha
görüyorsam cycle olduğu anlamına gelcek.
*Bunun için de bu node'u gördüm mü sorgusu yapmama lazım yani her gördüğüm node'u set veri tipine 
atmam gerekli.Kontrolü burdan sağlayacağım. cycle içine girdiğim anda döngüden çıkmam gerekli yoksa
sonsuz döngü olur.
*Ve aynı zamanda current=current.next ile gezineceğim için 
*Yani tanıdık eleman görüldüğü anda döngü biter ve true döndürülür.
current in visited DÖNGÜ KOKŞULUM


*Aynı zamanda bize indeks verilecek bu indeksin olduğu noktada bir cycle araştırması yapacağım






*********ÇÖZÜM*********


Çözüm aşamasında yazdığım sözde kodlar ve düşüncelerim bu problem için yeterli bir açıklamadır.


'''