class Solution:
    def findingUsersActiveMinutes(self, logs, k):
        dictionary = defaultdict(set)

        for id_, time_ in logs:
            dictionary[id_].add(time_)
        result = [0] * k

        for ts in dictionary.values():
            result[len(ts) - 1] += 1

        return result