import phonenumbers


def is_phone_valid(phone: str) -> bool:
    try:
        parsed = phonenumbers.parse(phone)
        if not phonenumbers.is_valid_number(parsed):
            return False
        return True
    except phonenumbers.phonenumberutil.NumberParseException:
        return False


def normalize_phone(phone: str) -> str:
    parsed = phonenumbers.parse(phone)
    return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
