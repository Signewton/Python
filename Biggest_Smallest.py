largest_so_far = None
smallest_so_far = None

while True:

 num = raw_input('Enter a number:')

 if num == 'done':
   break
 if len(num) < 1:
   break
   
 try:   
   num = int(num)
 except: 
   print 'Invalid input'
   continue  
                    
                    
 if largest_so_far is None:
    largest_so_far = num
    
   
 if num > largest_so_far:
     largest_so_far = num
     #print 'Maximum is', largest_so_far    

 if smallest_so_far is None:
    smallest_so_far = num
    
 if num < smallest_so_far:
     smallest_so_far = num
     
 print 'Maximum is', largest_so_far      
 print 'Minimum is', smallest_so_far    
   
