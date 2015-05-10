# Use words.txt as the file name
fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print 'File name can not be opened.'

for line in fh:
      line=line.rstrip()
      line=line.upper()
      print line