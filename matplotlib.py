def createchartmultipleline(title, x,xlabel, dict_y, figsize=(8,6), style='fivethirtyeight'):
    plt.style.use(style)
    plt.figure(figsize=figsize)
    plt.title(title)
    for key in dict_y.keys():
        plt.plot(x,dict_y[key], label = key)
    plt.xlabel(xlabel)
    plt.legend(shadow = True, frameon = True, facecolor = 'white')
    plt.show()
