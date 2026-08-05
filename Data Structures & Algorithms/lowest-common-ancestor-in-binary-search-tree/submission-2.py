# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:


        minik=min(p.val,q.val)
        buyuk=max(p.val,q.val)


        if minik <= root.val and buyuk >= root.val:       #3. Durumumuz base case oldu
            return root



        if minik <= root.val and buyuk <= root.val:

            return self.lowestCommonAncestor(root.left,p,q)
            

        if minik>= root.val and p.val >= root.val:

           return self.lowestCommonAncestor(root.right,p,q)


        




















'''
Problem:

Her bir node'u benzersiz olan b-tree verilmiş.Aynı zamanda bu b-tree 'den  node'lar olan p ve q değerleri verilmiş bizden istenen p ve q'nun
en küçük atası olan node'u bulmak ilk örnekte p=1,q=4 için en küçük ve derindkei ataları 3 node'u.
p=3,q=4 için en yakın ataları 3'ün kendisi olmakta


*********Çözüm:*********

BST'nin sıralı yapısından yararlanarak önce üç durumu (ikisi de küçük → sola in, ikisi de büyük → sağa in, biri küçük biri büyük → root LCA'dır) kavramsal olarak çözdük, sonra kodda TreeNode objelerini `.val` ile karşılaştırmayı, recursive çağrılarda doğru parametreleri (`root.left`/`root.right` ve orijinal `p`/`q` objeleri) göndermeyi, `p`/`q` sırasının garanti olmamasından doğan hatayı `min`/`max` ile düzeltmeyi ve gereksiz `return 0`'ı elemeyi öğrenerek çözümü tamamladık.


'''