import random


def payment_verification(number: str):
    errors = ["INVALID_CARD_NUMBER", "EXPIRED_CARD", "INVALID_CVV"]
    random_error = random.choice(errors)

    if ((len(number) == 8 or len(number) == 16)
            and int(number) % 2 == 0 and number[-1] != '0'):
        return 'successful operation'
    else:
        return random_error