import ast
import json

from store.models.courier import Courier
from store.models.order import Order
from store.tools.time_service import TimeService

HEADERS = {"Content-Type": "application/json"}
ROUTE = 'orders/complete'


def test_complete_one_valid_order_courier_type_foot(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "foot",
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
                "weight": 0.23,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }
    _ = test_client.post('orders', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
    }
    _ = test_client.post('orders/assign', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
        "order_id": 1,
        "complete_time": "2021-01-10T10:33:01.42Z"
    }
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))

    assert response.status_code == 200

    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert len(data) == 1
    assert data.get('order_id') == 1

    order = Order.objects.get(1)
    assert order.complete_time == TimeService().get_datetime('2021-01-10T10:33:01.42Z')
    assert order.is_complete
    assert order.courier_id == 1

    courier = Courier.objects.get(1)
    assert courier.current_weight == 0


def test_complete_one_valid_order_courier_type_bike(test_client):
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
                "weight": 0.23,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }
    _ = test_client.post('orders', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
    }
    _ = test_client.post('orders/assign', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
        "order_id": 1,
        "complete_time": "2021-01-10T10:33:01.42Z"
    }
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))

    assert response.status_code == 200

    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert len(data) == 1
    assert data.get('order_id') == 1

    order = Order.objects.get(1)
    assert order.complete_time == TimeService().get_datetime('2021-01-10T10:33:01.42Z')
    assert order.is_complete
    assert order.courier_id == 1

    courier = Courier.objects.get(1)
    assert courier.current_weight == 0


def test_complete_one_valid_order_courier_type_car(test_client):
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
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 0.23,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }
    _ = test_client.post('orders', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
    }
    _ = test_client.post('orders/assign', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
        "order_id": 1,
        "complete_time": "2021-01-10T10:33:01.42Z"
    }
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))

    assert response.status_code == 200

    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert len(data) == 1
    assert data.get('order_id') == 1

    order = Order.objects.get(1)
    assert order.complete_time == TimeService().get_datetime('2021-01-10T10:33:01.42Z')
    assert order.is_complete
    assert order.courier_id == 1

    courier = Courier.objects.get(1)
    assert courier.current_weight == 0


def test_complete_multiple_valid_orders_courier_type_foot(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "foot",
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
                "weight": 0.23,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            },
            {
                "order_id": 2,
                "weight": 0.23,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }
    _ = test_client.post('orders', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
    }
    _ = test_client.post('orders/assign', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
        "order_id": 1,
        "complete_time": "2021-01-10T10:33:01.42Z"
    }
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert len(data) == 1
    assert data.get('order_id') == 1

    order = Order.objects.get(1)
    assert order.complete_time == TimeService().get_datetime('2021-01-10T10:33:01.42Z')
    assert order.is_complete
    assert order.courier_id == 1

    courier = Courier.objects.get(1)
    assert courier.current_weight == 0.23

    data = {
        "courier_id": 1,
        "order_id": 2,
        "complete_time": "2021-01-10T10:33:01.42Z"
    }
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert len(data) == 1
    assert data.get('order_id') == 2

    order = Order.objects.get(1)
    assert order.complete_time == TimeService().get_datetime('2021-01-10T10:33:01.42Z')
    assert order.is_complete
    assert order.courier_id == 1

    courier = Courier.objects.get(1)
    assert courier.current_weight == 0


def test_complete_multiple_valid_orders_courier_type_bike(test_client):
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
                "weight": 0.23,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            },
            {
                "order_id": 2,
                "weight": 0.23,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }
    _ = test_client.post('orders', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
    }
    _ = test_client.post('orders/assign', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
        "order_id": 1,
        "complete_time": "2021-01-10T10:33:01.42Z"
    }
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert len(data) == 1
    assert data.get('order_id') == 1

    order = Order.objects.get(1)
    assert order.complete_time == TimeService().get_datetime('2021-01-10T10:33:01.42Z')
    assert order.is_complete
    assert order.courier_id == 1

    courier = Courier.objects.get(1)
    assert courier.current_weight == 0.23

    data = {
        "courier_id": 1,
        "order_id": 2,
        "complete_time": "2021-01-10T10:33:01.42Z"
    }
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert len(data) == 1
    assert data.get('order_id') == 2

    order = Order.objects.get(1)
    assert order.complete_time == TimeService().get_datetime('2021-01-10T10:33:01.42Z')
    assert order.is_complete
    assert order.courier_id == 1

    courier = Courier.objects.get(1)
    assert courier.current_weight == 0


def test_complete_multiple_valid_orders_courier_type_car(test_client):
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
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 0.23,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            },
            {
                "order_id": 2,
                "weight": 0.23,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }
    _ = test_client.post('orders', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
    }
    _ = test_client.post('orders/assign', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
        "order_id": 1,
        "complete_time": "2021-01-10T10:33:01.42Z"
    }
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert len(data) == 1
    assert data.get('order_id') == 1

    order = Order.objects.get(1)
    assert order.complete_time == TimeService().get_datetime('2021-01-10T10:33:01.42Z')
    assert order.is_complete
    assert order.courier_id == 1

    courier = Courier.objects.get(1)
    assert courier.current_weight == 0.23

    data = {
        "courier_id": 1,
        "order_id": 2,
        "complete_time": "2021-01-10T10:33:01.42Z"
    }
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert len(data) == 1
    assert data.get('order_id') == 2

    order = Order.objects.get(1)
    assert order.complete_time == TimeService().get_datetime('2021-01-10T10:33:01.42Z')
    assert order.is_complete
    assert order.courier_id == 1

    courier = Courier.objects.get(1)
    assert courier.current_weight == 0
