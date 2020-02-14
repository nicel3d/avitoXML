from dataclasses import dataclass
from datetime import datetime


@dataclass
class Ad:
  id: int = None
  category: str = None
  dateBegin: datetime = None
  dateEnd: datetime = None
  address: str = None
  latitude: float = None
  longitude: float = None
  description: str = None
  price: float = None
  companyName: str = None
  managerName: str = None
  allowEmail: bool = False
  contactPhone: str = False
  images: list = None
  videoURL: str = None
  adStatus: str = None
  rooms: int = None
  square: int = None
  floor: int = None
  floors: int = None
  houseType: str = None
  operationType: str = None
  leaseType: str = None
  propertyRights: str = None
  leaseCommissionSize: float = None
  leaseDeposit: str = None
  leaseBeds: float = None
  leaseSleepingPlaces: float = None
  leaseMultimedia: list = None
  leaseAppliances: list = None
  leaseComfort: list = None
  leaseAdditionally: list = None
  marketType: str = None
  newDevelopmentId: int = None
  cadastralNumber: str = None

  def __init__(self, initial_data):
    for key in initial_data:
      setattr(self, key, initial_data[key])

  def get_allow_email_text(self):
    return "Да" if self.allowEmail else "Нет"

  def get_date_begin_text(self):
    return datetime.strftime(self.dateBegin, "%Y-%m-%d") if self.dateBegin else ""

  def get_date_end_text(self):
    return datetime.strftime(self.dateEnd, "%Y-%m-%d") if self.dateEnd else ""

  def validate(self):
    return (
      self.id and self.category and self.operationType and self.address and
      self.square and self.description and self.price and self.adStatus
    )
