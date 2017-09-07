# Coming up with a model to fit the data
import matplotlib.pyplot as plt

def predict(a, b, x):
    return a * x + b


def predict_list(a, b, x_list):
    return [predict(a, b, x) for x in x_list]


def main():
    x_list = [1, 2, 3, 4]
    y_list = [2, 4, 6, 8]

    # Modify a and b values to match the trend
    a, b = 0, 0

    plt.grid(True)
    plt.xlabel('Size')
    plt.ylabel('Price')
    plt.plot(x_list, y_list, 'o')

    plt.plot(x_list, predict_list(a, b, x_list))
    plt.show()

if __name__ == '__main__':
    main()
