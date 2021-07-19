import random
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


x = []
y = []
labels = []
tries = 1
i = 0

while i < 1:
    random_number1 = random.randint(0,50)
    random_number2 = random.randint(0,50)
    random_number3 = random.randint(0,50)
    print()
    print("Does ",int(random_number1)," + ", int(random_number2) ," = ", random_number3,"?")
    if int(random_number1) + int(random_number2) == int(random_number3):
        print("Yes!!!")
        print("Found in",format(tries,","),"Tries")
        num = int(random_number1) + int(random_number2)
        x.append(num)
        labels.append(str(num))
        y.append(random_number3)
        break
    else:
        print("Nope!")
        print("Try #",format(tries,","))
        num = int(random_number1) + int(random_number2)
        x.append(num)
        labels.append(str(num))
    tries = tries + 1
    y.append(tries)
    
    dframe = pd.DataFrame(x)
    print()
    print(dframe)
    print()
    print("Mean:",np.mean(x))
    print()
    print("Median:",np.median(x))
    print()
    
    mode_output = str(stats.mode(x))
    #print("Mode: ",mode_output)
    
    comma_index = mode_output.find(",")
    #print("comma_index",comma_index)
    
    count_slice = mode_output[comma_index:]
    #print("count_slice",count_slice)
    count = count_slice.replace(", count=array([","").replace("]))","")
    #print("count",count)
    
    mode_output = mode_output[:comma_index]
    #print("mode_output",mode_output)
    left_bracket_index = mode_output.rfind("[")
    #print("left_bracket_index",left_bracket_index)
    mode_output = mode_output[left_bracket_index:].replace("[","").replace("]","").replace(")","")
    #print("mode_output",mode_output)
                
    print("Mode:",mode_output, "counted",count,"times")
    
    sd = np.std(x)
    print()
    print("Standard Deviation:",sd)
    
    v = np.var(x)
    print()
    print("Varience:",v)
    
    mymodel = np.poly1d(np.polyfit(x,y,3))
    line = np.linspace(min(x),max(x),max(y))
    
    plt.scatter(x,y)
    plt.plot(line, mymodel(line))
    plt.show()
    
    future = mymodel(max(x)+1)
    print()
    print("future =",future)



