from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    IN_STOCK = 'in_stock'
    LOW_STOCK = 'low_stock'
    OUT_OF_STOCK = 'out_of_stock'
    STOCK_STATUS_CHOICES = [
        (IN_STOCK, 'In stock'),
        (LOW_STOCK, 'Low stock'),
        (OUT_OF_STOCK, 'Out of stock'),
    ]

    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    name = models.CharField(max_length=200)
    series = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    stock_status = models.CharField(
        max_length=20, choices=STOCK_STATUS_CHOICES, default=OUT_OF_STOCK, editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        # Keep stock_status in sync with stock_quantity automatically
        if self.stock_quantity == 0:
            self.stock_status = self.OUT_OF_STOCK
        elif self.stock_quantity <= 3:
            self.stock_status = self.LOW_STOCK
        else:
            self.stock_status = self.IN_STOCK
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f'Image for {self.product.name}'
    