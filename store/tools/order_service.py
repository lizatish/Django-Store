
class OrderService:
    @staticmethod
    def add_orders(orders):
        success, errors = list(), list()
        for idx, order in enumerate(orders):

            order_id = order['order_id']
            temp_courier = Order.query.get(order_id)

            if not temp_courier:
                new_order = Order()
                new_order.from_dict(order)
                db.session.add(new_order)
                success.append(order_id)
            else:
                errors.append(order_id)
        if not errors:
            db.session.commit()
        return success, errors

    @staticmethod
    def get_order(id):
        order = Order.query.get(id)
        return order

    @staticmethod
    def release_orders(orders):
        for order in orders:
            order.courier_id = None
            order.assign_time = None
        db.session.commit()

    @staticmethod
    def complete_order(new_order, complete_time):
        from store.tools.courier_service import CourierService

        new_order.complete_order(complete_time)
        courier = CourierService.get_courier(new_order.courier_id)
        courier.complete_order(new_order)
        db.session.commit()

        last_complete_order = CompletedOrders.query.filter_by(
            courier_id=new_order.courier_id,
            region=new_order.region
        ).first()
        if not last_complete_order:
            last_complete_order = CompletedOrders(
                courier_id=new_order.courier_id,
                completed_orders=1,
                last_complete_time=new_order.complete_time,
                general_complete_seconds=(new_order.complete_time - new_order.assign_time).total_seconds(),
                region=new_order.region
            )
            db.session.add(last_complete_order)
        else:
            last_complete_order.update(new_order)

        db.session.commit()
