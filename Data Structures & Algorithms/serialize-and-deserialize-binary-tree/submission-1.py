# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def inorder(self,root:Optional[TreeNode],counter:int)->str:
        if root==None:
            return ''
        res1=self.inorder(root.left,counter+1)
        res2=self.inorder(root.right,counter+1)

        return res1+str(root.val)+':'+str(counter)+','+res2

    def preorder(self,root:Optional[TreeNode],counter)->str:
        if root == None:
            return ''
        
        res1=self.preorder(root.left,counter+1)
        res2=self.preorder(root.right,counter+1)

        return str(root.val)+':'+str(counter)+','+res1+res2




    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        str1=self.inorder(root,0)
        str2=self.preorder(root,0)

        return str1+'|'+str2

    def buildTree(self, preorder: List[str], inorder: List[str]) -> Optional[TreeNode]:

        indpre=0
        ind=-1

        for i in preorder:
            indpre+=1
            if i in inorder:
                ind=inorder.index(i)
                break
        if ind==-1:
            return None
        val=inorder[ind].split(':')[0]
        head=TreeNode(val,None,None)
        head.left=self.buildTree(preorder[indpre:],inorder[0:ind])
        head.right=self.buildTree(preorder[indpre:],inorder[ind+1:])

        return head
     
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr=data.split('|')
        inord=arr[0].split(',')
        preord=arr[1].split(',')
        inord=[s for s in inord if s!='']
        preord=[s for s in preord if s!='']

        print(inord,preord)

        head=self.buildTree(preord,inord)
        return head

            
