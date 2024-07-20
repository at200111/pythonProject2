## Итоговое задание №3


Программа анализирует данные о продажах продуктов в магазине и строит графики наглядного представления информации.

В программе реализованы следующие функции:

read_sales_data(file_path), которая принимает путь к файлу и возвращает список продаж. Продажи в свою очередь являются словарями с ключами product_name, quantity, price, date (название, количество, цена, дата).
total_sales_per_product(sales_data), которая принимает список продаж и возвращает словарь, где ключ - название продукта, а значение - общая сумма продаж этого продукта.
sales_over_time(sales_data), которая принимает список продаж и возвращает словарь, где ключ - дата, а значение общая сумма продаж за эту дату.
 

Входные хранятся в файле (файл "sales_list" в репозитории проекта).
В ходе анализа данных из файла выводятся на экран два значения:

-Продукт который принес наибольшую выручку.
-День в который была наибольшая сумма продаж.
 
В завершении работы программы строятся два графика:

График общей суммы продаж по каждому продукту.
График общей суммы продаж по дням.
