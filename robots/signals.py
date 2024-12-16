from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from robots.models import Robot
from orders.models import Order

@receiver(post_save, sender=Robot)
def notify_customer_on_robot_availability(sender, instance, created, **kwargs):
    if created:
        matching_orders = Order.objects.filter(robot_serial=f"{instance.model}-{instance.version}")
        for order in matching_orders:
            send_mail(
                subject="Робот теперь в наличии!",
                message=(
                    f"Добрый день!\n"
                    f"Недавно вы интересовались нашим роботом модели {instance.model}, версии {instance.version}.\n"
                    f"Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами."
                ),
                from_email="noreply@example.com",
                recipient_list=[order.customer.email],
                fail_silently=False,
            )
