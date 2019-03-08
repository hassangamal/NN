class FileData:
    def __init__(self):
        self.Feature = []
        self.Class = []
        self.FeatureX1 = []
        self.FeatureX2 = []
        self.FeatureX3 = []
        self.FeatureX4 = []

    def fileData(self):
        file = open('IrisData.txt', 'r')
        file.readline()
        for line in file:
            row = line.split(',')
            # print(row)
            self.FeatureX1.append(float(row[0]))
            self.FeatureX2.append(float(row[1]))
            self.FeatureX3.append(float(row[2]))
            self.FeatureX4.append(float(row[3]))
            if row[4] == 'Iris-setosa':
                self.Class.append(1)
            if row[4] == 'Iris-versicolor':
                self.Class.append(2)
            if row[4] == 'Iris-virginica':
                self.Class.append(3)
        self.Feature.append(self.FeatureX1)
        self.Feature.append(self.FeatureX2)
        self.Feature.append(self.FeatureX3)
        self.Feature.append(self.FeatureX4)
