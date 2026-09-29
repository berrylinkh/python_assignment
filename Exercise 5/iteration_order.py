
def iteration_order ():
    counter =1;
    print ("    1   2   3")

    for row in range(0,2):
        print (row, end= "   ")
        for column in range(1,4):
            print (    counter, end ="   ")
            counter +=1
        print()
            
    return  counter
iteration_order()            
