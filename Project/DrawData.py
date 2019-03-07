import matplotlib.pyplot as plt

class DrawData:
    def __init__(self):
        pass

    def plot(self,x1,x2):
        plt.scatter(x1,x2)

    def draw(self):
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('plotting  features')
        plt.show()