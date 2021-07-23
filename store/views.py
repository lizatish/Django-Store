# Create your views here.
from rest_framework.views import APIView

from store.tools.courier_service import CourierService
from store.tools.json_service import JsonService


class CourierView(APIView):
    def get(self, request, courier_id):
        pass

    def patch(self, request, courier_id):
        json_service = JsonService()

        data = request.data

        # errors = Validator().check_get_courier_validation(data)
        # if errors:
        #     return json_service.return_400()

        # TODO ошибки 404 вообще еще не покрыты тестами
        courier = CourierService.get_courier(courier_id)
        if not courier:
            return json_service.return_404()

        CourierService.edit_courier(courier, data)

        return json_service.return_200(courier.to_dict())

    def post(self, request):
        json_service = JsonService()

        return json_service.return_404()
