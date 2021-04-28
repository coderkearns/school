import matplotlib.pyplot as plt

x = []
y = []

def plot(f, v, data, xlabel, ylabel):
    l = len(data)
    data2 = data.copy()
    d, d2 = data.pop(), data.pop()
    bound = int(round(float(d.split(" | ")[0].strip())))
    s = int(round(float(d2.split(" | ")[1].strip())))

    for xv in range(-1*l, l, 1):
        x.append(xv)
        y.append(f(xv))

    ybound = int(round(float(v.split(", ")[1].replace(" )", ""))))
    ydiff = ybound*0.1


    plt.xlim([0, bound])
    plt.ylim([0, ybound+ydiff])

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.plot(x,y, marker="o")
    plt.show()
