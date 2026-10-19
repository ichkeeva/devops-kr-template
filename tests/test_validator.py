from validator import validate_phone

def test_validate_phone():
    assert validate_phone("+79991234567") is True
# fix typo
