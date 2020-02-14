#!/usr/bin/python3
from convert import build_avito_xml
from datetime import datetime

data = [
  {
    "id": "xjfdge4735202",
    "category": "Квартиры",
    "operationType": "Продам",
    "dateBegin": datetime.now(),
    "dateEnd": datetime(2006, 11, 21, 16, 30),
    "address": "Россия, Алтайский край, Барнаул, Парашютная улица, 49",
    "description": '''
			Новая, просторная, светлая и уютная квартира с типовым косметическим ремонтом в новом доме серии "П-44Т".

			Комнаты изолированные, 19 и 15 метров, кухня 13 метров с эркером, большая ванная, с/у раздельный, две застекленные лоджии.

			А также:
				* стеклопакеты,
				* паркетная доска,
				* свободна,
				* никто не прописан,
				* прямая продажа.
		''',
    "price": 123000,
    "companyName": "ООО \"Рога и копыта\"",
    "managerName": "Иван Петров-Водкин",
    "allowEmail": False,
    "contactPhone": "+7 916 683-78-22",
    "images": [
      "http://img.test.ru/8F7B-4A4F3A0F2BA1.jpg",
      "http://img.test.ru/8F7B-4A4F3A0F2XA3.jpg"
    ],
    "videoURL": "http://www.youtube.com/watch?v=YKmDXNrDdBI",
    "adStatus": "PushUp",
    "rooms": 2,
    "square": 61,
    "floor": 13,
    "floors": 16,
    "houseType": "Деревянный",
    "marketType": "Новостройка",
    "newDevelopmentId": 28212,
    "cadastralNumber": "77:04:0004011:3882"
  },
  {
    "id": "xjfdge4735204",
    "category": "Комнаты",
    "address": "Тамбовская область, Моршанск, Моршанский р-н, с. Устьи, ул. Лесная, 7",
    "latitude": 53.485221,
    "longitude": 41.840005,
    "description": '''
<![CDATA[
<p>Новая, просторная, <strong>светлая и уютная квартира<strong> с ремонтом и большим холодильником,<br />
комнаты изолированные, 11 и 10 метров, кухня 3 метра с балконом.</p>
<p><em>Важно:</em></p>
<ul>
<li>маленькая ванная,
<li>с/у совмещенный,
<li>3 застекленные лоджии,
<li>стеклопакеты,
<li>паркет,
<li>свободна.
</ul>
]]>
    ''',
    "price": 102000,
    "rooms": 2,
    "square": 61.3,
    "floor": 14,
    "floors": 16,
    "houseType": "Деревянный",
    "operationType": "Сдам",
    "leaseType": "На длительный срок",
    "propertyRights": "Посредник",
    "leaseCommissionSize": 50,
    "leaseDeposit": "2,5 месяца",
    "leaseBeds": 3,
    "leaseSleepingPlaces": 5,
    "leaseMultimedia": [
      "Wi-Fi",
      "Кабельное / цифровое ТВ"
    ],
    "leaseAppliances": [
      "Плита",
      "Стиральная машина",
      "Фен"
    ],
    "leaseComfort": [
      "Кондиционер",
      "Балкон / лоджия"
    ],
    "leaseAdditionally": [
      "Можно с питомцами",
      "Можно для мероприятий",
      "Можно курить"
    ],
    "images": [
      "a1.jpg",
      "a2.jpg",
      "a3.jpg"
    ],
    "allowEmail": False
  }
]

build_avito_xml(data)
