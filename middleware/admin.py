class Admin():

    # init
    def __init__(self, adminid=0, fullname=None, address=None, email=None, password=None):
        self.adminid = adminid
        self.fullname = fullname
        self.address = address
        self.email = email
        self.password = password

    # Getter

    def getAdminid(self):
        return self.adminid

    def getFullname(self):
        return self.fullname

    def getAddress(self):
        return self.address

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password

    # Setter

    def setAdminid(self, adminid):
        self.adminid = adminid

    def setFullname(self, fullname):
        self.fullname = fullname

    def setAddress(self, address):
        self.address = address

    def setEmail(self, email):
        self.email = email

    def setPassword(self, password):
        self.password = password

    # str
    def __str__(self):
        return "{},{},{},{},{}".format(self.adminid, self.fullname, self.address, self.email, self.password)
