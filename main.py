# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    df = pd.DataFrame(columns=['task', 'duration', 'result', 'done'])
    f = open("res1.txt", "r")
    for l in f:
        data = (l.strip().split(":"))
        print(data.__len__())
        if data.__len__()  < 4:
            continue
        duration = (data[1].replace("s for", " "))
        if(l.__contains__("RICHTIG")):
            result = data[2].split("=")
            task = data[2]
            done = data[3].strip()
        else:
            result = data[3].split("=")
            task = data[3]
            done = data[4].strip()
        df_temp = pd.DataFrame({"task": task,
                    "duration": int(duration),
                    "result": int(result[1]),
                    "done": done}, index=[0])

        df =  df.append(df_temp, ignore_index = True)

    df = df.sort_values(['duration'], ascending = [1])
    mean_time = (np.mean(df['duration']))
    max_time = (np.max(df['duration']))
    worst = df['duration'] >= max_time
    wrong = df['done'] == 'FALSCH'
    print(df[wrong])
    print(df[worst])
    sel = df['duration'] >= 10
    plotdata = df[sel]
# Press the green button in the gutter to run the script.
    plotdata.plot.bar(x= 'task', y='duration')
    plt.xticks(rotation=90)
    plt.show()


if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
