from AbstractFactoryItems import AbstractFactoryItems
from datetime import date
from datetime import datetime

class ConcreteFactoryUPC(AbstractFactoryItems):
    def __init__(self):
        self.Quantity = 0 #initializing quantity to 0
        self.DefaultDate = date(1970, 12, 31)
        self.ReceivedDate = DefaultDate #initializing received date initially to default value
        self.CheckOutDate = DefaultDate #initializing Checked Out date initially to default value
        self.Name = "" #Variable to store item name
        self.CheckedOutBy = "" #Variable to store student ID, that checked out this product
        self.ExpiryDate = DefaultDate #Initializing expiry date of the product to default date
        self.ID = "" #Donor ID

# Following are the getter and setters for the above variables
    def SetName(ItemName:str):
        self.Name = ItemName


    def GetName()->str:
        return self.Name


    def SetQuantity(Quant:int):
        self.Quantity = Quant


    def GetQuantity()->int:
        return self.Quantity


    def SetReceivedDate(Date:str):
        self.ReceivedDate = datetime.strptime(Date, '%y/%m/%d')


    def GetReceivedDate():
        return self.ReceivedDate.strftime('%y/%m/%d')


    def SetCheckOutDate(checkoutdate:str):
        self.CheckOutDate = datetime.strptime(checkoutdate, '%y/%m/%d')


    def GetCheckOutDate()->str:
        return self.CheckOutDate.strftime('%y/%m/%d')


    def SetExpiry(expirydate:str):
        self.ExpiryDate = datetime.strptime(expirydate, '%y/%m/%d')


    def GetExpiry()->str:
        return self.ExpiryDate.strftime('%y/%m/%d')


    def SetID(id:str):
        self.ID = id


    def GetID()->str:
        return self.ID
