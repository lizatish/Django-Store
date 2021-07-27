CourierId = {
    'type': 'object',
    'additionalProperties': False,
    'properties': {
        'courier_id': {
            'type': 'integer',
            'minimum': 0
        }
    },
    'required': ["courier_id"]
}
