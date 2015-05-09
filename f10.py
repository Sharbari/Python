name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
line=handle.read()
d=dict()
lst=list()
for line in handle:
    words=line.split()
    if len(words)==0:continue
    if words[0]!='From':continue
    else:    
        hr=words[5].split(':')
        lst.append(hr[0])
for h in lst:
    d[h]=d.get(h,0)+1
 
t=d.items()
t.sort()
for k,v in t:
    print k,v
