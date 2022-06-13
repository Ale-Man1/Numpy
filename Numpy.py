import numpy as np
import pandas as pd


def main():
    # Part 1:
    a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
    b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
    a1 = np.unique(a)
    b1 = np.unique(b)
    #print(a1)
    #print(b1)
    res = np.intersect1d(a, b)
    print(res, "\n")

    # Part 2:
    p2 = np.array(([(i * 5) + 1 for i in range(3)], [(j * 5) + 2 for j in range(3)], [(k * 5) + 3 for k in range(3)],
                   [(l * 5) + 4 for l in range(3)], [(m * 5) + 5 for m in range(3)]))
    print(p2, "\n")

    # Part 3:
    p3 = p2.flatten('F')
    print(p3, "\n")

    # Part 4:
    p4_h = p2.flatten('F')
    p4 = np.reshape(p4_h, (3, 5, 1))
    print(p4, "\n")

    # Part 5:
    p5 = np.reshape(p4, (5, 3))
    print(p5, "\n")

    # Part 6:
    a_1 = np.array([12, 5, 7, 15, 3, 1, 8])
    b_1 = np.array([14, 6, 3, 11, 19, 12, 5])
    b_2 = np.unique(b_1)
    a_2 = np.setdiff1d(a_1, b_2)
    print(a_2, "\n")

    # Part 7:
    # Part 7.1
    df = pd.read_csv('https://raw.githubusercontent.com/Ale-Man1/Numpy/main/Module6_Data.csv')
    pd.set_option('display.width', None)
    print(df)
    large_water = df["NYC Consumption(Million gallons per day)"].max()
    print(large_water)
    # Part 7.2
    print(df.shape[0])
    # print(df.__len__()) would also show how many years since every row is a year
    # Part 7.3 ,this part was taken and repurposed by the file 6_Numpy.ipynb
    colmean = np.mean(df["Per Capita(Gallons per person per day)"])
    print(colmean)

    colstddev = np.std(df["Per Capita(Gallons per person per day)"])
    print(colstddev)
    # Part 7.4


if __name__ == "__main__":
    main()
