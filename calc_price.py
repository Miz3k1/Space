# Расчёт стоимости съёмки в фотостудии
PRICES = {"portrait": 3500, "family": 5500, "product": 2000, "love_story": 6000}

def total(service: str, hours: int) -> int:
    """Возвращает стоимость съёмки за указанное число часов."""
    return PRICES[service] * hours

if __name__ == "__main__":
    print(total("portrait", 2))
