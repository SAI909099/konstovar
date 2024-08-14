from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, SlugField, DateTimeField, IntegerField, ImageField
from django.db.models import PositiveIntegerField, CASCADE, ForeignKey, TextChoices
from django_ckeditor_5.fields import CKEditor5Field
from mptt.models import MPTTModel, TreeForeignKey





class CreatedBaseModel(Model):
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    pass


class Category(MPTTModel):
    name = CharField(max_length=225, default="Default Category Name")
    slug = SlugField(max_length=225, null=True, blank=True)
    parent_id = TreeForeignKey('self', CASCADE, null=True, blank=True, related_name='children')  # Renamed to 'parent'

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(max_length=225)
    title = CharField(max_length=225)
    slug = SlugField()
    descriptions = CKEditor5Field()
    price = PositiveIntegerField()
    tag = CharField(max_length=225)
    category_id = ForeignKey('apps.Category', CASCADE,
                             related_name='products')  # Updated to reference 'Category' directly

    def __str__(self):
        return self.name

class ProductImage(Model):
    image = ImageField(upload_to='products/',null=True)
    product_id = ForeignKey('apps.Product',CASCADE,related_name='image')

class Order(CreatedBaseModel):
    class Status(TextChoices):
        PROCESSING = 'processing', 'Processing'
        ON_HOLD = 'on_hold', 'On Hold'
        PENDING = 'pending', 'Pending'
        COMPLETED = 'completed', 'Completed'

    class DeliveryMethod(TextChoices):
        PICKUP = 'pickup', 'Pickup'
        COURIER = 'courier', 'Courier'

    class PaymentMethod(TextChoices):
        CARD = 'card', 'Card',
        CASH = 'cash', 'Cash'

    user_id = ForeignKey('apps.User', CASCADE, related_name='order')
    total_amount = PositiveIntegerField()
    status = CharField(max_length=25, choices=Status.choices, default=Status.PROCESSING)
    delivery_method = CharField(max_length=25, choices=DeliveryMethod.choices, default=DeliveryMethod.COURIER)
    comment = CharField(max_length=255)
    payment_method = CharField(max_length=25, choices=PaymentMethod.choices, default=PaymentMethod.CARD)
    description = CharField(max_length=255, null=True, blank=True)


class OrderItem(CreatedBaseModel):
    product_id = ForeignKey('apps.Product', CASCADE, related_name='order')
    count = IntegerField()
    order_id = ForeignKey('apps.Order',CASCADE,related_name='order_item')


class AdPost(Model):
    category_id = ForeignKey('apps.Category',CASCADE,related_name='ad_post')
    image = ImageField(null=True)

class Courier(Model):
    address = ForeignKey('apps.UserAddress',CASCADE,related_name='courier')

class UserAddress(CreatedBaseModel):
    full_name = CharField(max_length=255)
    street = CharField(max_length=255)
    zip_code = PositiveIntegerField()
    city = CharField(max_length=255)
    phone = CharField(max_length=255)
    user = ForeignKey('apps.User', CASCADE, related_name='addresses')