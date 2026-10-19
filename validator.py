def validate_email(email: str) -> bool:
    return "@" in email

def validate_phone(phone: str) -> bool:
    return len(phone) >= 10

def validate_snils(snils: str) -> bool:
    return len(snils) == 11