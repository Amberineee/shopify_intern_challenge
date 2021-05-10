#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#load data
df = pd.read_csv('data.csv')
df['created_at']= pd.to_datetime(df['created_at']).dt.normalize()
#check aov
df.order_amount.mean()
df.order_amount.median()
#check aov on different payment methods
df_cash = df[df.payment_method == "cash"]
df_cash.order_amount.median()

df_credit_card = df[df.payment_method == "credit_card"]
df_credit_card.order_amount.median()
#seaborn plot
df['avg_7day'] = df.order_amount.rolling(7).mean().shift(-3)

sns.lineplot(x = 'created_at', y = 'order_amount', label = 'Daily', data = df, ci=None)
sns.lineplot(x = 'created_at', y = 'avg_7day', label = '7-day-avg', data = df, ci=None)
plt.xticks(rotation=90)
plt.xlabel("Date")
plt.ylabel("Order Amount")
plt.title('Time Series Plot of Order Amount with 7 Day Average')
plt.show()
