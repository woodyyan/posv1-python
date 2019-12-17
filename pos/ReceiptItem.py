class ReceiptItem:
    def __init__(self, barcode, name, price, count=0):
        self.barcode = barcode
        self.name = name
        self.price = price
        self.count = count
        self.total = 0
