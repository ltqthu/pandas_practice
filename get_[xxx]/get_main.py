import re

f = open("file.md","rt",encoding='utf-8')
F = open("new_file.md ","w",encoding='utf-8')
lines=f.readlines()

for i in lines:
    text=i
    pattern=re.compile("\\[(.*?)\\]\\((.*?)\\)")
    content=pattern.findall(text)
    if len(content) != 0:
        for tuple in content:
            title =  tuple[0]
            text = text.replace("[{}]({})".format(tuple[0], tuple[1]), tuple[0])
        F.write(text)
    else:
        F.write(text)
f.close()
F.close()
