import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, 0.01)
y = np.arange(-5, 5, 0.01)

x, y = np.meshgrid(x, y)

print(x, y)

z = x**2 - y**2

fig, ax = plt.subplots(subplot_kw={'projection':'3d'})
m = ax.plot_surface(x, y, z, cmap='magma')

fig.colorbar(m)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.style.use('dark_background')

rollno = [1,2,3,4,5,6,7,8,9,10]
marks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.figure(figsize = (5, 6))
plt.scatter(rollno, marks, color='g', marker='.')
plt.show()


temperature_pune = [25,34,21,45,28,6,43,18,7,2]
humidity_pune = [28, 25,29,20, 26, 50, 19, 29, 52, 55]

temperature_bangalore = [34,35,36,37,28,27,26,25,31,20]
humidity_bangalore = [40, 38, 36, 35, 42, 44, 41, 40, 34, 45]
plt.figure(figszie=(6, 8))
# to increase x line markers with 5 point
plt.xticks(np.arange(0, 50, 5))
plt.scatter(temperature_pune, humidity_pune, color='r')
plt.scatter(temperature_bangalore, humidity_bangalore)
plt.xlabel('temperature_pune')
plt.ylabel('humidity_pune')
plt.show()


df = pd.read_csv(r"C:\Users\user\OneDrive\Desktop\Data\Python\Data_analysis\Excel Data\iris.csv")
data = pd.DataFrame(df)

print(data.head())

plt.scatter(data['sepal_length'], data['sepal_width'], color='g')
plt.xlabel('sepal_length')
plt.ylabel('sepal_width')
plt.show()


# line plot

rollno = [1,2,3,4,5,6,7,8,9,10]
marks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.plot(rollno, marks, color='r', linestyle='--')
plt.xlabel('rollno')
plt.ylabel('marks')
plt.show()



study_hours = [2,3,4,4, 5, 6, 7, 7, 8, 9, 9, 10, 11, 11, 12]
marks = [6, 10, 15, 20, 34, 44, 55, 60, 55, 67, 70, 80, 90, 99, 100]
plt.figure(figsize=(10, 8))
plt.xticks(np.arange(0, 13, 1))
plt.yticks(np.arange(0, 105, 5))           
           
plt.plot(study_hours, marks, marker='.', mfc='b')
plt.xlabel('study_hours')
plt.ylabel('marks')
#plt.grid()
plt.show()


# bar plot

subjects = ['Maths', 'English', 'Science', 'Social Studies', 'Computer']
marks = [89, 90, 45, 78, 99]
# size of dashboard
plt.figure(figsize=(6, 4))
# increase number of x by n
plt.xticks(np.arange(0,105,10))
# bar chart into row
plt.bar(subjects, marks, width=0.5)
plt.bar(subjects + 0.4, marks + 0.6)
plt.xlabel([subjects])
plt.show()

# hist

plt.style.use('dark_background')
# plt.xticks(np.arange(0, 105, 5))
marks_student = np.random.randint(0,100, (50))
print(marks_student)

plt.hist(marks_student)
plt.show()


plt.style.use('dark_background')
plt.figure(figsize=(8, 6))
marks = np.random.randint(0, 100, (50))

plt.hist(marks)
plt.show()


# pie chart
plt.style.use('light_background')

classes = ['Physics', 'Chemistry', 'Maths', 'Science', 'SST']
marks = [89, 45, 78, 23, 90]
# explode pie chart specific value from visual
explode_values = [0, 0.05, 0, 0.05, 0]

plt.pie(marks, labels=classes, autopct='%1.1f%%', explode=explode_values)
plt.legend()
plt.show()


plt.figure(figsize = (6,6))

plt.pie(marks, labels = classes, autopct = '%0.1f%%', 
                                            explode=explode_values 
                                            )

plt.title('Subjects and Average Scores')
plt.legend(loc='right', bbox_to_anchor=(1, 0.5))
plt.show()



# supermarket data analysis

df = pd.read_csv(r"C:\Users\user\OneDrive\Desktop\Data\Python\Data_analysis\Excel Data\supermarket.csv")
data = pd.DataFrame(df)
print(data)

prod_line = data.groupby('Product line')['Total'].sum()
print(prod_line)

plt.pie(prod_line.values, labels = prod_line.index, autopct='%0.1f%%')
plt.show()

plt.bar(prod_line.index, prod_line.values)
plt.show()
# payment share
payment = data['Payment'].value_counts()
print(payment)
plt.pie(payment, labels = payment.index, autopct='%0.1f%%')
plt.show()

# gender
gender = data['Gender'].value_counts()
print(gender)

plt.pie(gender, labels=gender.index, autopct='%0.1f%%')
plt.show()

#city
city = data['City'].unique()
print(city)

ttl_city = data.groupby('City')['Total'].sum()
print(round(ttl_city,0))

plt.bar(ttl_city.index, ttl_city.values)
plt.show()

print(gender.index)
print(gender.values)


# subplots

study_hours = [2,3,4,4, 5, 6, 7, 7, 8, 9, 9, 10, 11, 11, 12]
marks = [6, 10, 15, 20, 34, 44, 55, 60, 55, 67, 70, 80, 90, 99, 100]
# scatter
plt.xticks(np.arange(2, 13, 1))
plt.scatter(study_hours, marks)
plt.show()

# hist
plt.hist(marks)
plt.show()
# plot
plt.plot(study_hours, marks)
plt.show()



# subplot
plt.subplot(2, 2, 1)
plt.xticks(np.arange(2, 13, 1))
plt.scatter(study_hours, marks)

plt.subplot(2, 2, 2)
plt.hist(marks)


plt.subplot(2, 2, 3)
plt.plot(study_hours, marks, color='r')

plt.subplot(2, 2, 4)
plt.bar(marks, study_hours)

plt.savefig('subplot.png')
plt.show()


plt.style.use('dark_background')
import matplotlib.pyplot as plt

plt.subplot(2, 2, 1)
plt.plot([1, 2, 3, 4])
plt.subplot(2, 2, 2)
plt.subplot(2, 2, 3)
plt.subplot(2, 2, 4)
plt.show()

plt.subplot(2, 2, 1)
plt.plot(np.arange(0, 10,0.5))
plt.scatter(np.arange(0,20), np.arange(0,20))
plt.subplot(2, 2, 2)
plt.subplot(2, 2, 3)
plt.subplot(2, 2, 4)
plt.show()

df = pd.read_csv(r"C:\Users\user\OneDrive\Desktop\Data\Python\Data_analysis\Excel Data\data.csv")
print(df)
print(df.columns)



x = np.random.random((1, 10))
y = np.random.random((1, 10))
print(y)
plt.scatter(x, y)
plt.title('abc', fontsize=15)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

import pandas as pd
df2 = pd.read_excel(r"C:\Users\user\OneDrive\Desktop\Data\Python\Data_analysis\Excel Data\absenteeism_at_work.xlsx")
print(df2)

df = pd.read_csv(r"C:\Users\user\OneDrive\Desktop\Data\Python\Data_analysis\Excel Data\US Holiday Dates (2004-2021).csv")
data = pd.DataFrame(df)
print(data.head().to_string())

# 3d models
from mpl_toolkits import mplot3d

ax = plt.axes(projection='3d')
z = np.linspace(0, 30, 100)
x = np.sin(z)
y = np.cos(z)
ax.plot3D(x, y, z)

plt.show()



x = np.arange(0, 100, 1)
y = np.sin(x)
y2 = x ** 2 +2 * x

ax = plt.subplot(211)
ax2 = plt.subplot(212)

ax.plot(x, y)
ax2.plot(x, y2)
plt.show()

x2 = x ** 2
plt.plot(x, x2)
plt.show()

import numpy as np
import pandas as pd
df = pd.read_csv(r"C:\Users\user\OneDrive\Desktop\Data\Python\Data_analysis\Excel Data\countries.csv")
data = pd.DataFrame(df)
print(data.head())


# drop column
data2 = data.drop(columns=['% of world'])
print(data2.head())
data3 = data2.rename(columns={'Country / Dependency': 'country'})
print(data3[data3['Region'] == 'Americas'])

print(data3.groupby(['Region', 'country'])['Population'].min())

print(data3['Population'].sort_values(ascending=True))

viz = data3.groupby('Region')['Population'].sum()
print(viz)

plt.pie(viz.values, labels = viz.index, autopct='%.2f %%')
plt.legend(bbox_to_anchor=(0.1,1))
plt.show()

x = np.arange(0, 6)
y = np.arange(1, 7)

plt.step(x, y, label='py')
plt.legend()
plt.show()




data = np.random.rand(5, 5)

plt.imshow(data)
plt.colorbar()

for i in range(len(data)):
    for j in range(len(data[i])):
        print(j)
        plt.annotate(str(round(data[i][j], 2), xy=(j, i)))
                     #horizontalalignment='center',
                     #verticalalignment='center')
        
plt.show()

import numpy as np
import matplotlib.pyplot as plt
plt.figure()
x1 = np.arange(5, 10)
XX = x1 ** 2
x2 = np.arange(6, 10)
xx2 = x2 **2
plt.plot(XX, label='Python')
plt.plot(xx2, label='SQL')

# plt.xticks([2011, 2012, 2013], ['2011', '2012', '2013'])

plt.legend()
plt.show()


x = np.arange(5, 9)
y = ['x', 'y', 'z', 'w']

plt.subplot(221)
plt.plot(x**2, y)
plt.subplot(222)
plt.subplot(223)
plt.scatter(x, y)
plt.show()





