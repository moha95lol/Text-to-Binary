f = open('TB.txt', 'r')

class Encrypt():
    def character(ch):
        global f
        for line in f.readlines():
            if line[0] == ch:
                index = 1
                List = []
                while index < 9:
                    List.append(line[index])
                    index += 1
                I = ''.join(List)
                return I
            
    def word(word):
        global f
        II = []
        for i in range(len(word)):
            for line in f.readlines():
                if line[0] == word[i]:
                    index = 1
                    List = []
                    while index < 9:
                        List.append(line[index])
                        index += 1
                    I = ''.join(List)
            II.append(I)
        LLL = ''.join(II)
        return LLL

            
