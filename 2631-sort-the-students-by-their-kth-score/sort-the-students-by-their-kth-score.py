class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        # Sort each student's scores by the kth score in descending order
        # sorted_scores = sorted(score, key=lambda student: student[k], reverse=True)
        # return sorted_scores
        return sorted(score, key=lambda student: student[k], reverse=True)