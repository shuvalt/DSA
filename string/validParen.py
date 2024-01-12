class Solution(object):
    def isValid(self, s):
        obj = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        arr = []
        for char in s:
            if(char in obj):
                arr.append(char)
            elif len(arr)==0 or char != obj[arr.pop()]:
                return False
        return len(arr)==0

        
