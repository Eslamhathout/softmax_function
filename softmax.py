import numpy as np
# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    expOfL=[]
    for number in L:
        expOfL.append(np.exp(number))
    softMaxOutput=[]
    expoSum=np.sum(expOfL)
    for expo_number in expOfL:
        softMaxOutput.append( expo_number/expoSum)
    return softMaxOutput
