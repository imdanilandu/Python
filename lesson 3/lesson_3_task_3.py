from adress import Adress

from mailing import Mailing

to_adress = Adress('654321', 'Krasnoyarsk', 'Kirenskogo', 2, 1)
from_adress = Adress('123456', 'Moscow', 'Lenina', 1, 2)
mailing = Mailing(from_adress, to_adress, '12345678901234', 100)

print(f'Отправление {mailing.track} из {mailing.from_adress.index}, {mailing.from_adress.city}, {mailing.from_adress.street}, {mailing.from_adress.house} - {mailing.from_adress.flat} в {mailing.to_adress.index}, {mailing.to_adress.city}, {mailing.to_adress.street}, {mailing.to_adress.house} - {mailing.to_adress.flat}. Стоимость {mailing.cost} рублей.')