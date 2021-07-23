from django.db import models


class CompletedOrders(models.Model):
    __tablename__ = 'completed_orders'

    courier_id = models.ForeignKey('Courier', on_delete=models.CASCADE)
    completed_orders = models.IntegerField(default=0)
    last_complete_time = models.DateTimeField()
    general_complete_seconds = models.FloatField()
    region = models.IntegerField()

    def update(self, order):
        total_secs = (order.complete_time - self.last_complete_time).total_seconds()
        self.completed_orders += 1
        self.last_complete_time = order.complete_time
        self.general_complete_seconds += total_secs
