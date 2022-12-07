class Booking():

    # init
    def __init__(self, bookingid=0, pickup_address=None, drop_address=None, pickup_date=None, pickup_time=None, status=None, cid=None, did=None):
        self.bookingid = bookingid
        self.pickup_address = pickup_address
        self.drop_address = drop_address
        self.pickup_date = pickup_date
        self.pickup_time = pickup_time
        self.status = status
        self.cid = cid
        self.did = did

    # Getters
    def getBookingid(self):
        return self.bookingid

    def getPickup_Address(self):
        return self.pickup_address

    def getDrop_Address(self):
        return self.drop_address

    def getPickup_Date(self):
        return self.pickup_date

    def getPickup_Time(self):
        return self.pickup_time

    def getStatus(self):
        return self.status

    def getCid(self):
        return self.cid

    def getDid(self):
        return self.did

    # Setter
    def setBookingid(self, bookingid):
        self.bookingid = bookingid

    def setPickup_Address(self, pickup_address):
        self.pickup_address = pickup_address

    def setDrop_Address(self, drop_address):
        self.drop_address = drop_address

    def setPickup_Date(self, pickup_date):
        self.pickup_date = pickup_date

    def setPickup_Time(self, pickup_time):
        self.pickup_time = pickup_time

    def setStatus(self, status):
        self.status = status

    def setCid(self, cid):
        self.cid = cid

    def setDid(self, did):
        self.did = did

    # str********
    def __str__(self):
        return "{},{},{},{},{},{},{},{}", format(self.bookingid, self.pickup_address, self.drop_address, self.pickup_date, self.pickup_time, self.status, self.cid, self.did)
