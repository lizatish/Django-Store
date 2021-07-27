import ast
import json

HEADERS = {"Content-Type": "application/json"}
ROUTE = '/couriers'


def test_post_one_courier_without_courier_id(test_client):
    data = {
        "data": [
            {
                "courier_type": "foot",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:05", "09:00-11:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 1
    assert couriers[0]['id'] == 1


def test_post_one_courier_without_courier_type(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:05", "09:00-11:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 1
    assert couriers[0]['id'] == 1


def test_post_one_courier_without_regions(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "foot",
                "working_hours": ["11:35-14:05", "09:00-11:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 1
    assert couriers[0]['id'] == 1


def test_post_one_courier_without_working_hours(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "foot",
                "regions": [1, 12, 22],
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 1
    assert couriers[0]['id'] == 1


def test_post_one_courier_with_another_field(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "foot",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:05", "09:00-11:00"],
                'another_field': 1
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 1
    assert couriers[0]['id'] == 1


def test_post_one_courier_without_list_data(test_client):
    data = {

        "courier_id": 1,
        "courier_type": "foot",
        "regions": [1, 12, 22],
        "working_hours": ["11:35-14:05", "09:00-11:00"]

    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 0


def test_post_one_courier_with_empty_data(test_client):
    data = {
        "data": [

        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 0


def test_post_one_courier_with_empty_data2(test_client):
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
    couriers = validation_data.get('couriers')
    assert len(couriers) == 1
    assert len(couriers) == 1


def test_post_one_courier_with_float_courier_id(test_client):
    data = {
        "data": [
            {
                "courier_id": 1.1,
                "courier_type": "foot",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:05", "09:00-11:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 1
    assert couriers[0]['id'] == 1.1


def test_post_one_courier_with_negative_courier_id(test_client):
    data = {
        "data": [
            {
                "courier_id": -1,
                "courier_type": "foot",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:05", "09:00-11:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 1
    assert couriers[0]['id'] == -1


def test_post_one_courier_with_str_courier_id(test_client):
    data = {
        "data": [
            {
                "courier_id": '12',
                "courier_type": "foot",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:05", "09:00-11:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 1
    assert couriers[0]['id'] == '12'


def test_post_one_courier_with_list_courier_id(test_client):
    data = {
        "data": [
            {
                "courier_id": [1],
                "courier_type": "foot",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:05", "09:00-11:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 1
    assert couriers[0]['id'] == [1]


def test_post_one_courier_with_another_str_courier_type(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "1foot",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:05", "09:00-11:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 1
    assert couriers[0]['id'] == 1


def test_post_one_courier_with_int_courier_type(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": 1,
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:05", "09:00-11:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 1
    assert couriers[0]['id'] == 1


def test_post_one_courier_with_empty_courier_type(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": '',
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:05", "09:00-11:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 1
    assert couriers[0]['id'] == 1


def test_post_one_courier_with_list_courier_type(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": [1],
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:05", "09:00-11:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 1
    assert couriers[0]['id'] == 1


def test_post_one_courier_with_empty_regions(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "foot",
                "regions": [],
                "working_hours": ["11:35-14:05", "09:00-11:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 1
    assert couriers[0]['id'] == 1


def test_post_one_courier_with_negative_regions(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "foot",
                "regions": [1, -12, 22],
                "working_hours": ["11:35-14:05", "09:00-11:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 1
    assert couriers[0]['id'] == 1


def test_post_one_courier_with_str_regions(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "foot",
                "regions": [1, 12, '22'],
                "working_hours": ["11:35-14:05", "09:00-11:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 1
    assert couriers[0]['id'] == 1


def test_post_one_courier_with_double_regions(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "foot",
                "regions": [1, 12.2, 22],
                "working_hours": ["11:35-14:05", "09:00-11:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 1
    assert couriers[0]['id'] == 1


def test_post_one_courier_with_empty_working_hours(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "foot",
                "regions": [1, 12, 22],
                "working_hours": []
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 1
    assert couriers[0]['id'] == 1


def test_post_one_courier_with_empty_working_hours2(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "foot",
                "regions": [1, 12, 22],
                "working_hours": ['']
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 1
    assert couriers[0]['id'] == 1


def test_post_one_courier_with_another_type_working_hours(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "foot",
                "regions": [1, 12, 22],
                "working_hours": ["111:35-14:05", "09:00-11:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 1
    assert couriers[0]['id'] == 1


def test_post_one_courier_with_another_type_working_hours2(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "foot",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-24:05", "09:00-11:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 1
    assert couriers[0]['id'] == 1


def test_post_one_courier_with_another_type_working_hours3(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "foot",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:60", "09:00-11:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 1
    assert couriers[0]['id'] == 1


def test_post_one_courier_with_addition_to_data(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "foot",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:05", "17:35-18:05"]
            }
        ],
        "another": 123
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 0


def test_post_one_courier_two_times(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "foot",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:05", "17:35-18:05"]
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
    couriers = validation_data.get('couriers')
    assert len(couriers) == 1
    assert couriers[0]['id'] == 1


def test_post_multiple_couriers_with_same_id(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "foot",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:40", "09:00-11:00"]
            },
            {
                "courier_id": 1,
                "courier_type": "foot",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:40", "09:00-11:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 1
    assert couriers[0]['id'] == 1


def test_post_multiple_couriers_with_errors_in_first(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "foot",
                "working_hours": ["11:35-14:40", "09:00-11:00"]
            },
            {
                "courier_id": 2,
                "courier_type": "foot",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:40", "09:00-11:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 1
    assert couriers[0]['id'] == 1


def test_post_multiple_couriers_with_errors_in_second(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "foot",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:40", "09:00-11:00"]
            },
            {
                "courier_id": 2,
                "courier_type": "foot",
                "working_hours": ["11:35-14:40", "09:00-11:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 1
    assert couriers[0]['id'] == 2


def test_post_multiple_couriers_with_errors_in_first_and_second(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "foot",
                "working_hours": ["11:35-14:40", "09:00-11:00"]
            },
            {
                "courier_id": 2,
                "courier_type": "foot",
                "working_hours": ["11:35-14:40", "09:00-11:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 2
    assert couriers[0]['id'] == 1
    assert couriers[1]['id'] == 2


def test_post_multiple_couriers_with_errors_after_success(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "foot",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:40", "09:00-11:00"]
            },
            {
                "courier_id": 2,
                "courier_type": "foot",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:40", "09:00-11:00"]
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
    couriers = validation_data.get('couriers')
    assert len(couriers) == 2
    assert couriers[0]['id'] == 1
    assert couriers[1]['id'] == 2


def test_post_multiple_couriers_with_errors_after_success2(test_client):
    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "foot",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:40", "09:00-11:00"]
            },
            {
                "courier_id": 2,
                "courier_type": "foot",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:40", "09:00-11:00"]
            }
        ]
    }

    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 201

    data = {
        "data": [
            {
                "courier_id": 1,
                "courier_type": "foot",
                "regions": [1, 12, 22],
                "working_hours": ["11:35-14:40", "09:00-11:00"]
            }
        ]
    }
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400

    data = ast.literal_eval(response.data.decode("UTF-8"))
    validation_data = data.get('validation_error')
    assert validation_data
    couriers = validation_data.get('couriers')
    assert len(couriers) == 1
    assert couriers[0]['id'] == 1
