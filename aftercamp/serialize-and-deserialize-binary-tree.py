# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'None'
        
        val1 = self.serialize(root.left)
        val2 = self.serialize(root.right)

        return str(root.val) + '.' + val1 + '.' + val2

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = data.split('.')
        
        def rec():
            val = arr.pop(0)
            if val == "None":
                return None
            
            newNode = TreeNode(int(val))
            newNode.left = rec()
            newNode.right = rec()
            return newNode
        return rec()
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))