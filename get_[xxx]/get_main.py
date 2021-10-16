import re

f = open("file.md","rt",encoding='utf-8')
F = open("new_file.txt","w",encoding='utf-8')
lines=f.readlines()

for i in lines:
    text=i
    pattern=re.compile("\\[(.*?)\\]\\((.*?)\\)")
    content=pattern.findall(text)
    if content != []:
        # print(content)
        for j in content:        
            new_content=j[0]
            # print(new_content)
            text=pattern.sub(new_content,text)
            F.write(text)
    else:
        F.write(text)
f.close
F.close




    
