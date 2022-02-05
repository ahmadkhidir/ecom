from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_single_data(self):
        return self.product_set.last()


class Product(models.Model):
    name = models.CharField(max_length=50)
    label = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    price = models.DecimalField(decimal_places=2, max_digits=999999)
    discount = models.DecimalField(decimal_places=2, default=0, max_digits=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_discount_price(self):
        return round(self.price - ((self.discount/100)*self.price), 2)

    def get_single_image(self):
        if self.image_set.count() != 0:
            print(self.image_set.count)
            return self.image_set.first().name.url
        return ''

    def get_multiple_image(self):
        r = 3
        if self.image_set.count() != 0:
            return [image.name.url for image in self.image_set.all()[:r]]
        return ['']*r

    def get_all_image(self):
        if self.image_set.count() != 0:
            return [image.name.url for image in self.image_set.all()]
        return ['']


class Image(models.Model):
    name = models.ImageField(upload_to="images/")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} ({self.name})"

    def get_image_url(self):
        return self.name.url


class Information(models.Model):
    text = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_modified = models.DateTimeField(auto_now=True)
    is_purchased = models.BooleanField(default=False)

    def get_total_price(self):
        return sum([p.get_sumed_price for p in self.cartitem_set])

    def is_empty(self):
        return False if self.cartitem_set.count else True
    
    def __str__(self):
        return f"{self.user.username} (cart {self.id})"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_sumed_price(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"Cart[{self.cart.id}] ({self.cart.user.username})"
