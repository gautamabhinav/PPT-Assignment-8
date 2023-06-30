from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def str2tree(s):
    if not s:
        return None

    stack = []
    i = 0
    while i < len(s):
        if s[i] == ')':
            stack.pop()
            i += 1
        elif s[i] == '(':
            i += 1
        else:
            j = i
            while j < len(s) and s[j] not in ['(', ')']:
                j += 1
            val = int(s[i:j])
            node = TreeNode(val)
            if stack:
                parent = stack[-1]
                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node
            stack.append(node)
            i = j

    root = stack[0]
    return root

def levelOrderTraversal(root):
    if not root:
        return []

    result = []
    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        level_vals = []

        for _ in range(level_size):
            node = queue.popleft()
            level_vals.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.extend(level_vals)

    return result

# Example usage
s = "4(2(3)(1))(6(5))"
root = str2tree(s)
output = levelOrderTraversal(root)
print(output)
