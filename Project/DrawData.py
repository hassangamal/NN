import matplotlib.pyplot as plt


class DrawData:
    def __init__(self):
        pass

    def plot(self, x1, x2):
        plt.plot(x1[0:50], x2[0:50], 'ro')
        plt.plot(x1[50:100], x2[50:100], 'go')

    def draw(self):
        plt.title('Plotting Features')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()

    def line(self, x1, x2, w1, w2, b):
        point1 = [x1, x2]
        x3 = -(w1 * x1 + b) / w2
        x4 = -(w1 * x2 + b) / w2
        point2 = [x3, x4]
        plt.plot(point1, point2)
