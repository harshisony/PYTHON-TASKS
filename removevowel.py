s='harshitha reddy'
v='a e i o u A E I O U'

for i in s:
    if i in v:
        s=s.replace(i,'')
    
print(s)