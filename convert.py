from lxml import etree
from models.Ad import *


def etree_grouping(_parent, _tag, _text: list):
  if _text and len(_text):
    group = etree.SubElement(_parent, _tag)
    for text in _text:
      etree.SubElement(group, "Option").text = text


def etree_item(_parent, _tag, _text: str or float):
  if _text:
    etree.SubElement(_parent, _tag).text = str(_text)


def build_avito_xml(data):
  list_ads = []
  for item in data:
    list_ads.append(Ad(item))

  ads = etree.Element("Ads", formatVersion="3", target="Avito.ru")

  for item in list_ads:
    if item.validate():
      ad = etree.SubElement(ads, "Ad")
      etree.SubElement(ad, "Id").text = item.id

      etree_item(ad, "Category", item.category)
      etree_item(ad, "OperationType", item.operationType)
      etree_item(ad, "DateBegin", item.get_date_begin_text())
      etree_item(ad, "DateEnd", item.get_date_end_text())
      etree_item(ad, "Address", item.address)
      etree_item(ad, "Latitude", item.latitude)
      etree_item(ad, "Longitude", item.longitude)
      etree_item(ad, "Description", item.description)
      etree_item(ad, "Price", item.price)
      etree_item(ad, "CompanyName", item.companyName)
      etree_item(ad, "ManagerName", item.managerName)
      etree_item(ad, "AllowEmail", item.get_allow_email_text())

      if item.images and len(item.images):
        group = etree.SubElement(ad, "Images")
        for url in item.images:
          etree.SubElement(group, "Images", url=url)

      etree_item(ad, "VideoURL", item.videoURL)
      etree_item(ad, "AdStatus", item.adStatus)
      etree_item(ad, "Rooms", item.rooms)
      etree_item(ad, "Square", item.square)
      etree_item(ad, "Floor", item.floor)
      etree_item(ad, "Floors", item.floors)

      etree_item(ad, "HouseType", item.houseType)
      etree_item(ad, "LeaseType", item.leaseType)
      etree_item(ad, "PropertyRights", item.propertyRights)
      etree_item(ad, "LeaseCommissionSize", item.leaseCommissionSize)
      etree_item(ad, "LeaseDeposit", item.leaseDeposit)
      etree_item(ad, "LeaseBeds", item.leaseBeds)
      etree_item(ad, "LeaseSleepingPlaces", item.leaseSleepingPlaces)

      etree_grouping(ad, "LeaseMultimedia", item.leaseMultimedia)
      etree_grouping(ad, "LeaseAppliances", item.leaseAppliances)
      etree_grouping(ad, "LeaseComfort", item.leaseComfort)
      etree_grouping(ad, "LeaseAdditionally", item.leaseAdditionally)

      etree_item(ad, "MarketType", item.marketType)
      etree_item(ad, "NewDevelopmentId", item.newDevelopmentId)

  tree = etree.ElementTree(ads)
  tree.write("output/avito.xml", pretty_print=True, xml_declaration=True, encoding="utf-8")
