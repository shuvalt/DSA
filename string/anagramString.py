def isAnagram(self, s, t):
        map1 = {}
        map2 = {}
        for char in s:
            if(char not in map1):
                map1[char] = 1
            else:
                map1[char] += 1
        for char in t:
            if(char not in map2):
                map2[char] = 1
            else:
                map2[char] += 1
        if(map1 == map2):
            return True
        return False
