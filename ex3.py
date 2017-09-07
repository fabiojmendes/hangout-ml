# Plotting the cost curve for different options of a and b
import matplotlib.pyplot as plt

def predict(a, b, x):
    return a + b * x


def predict_list(a, b, x_list):
    return [predict(a, b, x) for x in x_list]


def calculate_cost(a, b, x_list, y_list):
    m = len(x_list)
    cost = 0
    for x, y in zip(x_list, y_list):
        cost += (predict(a, b, x) - y)**2

    return 1/(2*m) * cost


def main():
    x_list = [1, 2, 3, 4]
    y_list = [2, 4, 6, 8]

    plt.subplot(121)
    plt.grid(True)
    plt.xlabel('Size')
    plt.ylabel('Price')
    plt.plot(x_list, y_list, 'o')

    a = 0
    b_list = list(range(-5, 10))
    cost_history = []
    for b in b_list:
        cost_history.append(calculate_cost(a, b, x_list, y_list))
        plt.plot(x_list, predict_list(a, b, x_list))

    plt.subplot(122)
    plt.grid(True)
    plt.xlabel('Value (b)')
    plt.ylabel('Cost')
    plt.plot(b_list, cost_history)

    plt.show()

if __name__ == '__main__':
    main()
