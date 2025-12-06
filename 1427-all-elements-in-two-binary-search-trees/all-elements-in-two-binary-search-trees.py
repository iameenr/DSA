from collections import Counter

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder_traversal(node: Optional[TreeNode], values: List[int]) -> None:
            """inorder traversal and collecting node values."""
            if node is None:
                return
            inorder_traversal(node.left, values)
            values.append(node.val)   # <-- FIXED: use .val
            inorder_traversal(node.right, values)

        def merge_sorted_lists(list1: List[int], list2: List[int]) -> List[int]:
            """Merge two sorted lists into one sorted list."""
            merged_list = []
            index1 = index2 = 0

            while index1 < len(list1) and index2 < len(list2):
                if list1[index1] <= list2[index2]:
                    merged_list.append(list1[index1])
                    index1 += 1
                else:
                    merged_list.append(list2[index2])
                    index2 += 1

            while index1 < len(list1):
                merged_list.append(list1[index1])
                index1 += 1

            while index2 < len(list2):
                merged_list.append(list2[index2])
                index2 += 1

            return merged_list

        values1, values2 = [], []
        inorder_traversal(root1, values1)
        inorder_traversal(root2, values2)

        return merge_sorted_lists(values1, values2)
