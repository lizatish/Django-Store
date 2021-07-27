import ast
import json

HEADERS = {"Content-Type": "application/json"}
ROUTE = 'orders/assign'


def init_data(test_client):
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


def test_assign_courier_not_found(test_client):
    init_data(test_client)

    data = {
        "courier_id": 3
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_assign_courier_id_str(test_client):
    init_data(test_client)

    data = {
        "courier_id": '1'
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_assign_courier_id_float(test_client):
    init_data(test_client)

    data = {
        "courier_id": 1.1,
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data

def test_assign_addition_data(test_client):
    init_data(test_client)

    data = {
        "courier_id": 1.1,
        "123": 1.1,

    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data
