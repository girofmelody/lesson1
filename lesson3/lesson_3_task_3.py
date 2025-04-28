# lesson_3_task_3.py

from address import Address
from mailing import Mailing

# Создаем адреса для отправления и получения
to_address = Address("123456", "Москва", "Ленина", "10", "5")
from_address = Address("654321", "Санкт-Петербург", "Пушкина", "15", "12")

# Создаем экземпляр класса Mailing
mailing = Mailing(to_address, from_address, cost=250.0, track="TRK123456")

# Печатаем информацию об отправлении в заданном формате
print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")