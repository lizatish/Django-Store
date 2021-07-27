# Create your views here.
from rest_framework.views import APIView

from store.tools.courier_service import CourierService
from store.tools.json_service import JsonService
from store.tools.order_service import OrderService
from store.tools.validation import Validator


class OneCourierView(APIView):
    def get(self, request, courier_id):
        json_service = JsonService()

        courier = CourierService.get_courier(courier_id)
        if not courier:
            return json_service.return_404()

        json_data = courier.to_dict()
        return json_service.return_200(json_data)

    def patch(self, request, courier_id):
        json_service = JsonService()

        data = request.data

        errors = Validator().check_get_courier_validation(data)
        if errors:
            return json_service.return_400()

        # TODO ошибки 404 вообще еще не покрыты тестами
        courier = CourierService.get_courier(courier_id)
        if not courier:
            return json_service.return_404()

        CourierService.edit_courier(courier, data)

        return json_service.return_200(courier.to_dict())


class CouriersView(APIView):

    def post(self, request):
        json_service = JsonService()

        couriers = request.data

        errors = Validator().check_post_couriers_validation(couriers)
        if errors:
            return json_service.return_validation_error_400('couriers', couriers, errors)

        success, errors = CourierService.add_couriers(couriers['data'])
        if errors:
            return json_service.return_courier_logic_error_answer_400(errors)

        return json_service.return_201('couriers', success)


class OrdersView(APIView):
    def post(self, request):
        json_service = JsonService()

        orders = request.data

        errors = Validator().check_post_orders_validation(orders)
        if errors:
            return json_service.return_validation_error_400('orders', orders, errors)

        success, errors = OrderService.add_orders(orders['data'])
        if errors:
            return json_service.return_order_logic_error_answer_400(errors)

        return json_service.return_201('orders', success)


class AssignOrdersView(APIView):
    def post(self, request):
        json_service = JsonService()

        data = request.data

        errors = Validator().check_post_orders_assign_validation(data)
        if errors:
            return json_service.return_400()

        courier = CourierService.get_courier(data['courier_id'])
        if not courier:
            return json_service.return_400()

        orders = CourierService.get_assign_orders(courier)
        return json_service.return_order_assign_200(orders)


class CompleteOrdersView(APIView):
    def post(self, request):
        json_service = JsonService()

        data = request.data

        errors = Validator().check_post_orders_complete(data)
        if errors:
            return json_service.return_400()

        order = OrderService.get_order(data['order_id'])
        if not order or order.courier_id != data['courier_id']:
            return json_service.return_400()

        if not order.is_complete:
            OrderService.complete_order(order, data['complete_time'])

        return json_service.return_200({'order_id': order.id})
