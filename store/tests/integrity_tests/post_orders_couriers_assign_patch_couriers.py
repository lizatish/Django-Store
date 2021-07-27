import ast

from store.models.courier import Courier
from store.models.order import Order

HEADERS = {"Content-Type": "application/json"}


def test_patch_courier_with_assign_orders_bike_to_foot(test_client):
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
                "weight": 8,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            },
            {
                "order_id": 2,
                "weight": 6,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            },
            {
                "order_id": 3,
                "weight": 1,
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
        "courier_type": "foot"
    }
    response = test_client.patch('couriers/1', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.max_weight == 10
    assert courier.current_weight == 9
    assert len(courier.orders) == 2

    order1 = Order.objects.get(1)
    assert order1.courier_id == 1

    order2 = Order.objects.get(2)
    assert order2.courier_id == None
    assert order2.assign_time == None

    order3 = Order.objects.get(3)
    assert order3.courier_id == 1


def test_patch_courier_with_assign_orders_bike_to_car(test_client):
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
                "weight": 8,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            },
            {
                "order_id": 2,
                "weight": 6,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            },
            {
                "order_id": 3,
                "weight": 1,
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
        "courier_type": "car"
    }
    response = test_client.patch('couriers/1', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.max_weight == 50
    assert courier.current_weight == 15
    assert len(courier.orders) == 3

    order1 = Order.objects.get(1)
    assert order1.courier_id == 1

    order2 = Order.objects.get(2)
    assert order2.courier_id == 1

    order3 = Order.objects.get(3)
    assert order3.courier_id == 1


def test_patch_courier_with_assign_orders_car_to_bike(test_client):
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
                "weight": 18,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            },
            {
                "order_id": 2,
                "weight": 16,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            },
            {
                "order_id": 3,
                "weight": 11,
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
    assert courier.current_weight == 11
    assert len(courier.orders) == 1

    order1 = Order.objects.get(1)
    assert order1.courier_id == None
    assert order1.assign_time == None

    order2 = Order.objects.get(2)
    assert order2.courier_id == None
    assert order2.assign_time == None

    order3 = Order.objects.get(3)
    assert order3.courier_id == 1


def test_patch_courier_with_assign_orders_car_to_bike2(test_client):
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
                "weight": 10,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            },
            {
                "order_id": 2,
                "weight": 1,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            },
            {
                "order_id": 3,
                "weight": 11,
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
    assert courier.current_weight == 12
    assert len(courier.orders) == 2


def test_patch_courier_with_assign_orders_car_to_foot(test_client):
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
                "weight": 18,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            },
            {
                "order_id": 2,
                "weight": 16,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            },
            {
                "order_id": 3,
                "weight": 1,
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
        "courier_type": "foot"
    }
    response = test_client.patch('couriers/1', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.max_weight == 10
    assert courier.current_weight == 1
    assert len(courier.orders) == 1

    order1 = Order.objects.get(1)
    assert order1.courier_id == None
    assert order1.assign_time == None

    order2 = Order.objects.get(2)
    assert order2.courier_id == None
    assert order2.assign_time == None

    order3 = Order.objects.get(3)
    assert order3.courier_id == 1


def test_patch_courier_with_assign_orders_car_to_foot2(test_client):
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
                "weight": 12,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            },
            {
                "order_id": 2,
                "weight": 9,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            },
            {
                "order_id": 3,
                "weight": 1,
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
        "courier_type": "foot"
    }
    response = test_client.patch('couriers/1', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.max_weight == 10
    assert courier.current_weight == 10
    assert len(courier.orders) == 2


def test_patch_courier_with_assign_orders_foot_to_bike(test_client):
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


def test_patch_courier_with_assign_orders_foot_to_car(test_client):
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
        "courier_type": "car"
    }
    response = test_client.patch('couriers/1', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.max_weight == 50
    assert courier.current_weight == 9.2
    assert len(courier.orders) == 3


def test_patch_courier_with_assign_orders_foot_to_foot(test_client):
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
        "courier_type": "foot"
    }
    response = test_client.patch('couriers/1', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.max_weight == 10
    assert courier.current_weight == 9.2
    assert len(courier.orders) == 3


def test_patch_courier_with_assign_orders_car_to_car(test_client):
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
        "courier_type": "car"
    }
    response = test_client.patch('couriers/1', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.max_weight == 50
    assert courier.current_weight == 9.2
    assert len(courier.orders) == 3


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


def test_patch_courier_with_assign_orders_change_region(test_client):
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
                "region": 1,
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
                "region": 1,
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
        "regions": [1]
    }
    response = test_client.patch('couriers/1', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.current_weight == 9.1
    assert len(courier.orders) == 2


def test_patch_courier_with_assign_orders_change_region2(test_client):
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
                "region": 1,
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
                "region": 1,
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
        "regions": [12]
    }
    response = test_client.patch('couriers/1', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert round(courier.current_weight, 1) == 0.1
    assert len(courier.orders) == 1


def test_patch_courier_with_assign_orders_change_region3(test_client):
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
                "region": 1,
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
                "region": 1,
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
        "regions": [5]
    }
    response = test_client.patch('couriers/1', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.current_weight == 0
    assert len(courier.orders) == 0


def test_patch_courier_with_assign_orders_change_working_hours(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "bike",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:05", "12:00-18:00"]
            }
        ]
    }
    _ = test_client.post('couriers', headers=HEADERS, data=json.dumps(data))
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 9,
                "region": 1,
                "delivery_hours": ["17:00-18:00"]
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
                "region": 1,
                "delivery_hours": ["17:00-18:00"]
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
        "working_hours": ["09:00-11:00"]
    }
    response = test_client.patch('couriers/1', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert round(courier.current_weight, 1) == 0.1
    assert len(courier.orders) == 1


def test_patch_courier_with_assign_orders_change_working_hours2(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "bike",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:05", "12:00-18:00"]
            }
        ]
    }
    _ = test_client.post('couriers', headers=HEADERS, data=json.dumps(data))
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 9,
                "region": 1,
                "delivery_hours": ["17:00-18:00"]
            },
            {
                "order_id": 2,
                "weight": 0.1,
                "region": 12,
                "delivery_hours": ["09:00-12:00"]
            },
            {
                "order_id": 3,
                "weight": 0.1,
                "region": 1,
                "delivery_hours": ["17:00-18:00"]
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
        "working_hours": ["17:00-17:30"]
    }
    response = test_client.patch('couriers/1', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.current_weight == 9.1
    assert len(courier.orders) == 2


def test_patch_courier_with_assign_orders_change_working_hours3(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "bike",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:05", "12:00-18:00"]
            }
        ]
    }
    _ = test_client.post('couriers', headers=HEADERS, data=json.dumps(data))
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 9,
                "region": 1,
                "delivery_hours": ["17:00-18:00"]
            },
            {
                "order_id": 2,
                "weight": 0.1,
                "region": 12,
                "delivery_hours": ["09:00-12:00"]
            },
            {
                "order_id": 3,
                "weight": 0.1,
                "region": 1,
                "delivery_hours": ["17:00-18:00"]
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
        "working_hours": ["7:00-8:30"]
    }
    response = test_client.patch('couriers/1', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.current_weight == 0
    assert len(courier.orders) == 0


def test_patch_courier_with_assign_orders_change_region_and_working_hours(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "bike",
                "regions": [1, 12, 4],
                "working_hours": ["11:35-14:05", "12:00-18:00"]
            }
        ]
    }
    _ = test_client.post('couriers', headers=HEADERS, data=json.dumps(data))
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 9,
                "region": 1,
                "delivery_hours": ["17:00-18:00"]
            },
            {
                "order_id": 2,
                "weight": 0.1,
                "region": 12,
                "delivery_hours": ["09:00-12:00"]
            },
            {
                "order_id": 3,
                "weight": 0.1,
                "region": 4,
                "delivery_hours": ["17:00-18:00"]
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
        "working_hours": ["17:00-17:30"],
        "regions": [4],

    }
    response = test_client.patch('couriers/1', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert round(courier.current_weight, 2) == 0.1
    assert len(courier.orders) == 1


def test_patch_courier_with_assign_orders_change_region_and_working_hours2(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "bike",
                "regions": [1, 12, 4],
                "working_hours": ["11:35-14:05", "12:00-18:00"]
            }
        ]
    }
    _ = test_client.post('couriers', headers=HEADERS, data=json.dumps(data))
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 9,
                "region": 1,
                "delivery_hours": ["17:00-18:00"]
            },
            {
                "order_id": 2,
                "weight": 0.1,
                "region": 1,
                "delivery_hours": ["09:00-12:00"]
            },
            {
                "order_id": 3,
                "weight": 0.1,
                "region": 4,
                "delivery_hours": ["17:00-18:00"]
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
        "working_hours": ["17:00-17:30"],
        "regions": [1],

    }
    response = test_client.patch('couriers/1', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.current_weight == 9
    assert len(courier.orders) == 1


def test_patch_courier_with_assign_orders_change_region_and_working_hours3(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "bike",
                "regions": [1, 12, 4],
                "working_hours": ["11:35-14:05", "12:00-18:00"]
            }
        ]
    }
    _ = test_client.post('couriers', headers=HEADERS, data=json.dumps(data))
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 9,
                "region": 1,
                "delivery_hours": ["17:00-18:00"]
            },
            {
                "order_id": 2,
                "weight": 0.1,
                "region": 12,
                "delivery_hours": ["09:00-12:00"]
            },
            {
                "order_id": 3,
                "weight": 0.1,
                "region": 4,
                "delivery_hours": ["17:00-18:00"]
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
        "working_hours": ["17:00-17:30"],
        "regions": [22],

    }
    response = test_client.patch('couriers/1', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.current_weight == 0
    assert len(courier.orders) == 0


def test_patch_courier_with_assign_orders_change_courier_type_and_working_hours(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "bike",
                "regions": [1, 12, 4],
                "working_hours": ["11:35-14:05", "12:00-18:00"]
            }
        ]
    }
    _ = test_client.post('couriers', headers=HEADERS, data=json.dumps(data))
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 10,
                "region": 1,
                "delivery_hours": ["17:00-18:00"]
            },
            {
                "order_id": 2,
                "weight": 0.1,
                "region": 12,
                "delivery_hours": ["09:00-12:00"]
            },
            {
                "order_id": 3,
                "weight": 0.1,
                "region": 4,
                "delivery_hours": ["17:00-18:00"]
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
        "working_hours": ["17:00-17:30"],
        "courier_type": "foot"
    }
    response = test_client.patch('couriers/1', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.current_weight == 10
    assert len(courier.orders) == 1


def test_patch_courier_with_assign_orders_change_courier_type_and_working_hours2(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "bike",
                "regions": [1, 12, 4],
                "working_hours": ["11:35-14:05", "12:00-18:00"]
            }
        ]
    }
    _ = test_client.post('couriers', headers=HEADERS, data=json.dumps(data))
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 8,
                "region": 1,
                "delivery_hours": ["17:00-18:00"]
            },
            {
                "order_id": 2,
                "weight": 2,
                "region": 12,
                "delivery_hours": ["09:00-12:00"]
            },
            {
                "order_id": 3,
                "weight": 0.1,
                "region": 4,
                "delivery_hours": ["17:00-18:00"]
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
        "working_hours": ["17:00-17:30"],
        "courier_type": "foot"
    }
    response = test_client.patch('couriers/1', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.current_weight == 8.1
    assert len(courier.orders) == 2


def test_patch_courier_with_assign_orders_change_rigion_and_courier_type(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "bike",
                "regions": [1, 12, 4],
                "working_hours": ["11:35-14:05", "12:00-18:00"]
            }
        ]
    }
    _ = test_client.post('couriers', headers=HEADERS, data=json.dumps(data))
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 8,
                "region": 1,
                "delivery_hours": ["17:00-18:00"]
            },
            {
                "order_id": 2,
                "weight": 2,
                "region": 12,
                "delivery_hours": ["09:00-12:00"]
            },
            {
                "order_id": 3,
                "weight": 0.1,
                "region": 4,
                "delivery_hours": ["17:00-18:00"]
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
        "regions": [1],
        "courier_type": "foot"
    }
    response = test_client.patch('couriers/1', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.current_weight == 8
    assert len(courier.orders) == 1


def test_patch_courier_with_assign_orders_change_rigion_and_courier_type2(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "car",
                "regions": [1, 12, 4],
                "working_hours": ["11:35-14:05", "12:00-18:00"]
            }
        ]
    }
    _ = test_client.post('couriers', headers=HEADERS, data=json.dumps(data))
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 28,
                "region": 1,
                "delivery_hours": ["17:00-18:00"]
            },
            {
                "order_id": 2,
                "weight": 12,
                "region": 12,
                "delivery_hours": ["09:00-12:00"]
            },
            {
                "order_id": 3,
                "weight": 0.1,
                "region": 4,
                "delivery_hours": ["17:00-18:00"]
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
        "regions": [12, 1],
        "courier_type": "bike"
    }
    response = test_client.patch('couriers/1', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.current_weight == 12
    assert len(courier.orders) == 1


def test_patch_courier_with_assign_orders_change_rigion_and_courier_type3(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "car",
                "regions": [1, 12, 4],
                "working_hours": ["11:35-14:05", "12:00-18:00"]
            }
        ]
    }
    _ = test_client.post('couriers', headers=HEADERS, data=json.dumps(data))
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 18,
                "region": 1,
                "delivery_hours": ["17:00-18:00"]
            },
            {
                "order_id": 2,
                "weight": 12,
                "region": 12,
                "delivery_hours": ["09:00-12:00"]
            },
            {
                "order_id": 3,
                "weight": 10,
                "region": 4,
                "delivery_hours": ["17:00-18:00", "9:00-11:00"]
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
        "regions": [12, 4],
        "courier_type": "foot"
    }
    response = test_client.patch('couriers/1', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.current_weight == 10
    assert len(courier.orders) == 1


def test_patch_courier_with_assign_orders_change_courier_type_region_and_working_hours(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "car",
                "regions": [1, 12, 4],
                "working_hours": ["11:35-14:05", "12:00-18:00"]
            }
        ]
    }
    _ = test_client.post('couriers', headers=HEADERS, data=json.dumps(data))
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 18,
                "region": 1,
                "delivery_hours": ["17:00-18:00"]
            },
            {
                "order_id": 2,
                "weight": 12,
                "region": 12,
                "delivery_hours": ["09:00-12:00"]
            },
            {
                "order_id": 3,
                "weight": 10,
                "region": 4,
                "delivery_hours": ["17:00-18:00", "9:00-11:00"]
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
        "regions": [12, 4],
        "courier_type": "foot",
        "working_hours": ["11:35-14:05"]
    }
    response = test_client.patch('couriers/1', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.current_weight == 0
    assert len(courier.orders) == 0


def test_patch_courier_with_assign_orders_change_courier_type_region_and_working_hours2(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "car",
                "regions": [1, 12, 4],
                "working_hours": ["11:35-14:05", "12:00-18:00"]
            }
        ]
    }
    _ = test_client.post('couriers', headers=HEADERS, data=json.dumps(data))
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 11,
                "region": 1,
                "delivery_hours": ["17:00-18:00"]
            },
            {
                "order_id": 2,
                "weight": 2,
                "region": 12,
                "delivery_hours": ["09:00-12:00"]
            },
            {
                "order_id": 3,
                "weight": 1,
                "region": 4,
                "delivery_hours": ["17:00-18:00", "9:00-11:00"]
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
        "regions": [12, 4],
        "courier_type": "foot",
        "working_hours": ["9:35-11:05"]
    }
    response = test_client.patch('couriers/1', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.current_weight == 3
    assert len(courier.orders) == 2

def test_patch_courier_with_assign_orders_change_courier_type_region_and_working_hours3(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "bike",
                "regions": [1, 12, 4],
                "working_hours": ["11:35-14:05", "12:00-18:00"]
            }
        ]
    }
    _ = test_client.post('couriers', headers=HEADERS, data=json.dumps(data))
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 11,
                "region": 1,
                "delivery_hours": ["17:00-18:00"]
            },
            {
                "order_id": 2,
                "weight": 2,
                "region": 12,
                "delivery_hours": ["09:00-12:00"]
            },
            {
                "order_id": 3,
                "weight": 1,
                "region": 4,
                "delivery_hours": ["17:00-18:00", "9:00-11:00"]
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
        "regions": [12, 4],
        "courier_type": "car",
        "working_hours": ["11:35-16:05"]
    }
    response = test_client.patch('couriers/1', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.current_weight == 2
    assert len(courier.orders) == 1
