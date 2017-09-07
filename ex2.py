# Showing the cost for each value for the parameters a and b
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

    # Modify a and b values see the changes in the cost value
    a, b = 0, 0

    plt.grid(True)
    plt.xlabel('Size')
    plt.ylabel('Price')
    plt.plot(x_list, y_list, 'o')

    cost = calculate_cost(a, b, x_list, y_list)

    plt.plot(x_list, predict_list(a, b, x_list))
    plt.title(f"Cost: {cost:.4f}")
    plt.show()

if __name__ == '__main__':
    main()
