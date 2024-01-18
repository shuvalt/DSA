#extract key value pair
def extract_key(s,c):
    result = []
    for char in s:
        temp = char.split(" ")
        result.append(temp)
    return result

    
n = int(input("enter number of element:"))
string = []
for i in range(n):
    string.append(str(input(f"enter the value of the {i}th index string:")))
reverse = input("enter true or false to reverse:")
compare = input("num or lexi:")
column = int(input("enter the key column:"))
print(extract_key(string,column))
print(n)
print(string)
print(reverse)
print(compare)

#sorting portion
def numsort(s1):
    key1 = s1[1]
    return int(key1)

def lexisort(e):
    key2 = e[1]
    return key2
    
    

string = [["89","13"],["98","022"],["102","12"]]
rev = True
ty = 'l'

if(ty == 'n'):
    string.sort(reverse=rev,key=numsort)
else:
    string.sort(reverse=rev,key=lexisort)

print(string)
