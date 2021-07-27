import ast
import json

from store.tools.time_service import TimeService

HEADERS = {"Content-Type": "application/json"}
ROUTE = 'orders/complete'


def test_complete_one_valid_order_courier_type_foot(test_client):
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
                "delivery_hours": ["09:00-12:00"]
            },
            {
                "order_id": 2,
                "weight": 0.1,
                "region": 12,
                "delivery_hours": ["9:00-11:40"]
            },
            {
                "order_id": 3,
                "weight": 0.1,
                "region": 12,
                "delivery_hours": ["12:00-13:00"]
            }
        ]
    }
    _ = test_client.post('orders', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
    }
    response = test_client.post('orders/assign', headers=HEADERS, data=json.dumps(data))
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assign_time = data.get('assign_time')

    response = test_client.get('couriers/1', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert data.get('earnings') == 0
    assert data.get('rating') == None

    complete_time = TimeService().get_assign_time()
    data = {
        "courier_id": 1,
        "order_id": 1,
        "complete_time": complete_time
    }

    timedelta = (TimeService().get_datetime(complete_time) - TimeService().get_datetime(assign_time)).seconds
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))

    etalon_rating = (60 * 60 - min(timedelta, 60 * 60)) / (60 * 60) * 5

    response = test_client.get('couriers/1', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert data.get('earnings') == 500 * 5
    assert data.get('rating') == etalon_rating

def test_complete_one_valid_order_courier_type_foot2(test_client):
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
                "delivery_hours": ["09:00-12:00"]
            },
            {
                "order_id": 2,
                "weight": 0.1,
                "region": 12,
                "delivery_hours": ["9:00-11:40"]
            },
            {
                "order_id": 3,
                "weight": 0.1,
                "region": 12,
                "delivery_hours": ["12:00-13:00"]
            }
        ]
    }
    _ = test_client.post('orders', headers=HEADERS, data=json.dumps(data))

    data = {
        "courier_id": 1,
    }
    response = test_client.post('orders/assign', headers=HEADERS, data=json.dumps(data))
    data = ast.literal_eval(response.data.decode("UTF-8"))
    assign_time = data.get('assign_time')

    response = test_client.get('couriers/1', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert data.get('earnings') == 0
    assert data.get('rating') == None

    complete_time = TimeService().get_assign_time()
    data = {
        "courier_id": 1,
        "order_id": 1,
        "complete_time": complete_time
    }

    timedelta = (TimeService().get_datetime(complete_time) - TimeService().get_datetime(assign_time)).seconds
    response = test_client.post(ROUTE, headers=HEADERS, data=json.dumps(data))

    etalon_rating = (60 * 60 - min(timedelta, 60 * 60)) / (60 * 60) * 5

    response = test_client.get('couriers/1', headers=HEADERS, data=json.dumps(data))
    assert response.status_code == 200

    data = ast.literal_eval(response.data.decode("UTF-8"))
    assert data.get('earnings') == 500 * 5
    assert data.get('rating') == etalon_rating
