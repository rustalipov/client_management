from django.db import models

class Client(models.Model):
    registration_number = models.IntegerField(unique=True)
    registration_date = models.DateField()
    client_name = models.CharField(max_length=150)
    inn = models.BigIntegerField()  # Используем BigIntegerField для длинных чисел
    phone_number = models.CharField(max_length=15)
    kkm_model = models.CharField(max_length=50)
    znm = models.CharField(max_length=100)
    email = models.EmailField(default='')
    password_hash = models.CharField(max_length=128)  # Хешированный пароль
    status = models.IntegerField(choices=((0, 'Активный'), (1, 'Временный'), (2, 'Снятый с учета')))
    payment_date = models.DateField()
    end_of_service_date = models.DateField()

    def __str__(self):
        return str(self.registration_number)  # Приводим к строке
