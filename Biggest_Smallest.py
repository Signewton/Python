largest_so_far = None #starting point for our largest and smallest numbers 
smallest_so_far = None

while True:

 num = raw_input('Enter a number:') #prompt user for a number 

 if num == 'done': 
   break
 if len(num) < 1:
   break
   
 try:   
   num = int(num)
 except: 
   print 'Invalid input'
   continue  
                    
                    
 if largest_so_far is None: #assigning a value for the start of our loop before a user enters input 
    largest_so_far = num
    
   
 if num > largest_so_far: #checking to see if the latest number entered is the largest so far 
     largest_so_far = num
     #print 'Maximum is', largest_so_far    

 if smallest_so_far is None:  #same as above but for the smallest number 
    smallest_so_far = num 
    
 if num < smallest_so_far:
     smallest_so_far = num
     
 print 'Maximum is', largest_so_far      
 print 'Minimum is', smallest_so_far    
   
