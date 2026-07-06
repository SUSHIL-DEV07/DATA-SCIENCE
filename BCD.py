print ("Hellow")

import numpy as np 
import time 

size = 1_000_000
L1 = list (range (size) )
L2 = list (range (size) )
start = time.time() 

add = [x + y for x, y in zip (L1,L2)]
end = time.time () 

print (add [:10]) 
print ("Time : ", end - start )
