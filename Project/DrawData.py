import matplotlib.pyplot as plt


class DrawData:
    def __init__(self):
        pass

    def plot(self, x1, x2):
        plt.plot(x1[0:50], x2[0:50], 'ro')
        plt.plot(x1[50:100], x2[50:100], 'go')

    def draw(self):
        plt.title('plotting  features')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
