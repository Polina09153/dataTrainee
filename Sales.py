import pandas as pd
from faker import Faker
import matplotlib.pyplot as plt

#генерация данных
num_rows = 1000
fake = Faker()

product_ids = [f'product_{i}' for i in range(1, 101)]
categories = ['electronics', 'clothing', 'home', 'sports', 'toys']
regions = ['north', 'south', 'east', 'west']
managers = [f'manager_{i}' for i in range(1, 101)]


data = {
    'product_id': [fake.random_element(product_ids) for _ in range(num_rows)],
    'category': [fake.random_element(categories) for _ in range(num_rows)],
    'region': [fake.random_element(regions) for _ in range(num_rows)],
    'manager': [fake.random_element(managers) for _ in range(num_rows)],
    'sales_date': [fake.date_between(start_date='-1y', end_date='today') for _ in range(num_rows)],
    'quantity': [fake.pyint(min_value=1, max_value=100) for _ in range(num_rows)],
    'price': [fake.pyfloat(min_value=10, max_value=100, right_digits=2) for _ in range(num_rows)],
    'revenue': [fake.pyfloat(min_value=100, max_value=10000, right_digits=2) for _ in range(num_rows)]
}

df = pd.DataFrame(data)

df.to_csv('sales_data.csv', index=False)
print(f'CSV-файл "sales_data.csv" создан')


total_revenue = df['revenue'].sum()
print(f'Общий объем продаж: {total_revenue:.2f}')

# Анализ по категориям
sales_by_category = df.groupby('category')['revenue'].sum().sort_values(ascending=False)
print('\nПродажи по категориям:')
print(sales_by_category)

plt.figure(figsize=(10, 6))
sales_by_category.plot(kind='bar')
plt.title('Продажи по категориям')
plt.xlabel('Категория')
plt.ylabel('Объем продаж')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# 10 продуктов по продажам
top_products = df.groupby('product_id')['revenue'].sum().sort_values(ascending=False).head(10)
print('\n10 продуктов по продажам:')
print(top_products)

# Средняя цена и количество по категориям
print('\nСредняя цена и количество по категориям:')
print(df.groupby('category')[['price', 'quantity']].mean())