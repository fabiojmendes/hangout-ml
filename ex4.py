# Implementation of gradient descent
import matplotlib.pyplot as plt

def predict(a, b, x):
    return a + b * x


def predict_list(a, b, x_list):
    return [predict(a, b, x) for x in x_list]


def calculate_cost(a, b, x_list, y_list):
    cost = 0
    for x, y in zip(x_list, y_list):
        cost += (predict(a, b, x) - y)**2

    cost = cost / (2 * len(x_list))
    return cost


def calculate_gradient(a, b, x_list, y_list, alpha):
    grad_a = 0
    for x, y in zip(x_list, y_list):
        grad_a += predict(a, b, x) - y

    a_new = a - alpha * (1/len(x_list) * grad_a)

    grad_b = 0
    for x, y in zip(x_list, y_list):
        grad_b += (predict(a, b, x) - y) * x

    b_new = b - alpha * (1/len(x_list) * grad_b)

    return (a_new, b_new)


def main():
    x_list = range(1, 100)
    y_list = list(map(lambda x: x * 2, x_list))

    a, b = 0, 0

    plt.subplot(121)
    plt.grid(True)
    plt.xlabel('Size')
    plt.ylabel('Price')
    plt.plot(x_list, y_list, 'o')

    cost_history = []

    alpha = 0.00003
    for i in range(0, 200):
        plt.plot(x_list, predict_list(a, b, x_list))
        cost_history.append(calculate_cost(a, b, x_list, y_list))
        a, b = calculate_gradient(a, b, x_list, y_list, alpha)

    cost = calculate_cost(a, b, x_list, y_list)

    plt.plot(x_list, predict_list(a, b, x_list))
    plt.title(f"Final Cost: {cost:.6}, Params: ({a:.4}, {b:.4})")

    plt.subplot(122)
    plt.grid(True)
    plt.xlabel('Iteration')
    plt.ylabel('Cost')
    plt.plot(cost_history)
    plt.show()

if __name__ == '__main__':
    main()
