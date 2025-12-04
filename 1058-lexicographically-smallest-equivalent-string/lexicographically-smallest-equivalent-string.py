class Solution:
    def smallestEquivalentString(self, string1: str, string2: str, base_string: str) -> str:
        parent = list(range(26))  # UnionFind parent array

        def find_root(char_index: int) -> int:
            """Find the root representative of a character index."""
            if parent[char_index] != char_index:
                parent[char_index] = find_root(parent[char_index])
            return parent[char_index]

        # Union step -- merge equivalence classes
        for index in range(len(string1)):
            char1_index = ord(string1[index]) - ord('a')
            char2_index = ord(string2[index]) - ord('a')

            root1 = find_root(char1_index)
            root2 = find_root(char2_index)

            if root1 < root2:
                parent[root2] = root1
            else:
                parent[root1] = root2
        result_chars = []
        for char in base_string:
            char_index = ord(char) - ord('a')
            smallest_equivalent = chr(find_root(char_index) + ord('a'))
            result_chars.append(smallest_equivalent)

        return ''.join(result_chars)