import ast
import json

HEADERS = {"Content-Type": "application/json"}


def get_route(id):
    return f'/couriers/{id}'


def init_data(client):
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
    _ = client.post('couriers', headers=HEADERS, data=json.dumps(data))


def test_patch_one_courier_with_int_courier_type(test_client):
    init_data(test_client)

    data = {
        "courier_type": 1,
    }

    response = test_client.patch(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_patch_one_courier_with_error_in_str_courier_type(test_client):
    init_data(test_client)

    data = {
        "courier_type": 'fooot',
    }

    response = test_client.patch(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_patch_one_courier_with_empty_courier_type(test_client):
    init_data(test_client)

    data = {
        "courier_type": '',
    }

    response = test_client.patch(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_patch_one_courier_with_empty_regions(test_client):
    init_data(test_client)

    data = {
        "regions": []
    }

    response = test_client.patch(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_patch_one_courier_with_int_regions(test_client):
    init_data(test_client)

    data = {
        "regions": 1
    }

    response = test_client.patch(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_patch_one_courier_with_negative_regions(test_client):
    init_data(test_client)

    data = {
        "regions": [-1]
    }

    response = test_client.patch(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_patch_one_courier_with_double_regions(test_client):
    init_data(test_client)

    data = {
        "regions": [12.2]
    }

    response = test_client.patch(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_patch_one_courier_with_empty_working_hours(test_client):
    init_data(test_client)

    data = {
        "working_hours": [""]
    }

    response = test_client.patch(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_patch_one_courier_with_empty_working_hours2(test_client):
    init_data(test_client)

    data = {
        "working_hours": []
    }

    response = test_client.patch(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_patch_one_courier_with_error_in_working_hours(test_client):
    init_data(test_client)

    data = {
        "working_hours": ["11:35-121:05"]
    }

    response = test_client.patch(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_patch_one_courier_with_error_in_working_hours2(test_client):
    init_data(test_client)

    data = {
        "working_hours": ["11:35-25:05"]
    }

    response = test_client.patch(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_patch_one_courier_with_error_in_working_hours3(test_client):
    init_data(test_client)

    data = {
        "working_hours": ["11:35-12:65"]
    }

    response = test_client.patch(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_patch_one_courier_with_another_field(test_client):
    init_data(test_client)

    data = {
        "courier_id": 1,
        "working_hours": ["11:35-12:05"]
    }

    response = test_client.patch(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data


def test_patch_one_courier_with_many_fields(test_client):
    init_data(test_client)

    data = {
        "courier_id": 1,
        "working_hours": ["11:35-12:05"],
        "regions": [-1]
    }

    response = test_client.patch(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 400
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert not data
