from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from .views import data


@receiver(post_save, sender=Order)
def check_robot(sender, instance, created, **kwargs):
    if created and instance.model == data['model'] and instance.version == data['version']:
        print(f'Добрый день! Недавно вы интересовались нашим роботом модели {data["model"]}, версии {data["version"]}.'
              f' Этот робот теперь в наличии. Если вам подходит этот вариант, пожалуйста, свяжитесь с нами.')
