class Order:
    def __init__(self):
        self.items={}
    
    def add_item(self, item):
        if item in self.items:
            self.items[item]+=item.quantity #jodi cart a item ta already thake
        else:
            self.items[item]=item.quantity #cart a item jodi na thake

    def remove(self, item):
        if item in self.items:
            del self.items[item]
    
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())
    
    def clear(self):
        self.items={}