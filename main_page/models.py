from django.db import models

# Создаем таблицу категорий
class Category(models.Model):

   # Создаем колонки для таблицы
    category_name = models.CharField(max_length=75) #Cоздаем колонку с именами, задаем длину в 75 символов
    reg_date = models.DateTimeField(auto_now_add=True) #Cоздаем колонку с датой, автозаполнение текущей даты

    # Вывод информации в нормальном виде
    def __str__(self):
        return self.category_name


# Создаем таблицу продуктов
class Product(models.Model):
    # Создаем колонки для таблицы
    prod_name = models.CharField(max_length=75)  # Cоздаем колонку с именами, задаем длину в 75 символов
    prod_count = models.IntegerField()  # Cоздаем колонку с количеством
    prod_price = models.FloatField() # Cоздаем колонку с ценой
    prod_photo = models.ImageField(upload_to='media') # Cоздаем колонку с фото
    prod_des = models.TextField() # Cоздаем колонку с описанием
    prod_coteg = models.ForeignKey(Category, on_delete=models.CASCADE) # Cоздаем колонку с выбором категории
    prod_rdate = models.DateTimeField(auto_now_add=True) # Cоздаем колонку с датой, автозаполнение текущей даты

    # Вывод информации в нормальном виде
    def __str__(self):
        return self.prod_name

class Cart(models.Model):
    # Создаем колонки для таблицы
    cart_user_id = models.IntegerField()  # Cоздаем колонку с ID пользователя
    cart_prod_name = models.ForeignKey(Product, on_delete=models.CASCADE)  # Cоздаем колонку с наименованием продуктов
    cart_prod_quantity = models.IntegerField() # Cоздаем колонку с количеством
    cart_prod_total = models.FloatField() # Cоздаем колонку с суммой продукта
    cart_reg_date = models.DateTimeField(auto_now_add=True)  # Cоздаем колонку с датой, автозаполнение текущей даты
    # Вывод информации в нормальном виде
    def __str__(self):
        return str(self.cart_user_id)