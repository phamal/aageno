class Company:
    'Common base class for all employees'
    empCount = 0

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getSymbol(self):
        return self.symbol

    def setSymbol(self, symbol):
        self.symbol = symbol

    def getWebsite(self):
        return self.website

    def setWebsite(self, website):
        self.website = website

    def getSector(self):
        return self.sector

    def setSector(self, sector):
        self.sector = sector

    def getLastChangePrice(self):
        return self.lastChangePrice

    def setLastChangePrice(self, lastChangePrice):
        self.lastChangePrice = lastChangePrice

    def getLink(self):
        return self.link

    def setLink(self, link):
        self.link = link
