counts = dict() #create dictionary to store emails
bigcount = None #setting counts equal to none to deterine biggest
bigword = None
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt" #opening file 
handle = open(name)

for line in handle:
   line = line.strip()
   if not line.startswith('From '): continue  #splicing lines
   words = line.split() #splitting the relevant lines into words
   #print  words[1]  to check results 
   counts[words[1]] = counts.get(words[1],0) +1  #adding each new email to our dictionary 
   #print counts
        
for email,count in counts.items():  #loop to determine whcih email address sent hte most 
 if bigcount is None or count > bigcount:
  bigword = email
  bigcount = count
print bigword, bigcount 