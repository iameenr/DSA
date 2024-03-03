class Solution:
    def slowestKey(self, release_times: List[int], keys_pressed: str) -> str:
        key = [keys_pressed[0]]
        max_duration = release_times[0]

        for i in range(1, len(release_times)):
            if release_times[i] - release_times[i - 1] == max_duration:
                key.append(keys_pressed[i])

            if release_times[i] - release_times[i - 1] > max_duration:
                max_duration = release_times[i] - release_times[i - 1]
                key = [keys_pressed[i]]


        return max(key)