import matplotlib.pyplot as plt


class DrawData:
    def __init__(self):
        pass

    def plot(self, x1, x2):
        # plt.plot([0.5, 2], [3, 5])
        plt.plot(x1[0:50], x2[0:50], 'ro')
        plt.plot(x1[50:100], x2[50:100], 'go')

    def draw(self):
        plt.title('plotting  features')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()

    def line(self, w1, w2, b):
        x1 = (-b / w1)
        x2 = (-b / w2)
        point1 = [w1, x1]
        point2 = [w2, x2]
        plt.plot(point1, point2)
