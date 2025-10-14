class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def _generateParenthesis(curr_comb, open_count, close_count):
            if open_count == n and close_count == n:
                result.append(curr_comb)
                return
            if open_count < n:
                _generateParenthesis(curr_comb + "(", open_count + 1, close_count)
            if close_count < n and open_count > close_count:
                _generateParenthesis(curr_comb + ")", open_count, close_count + 1)

        result = []
        _generateParenthesis("", 0, 0)
        return result