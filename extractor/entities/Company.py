class Company:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, symbol,sector,link):
        self.name = name
        self.symbol = symbol
        self.sector = sector
        self.link = link


    def displayCompany(self):
        print "Name : ", self.name, ", Symbol: ", self.symbol