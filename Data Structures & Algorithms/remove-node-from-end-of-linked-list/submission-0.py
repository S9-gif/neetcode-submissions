# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head
        L=dummy
        R=dummy

        for i in range(n + 1):
            R = R.next


        while R is not None:
            L = L.next
            R = R.next
            #Bu döngü bittiğinde L istenen yerde olacak ve silme işlemini yapıcaz.
            
        L.next=L.next.next

        return dummy.next











'''

Problem:


Verilen n değeri, linked list'in en sonundan sileceğimiz node'u işaret eder.
1,2,3,4,5 şeklindeki bir liste ve n=2 için sondan 2. node 4 olacağı iç,n 4 silinir ve yeni liste 
1,2,3,5 olacaktır.

*Başlık olarak two pointers verilmiş 
*Benim düşüncem de listeyi ters çevirmek.Listeyi ters çevirdikten sonra bir şekilde belirtilen indeksi
anlamak ve silip kalan iki node u birbirine bağlamak.

*Two pointer ile nasıl sondan ilerleyebiliirm.Şöyle ki mesela bi tane L pointer olsun bi tane de 
en sonda R pointer olsun.Bu durumda L pointerı R ile hareket ettirebliriz.
*Ama R imleci nasıl sona koyucam ki linked listlerde indeksleme yok.Bu nedenle L imleci ana listede 
gezinirken R imleci de ters çevirilmiş listede gezinecek ve bunu birlikte yapıcaklar.


*Sırf two pointer başlığı olduğu için böyle garip bir çözüm yöntemi buldum yoksa yapacağım şu:
Listeyi ters çevir,bir sayaç değişken tut bir yandan da imleç ile listenin head node'undan başlayarak geezmeye başla
bu sayaç n'e eşit olunca dur ve pop ile sil ya da remove et,daha sonrasilinmeden kaynaklı iki node arası bir kopukluk olacak
aslında bu kısmı silme işleminden önce yapmalıyım çünkü silince ulaşımım kalmaz bunları silme işleminden
önce tuttuğumuzu varsayarsak bunları birbirine bağlıycam sonra.Ama claude'un dediği gibi şöyle bir sorun var.
Benim listem şuan ters o yüzden bi ters çevrime işlemi daha yapmam gerekecek.Bu adımla birlikte de 
bu mantık da arap saçına döndü


*
tamam anladım her şeyi adım adım açıklıyayım:

n=lenlist hariç açıklama yapıyorum ona sonra değineceğim

Öncelikle sondan n.node'u silmek ve listeyi yeniden yazdırmak istiyoruz.Bunun için şöyle
düşündük.Tıpkı daha önceki problemlerde buludğunuz tavşan ve kaplumbağa node'lar gibi burda 
da ona benzer bir işlem yaptık L sabit iken R n kadar ilerletildi.Daha sonra bizim ihtiyacımız 
head de bulunan L ile n +1 birim uzaktaki R arasındaki sabit uzaklık.Burda amaça bu ikisini 
ideal uzklıkta ayırdıktan sonra birlikte ilerletmek.(R'yi L imlecinden n+1 uzatmamızdaki neden
de linked list'lerde bir node silinmek isteniyorsa ondan önceki node ile yapılabilir bu işlem.)
Taa ki R listenin sonuna gelene kadar.R listenin sonuna geldiğinde (aslında R imleci None
olduğunda) döngü biter ve L imleci sondan n uzaklıktaki node da bulunur bu da silmek
istediğimiz node'un bir önceki node'una karşılık gelmekte.Daha sonra ilgili node 
silinmeden bağlamak için bilgilerini geçici olarak saklayıp listeyi yeniden bağlıyoruz ve 
head ile çıktı veriyoruz.









'''