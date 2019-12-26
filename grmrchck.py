import language_check
tool=language_check.LanguageTool('en-US')
grammatical_error=0
c=0
f=open('output.txt','r',encoding='utf-8')
for line in f:
    match=tool.check(line)
    if(len(match)>0):
        grammatical_error+=1
    c+=1
f.close()
print(c)
print(grammatical_error)
print(1 - grammatical_error/c)

#print total number of questions
#print questions having grammatical or spelling error
#print ratio of grammatical correctness
