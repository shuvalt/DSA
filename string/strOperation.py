def finalValueAfterOperations(self, operations):
        re = 0
        for o in operations:
            if('+' in o):
                re+=1
            else:
                re-=1
        return re
