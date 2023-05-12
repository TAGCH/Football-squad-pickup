Name = ['a','b','c']
overall = ['1','2','3']
Overall = []
Len = 3
for i in range(Len):
    Dic = {Name[i]:overall[i]}
    Overall.append(Dic)
    
b = 0

Name.remove('a')
print(Name)