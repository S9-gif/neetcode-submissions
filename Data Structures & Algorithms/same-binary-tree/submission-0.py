'''3-Same Binary Tree'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        

    

        # 1. durum: ikisi de None
        if not p and not q:
            return True

        # 2. durum: biri None, diğeri değil
        if not p or not q:
            return False

        # 3. durum: ikisi de dolu -> değer kontrolü + iki recursive çağrı
        return (p.val == q.val) and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)










'''
Problem:

p ve q olmak üzere iki b-tree'nin root'ları bize verilmiş.
Sorunun bizden istediği bu iki b-tree'nin aynı yapıya sahip olup olmadığını belirlememiz.
Aynı ise true değil ise false döndürmemiz isteniyor.



*Verilen iki root'a bağlı tree'ler birebir aynı olabilir-->True
*Verilen iki root'a bağlı tree'lerin dizilişleri farklı olabilir-->False
*Verilen iki root'a bağlı tree'ler None olabilir-->True

Bunlar Base case'lerim olacak bu durumlar için recursive bitmeli




*********Çözüm:*********


Problemde safhasında da bahsettiğim gibi incelenmesi gereken üç durum var None koşullarını 
kontrol ederken recursion yapmamıza gerek yok.Tam uyum aradığımızda fonksiyonlara doğru 
parametrelreri verdik.



'''