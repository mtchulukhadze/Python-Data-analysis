import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('default')
df = pd.read_csv(r"C:\Users\user\OneDrive\Desktop\Data\Python\Data_analysis\Excel Data\supermarket.csv")
store_data = pd.DataFrame(df)
print(store_data)
# average revenue by city
city = store_data.groupby('Branch')['Total'].mean()
payment = store_data.groupby('Payment')['Total'].sum()
gender = store_data.groupby('Gender')['Quantity'].sum()
print(payment)
plt.subplot(221)
plt.title('payment_method')
plt.barh(payment.index, payment.values / 1000, left=0.25)

plt.subplot(222)
plt.title('cogs by city')
plt.plot(city.index, city.values ** 2)

plt.subplot(223)
plt.title('share by gender')
cl = ['#abcdef', '#aabbcc']
plt.pie(gender.values, labels=gender.index, autopct='%.2f %%', colors=cl)

plt.subplot(224)
plt.imshow(np.random.rand(5, 5))
plt.colorbar()
plt.savefig('retail_data_analysis')
plt.show()


df = pd.read_csv(r"C:\Users\user\OneDrive\Desktop\Data\Python\Data_analysis\Excel Data\gas_prices.csv")
prices = pd.DataFrame(df)
prices = prices[prices['Year'] >= 2001]
print(prices)
plt.style.use('bmh')

yr = prices.Year

plt.plot(yr, prices.France)
plt.plot(yr, prices.Canada, 'm--')
plt.plot(yr, prices.Mexico)
plt.plot(yr, prices.Japan)
plt.xlabel('year')
plt.ylabel('USD $')

plt.yticks(np.arange(0, 10, 0.5))
# legend index
plt.legend(prices.columns[1:], title='country', title_fontsize=13, loc="upper left")
plt.title('gas price evolution by year & country')
plt.savefig('prices.png')
plt.show()




