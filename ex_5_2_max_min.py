#find the largest and smallest number
largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
      # print num
    try:
        n=int(num)
    except:
        print "Invalid input"
        continue
    
    if n>largest:
        largest=n
	if smallest=None:
        smallest=n	
    elif n<smallest:
        smallest=n
print "Maximum is",largest
print "Minimum is",smallest