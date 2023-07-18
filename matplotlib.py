def createchartmultipleline(title, x,xlabel, dict_y, figsize=(8,6), style='fivethirtyeight'):
    plt.style.use(style)
    plt.figure(figsize=figsize)
    plt.title(title)
    for key in dict_y.keys():
        plt.plot(x,dict_y[key], label = key)
    plt.xlabel(xlabel)
    plt.legend(shadow = True, frameon = True, facecolor = 'white')

    plt.show()

plt.bar(x, y, width=, color  = , align= 'edge')
plt.bar(x, y, width=, color  = , bottom=)

plt.figure(figsize=(2,6), dpi = )
plt.style.available #check style available
plt.style.use('fivethirtyeight')
#https://flatuicolors.com/
plt.plot(nums,nums**3, color = '', linewidth = 
         , linestyle= , marker = , markersize = 
          , markerfacecolor = , label = )
plt.title("titleName", loc = )
plt.xlable("", labelpad = )
plt.ylable("", labelpad = )
plt.xticks([list of bin in row])
plt.yticks([list of bin in col],labels = [])
plt.xlim()
plt.ylim()
plt.legend()
plt.legend(bbox_to_anchor = (1.05,1) #set legend outside of the box)
           
plt.hist(data, label = , alpha = )

