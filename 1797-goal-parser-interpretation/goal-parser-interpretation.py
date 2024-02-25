class Solution:
    def interpret(self, command: str) -> str:

        interp = []
        i = 0
        while i < len(command):
            c = command[i]
            if c == 'G':
                interp.append('G')
            if c == ')':
                interp.append('o')
            if c == 'l':
                interp.append('al')
                i += 1
            i += 1
            


        return "".join(interp) 