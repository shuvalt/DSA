#extract key value pair
def extract_key(s,c):
    result = []
    for char in s:
        temp = char.split(" ")
        result.append(temp[c-1])
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
