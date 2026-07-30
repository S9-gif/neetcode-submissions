# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next




class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        # Daha önce yazdığın iki listeyi merge eden fonksiyon
        def mergeTwoLists(l1, l2):
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            tail.next = l1 if l1 else l2
            return dummy.next
        
        # Divide and conquer: liste sayısı 1'e inene kadar ikişerli merge et
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    merged = mergeTwoLists(lists[i], lists[i + 1])
                else:
                    merged = lists[i]  # eşi olmayan liste olduğu gibi kalıyor
                merged_lists.append(merged)
            lists = merged_lists
        
        return lists[0]








'''
Problem:

Bize k sayıda küçükten büyüğe sıralanmış linked list'leri içeren 'lists' adında bir liste verilmiş:
Input: lists = [[1,2,4],[1,3,5],[3,6]]

Bizden istenen,verilen linked listleri sıralayarak tek bir linked list olarak döndürmek.



*Daha önceden buna benzer bir soru çözmüştük diye hatırlıyorum onda iki tane linked list 
birleştiriliyordu.

*Burda sorun olabilecek şey linked list'lerin head'leri bize doğrudan verilmemiş yani liste içinden
kendimiz ulaşmalıyız.Her linked list için head'e ulaştıktan sonra önceki problemde yaptığımız karşılaştırma
işlemlerini... hmmmm listemde k tane liste var yani kaç tane listeyi merge edeceğimi bilmiyorum.
Yazdığımız kodun otomatik k tane listeyi merge etmesi lazım ama bu noktada da yanlış düşündüğümü 
düşünüyorum.
*Asıl problem kaç tane linked list'e sahip olduğumuzu bilmiyor olmak.
*Topic'lerde verilen en dikkat çekici başlık divide and conquer.Bu da her adımda ikiye bölerek
işlem yapmayı içeriyor.

* bunlar artan linked liste oldukları için her linked list'in ilk elemanı(head'i) aslında en küçüğü olacak 
bu da karşılaştırbilmek için uygun.
* bence her türlü if blokları ile bir karşılaştırma işlemi yapacağız ama sorun kağıttan olması
* for döngüsü ile elimde ne liste elemanı varsa gezebilirim her bulunduğum listede bir tane head alırım
Kenara koyarım sonra aynısını ikinci döngüde de bir hediye alırım ilk alınan ile(iki for döngüsü olacak)
Sürekli karşılaştırılarak merge edilecek.


*Divide and conquer ile önceki merge etmeyi entergre ettik her adımda iki liste merge edilecek.



*Amaç lists listesini sürekli olarak ikiye bölmek.Elimizde iki liste kalınca bu iki liste elemanını
merge etmek.


*Ama nasıl gruplama yapacağımı anlayamadım bu nedenle çözüme yöneliyorum.


*********Çözüm:*********



Ya bence claude kafamı karıştırdı benim ben ne güzel for döngüleri ile gezinip sıra iile merge edicektim
bana verimsiz olur bişyler dedi engelledi.
Her adımda for döngüleri ile aldığım iki linked list elemanını merge ederdim sadece
Evet verimsiz olurdu ama yine de lineer zamanda çözülürdü.

Ama çözümde de bunu önermiyor.Keza algoritmayı açıklarken de üstte yazdığımdna farklı bir şey demiyor.
Anlamadığım şey koda nasıl dökücek olmamız.












'''