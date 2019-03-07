from Project.ReadData import ReadData
from Project.DrawData import DrawData
import matplotlib.pyplot as plt
import numpy as np


#read Data
rd=ReadData()
rd.readData()

# plot Date
dr =DrawData()
print(rd.Feature[0])
print(rd.Feature[1])
for i in range(4):
    for j in range(i+1,4):
        dr.plot(rd.Feature[i],rd.Feature[j])

#dr.draw()

weights = [np.random.rand(1)[0], np.random.rand(1)[0], np.random.rand(1)[0]]
print(weights)