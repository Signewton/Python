# Use the file name mbox-short.txt as the file name
count = 0 
sum = 0
fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    
    number = line.find(':')
    target = line[number+1:]    # splicing to find the numbers after the colon 
    target = float(target) #changing type from a string to float
    
    #print target #printing out numbers after the colon to check work
    count = count + 1  #increase count for the loop
    sum = sum + target 
    

avg = sum / count # finding average 



print 'Average spam confidence:', avg 