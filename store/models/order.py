from django.db import models

from store.models.order_assign_time import OrderAssignTime


class Order(models.Model):
    # __tablename__ = 'order'

    id = models.IntegerField(primary_key=True, unique=True)
    courier_id = models.ForeignKey('Courier', on_delete=models.CASCADE)

    weight = models.FloatField()
    region = models.IntegerField()

    is_complete = models.BooleanField(default=False)
    complete_time = models.DateTimeField()
    assign_time = models.DateTimeField()

    # assign_times: List[OrderAssignTime] = db.relationship(OrderAssignTime, backref=db.backref('order'))

    def get_assign_times(self):
        return OrderAssignTime.query.filter_by(
            order_id=self.id
        ).order_by(OrderAssignTime.time_start_hour, OrderAssignTime.time_start_min,
                   OrderAssignTime.time_finish_hour, OrderAssignTime.time_finish_min).all()

    def from_dict(self, data):
        for field in ['order_id', 'weight', 'region', 'delivery_hours']:
            if field in data:
                if field == 'delivery_hours':
                    for working_hour in data[field]:
                        assign_time = OrderAssignTime(working_hour, data['order_id'])
                        db.session.add(assign_time)
                elif field == 'order_id':
                    setattr(self, 'id', data[field])
                else:
                    setattr(self, field, data[field])

    def complete_order(self, complete_time):
        self.is_complete = True
        self.complete_time = complete_time

    def get_delivery_hours(self):
        return [str(assign_time) for assign_time in self.assign_times]
