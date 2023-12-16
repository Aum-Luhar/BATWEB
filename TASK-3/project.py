def contains_even_number(l): 
    for ele in l: 
        if ele % 2 == 0: 
            print ("list contains an even number") 
            break
  
    else:      
        print ("list does not contain an even number") 

 print ("For List 1:") 
 contains_even_number([1, 4, 8]) 
 print (" \nFor List 2:") 
 contains_even_number([1, 3, 7])
