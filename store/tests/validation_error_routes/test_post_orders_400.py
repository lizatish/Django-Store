import ast
import json

HEADERS = {"Content-Type": "application/json"}
ROUTE = '/orders'


def test_post_one_order_without_order_id(test_client):
    data = {
        "data": [
            {
                "weight": 0.23,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 1
    assert orders[0]['id'] == 1


def test_post_one_order_without_weight(test_client):
    data = {
        "data": [
            {
                "order_id": 1,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 1
    assert orders[0]['id'] == 1


def test_post_one_order_without_region(test_client):
    data = {
        'data': [
            {
                "order_id": 1,
                "weight": 0.23,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 1
    assert orders[0]['id'] == 1


def test_post_one_order_without_delivery_hours(test_client):
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 0.23,
                "region": 12,
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 1
    assert orders[0]['id'] == 1


def test_post_one_order_with_another_field(test_client):
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 0.23,
                "region": 12,
                "delivery_hours": ["09:00-18:00"],
                'another_field': 1
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 1
    assert orders[0]['id'] == 1


def test_post_one_order_without_list_data(test_client):
    data = {
        "order_id": 1,
        "weight": 0.23,
        "region": 12,
        "delivery_hours": ["09:00-18:00"]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 0


def test_post_one_order_with_empty_data(test_client):
    data = {
        "data": [

        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 0


def test_post_one_order_with_empty_data2(test_client):
    data = {
        "data": [
            {

            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 1
    assert len(orders) == 1


def test_post_one_order_with_float_order_id(test_client):
    data = {
        "data": [
            {
                "order_id": 1.1,
                "weight": 0.23,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 1
    assert orders[0]['id'] == 1.1


def test_post_one_order_with_negative_order_id(test_client):
    data = {
        "data": [
            {
                "order_id": -1,
                "weight": 0.23,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 1
    assert orders[0]['id'] == -1


def test_post_one_order_with_str_order_id(test_client):
    data = {
        "data": [
            {
                "order_id": '12',
                "weight": 0.23,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 1
    assert orders[0]['id'] == '12'


def test_post_one_order_with_list_order_id(test_client):
    data = {
        "data": [
            {
                "order_id": [1],
                "weight": 0.23,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 1
    assert orders[0]['id'] == [1]


def test_post_one_order_with_another_str_weight(test_client):
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": '0.23',
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 1
    assert orders[0]['id'] == 1


def test_post_one_order_with_negative_weight(test_client):
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": -0.23,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 1
    assert orders[0]['id'] == 1


def test_post_one_order_with_min_weight(test_client):
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 0.009,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 1
    assert orders[0]['id'] == 1


def test_post_one_order_with_max_weight(test_client):
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 50.1,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 1
    assert orders[0]['id'] == 1


def test_post_one_order_with_negatove_region(test_client):
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 21.1,
                "region": -12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 1
    assert orders[0]['id'] == 1


def test_post_one_order_with_list_region(test_client):
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 21.1,
                "region": [],
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 1
    assert orders[0]['id'] == 1


def test_post_one_order_with_float_region(test_client):
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 21.1,
                "region": 12.2,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 1
    assert orders[0]['id'] == 1


def test_post_one_order_with_str_region(test_client):
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 21.1,
                "region": '12',
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 1
    assert orders[0]['id'] == 1


def test_post_one_order_with_empty_delivery_hours(test_client):
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 21.1,
                "region": 12,
                "delivery_hours": []
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 1
    assert orders[0]['id'] == 1


def test_post_one_order_with_another_type_delivery_hours(test_client):
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 21.1,
                "region": 12,
                "delivery_hours": ["019:00-18:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 1
    assert orders[0]['id'] == 1


def test_post_one_order_with_another_type_delivery_hours2(test_client):
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 21.1,
                "region": 12,
                "delivery_hours": ["24:00-18:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 1
    assert orders[0]['id'] == 1


def test_post_one_order_with_empty_delivery_hours3(test_client):
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 21.1,
                "region": 12,
                "delivery_hours": ['']
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 1
    assert orders[0]['id'] == 1


def test_post_one_order_with_another_type_delivery_hours3(test_client):
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 21.1,
                "region": 12,
                "delivery_hours": ["09:61-18:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 1
    assert orders[0]['id'] == 1


def test_post_one_order_with_addition_to_data(test_client):
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 21.1,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ],
        "another": 123
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 0


def test_post_one_order_two_times(test_client):
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 21.1,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 201

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 1
    assert orders[0]['id'] == 1


def test_post_multiple_orders_with_same_id(test_client):
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 21.1,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            },
            {
                "order_id": 1,
                "weight": 21.1,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 1
    assert orders[0]['id'] == 1


def test_post_multiple_orders_with_errors_in_first(test_client):
    data = {
        "data": [
            {
                "order_id": 1,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            },
            {
                "order_id": 2,
                "weight": 21.1,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 1
    assert orders[0]['id'] == 1


def test_post_multiple_orders_with_errors_in_second(test_client):
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 21.1,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            },
            {
                "order_id": 2,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 1
    assert orders[0]['id'] == 2


def test_post_multiple_orders_with_errors_in_first_and_second(test_client):
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 21.1,
                "region": 12,
            },
            {
                "order_id": 2,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 2
    assert orders[0]['id'] == 1
    assert orders[1]['id'] == 2


def test_post_multiple_orders_with_errors_after_success(test_client):
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 21.1,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            },
            {
                "order_id": 2,
                "weight": 21.1,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 201
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 2
    assert orders[0]['id'] == 1
    assert orders[1]['id'] == 2


def test_post_multiple_orders_with_errors_after_success2(test_client):
    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 21.1,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            },
            {
                "order_id": 2,
                "weight": 21.1,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 201

    data = {
        "data": [
            {
                "order_id": 1,
                "weight": 21.1,
                "region": 12,
                "delivery_hours": ["09:00-18:00"]
            }
        ]
    }
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    orders = validation_data.get('orders')
    assert len(orders) == 1
    assert orders[0]['id'] == 1
