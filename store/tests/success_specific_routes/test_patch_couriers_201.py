import json

from store.models.courier import Courier
from store.models.courier_type import CourierType
HEADERS = {"Content-Type": "application/json"}


def get_route(id):
    return f'/couriers/{id}'


def test_patch_courier_foot_to_car(test_client):
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
        "courier_type": "car"
    }
    response = test_client.patch(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.courier_type == CourierType.CAR
    assert courier.current_weight == 0
    assert courier.max_weight == 50
    assert courier.regions == [1, 12, 22]
    assert courier.get_working_hours() == ["11:35-14:05", "09:00-11:00"]


def test_patch_courier_type_foot_to_bike(test_client):
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
        "courier_type": "bike"
    }
    response = test_client.patch(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.courier_type == CourierType.BIKE
    assert courier.current_weight == 0
    assert courier.max_weight == 15
    assert courier.regions == [1, 12, 22]
    assert courier.get_working_hours() == ["11:35-14:05", "09:00-11:00"]


def test_patch_courier_type_foot_to_foot(test_client):
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
        "courier_type": "foot"
    }
    response = test_client.patch(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.courier_type == CourierType.FOOT
    assert courier.current_weight == 0
    assert courier.max_weight == 10
    assert courier.regions == [1, 12, 22]
    assert courier.get_working_hours() == ["11:35-14:05", "09:00-11:00"]


def test_patch_courier_bike_to_car(test_client):
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
        "courier_type": "car"
    }
    response = test_client.patch(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.courier_type == CourierType.CAR
    assert courier.current_weight == 0
    assert courier.max_weight == 50
    assert courier.regions == [1, 12, 22]
    assert courier.get_working_hours() == ["11:35-14:05", "09:00-11:00"]


def test_patch_courier_bike_to_foot(test_client):
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
        "courier_type": "foot"
    }
    response = test_client.patch(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.courier_type == CourierType.FOOT
    assert courier.current_weight == 0
    assert courier.max_weight == 10
    assert courier.regions == [1, 12, 22]
    assert courier.get_working_hours() == ["11:35-14:05", "09:00-11:00"]


def test_patch_courier_bike_to_bike(test_client):
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
        "courier_type": "bike"
    }
    response = test_client.patch(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.courier_type == CourierType.BIKE
    assert courier.current_weight == 0
    assert courier.max_weight == 15
    assert courier.regions == [1, 12, 22]
    assert courier.get_working_hours() == ["11:35-14:05", "09:00-11:00"]


def test_patch_courier_car_to_foot(test_client):
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
        "courier_type": "foot"
    }
    response = test_client.patch(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.courier_type == CourierType.FOOT
    assert courier.current_weight == 0
    assert courier.max_weight == 10
    assert courier.regions == [1, 12, 22]
    assert courier.get_working_hours() == ["11:35-14:05", "09:00-11:00"]


def test_patch_courier_car_to_bike(test_client):
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
        "courier_type": "bike"
    }
    response = test_client.patch(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.courier_type == CourierType.BIKE
    assert courier.current_weight == 0
    assert courier.max_weight == 15
    assert courier.regions == [1, 12, 22]
    assert courier.get_working_hours() == ["11:35-14:05", "09:00-11:00"]


def test_patch_courier_car_to_car(test_client):
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
        "courier_type": "car"
    }
    response = test_client.patch(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.courier_type == CourierType.CAR
    assert courier.current_weight == 0
    assert courier.max_weight == 50
    assert courier.regions == [1, 12, 22]
    assert courier.get_working_hours() == ["11:35-14:05", "09:00-11:00"]


def test_patch_regions_to_smaller(test_client):
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
        "regions": [4]
    }
    response = test_client.patch(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.courier_type == CourierType.FOOT
    assert courier.regions == [4]
    assert courier.get_working_hours() == ["11:35-14:05", "09:00-11:00"]


def test_patch_regions_to_higher(test_client):
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
        "regions": [1, 12, 22, 33]
    }
    response = test_client.patch(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.courier_type == CourierType.FOOT
    assert courier.regions == [1, 12, 22, 33]
    assert courier.get_working_hours() == ["11:35-14:05", "09:00-11:00"]


def test_patch_working_hours_to_multiple(test_client):
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
        "working_hours": ["08:00-13:00", "14:00-15:00"]
    }
    response = test_client.patch(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.courier_type == CourierType.FOOT
    assert courier.regions == [1, 12, 22]
    assert courier.get_working_hours() == ["08:00-13:00", "14:00-15:00"]


def test_patch_working_hours_to_one_hour(test_client):
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
        "working_hours": ["08:00-13:00"]
    }
    response = test_client.patch(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.courier_type == CourierType.FOOT
    assert courier.regions == [1, 12, 22]
    assert courier.get_working_hours() == ["08:00-13:00"]


def test_patch_many_fields(test_client):
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
        "working_hours": ["08:00-13:00"],
        "regions": [1, 12],
    }
    response = test_client.patch(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.courier_type == CourierType.FOOT
    assert courier.regions == [1, 12]
    assert courier.get_working_hours() == ["08:00-13:00"]


def test_patch_many_fields2(test_client):
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
        "working_hours": ["08:00-13:00"],
        "regions": [1, 12],
        "courier_type": "car"
    }
    response = test_client.patch(get_route(1), headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    courier = Courier.objects.get(1)
    assert courier.courier_type == CourierType.CAR
    assert courier.regions == [1, 12]
    assert courier.get_working_hours() == ["08:00-13:00"]
