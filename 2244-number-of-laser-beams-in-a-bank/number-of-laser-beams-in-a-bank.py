class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total_beams = 0
        prev_devices = 0

        for row in bank:
            devices = row.count("1")
            if devices > 0:
                total_beams += prev_devices * devices
                prev_devices = devices

        return total_beams
