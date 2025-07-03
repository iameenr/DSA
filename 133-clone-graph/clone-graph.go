/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Neighbors []*Node
 * }
 */

func cloneGraph(node *Node) *Node {
	if node == nil {
		return nil
	}

	cloned := make(map[*Node]*Node)

	var dfs func(node *Node, clone_node *Node)
	dfs = func(node *Node, clone_node *Node) {
		clone_node.Val = node.Val
		cloned[node] = clone_node

		for _, neighbor := range node.Neighbors {
			if _, found := cloned[neighbor]; !found {
				clone_neighbor := &Node{}
				dfs(neighbor, clone_neighbor)
				clone_node.Neighbors = append(clone_node.Neighbors, clone_neighbor)
			} else {
				clone_node.Neighbors = append(clone_node.Neighbors, cloned[neighbor])
			}
		}
	}

	clone_head := &Node{}
	dfs(node, clone_head)
	return clone_head  
}