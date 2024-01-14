def canConstruct(self, ransomNote, magazine):
        ran = {}
        mag = {}
        for char in ransomNote:
            if(char not in ran):
                ran[char] = 1
            else:
                ran[char] += 1
        for char in magazine:
            if(char not in mag):
                mag[char] = 1
            else:
                mag[char] += 1
        for item in ran:
            if(item not in mag):
                return False
            elif(ran[item]>mag[item]):
                return False

        return True
