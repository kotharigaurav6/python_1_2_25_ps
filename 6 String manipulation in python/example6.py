# Program to find out frequency of characters

# dictValue = { 'a' : 101}
# print(dictValue.get('c'))
# print(dictValue.get('c',0))

str = "Programming Mania"
dictValue={}
for ch in str:
    dictValue[ch] = dictValue.get(ch,0)+1
print(dictValue)