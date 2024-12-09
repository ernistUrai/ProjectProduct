
from django.db import models
from django.contrib.auth.models import User




class Category(models.Model):
    name = models.CharField("Категория", max_length=100, unique=True)
    product = models.ManyToManyField('Product', related_name="categories", blank=True)
    created_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    

class Product(models.Model):
    SIZE_CHOICES = (
        ('36', '36'),
        ('42', '42'),
        ('44', '44'),
        ('46', '46'),
        ('48', '48'),
        ('50', '50'),
    )
    
    COLOR_CHOICES = (
        ('Черный', 'Черный'),
        ('Белый', 'Белый'),
        ('Желтый', 'Желтый'),
        ('Синий', 'Синий'),
        ('Красный', 'Красный'),
        ('Зеленый', 'Зеленый'),
    )
        
    name = models.CharField("Название", max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="shoes_list")
    image = models.ImageField("Изображение", upload_to="Product/images/")
    description = models.TextField("Описание")
    size = models.CharField("Размер", max_length=2, choices=SIZE_CHOICES)
    color = models.CharField("Цвет", max_length=15, choices=COLOR_CHOICES)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    created_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    quantity = models.PositiveIntegerField('Количество', default=1)
    created_data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Cart {self.user.username}'
    
    
class Order(models.Model):
    STATUS_CHOICES = (
        ('С картой', 'С картой'),
        ('Наличными', 'Наличными'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    total_price = models.DecimalField('Сумма заказа', max_digits=10, decimal_places=2, default=0)  
    delivery_address = models.CharField('Адрес доставки', max_length=100)
    payment_status = models.CharField('Статус оплаты', max_length=50, choices=STATUS_CHOICES)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    

    def __str__(self):
        return f'Заказ от {self.user.username}'
