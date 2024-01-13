def wordPattern(self, pattern, s):
        p = list(pattern)
        string = s.split(" ")
        map1 = []
        map2 = []
        for i in p:
            map1.append(p.index(i))
        for i in string:
            map2.append(string.index(i))
        if(map1 == map2):
            return True
        return False
