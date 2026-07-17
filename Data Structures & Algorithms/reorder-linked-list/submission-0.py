# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        


        slow=head
        fast=head

        while fast is not None and fast.next is not None:
            
            slow=slow.next
            fast=fast.next.next

        #Bu döngü bittiğinde slow pointerı ortancada olacak yapmamız gereken bu noktada listeyi bölmek
                
        second_half_head = slow.next   
        slow.next = None   

        #Şimdi de bu yeni head'imi kullanarak reverse edicem

        curr2=second_half_head#head ile başlıyoorum
        prev=None#Bir tane değişken atamamı sağlayacak prev değer
        while curr2:

            next_node=curr2.next     
            curr2.next=prev

            prev = curr2
            curr2 = next_node


        second_half_head=prev #prev aslında yeni head olacak burda return etmiyorum sadece oluşturuyorum return edersem kod durur ve çıktı vermeye çalışır ama biz daha merge edicez.

        #Bu sayede de ikinci listemi de ters çevirmiş oldum şuan elimde şu yapı var:
        #first_half:          0 -> 1 -> 2 -> 3 -> None
        #reversed_second_half: 6 -> 5 -> 4 -> None
        #Şimdi sıra sıra yine bir döngü ile birbirlerine bağlayıp return edicem


        l=head
        r=second_half_head
        while l is not None and r is not None:
            
            l_next = l.next      # l_next = node1 (l.next'i kaybetmeden önce sakla)
            r_next = r.next      # r_next = node5

            l.next = r            # node0.next = node6   → 0 -> 6 bağlandı
            r.next = l_next       # node6.next = node1   → 6 -> 1 bağlandı

            l = l_next            # l artık node1'i gösteriyor
            r = r_next 

            #Bu kısmı kağıtta çizdim orda daha anlaşılır











'''

PROBLEM:
Her zamanki gibi bize linked list'in head'i veriliyor.
Başlangıçta yedi uzunluğundaki bir listenin dağılımı, örnek olarak sıralı biçimde verilmiş.
Bu linked list'i istenilen sırada yeniden oluşturucaz.
Liste,n listedeki eleman sayısı olmak üzere şu kurala göre düzenlenmektedir:
[0, n-1, 1, n-2, 2, n-3, 3]

Ve aynı zamanda modifiye etmek değil de baştan sıralamamız gerektiği belirtilmiş.

Topic olarak da two pointers ve stack konuları verilmiş
O(n) zaman ve O(1) süre istenen özelliklerdir.


---------------------------------

*Başlık olarak two pointer vermiş ideal çözümde bunun olması gerekli fakat burda nasıl kullanıcam.--Two pinters linked list'innortancasını bulmak için kullanıldı
*Öncelikle sorunu tanımlayalım elimizde bir linked list'in head'i var ve biz bu head sayesinde sıra
sıra liste elemanlarına ulaşıyorum.Problemin benden istediği verilen linked list için belli bir 
düzende bunu yeniden sıralamam yani düzenlemem gerekli.

*n burda listedeki eleman sayısıdır yani listenin uzunluğu aslında lazım olusa bir sayaç ve döngü ile
n'e ulaşabilirim.-->ama n'e ulaşmam önemli değil ,yani n'i kullanarak çözüme ulaşmayacağım.

*Burda ,indeksler ile değil de listeleme kuralı aslında şunu göstermekte sıra  ile ilk soldan eleman
yaz bir arttır,soldan eleman yaz bir arttır şekline ilerliyor.İki pointer de none olduğunda listem 
istendiği gibi düzenlenmiş olacak.

Pekii biz linked list kullandığımız için burda nasıl ilerleyeceğiz elimizde sadece head var ben 
nasıl left ve right pointerlar ile teker teker bunu yazdıracağım kilit nokta burası.Topiclerden 
anladığım kadarı ile stack kullanacağım ama yine burda linked list problem yaratıyor çünküü hiçbir
şeyi normal listelerde olduğu gibi yapamıyorum.

*Claude beni şöyle düşünmeye yönlendirdi.Ya bu linked list'i ortadan ikiye bölebilsek ve listenin sonunda
yer alan kısmı ters çeviriğ sıra sıra bunları bastırabilsek? Sonuçta bir soldan bir sağdan 
elemanları bastırıcam bunu yapabilmek için listeyi ortadan bulmam gerekli.

*Bu noktada çok akılcı bir işlem yapıyoruz fast ve slow pointer mantığı bir pointer diğer pointerın
iki katı hızda ilerlerse her adımda,fast pointer bütün listeyi gezip None olduğunda slow pointer 
listenin yarısına gelmiş olacak.Yani listenin orta elemanı slow pointer olmuş olacak.Burası ayırma
noktam.

*Ortanca ile birlikte ilk yarıyı bitirmiş olacağız None yaparak ve öncesinde nexxt ile ikinci parçanın
başını belirticez.İkinci listenin head'ini kullanarak ters çeviricez.



**O zaman yapacaklarım:
Öncelikle baştan iki pointer ile başlayacağım ve bu iki pointerın her döngüdeki hızı bire iki oranında olacak ki hızlo olan pointer bitince slow pointer ortancaya denk gelmiş olsun.
Bu noktada slow pointer ortancada yani yapılması gereken ortanca elemana göre burdan ayırmak.Bunu da önce next elemanını bir yerde tutup sonra next elemanı None yapmak bu sayede iki tane head 'im olmş olacak
Sonra elimde bulunan ikinci head ile ters çevirme işlemi yapacağım ve final olarak sırası ile listeleri birbirleri ile bağlıycam 
ama bu işlem adımları sırasında çok döngü yok mu yoksa tek while döngüsünde mi yapıcam--> Evt bunların her birine bir while döngüsü denk gelecek




*********ÇÖZÜM*********

Çözüm aşamalarım çözümün anlaşılması için yeterlidir.




'''