from store.models.courier import Courier
from store.tools.order_service import OrderService
from store.tools.time_service import TimeService


class CourierService:
    @staticmethod
    def add_couriers(couriers):
        success, errors = list(), list()
        for idx, courier in enumerate(couriers):

            courier_id = courier['courier_id']
            temp_courier = Courier.objects.filter(id=courier_id).first()

            if not temp_courier:
                new_courier = Courier()
                new_courier.from_dict(courier)
                new_courier.save()
                # TODO дичь
                new_courier.set_assign_time(courier['working_hours'])
                new_courier.save()
                success.append(courier_id)
            else:
                errors.append(courier_id)
        # TODO подумать про транзации
        # if not errors:
        #    new_courier.save()
        return success, errors

    @staticmethod
    def get_courier(id):
        courier = Courier.objects.filter(id=id).first()
        return courier

    @staticmethod
    def edit_courier(courier, data):
        courier.edit(data)
        intersection_orders = courier.check_intersection_with_orders()
        OrderService.release_orders(intersection_orders)

    @staticmethod
    def get_assign_orders(courier):
        orders = courier.balancer_orders()
        time_service = TimeService()
        for order in orders:
            order.assign_time = time_service.get_assign_time()
            order.save()
        # db.session.commit()
        return orders
