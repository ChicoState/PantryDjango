from AbstractFactoryItems import AbstractFactoryItems
from datetime import date 

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


    def SetName(ItemName:str):
        self.Name = ItemName


    def GetName()->str:
        return self.Name


    def SetQuantity(Quant:int):
        self.Quantity = Quant


    def GetQuantity()->int:
        return self.Quantity


    def SetReceivedDate(Date:str):
        self.ReceivedDate = Date


    def GetReceivedDate():
        return self.ReceivedDate


    def SetCheckOutDate(checkoutdate:str):
        self.CheckOutDate = checkoutdate


    def SetExpiry(expirydate:str):
        self.ExpiryDate = expirydate


    def GetExpiry()->str:
        return self.ExpiryDate


    def SetID(id:str):
        self.ID = id


    def GetID()->str:
        return self.ID
