from Project.FileData import FileData


class ReadData:
    def GuiData(self, x, y, c1, c2):
        featurex = self.returnFeature(x)
        featurey = self.returnFeature(y)
        classLabel = []
        featureX = []
        featureY = []
        if c1 == 1:
            featureX = featurex[0:30]
            featureY = featurey[0:30]
            classLabel = [1 for i in range(0, 30)]
            if c2 == 2:
                featureX.extend(featurex[50:80])
                featureY.extend(featurey[50:80])
                classLabel.extend([-1 for i in range(0, 30)])
            else:
                featureX.extend(featurex[100:130])
                featureY.extend(featurey[100:130])
                classLabel.extend([-1 for i in range(0, 30)])
        elif c1 == 2:
            featureX = featurex[50:80]
            featureY = featurey[50:80]
            classLabel = [1 for i in range(0, 30)]
            featureX.extend(featurex[100:130])
            featureY.extend(featurey[100:130])
            classLabel.extend([-1 for i in range(0, 30)])
        return (featureX, featureY, classLabel)

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
