def parse_names(value: str | tuple | list | dict) -> str:
    match value:
        case surname, name, second_name:
            pass
        case {'surname': surname, 'name': name, 'second_name': second_name} if len(value) == 3:
            pass
        case str() if len(value.split()) == 3:
            surname, name, second_name = value.split()
            pass
        case _:
            return 'Error'
    return f'Фамілія: {surname}, Ім\'я: {name}, По бітькові: {second_name}'

if __name__ == '__main__':
    assert parse_names(('Іванов', 'Іван', 'Іванович')) == 'Фамілія: Іванов, Ім\'я: Іван, По бітькові: Іванович'
    assert parse_names(['Іванов', 'Іван', 'Іванович']) == 'Фамілія: Іванов, Ім\'я: Іван, По бітькові: Іванович'
    assert parse_names({'surname': 'Іванов',
                        'name': 'Іван',
                        'second_name': 'Іванович'}) == 'Фамілія: Іванов, Ім\'я: Іван, По бітькові: Іванович'
    assert parse_names('Іванов Іван Іванович') == 'Фамілія: Іванов, Ім\'я: Іван, По бітькові: Іванович'
    assert parse_names(('Іванов', 'Іван', 'Іван', 'Іванович')) == 'Error'
    assert parse_names(('Іванов', 'Іванович')) == 'Error'
    assert parse_names({'surname': 'Іванов',
                        'name': 'Іван',
                        'second_name': 'Іванович',
                        'sex': 'male'}) == 'Error'
    assert parse_names({'a': 'Іванов',
                        'b': 'Іван',
                        'c': 'Іванович'}) == 'Error'
