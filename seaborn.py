import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\Users\user\Downloads\supermarket_sales.xlsx")
data = pd.DataFrame(df)
print(data.head().to_string())

filt = data[['Gender', 'Payment', 'Unit price', 'Quantity', 'Total', 'gross income']]
# pivot table
filt2 = filt.pivot_table(index='Payment', columns='Gender', values='Total')

plt.figure(figsize=(9, 6))
plt.subplot(221)
sns.stripplot(x='Payment', y='Total', data=data)
plt.subplot(222)
ax = sns.violinplot(x='Payment', y='Total', data=data, hue='Gender')
sns.move_legend(ax, "lower center",
                bbox_to_anchor=(.5, 1), ncol=2, title=None
                )
plt.subplot(223)
sns.histplot(x=filt['Total'], hue=filt['Gender'], multiple='stack', kde=True)
plt.subplot(224)
sns.boxplot(x='Payment', y='Total', hue='Gender', data=data)
plt.savefig("Payment Analysis.png")

sns.heatmap(filt2,
            annot=True,
            fmt='.0f',
            cmap='Blues')
plt.savefig('heatmap_dashboard.png')

# count-plots
x = data.groupby('Gender')['Gender'].count()
sns.countplot(x=data['Gender'])

plt.figure(figsize=(15, 5))
sns.countplot(x='Product line', hue='Gender', data=data)

plt.figure(figsize=(15, 5))
sns.countplot(x='Product line', hue='Gender', data=data, palette='PuBuGn_r')

# barplots
print(data.head().to_string())
plt.figure(figsize=(15, 5))
sns.barplot(x='Product line', y='Total', hue='Gender', data=data)
print(data.groupby(['Product line', 'Gender'])['Total'].mean())

# change bar to bar_horizontal
plt.figure(figsize=(15, 5))
sns.barplot(y='Product line', x='Total', hue='Gender', data=data, palette='cividis')
plt.subplots_adjust(left=0.26)
plt.show()
# box_plots
sns.boxplot(x='Payment', y='Total', hue='Gender', data=data)

plt.figure(figsize=(10, 6))
sns.boxplot(x='Payment', y='Total', hue='Gender', data=data, showmeans=True, palette='CMRmap', width=0.8)
# violin_plots
sns.violinplot(x='Payment', y='Total', data=data)

sns.violinplot(x='Payment', y='Total', data=data, hue='Gender')

# subplot_of strip&violin plots

plt.style.use('bmh')
var = [1, 1, 1, 1, 2, 2, 3, 3, 4, 5]
sns.swarmplot(y=var)

city = data.groupby('City')['Total'].agg('mean')
print(data.head().to_string())
print(filt2)
print(filt2.to_csv("pivot.csv"))


y = filt[filt['Payment'] == 'Cash'].head()

x = filt.groupby('Payment')['gross income'].agg('sum')
print(x)
sns.histplot(data=filt, x='Payment', y='Total', multiple='stack', kde=True)

plt.figure(figsize=(6, 5))

sns.histplot(x=filt['Total'], hue=filt['Gender'], kde=True)

# total payment distribution
sns.histplot(x=filt['Total'], hue=filt['Gender'], multiple='stack', kde=True)
plt.savefig('seaborn_histplot.pdf')

sns.kdeplot(data=filt, x='Total', hue='Payment', multiple='stack')
plt.savefig('kde_plot.pdf')

sns.kdeplot(data=filt, x='Total', hue='Payment', multiple='stack', linewidth=1, palette='Dark2')
plt.savefig('seaborn_plot')

sns.kdeplot(data=filt, x='Unit price', y='gross income', hue='Gender')

# heat map for seaborn
import pandas as pd

df = pd.read_excel(r"C:\Users\user\Downloads\mart_linePlot.xlsx")
mart = pd.DataFrame(df)
print(mart.head().to_string())

# pivot table
x = mart.pivot_table(index='Outlet_Year', columns='Outlet_Size', values='Sales')
print(x)

sns.heatmap(mart_piv,
            annot=True,
            fmt='.0f'
            )

df = pd.read_excel(r"C:\Users\user\Downloads\sample_pivot.xlsx")
print(df.head())

print(df.pivot_table(index='Type', columns='Region', values='Sales'))
pivot1 = df.pivot_table(index='Region', values=['Sales', 'Units'])
print(pivot1)

pivot2 = df.pivot_table(index='Region', values='Sales', aggfunc=['sum', 'mean'])
print(pivot2.sort_values(ascending=True, by='Region'))

pivot3 = df.pivot_table(index='Region', columns='Type', values='Units')
print(pivot3)

pivot4 = df.pivot_table(index='Region', columns='Type', values='Sales', aggfunc='sum', margins=True)
print(pivot4)


df = pd.read_csv(r"C:\Users\user\OneDrive\Desktop\marketing raw.csv")
print(df.head().to_string())

sns.lineplot(x='Week_ID', y='Revenue', data=df)

plt.figure(figsize=(10, 6))
sns.lineplot(x='Week_ID', y='Revenue', hue='Promo', style='Promo', data=df)

plt.figure(figsize=(10, 6))
sns.lineplot(x='Week_ID', y='Revenue', hue='Promo', style='Promo', markers=True,  data=df)

plt.figure(figsize=(10, 6))
sns.lineplot(x=str('Year'), y='Revenue', hue='Promo', style='Promo', markers=True,  data=df)

sns.barplot(x='Month_ID', y='Revenue', data=df, ci=None, hue='Promo')
for i, val in enumerate(df['Revenue']):
    plt.text(i, val, str(val), horizontalalignment='center', verticalalignment='bottom')

print(round(df.groupby('Month_ID')['Revenue'].agg('mean'),0))
# horizontal bar
sns.barplot(y='Month_ID', x='Revenue', data=df, ci=None, hue='Promo', orient='h')

print(df['Revenue'].values)
sns.histplot(df['Revenue'].values)
sns.distplot(df['Revenue'].values, color='blue')
mean = df['Revenue'].mean()
plt.axvline(mean, 0, 1, color='r')

df = pd.read_csv(r"C:\Users\user\OneDrive\Desktop\marketing raw.csv")
print(df.head().to_string())
print(df['Revenue'].values)
sns.boxplot(df['Revenue'].values)

plt.figure(figsize=(10, 5))
sns.boxplot(x=df['Day_Name'], y=df['Revenue'], hue=df['Promo'], color='green')
plt.savefig('box_plot.png')
# relationship between marketing spend and revenue
sns.scatterplot(y=df['Revenue'], x=df['Marketing Spend'], color='#1899C7')

sns.scatterplot(y=df['Revenue'], x=df['Marketing Spend'], color='#1899C7', hue=df['Promo'], size=df['Revenue'])

df = pd.read_csv(r"C:\Users\user\OneDrive\Desktop\marketing raw.csv")
print(df.head().to_string())
# countplot
sns.countplot(data=df, y='Year', hue='Day_Name')

sns.histplot(data=df, x='Visitors')

sns.kdeplot(data=df, x='Revenue', shade=True)

print(df)
sns.scatterplot(data=df, x='Marketing Spend', y='Revenue', color='#27A3D0', hue='Promo')


mar = df.groupby('Promo')['Marketing Spend'].agg('sum')
print(mar)
plt.pie(mar.values, labels=mar.index,
        colors=sns.color_palette('Set2'),
        autopct='%1.2f%%',
        explode=[0, 0.05, 0])
plt.show()

import numpy as np
print(np.random.rand(5, 5))

sns.heatmap(np.random.rand(5, 5), annot=True, cmap='Blues')
