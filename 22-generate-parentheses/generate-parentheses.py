class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def _generateParenthesis(open_count, close_count, paran):
            if open_count == n and close_count == n:
                well_formed_paranthesis.append("".join(paran))
                return

            if open_count < n:
                _generateParenthesis(open_count+1, close_count, paran + ['('])
            if close_count < open_count and close_count < n:
                _generateParenthesis(open_count, close_count+1, paran + [')'])
            
        well_formed_paranthesis = []
        _generateParenthesis(0, 0, [])
        return well_formed_paranthesis