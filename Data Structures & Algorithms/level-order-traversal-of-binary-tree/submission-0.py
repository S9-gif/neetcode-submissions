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









'''