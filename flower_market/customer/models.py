from django.db import models


class OrderCall(models.Model):
    IN_PROCESS, ACCEPTED, CANCELED = range(0, 3)
    STATUS_CHOICES = ((IN_PROCESS, 'Обрабатывается'), (ACCEPTED, 'Принято'), (CANCELED, 'Отменено'))
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)

    call_time = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=IN_PROCESS)


class OrderDetail(models.Model):
    PICKUP, COURIER = 0, 1
    DELIVERY_CHOICES = ((PICKUP, 'Самовывоз'), (COURIER, 'Курьер'))
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)

    delivery_type = models.IntegerField(choices=DELIVERY_CHOICES, default=PICKUP)
    address = models.CharField(max_length=255, blank=True)


class Order(models.Model):
    IN_PROCESS, ACCEPTED, CANCELED, COMPLETED = range(0, 4)
    STATUS_CHOICES = ((IN_PROCESS, 'Обрабатывается'), (ACCEPTED, 'Принято'),
                      (CANCELED, 'Отменено'), (COMPLETED, 'Завершено'))

    amount = models.IntegerField()
    ordered_time = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=IN_PROCESS)
    order_detail = models.OneToOneField(OrderDetail, on_delete=models.CASCADE)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    flower_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.IntegerField()


