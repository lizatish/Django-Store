import ast
import json

HEADERS = {"Content-Type": "application/json"}
ROUTE = 'orders/complete'


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

    data = {
        "courier_id": 1,
    }
    _ = test_client.post('orders/assign', headers=HEADERS, data=json.dumps(data))


def test_complete_not_valid_courier_id(test_client):
    init_data(test_client)

    data = {
        "courier_id": 2,
        "order_id": 1,
        "complete_time": "2021-01-10T10:33:01.42Z"
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_complete_not_valid_order_id(test_client):
    init_data(test_client)

    data = {
        "courier_id": 1,
        "order_id": 2,
        "complete_time": "2021-01-10T10:33:01.42Z"
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_complete_without_order_id(test_client):
    init_data(test_client)

    data = {
        "courier_id": 1,
        "complete_time": "2021-01-10T10:33:01.42Z"
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_complete_without_courier_id(test_client):
    init_data(test_client)

    data = {
        "order_id": 2,
        "complete_time": "2021-01-10T10:33:01.42Z"
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_complete_without_complete_time(test_client):
    init_data(test_client)

    data = {
        "courier_id": 1,
        "order_id": 1,
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_complete_with_addition_param(test_client):
    init_data(test_client)

    data = {
        "courier_id": 1,
        "order_id": 1,
        "complete_time": "2021-01-10T10:33:01.42Z",
        "12": "2021-01-10T10:33:01.42Z"

    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_complete_with_empty_complete_time(test_client):
    init_data(test_client)

    data = {
        "courier_id": 1,
        "order_id": 1,
        "complete_time": "",
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_complete_with_error_in_complete_time(test_client):
    init_data(test_client)

    data = {
        "courier_id": 1,
        "order_id": 1,
        "complete_time": "20211-01-10T10:33:01.42Z",
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_complete_with_error_in_complete_time2(test_client):
    init_data(test_client)

    data = {
        "courier_id": 1,
        "order_id": 1,
        "complete_time": "2021-13-10T10:33:01.42Z",
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_complete_with_error_in_complete_time3(test_client):
    init_data(test_client)

    data = {
        "courier_id": 1,
        "order_id": 1,
        "complete_time": "2021-01-10T24:33:01.42Z"
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_complete_with_error_in_complete_time5(test_client):
    init_data(test_client)

    data = {
        "courier_id": 1,
        "order_id": 1,
        "complete_time": "2021-01-10T10:65:01.42Z"
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_complete_with_error_in_complete_time6(test_client):
    init_data(test_client)

    data = {
        "courier_id": 1,
        "order_id": 1,
        "complete_time": "2021-01-10T10:05:65.42Z"
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_complete_with_str_courier_id(test_client):
    init_data(test_client)

    data = {
        "courier_id": '1',
        "order_id": 1,
        "complete_time": "2021-01-10T10:05:15.42Z"
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_complete_with_double_courier_id(test_client):
    init_data(test_client)

    data = {
        "courier_id": 1.1,
        "order_id": 1,
        "complete_time": "2021-01-10T10:05:15.42Z"
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_complete_with_negative_courier_id(test_client):
    init_data(test_client)

    data = {
        "courier_id": -1,
        "order_id": 1,
        "complete_time": "2021-01-10T10:05:15.42Z"
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_complete_with_double_order_id(test_client):
    init_data(test_client)

    data = {
        "courier_id": 1,
        "order_id": 1.1,
        "complete_time": "2021-01-10T10:05:15.42Z"
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_complete_with_str_order_id(test_client):
    init_data(test_client)

    data = {
        "courier_id": 1,
        "order_id": '1',
        "complete_time": "2021-01-10T10:05:15.42Z"
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_complete_with_negative_order_id(test_client):
    init_data(test_client)

    data = {
        "courier_id": 1,
        "order_id": -1,
        "complete_time": "2021-01-10T10:05:15.42Z"
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data
