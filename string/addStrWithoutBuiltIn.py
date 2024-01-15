def addStrings(self, num1, num2):
        result = ""
        i = len(num1) - 1
        j = len(num2) - 1
        c = 0
        while(i>=0 or j>=0 or c>0):
            d1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            d2 = ord(num2[j])- ord('0') if j >= 0 else 0
            sum = d1 + d2 + c
            c = sum // 10
            digit = sum % 10
            result = chr(digit + ord('0')) + result
            i -= 1
            j -= 1
        
        return result
