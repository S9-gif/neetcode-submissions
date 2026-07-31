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



        sol_swap = self.invertTree(root.left)#Burdan örnek vericek olursak 2 için değiştirmeyi yaptık aynısını 3 için de yaptık
        sag_swap = self.invertTree(root.right)

        #İlk swaplama bitti bunları tuttum değişkenlerde şimdi 1 için root da swaplama yapıcam


        root.left=sag_swap #Bu değiştirilmişleri yer değiştirdik
        root.right=sol_swap








        return root




















