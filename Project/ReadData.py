class ReadData:
    def __init__(self):
        self.Feature = []
        self.Class=[]

    def readData(self):
        file =open('IrisData.txt','r')
        file.readline()
        FeatureX1=[]
        FeatureX2=[]
        FeatureX3=[]
        FeatureX4=[]
        for line in file:
            row = line.split(',')
            #print(row)
            FeatureX1.append(float(row[0]))
            FeatureX2.append(float(row[1]))
            FeatureX3.append(float(row[2]))
            FeatureX4.append(float(row[3]))
            if row[4]=='Iris-setosa':
                self.Class.append(1)
            if row[4] == 'Iris-versicolor':
                self.Class.append(2)
            if row[4] == 'Iris-virginica':
                self.Class.append(3)
        self.Feature.append(FeatureX1)
        self.Feature.append(FeatureX2)
        self.Feature.append(FeatureX3)
        self.Feature.append(FeatureX4)
