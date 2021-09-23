import random
songaunhien = {} 
for i in range(10):
    a = random.randint(1,10)
    i=i+1
    songaunhien.update({str(i) : a})
    
    print(songaunhien)