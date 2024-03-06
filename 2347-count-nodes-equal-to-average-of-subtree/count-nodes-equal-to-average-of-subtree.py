class Solution:
    def __init__(self):
        self.matching_subtree_count = 0  

    def calculate_subtree_values(self, current_node):
        if current_node is None:
            return 0, 0  

        left_subtree  = self.calculate_subtree_values(current_node.left)
        right_subtree = self.calculate_subtree_values(current_node.right)

        sum_of_values  = left_subtree[0] + right_subtree[0] + current_node.val
        number_of_nodes  = left_subtree[1] + right_subtree[1] + 1

        if sum_of_values // number_of_nodes == current_node.val:
            self.matching_subtree_count += 1

        return sum_of_values, number_of_nodes  

    def averageOfSubtree(self, root):
        self.calculate_subtree_values(root) 
        return self.matching_subtree_count
