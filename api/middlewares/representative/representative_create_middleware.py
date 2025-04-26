def validate_representant_data(data):
    required_fields = ['name', 'cnpj', 'email', 'phone']
    for field in required_fields:
        if field not in data:
            return f"Missing field: {field}"
    return None