import ast
import json

from store.models.order import Order

HEADERS = {"Content-Type": "application/json"}
ROUTE = '/orders'


def test_post_one_order_base_data(test_client):
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

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 201

    data = ast.literal_eval(response.data.decode("UTF-8"))
    success_orders = data.get('orders')
    assert success_orders is not None
    assert len(success_orders) == 1
    assert success_orders[0]['id'] == 1

    order = Order.objects.get(1)
    assert order.weight== 0.23
    assert order.region == 12
    assert order.get_delivery_hours() == ["09:00-18:00"]


def test_post_one_order_base_data2(test_client):
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 0.23,
                "region": 12,
                "delivery_hours": ["09:00-11:00", "12:00-18:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 201

    data = ast.literal_eval(response.data.decode("UTF-8"))
    success_orders = data.get('orders')
    assert success_orders is not None
    assert len(success_orders) == 1
    assert success_orders[0]['id'] == 1

    order = Order.objects.get(1)
    assert order.weight== 0.23
    assert order.region == 12
    assert order.get_delivery_hours() == ["09:00-11:00", "12:00-18:00"]


def test_post_one_order_base_data3(test_client):
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 12,
                "region": 12,
                "delivery_hours": ["09:00-11:00", "12:00-18:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 201

    data = ast.literal_eval(response.data.decode("UTF-8"))
    success_orders = data.get('orders')
    assert success_orders is not None
    assert len(success_orders) == 1
    assert success_orders[0]['id'] == 1

    order = Order.objects.get(1)
    assert order.weight== 12
    assert order.region == 12
    assert order.get_delivery_hours() == ["09:00-11:00", "12:00-18:00"]


def test_post_one_order_base_data4(test_client):
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

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 201

    data = ast.literal_eval(response.data.decode("UTF-8"))
    success_orders = data.get('orders')
    assert success_orders is not None
    assert len(success_orders) == 1
    assert success_orders[0]['id'] == 1

    order1 = Order.objects.get(1)
    order2 = Order.objects.get(1)
    assert order1 == order2


def test_post_multiple_couriers(test_client):
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 12,
                "region": 12,
                "delivery_hours": ["09:00-11:00", "12:00-18:00"]
            },
            {
                "order_id": 2,
                "weight": 0.1,
                "region": 1,
                "delivery_hours": ["17:00-18:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 201

    data = ast.literal_eval(response.data.decode("UTF-8"))
    success_orders = data.get('orders')
    assert success_orders is not None
    assert len(success_orders) == 2
    assert success_orders[0]['id'] == 1
    assert success_orders[1]['id'] == 2

    order = Order.objects.get(1)
    assert order.weight== 12
    assert order.region == 12
    assert order.get_delivery_hours() == ["09:00-11:00", "12:00-18:00"]

    order = Order.objects.get(2)
    assert order.weight== 0.1
    assert order.region == 1
    assert order.get_delivery_hours() == ["17:00-18:00"]
