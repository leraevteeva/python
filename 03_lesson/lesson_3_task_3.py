from address import Address
from mailing import Mailing

to_addr = Address("123456", "Москва", "Тверская", "10", "15")
from_addr = Address("654321", "Санкт-Петербург", "Невский проспект", "5", "8")

mail = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=350,
    track="TRACK123456789"
)

print(
    f"Отправление {mail.track} из "
    f"{mail.from_address.index}, {mail.from_address.city}, {mail.from_address.street}, "
    f"{mail.from_address.house} - {mail.from_address.apartment} в "
    f"{mail.to_address.index}, {mail.to_address.city}, {mail.to_address.street}, "
    f"{mail.to_address.house} - {mail.to_address.apartment}. "
    f"Стоимость {mail.cost} рублей."
)
