# Just the plain data
import matplotlib.pyplot as plt

def main():
    x_list = [1, 2, 3, 4]
    y_list = [2, 4, 6, 8]

    plt.grid(True)
    plt.xlabel('Size')
    plt.ylabel('Price')
    plt.plot(x_list, y_list, 'o')
    plt.show()

if __name__ == '__main__':
    main()
