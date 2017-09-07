# Implementation of gradient descent
import matplotlib.pyplot as plt
from random import random

def predict(a, b, x):
    return a * x + b


def predict_list(a, b, x_list):
    return [predict(a, b, x) for x in x_list]


def calculate_cost(a, b, x_list, y_list):
    m = len(x_list)
    cost = 0
    for x, y in zip(x_list, y_list):
        cost += (predict(a, b, x) - y)**2

    return 1/(2*m) * cost


def calculate_gradient(a, b, x_list, y_list, alpha):
    m = len(x_list)
    grad_a = 0
    grad_b = 0
    for x, y in zip(x_list, y_list):
        h = predict(a, b, x)
        grad_a += (h - y) * x
        grad_b += (h - y)

    a_new = a - alpha * (1/m) * grad_a
    b_new = b - alpha * (1/m) * grad_b
    return (a_new, b_new)


def main():
    x_list = [x / 10 for x in range(1, 50)]
    y_list = [x * 2 for x in x_list]

    # Uncomment to add some variance
    # y_list = [y + random() for y in y_list]

    a, b = 0, 0

    plt.subplot(121)
    plt.grid(True)
    plt.xlabel('Size')
    plt.ylabel('Price')
    plt.plot(x_list, y_list, 'o')

    cost_history = []

    alpha = 0.01
    for i in range(0, 100):
        plt.plot(x_list, predict_list(a, b, x_list))
        cost_history.append(calculate_cost(a, b, x_list, y_list))
        a, b = calculate_gradient(a, b, x_list, y_list, alpha)

    cost = calculate_cost(a, b, x_list, y_list)

    plt.plot(x_list, predict_list(a, b, x_list))
    plt.title(f"Final Cost: {cost:.4f}, Params: ({a:.4f}, {b:.4f})")

    plt.subplot(122)
    plt.grid(True)
    plt.xlabel('Iteration')
    plt.ylabel('Cost')
    plt.plot(cost_history)
    plt.show()

    # Finally we predict the result for a new data point
    # h = predict(a, b, 20)
    # print(f'Prediction for a new value of x (20): {h:.4f}')

if __name__ == '__main__':
    main()
