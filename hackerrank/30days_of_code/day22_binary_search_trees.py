class Node(object):
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution(object):
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        if root is None:
            return -1
        else:
            left_height = self.getHeight(root.left)
            right_height = self.getHeight(root.right)

            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1


T = int(input())

myTree = Solution()
root = None

for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)

height = myTree.getHeight(root)
print(height)
