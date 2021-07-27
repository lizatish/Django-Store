import ast
import json

from store.models.courier import Courier

HEADERS = {"Content-Type": "application/json"}


def test_patch_courier_with_assign_orders_bike_to_bike(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "bike",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:05", "09:00-11:00"]
            }
        ]
    }
    _ = test_client.post('couriers', headers=HEADERS, data=json.dumps(data))
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 9,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            },
            {
                "order_id": 2,
                "weight": 0.1,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            },
            {
                "order_id": 3,
                "weight": 0.1,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }
    _ = test_client.post('orders', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1
    }
    response = test_client.post('orders/assign', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert len(data) == 2
    assert len(data.get('orders')) == 3

    data = {
        "courier_type": "bike"
    }
    response = test_client.patch('couriers/1', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.max_weight == 15
    assert courier.current_weight == 9.2
    assert len(courier.orders) == 3
