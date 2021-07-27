OrderComplete = {
    'type': 'object',
    'additionalProperties': False,
    'properties': {
        'courier_id': {
            'type': 'integer',
            'minimum': 0
        },
        'order_id': {
            'type': 'integer',
            'minimum': 0
        },
        'complete_time': {
            "format": "date-time",
            "type": "string"
        }
    },
    'required': ['courier_id', 'order_id', 'complete_time']
}
