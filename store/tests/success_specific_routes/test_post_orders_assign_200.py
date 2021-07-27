import ast
import json
from datetime import datetime

from store.models.courier import Courier
from store.models.order import Order
from store.tools.time_service import TimeService

HEADERS = {"Content-Type": "application/json"}
ROUTE = 'orders/assign'


def test_assign_one_valid_order(test_client):
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
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert len(data) == 2
    assert len(data.get('orders')) == 1
    assert data.get('orders')[0]['id'] == 1
    assert data.get('assign_time')
    assert (datetime.utcnow() - TimeService().get_datetime(data.get('assign_time'))).seconds <= 5


def test_assign_multiple_valid_orders(test_client):
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
                "delivery_hours": ["12:00-18:00"]
            }
        ]
    }
    _ = test_client.post('orders', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
    }
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert len(data) == 2
    assert len(data.get('orders')) == 2
    assert data.get('orders')[0]['id'] == 1
    assert data.get('orders')[0]['id'] == 1
    assert data.get('assign_time')
    assert (datetime.utcnow() - TimeService().get_datetime(data.get('assign_time'))).seconds <=5


def test_assign_one_valid_order_addition_params(test_client):
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
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    data = ast.literal_eval(response.data.decode("UTF-8"))

    courier = Courier.objects.get(1)
    assert courier.max_weight == 10
    assert courier.current_weight== 0.23

    order = Order.objects.get(1)
    assert order.assign_time == TimeService().get_datetime(data.get('assign_time'))
    assert order.courier_id == 1


def test_assign_multiple_valid_orders_addition_params(test_client):
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
                "delivery_hours": ["12:00-18:00"]
            }
        ]
    }
    _ = test_client.post('orders', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
    }
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    data = ast.literal_eval(response.data.decode("UTF-8"))

    courier = Courier.objects.get(1)
    assert courier.max_weight == 10
    assert courier.current_weight== 0.23 + 0.23

    order = Order.objects.get(1)
    assert order.assign_time == TimeService().get_datetime(data.get('assign_time'))
    assert order.courier_id == 1
    order = Order.objects.get(2)
    assert order.assign_time == TimeService().get_datetime(data.get('assign_time'))
    assert order.courier_id == 1


def test_assign_one_valid_order_from_courier_type_bike(test_client):
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
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    data = ast.literal_eval(response.data.decode("UTF-8"))

    courier = Courier.objects.get(1)
    assert courier.max_weight == 15
    assert courier.current_weight== 0.23

    order = Order.objects.get(1)
    assert order.assign_time == TimeService().get_datetime(data.get('assign_time'))
    assert order.courier_id == 1


def test_assign_one_valid_order_from_courier_type_car(test_client):
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
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    data = ast.literal_eval(response.data.decode("UTF-8"))

    courier = Courier.objects.get(1)
    assert courier.max_weight == 50
    assert courier.current_weight== 0.23

    order = Order.objects.get(1)
    assert order.assign_time == TimeService().get_datetime(data.get('assign_time'))
    assert order.courier_id == 1


def test_assign_one_notvalid_on_weight_order_from_courier_type_foot(test_client):
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
                "weight": 10.23,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }
    _ = test_client.post('orders', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
    }
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    data = ast.literal_eval(response.data.decode("UTF-8"))

    assert len(data) == 1
    assert data.get('orders') == []

    order = Order.objects.get(1)
    assert order.courier_id is None
    assert order.assign_time is None


def test_assign_one_notvalid_on_weight_order_from_courier_type_bike(test_client):
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
                "weight": 15.23,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }
    _ = test_client.post('orders', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
    }
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    data = ast.literal_eval(response.data.decode("UTF-8"))

    assert len(data) == 1
    assert data.get('orders') == []

    order = Order.objects.get(1)
    assert order.courier_id is None
    assert order.assign_time is None


def test_assign_one_notvalid_on_weight_order_from_courier_type_car(test_client):
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
                "weight": 40.23,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            },
            {
                "order_id": 2,
                "weight": 40.23,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }
    _ = test_client.post('orders', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
    }
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    data = ast.literal_eval(response.data.decode("UTF-8"))

    assert len(data) == 2
    assert len(data.get('orders')) == 1
    assert data.get('orders')[0]['id'] == 1
    assert (datetime.utcnow() - TimeService().get_datetime(data.get('assign_time'))).seconds <= 5

    order = Order.objects.get(1)
    assert order.courier_id == 1
    assert order.assign_time == TimeService().get_datetime(data.get('assign_time'))

    order = Order.objects.get(2)
    assert order.courier_id is None
    assert order.assign_time is None


def test_assign_one_notvalid_on_weight_order_from_regions_courier_type_foot(test_client):
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
                "region": 13,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }
    _ = test_client.post('orders', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
    }
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    data = ast.literal_eval(response.data.decode("UTF-8"))

    assert len(data) == 1
    assert data.get('orders') == []

    order = Order.objects.get(1)
    assert order.courier_id is None
    assert order.assign_time is None


def test_assign_one_notvalid_on_weight_order_from_regions_courier_type_bike(test_client):
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
                "region": 13,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }
    _ = test_client.post('orders', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
    }
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    data = ast.literal_eval(response.data.decode("UTF-8"))

    assert len(data) == 1
    assert data.get('orders') == []

    order = Order.objects.get(1)
    assert order.courier_id is None
    assert order.assign_time is None


def test_assign_one_notvalid_on_weight_order_from_regions_courier_type_car(test_client):
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
                "region": 13,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }
    _ = test_client.post('orders', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
    }
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    data = ast.literal_eval(response.data.decode("UTF-8"))

    assert len(data) == 1
    assert data.get('orders') == []

    order = Order.objects.get(1)
    assert order.courier_id is None
    assert order.assign_time is None


def test_assign_one_notvalid_on_weight_order_from_working_hours_courier_type_car(test_client):
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
                "region": 13,
                "delivery_hours": ["17:00-18:00"]
            }
        ]
    }
    _ = test_client.post('orders', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
    }
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    data = ast.literal_eval(response.data.decode("UTF-8"))

    assert len(data) == 1
    assert data.get('orders') == []

    order = Order.objects.get(1)
    assert order.courier_id is None
    assert order.assign_time is None


def test_assign_one_notvalid_on_weight_order_from_working_hours_courier_type_car2(test_client):
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
                "region": 13,
                "delivery_hours": ["6:00-7:00"]
            }
        ]
    }
    _ = test_client.post('orders', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
    }
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    data = ast.literal_eval(response.data.decode("UTF-8"))

    assert len(data) == 1
    assert data.get('orders') == []

    order = Order.objects.get(1)
    assert order.courier_id is None
    assert order.assign_time is None


def test_assign_one_notvalid_on_weight_order_from_working_hours_courier_type_car3(test_client):
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
                "region": 13,
                "delivery_hours": ["11:00-11:35"]
            }
        ]
    }
    _ = test_client.post('orders', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
    }
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    data = ast.literal_eval(response.data.decode("UTF-8"))

    assert len(data) == 1
    assert data.get('orders') == []

    order = Order.objects.get(1)
    assert order.courier_id is None
    assert order.assign_time is None


def test_assign_one_notvalid_on_weight_order_from_working_hours_courier_type_bike(test_client):
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
                "region": 13,
                "delivery_hours": ["17:00-18:00"]
            }
        ]
    }
    _ = test_client.post('orders', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
    }
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    data = ast.literal_eval(response.data.decode("UTF-8"))

    assert len(data) == 1
    assert data.get('orders') == []

    order = Order.objects.get(1)
    assert order.courier_id is None
    assert order.assign_time is None


def test_assign_one_notvalid_on_weight_order_from_working_hours_courier_type_bike2(test_client):
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
                "region": 13,
                "delivery_hours": ["6:00-7:00"]
            }
        ]
    }
    _ = test_client.post('orders', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
    }
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    data = ast.literal_eval(response.data.decode("UTF-8"))

    assert len(data) == 1
    assert data.get('orders') == []

    order = Order.objects.get(1)
    assert order.courier_id is None
    assert order.assign_time is None


def test_assign_one_notvalid_on_weight_order_from_working_hours_courier_type_bike3(test_client):
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
                "region": 13,
                "delivery_hours": ["11:00-11:35"]
            }
        ]
    }
    _ = test_client.post('orders', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
    }
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    data = ast.literal_eval(response.data.decode("UTF-8"))

    assert len(data) == 1
    assert data.get('orders') == []

    order = Order.objects.get(1)
    assert order.courier_id is None
    assert order.assign_time is None


def test_assign_one_notvalid_on_weight_order_from_working_hours_courier_type_foot(test_client):
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
                "region": 13,
                "delivery_hours": ["17:00-18:00"]
            }
        ]
    }
    _ = test_client.post('orders', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
    }
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    data = ast.literal_eval(response.data.decode("UTF-8"))

    assert len(data) == 1
    assert data.get('orders') == []

    order = Order.objects.get(1)
    assert order.courier_id is None
    assert order.assign_time is None


def test_assign_one_notvalid_on_weight_order_from_working_hours_courier_type_foot2(test_client):
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
                "region": 13,
                "delivery_hours": ["6:00-7:00"]
            }
        ]
    }
    _ = test_client.post('orders', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
    }
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    data = ast.literal_eval(response.data.decode("UTF-8"))

    assert len(data) == 1
    assert data.get('orders') == []

    order = Order.objects.get(1)
    assert order.courier_id is None
    assert order.assign_time is None


def test_assign_one_notvalid_on_weight_order_from_working_hours_courier_type_foot3(test_client):
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
                "region": 13,
                "delivery_hours": ["11:00-11:35"]
            }
        ]
    }
    _ = test_client.post('orders', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
    }
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    data = ast.literal_eval(response.data.decode("UTF-8"))

    assert len(data) == 1
    assert data.get('orders') == []

    order = Order.objects.get(1)
    assert order.courier_id is None
    assert order.assign_time is None
