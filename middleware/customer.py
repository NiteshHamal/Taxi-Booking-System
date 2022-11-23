class Customer():
    # init
    def __init__(self, cid=0, fullname=None, address=None, email=None, number=0, password=None, payment=None, status=None):
        self.cid = cid
        self.fullname = fullname
        self.address = address
        self.email = email
        self.number = number
        self.password = password
        self.payment = payment
        self.status = status

    # Getters
    def getCid(self):
        return self.cid

    def getFullName(self):
        return self.fullname

    def getAddress(self):
        return self.address

    def getEmail(self):
        return self.email

    def getNumber(self):
        return self.number

    def getPassword(self):
        return self.password

    def getPayment(self):
        return self.payment

    def getStatus(self):
        return self.status

    # Setter
    def setCid(self, cid):
        self.cid = cid

    def setFullName(self, fullname):
        self.fullname = fullname

    def setAddress(self, address):
        self.address = address

    def setEmail(self, email):
        self.email = email

    def setNumber(self, number):
        self.number = number

    def setPassword(self, password):
        self.password = password

    def setPayment(self, payment):
        self.payment = payment

    def setStatus(self, status):
        self.status = status

    # str
    def __str__(self):
        return "{}, {}, {}, {}, {}, {}, {}, {}".format(self.cid, self.fullname, self.address, self.email, self.number, self.password, self.payment, self.status)
