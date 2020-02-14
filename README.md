# AvitoXml

1. все зависимости для проекта устанавливаются из файла `requirements.txt`
2. `index.py` содержит в себе массив `data` получаемый из вне(БД, либо ф-ций) 
в дальнейшем исп. метод `build_avito_xml` для получения файла `output/avito.xml`
3. `models/Ad.py` служит для валидации данных и форматирования полей таких как `Дата`, 
`Да/Нет`
4. `convert.py` содержит в себе все методы для сборки `XML` документа


### Добавлять доп. проверки
исп. для этого метод в `models/Ad.py`
```python
  def validate(self):
    return (
      self.id and self.category and self.operationType and self.address and
      self.square and self.description and self.price and self.adStatus
    )
``` 

### Добавлять новые поля
1. Добавляем сначало в модель `models/Ad.py`
```python
class Ad:
  id: int = None
```

2. Затем в метод `build_avito_xml`в файле `convert.py` 
```python
for item in list_ads:
    if item.validate():
      ad = etree.SubElement(ads, "Ad")
      etree_item(ad, "Id", item.id)
```