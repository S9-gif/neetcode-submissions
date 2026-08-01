'''2-Maximum Depth of Binary Tree'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        

        if root is None:    #Base koşulum recursion için.
            return 0


        
        left_d = self.maxDepth(root.left)    
        right_d = self.maxDepth(root.right)

        #maxDepth fonksiyonu işi yapan gömülü bir fonksiyon
        depth=1+max(left_d,right_d)

        return depth



'''
Problem:

Maksimum derinliği bulmamızı istiyor binary tree yapısı için en derin depth sorulmuş.



*********ÇÖzüm:*********
*recursion ile maxDepth() fonksiyonunu sürekli çalıştırdım bunu kendisi yapmakta zaten bunu da claude 'a sorarak öğrendim .Böyle bir fonksiyon var mı diye.Daha sonra root'U da unutmadan ki bence kritik nokta burası çünkü derinlik her eleman seviyesi ve maxDepth(root.left)   diyerek aslında root haricinde almış oluyoruz o yüzden buna da 1 ekledim . Aynı zamanda şunu da öğrendim tree lerde node bir obje yapısı olduğu için bir sonraki eleman boş ise none olabilir 0 değil.

Recursion üzerinde durmam lazım
'''



