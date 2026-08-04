'''1-Invert Binary Tree'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:


        if root is None:
            return None


        tmp=root.left
        root.left=root.right
        root.right=tmp


        self.invertTree(root.left)
        self.invertTree(root.right)





        return root







'''


Problem:
Bana bir root vermiş binary tree ye ait istenen bütün left Right iklimlerinin
Yerlerinin değiştirmem left = wright yeni right = left yeni olacak

*********Çözüm:*********

*Her seviyedeki her node L-R swap oluyor.
* invert(3) üç node nu altındaki nodeları swap ediyor.
*Önce iki ile üçü swap ettim sonra bu swap edilenleri root'un yeni sağı ve solu olarak değiştirdim.

'''








