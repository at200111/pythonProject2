

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
import sys

def read_sales_data(file_path):
    '''Функция, которая принимает путь к файлу и возвращает список продаж.
     Продажи в свою очередь являются словарями с ключами product_name,
     quantity, price, date (название, количество, цена, дата).'''
    with open(file_path) as f:
        data = f.readlines()
        sales_list = []
        for i in data:
            row = i.split(',')
            sales_list.append({'product_name' : row[0],
                               'quantity': int(row[1]),
                               'price': float(row[2]),
                               'date': datetime.strptime(row[3].strip(), '%Y-%m-%d')})
    return sales_list


def total_sales_per_product(sales_data):
    '''Функция которая принимает список продаж и возвращает словарь,
    где ключ - название продукта, а значение - общая сумма продаж этого продукта.'''
    product_sales = {}
    for sale in sales_data:
        product_name = sale['product_name']
        total_sale = sale['quantity'] * sale['price']
        if product_name in product_sales:
            product_sales[product_name] += total_sale
        else:
            product_sales[product_name] = total_sale
    return product_sales


def sales_over_time(sales_data):
    sales_by_date = {}
    for sale in sales_data:
        sale_date = sale['date'].date()
        total_sale = sale['quantity'] * sale['price']
        if sale_date in sales_by_date:
            sales_by_date[sale_date] += total_sale
        else:
            sales_by_date[sale_date] = total_sale
    return sales_by_date

def plot_total_sales_per_product(total_sales_per_product):
    products = list(total_sales_per_product.keys())
    sales = list(total_sales_per_product.values())

    plt.figure(figsize=(10, 6))
    plt.bar(products, sales, color='skyblue')
    plt.xlabel('Products')
    plt.ylabel('Total Sales')
    plt.title('Total Sales per Product')
    plt.show()


def plot_sales_over_time(sales_over_time):
    dates = sorted(sales_over_time.keys())
    sales = [sales_over_time[date] for date in dates]
    plt.figure(figsize=(10, 6))
    plt.plot(dates, sales, marker='o', linestyle='-', color='skyblue')
    plt.xlabel('Date')
    plt.ylabel('Total Sales')
    plt.title('Total Sales Over Time')

    # Форматирование оси X для отображения дат
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.gcf().autofmt_xdate()  # Автоматический поворот меток на оси X для лучшего отображения

    plt.show()



if __name__ == '__main__':
    data = read_sales_data('sales_list.txt')
    total_sales = total_sales_per_product(data)
    sales_over_time = sales_over_time(data)
    print(max(total_sales, key = total_sales.get))
    print(max(sales_over_time, key = sales_over_time.get))
    plot_total_sales_per_product(total_sales)
    plot_sales_over_time(sales_over_time)
    sys.exit()





