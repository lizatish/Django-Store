import ast
import json

from store.models.courier import Courier
from store.models.courier_type import CourierType

HEADERS = {"Content-Type": "application/json"}


def get_route(id):
    return f'/couriers/{id}'


def test_get_one_courier(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "car",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:05", "09:00-11:00"]
            }
        ]
    }
    _ = test_client.post('couriers', headers=HEADERS, data=json.dumps(data))
    response = test_client.get(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert len(data) == 5
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert data.get('courier_id') == 1
    assert data.get('courier_type') == 'car'
    assert data.get('regions') == [1, 12, 22]
    assert data.get('working_hours') == ["11:35-14:05", "09:00-11:00"]
    assert data.get('earnings') == 0

    courier = Courier.objects.get(1)
    assert courier.courier_type == CourierType.CAR
    assert courier.regions == [1, 12, 22]
    assert courier.get_working_hours() == ["11:35-14:05", "09:00-11:00"]

