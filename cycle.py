classes=[{'school_class': '3a','scores': [3,4,4,5,2] },
{'school_class': '4a', 'scores': [3,4,4,5,2,5,4,6]},
{'school_class': '5a', 'scores': [3,4,4,5,2,2,1,1000]},
{'school_class': '6b', 'scores': [3,4,4,5,2,3,1,3]}]
[]
def average(dic_average):
    summ=0

    for x in dic_average:
    	summ=summ+x

    return summ/len(dic_average)


summ1=0
for x in classes:
    print(x['scores'])
    print(average(x['scores']))
    summ1+=average(x['scores'])
print(summ1/len(classes))

