from store.models import Courier


class CourierService:
    @staticmethod
    def add_couriers(couriers):
        success, errors = list(), list()
        for idx, courier in enumerate(couriers):

            courier_id = courier['courier_id']
            temp_courier = Courier.query.get(courier_id)

            if not temp_courier:
                new_courier = Courier()
                new_courier.from_dict(courier)
                db.session.add(new_courier)
                success.append(courier_id)
            else:
                errors.append(courier_id)
        if not errors:
            db.session.commit()
        return success, errors

    @staticmethod
    def get_courier(id):
        courier = Courier.objects.filter(pk=id)
        return courier

    @staticmethod
    def edit_courier(courier, data):
        courier.edit(data)
        intersection_orders = courier.check_intersection_with_orders()
        OrderService.release_orders(intersection_orders)


    # TODO нужна ли статика?
    @staticmethod
    def get_assign_orders(courier):
        orders = courier.balancer_orders()
        time_service = TimeService()
        for order in orders:
            order.assign_time = time_service.get_assign_time()
        db.session.commit()
        return orders
