import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import statistics

fav_subj = ["c", "f", "f", "m", "c", "f", "c", "c", "f", "f", "c", "c", "m", "f", "c", "c", "m", "f", "f", "f"]


fav_subj_unique= [] 
for i in fav_subj: 
    if i not in fav_subj_unique : 
        fav_subj_unique.append(i) 
fav_subj_unique.sort()

numbers=[]
for i in fav_subj_unique:
    x=0
    for j in fav_subj:
        if i == j:
              x=x+1
    numbers.append(x)

#cummilative numbers 
cumN=[]
cumfreq=[]
freq=[]
total = len(fav_subj)
for i in range(0,3):
     freq.append(numbers[i]/total)    
     sum=0
     sumN=0
     for z in range(0,i+1):
             sum=sum+freq[z]
             sumN=sumN+numbers[z]
     cumfreq.append(round(sum,2))
     cumN.append(sum)

#we make them a data frame

dic = {"fav_subjict": fav_subj_unique,"numbers":numbers,"cumilative_numbers":cumN,"frequencies":freq,"cumilative_frequencies":cumfreq}
df = pd.DataFrame(dic)

#the mode is :
mode=statistics.mode(fav_subj)


style.use('ggplot')
color =['blue','red','green']
mylabels = ["accounting", "finance", "Management control"]
myexplode = [0, 0.1, 0]
plt.pie(df.numbers,labels = mylabels, explode=myexplode, shadow = True)
plt.legend(title = "the subjects:", loc = "upper left")
plt.show() 
plt.subplot(121)
plt.bar(df.fav_subjict, df.cumilative_numbers,color="blue",width=0.3,alpha=0.5)
plt.bar(df.fav_subjict, df.numbers,color=color,width=0.3)
plt.ylabel("Numbers")
plt.xlabel("fav_subj")
plt.subplot(122)
plt.bar(df.fav_subjict, df.cumilative_frequencies,color="blue",width=0.3,alpha=0.5)
plt.bar(df.fav_subjict, df.frequencies,color=color,width=0.3)
plt.ylabel("Frequencies")
plt.xlabel("fav_subj")
plt.suptitle('the study of the students favourite subjects')

plt.show()
print(df)
print (f'the mode of ages is {mode}')