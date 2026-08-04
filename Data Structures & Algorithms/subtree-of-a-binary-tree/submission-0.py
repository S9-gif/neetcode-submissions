# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def isSametree(self, root, subRoot):
        
        # 1. durum: ikisi de None
        if not root and not subRoot:
            return True

        # 2. durum: biri None, diğeri değil
        if not root or not subRoot:
            return False

        # 3. durum: ikisi de dolu -> değer kontrolü + iki recursive çağrı
        return (root.val == subRoot.val) and self.isSametree(root.left,subRoot.left) and self.isSametree(root.right,subRoot.right)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        if root is None:
            return False

        
        if self.isSametree(root,subRoot):
            return True

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)












'''
Problem:

*İnput olarak verilen root ve subRoot için root içinde subRoot var mı diye kontrol ediyoruz.
*Root içinde birebir aynı yapı varsa True döndürüyoruz,değilse False.

*Kısacası subRoot root içinde var mıdır.




'''