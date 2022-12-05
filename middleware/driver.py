class Driver():

    # init
    def __init__(self, did=0, fullname=None, address=None, email=None, licenseno=None, status=None, password=None):
        self.did = did
        self.fullname = fullname
        self.address = address
        self.email = email
        self.licenseno = licenseno
        self.status = status
        self.password = password

    # Getters
    def getDid(self):
        return self.did

    def getFullname(self):
        return self.fullname

    def getAddress(self):
        return self.address

    def getEmail(self):
        return self.email

    def getLicenseno(self):
        return self.licenseno

    def getStatus(self):
        return self.status

    def getPassword(self):
        return self.password

    # Setters

    def setDid(self, did):
        self.did = did

    def setFullname(self, fullname):
        self.fullname = fullname

    def setAddress(self, address):
        self.address = address

    def setEmail(self, email):
        self.email = email

    def setLicenseno(self, licenseno):
        self.licenseno = licenseno

    def setStatus(self, status):
        self.status = status

    def setPassword(self, password):
        self.password = password

    # str
    def __str__(self):
        return "{},{},{},{},{},{},{}".format(self.did, self.fullname, self.address, self.email, self.licenseno, self.status, self.password)
