def splitNum(self, num):
        toStr = str(num)
        toArr = [x for x in toStr]
        toArr.sort()
        left =''.join([toArr[i] for i in range(0, len(toArr), 2)])
        right =''.join([toArr[i] for i in range(1, len(toArr), 2)])
        return int(right)+int(left)
