from Project.FileData import FileData
from Project.DrawData import DrawData
from Project.ReadData import ReadData
import matplotlib.pyplot as plt
import numpy as np


#read Data
rd=FileData()
rd.fileData()

# plot Date
dr =DrawData()
dr.plot(rd.Feature[1],rd.Feature[2])

#dr.draw()

weights = [np.random.rand(1)[0], np.random.rand(1)[0], np.random.rand(1)[0]]
print(weights)


rd1=ReadData()
print(rd1.GuiDate(1,2,1,2))