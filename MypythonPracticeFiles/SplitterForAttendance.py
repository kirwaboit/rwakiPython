class AppleBasket():
    '''This class populates an apple basket with appoles of specified color and price'''
    def __init__(self,apple_color,apple_quantity):
        self.apple_color = apple_color
        self.apple_quantity = apple_quantity
    def increase(self):
        self.apple_quantity = self.apple_quantity+1
    def __str__(self):  # if you don't put this method then an actual instance memory point of the instance will be printed when you use "print"
        return 'A basket of {} {} apples.' .format(self.apple_quantity, self.apple_color)  