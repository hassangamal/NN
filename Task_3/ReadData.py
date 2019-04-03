from Task_1_2.FileData import FileData


class ReadData:
    def GUIData(self):
        feature1 = self.returnFeature(0)
        feature2 = self.returnFeature(1)
        feature3 = self.returnFeature(2)
        feature4 = self.returnFeature(3)

        classLabel = []
        featureX1 = []
        featureX2 = []
        featureX3 = []
        featureX4 = []

        # first class
        featureX1 = feature1[0:30]
        featureX2 = feature2[0:30]
        featureX3 = feature3[0:30]
        featureX4 = feature4[0:30]
        classLabel = [1 for i in range(0, 30)]

        # second class
        featureX1.extend(feature1[50:80])
        featureX2.extend(feature2[50:80])
        featureX3.extend(feature3[50:80])
        featureX4.extend(feature4[50:80])
        classLabel.extend([2 for i in range(0, 30)])

        # third class
        featureX1.extend(feature1[100:130])
        featureX2.extend(feature2[100:130])
        featureX3.extend(feature3[100:130])
        featureX4.extend(feature4[100:130])
        classLabel.extend([3 for i in range(0, 30)])

        return (featureX1, featureX2, featureX3, featureX4, classLabel)

    def returnFeature(self, index):
        fd = FileData()
        fd.fileData()
        feature = []
        if index == 0:
            feature = fd.FeatureX1
        elif index == 1:
            feature = fd.FeatureX2
        elif index == 2:
            feature = fd.FeatureX3
        else:
            feature = fd.FeatureX4
        return feature

    def TestingData(self):
        feature1 = self.returnFeature(0)
        feature2 = self.returnFeature(1)
        feature3 = self.returnFeature(2)
        feature4 = self.returnFeature(3)

        classLabel = []
        featureX1 = []
        featureX2 = []
        featureX3 = []
        featureX4 = []

        # first class
        featureX1 = feature1[30:50]
        featureX2 = feature2[30:50]
        featureX3 = feature3[30:50]
        featureX4 = feature4[30:50]
        classLabel = [1 for i in range(0, 30)]

        # second class
        featureX1.extend(feature1[80:100])
        featureX2.extend(feature2[80:100])
        featureX3.extend(feature3[80:100])
        featureX4.extend(feature4[80:100])
        classLabel.extend([2 for i in range(0, 30)])

        # third class
        featureX1.extend(feature1[130:150])
        featureX2.extend(feature2[130:150])
        featureX3.extend(feature3[130:150])
        featureX4.extend(feature4[130:150])
        classLabel.extend([3 for i in range(0, 30)])

        return (featureX1, featureX2, featureX3, featureX4, classLabel)
