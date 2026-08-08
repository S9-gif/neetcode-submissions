# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        #Base case:
        if root is None:
            return []


        queue = deque([root])    #deque objesi FIFO ya da LIFO yapısı için gerekli
        sonuc = []
    
        while queue:
            level_listesi=[]
            for i in range(len(queue)):
                x=queue.popleft()
                level_listesi.append(x.val)

                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)

            sonuc.append(level_listesi)
      
    
        return sonuc












'''
Problem:
*Bana verilen binary tree'nin root'u.Benden istenen tüm ağaç yapısını seviylerine göre ayırmam.
*Bunu da BFS algoritmasını gruplama yaparak çözebilirim.


*********Çözüm:*********


*BFS algoritması her ağaç dalının sıra ile keşfedilmesini sağlar.DFS gibi en derine
kadar inmez.Aslında benim burda istediğim seviye gruplamasını roota olan uzaklıklara
göre yapmaktı.Hatta bunun için önceki sorulardaki maxdepth fonksiyonunda da 
yararlanmayı düşündüm.Ama hem claude un yönlendirmesi hemde youtube da izlediğim
videolar saysesinde BFS algortimasını sadece ekstra bir yapı ile gruplama için kullan
maya kara verdim.


*   Kod nasıl işliyor:

Her recursive algortimada olduğu gibi burda da bir base case'im var.Kod bu sayede dön
güden çıkabilecek.Daha sonra bu problemde öğrendiğim ve FIFO ile LIFO yapmamıza yardımcı olan deque objesin queue oluşturmak için kullandım ve ilk eleman olarak da 
başlangıç noktamız root'u verdim.while döngüsü ile bu queue yapımdaki elemanlar 
bitene kadar döngüme devam ettim.Dmngü içerisinde her queu elemanını doğru sıra ile yazabilemk için döngü içinde local bri liste oluşturdum.İşi biten elemanlar burdaki
level_listesine val olarak ekleniyor.Burdan da final hali olarak bütünü sonuc adlı
listeye ekleniyor.Aynı zamanda queue listesine de aktif olarak sonraki elemanlar
varsa onları eklemem gerektiğinde if koşulları ile kontrol edip queue ya objelerini
ekliyorum.

Olay,zorluk tamamen queue yapısını ve onun LIFO FIFO yapısını anlayıp işleyebilmekte.









'''