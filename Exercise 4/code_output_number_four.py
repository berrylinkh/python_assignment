


def mystery(x):
    y = 0
    for value in x:
        y += value ** 2
    return y

print(mystery([1,2,3,4,5]))


# it calculate the sum of each square result. 1*1 =0 , y+1= 1, then the loop runs again
