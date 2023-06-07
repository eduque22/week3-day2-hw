class Cart():
    '''Our cart will have T-Shirts, Crewnecks, Hoodies and Long Sleeve Tees.'''

    def __init__(self, t_shirts, crewnecks, hoodies, long_sleeve_tees):
        self.t_shirts = t_shirts
        self.crewnecks = crewnecks
        self.hoodies = hoodies
        self.long_sleeve_tees = long_sleeve_tees

    def shop(self):
        print('\nWhat would you like to purchase today?')
        purchase = input('T-Shirt("t") | Long Sleeve Tee("l") | Crewneck("c") | Hoodie("h")\nEnter Here: ')
        if purchase.lower() == 't':
            amt = input('\nNice, how many T-Shirts would you like to buy?\nAmt: ')
            if self.t_shirts == 0:
                self.t_shirts = int(amt)
            else:
                self.t_shirts += int(amt)
            print('Great, those have been added to your cart!')
        if purchase.lower() == 'l':
            amt = input('\nGreat choice, how many Long Sleeve Tees would you like to buy?\nAmt: ')
            if self.long_sleeve_tees == 0:
                self.long_sleeve_tees = int(amt)
            else:
                self.long_sleeve_tees += int(amt)
            print('Great, those have been added to your cart!')
        if purchase.lower() == 'c':
            amt = input('\nNice pick! How many Crewnecks would you like to buy?\nAmt: ')
            if self.crewnecks == 0:
                self.crewnecks = int(amt)
            else:
                self.crewnecks += int(amt)
            print('Great, those have been added to your cart!')
        if purchase.lower() == 'h':
            amt = input('\nMy favorites! How many Hoodies, would you like to buy?\nAmt: ')
            if self.hoodies == 0:
                self.hoodies = int(amt)
            else:
                self.hoodies += int(amt)
            print('Great, those have been added to your cart!')

    def add(self):
        print('What item are you looking to add?')
        added_item = input('\nT-Shirt("t") | Long Sleeve Tee("l") | Crewneck("c") | Hoodie("h"):\nEnter Here: ')
        if added_item.lower() == 't':
            how_many = input('How many T-Shirts would you like to add?\nAmt: ')
            self.t_shirts += int(how_many)
            print('Great, your cart has been updated!')
        if added_item.lower() == 'l':
            how_many = input('How many Long Sleeve Tees would you like to add?\nAmt: ')
            self.long_sleeve_tees += int(how_many)
            print('Great, your cart has been updated!')
        if added_item.lower() == 'c':
            how_many = input('How many Crewnecks would you like to add?\nAmt: ')
            self.crewnecks += int(how_many)
            print('Great, your cart has been updated!')
        if added_item.lower() == 'h':
            how_many = input('How many Hoodies would you like to add?\nAmt: ')
            self.hoodies += int(how_many)
            print('Great, your cart has been updated!')

    def sub(self):
        print('\nWhat item are you looking to remove?')
        remove_item = input('T-Shirt("t") | Long Sleeve Tee("l") | Crewneck("c") | Hoodie("h"):\nEnter Here: ')
        if remove_item.lower() == 't':
            how_many = input('How many T-Shirts are you looking to remove?\nAmt: ')
            self.t_shirts -= int(how_many)
            if self.t_shirts < 0:
                self.t_shirts = 0
            print('Okay, those items have been removed!')
        if remove_item.lower() == 'l':
            how_many = input('How many Long Sleeve Tees are you looking to remove?\nAmt: ')
            self.long_sleeve_tees -= int(how_many)
            if self.long_sleeve_tees < 0:
                self.long_sleeve_tees = 0
            print('Okay, those items have been removed!')
        if remove_item.lower() == 'c':
            how_many = input('How many Crewnecks are you looking to remove?\nAmt: ')
            self.crewnecks -= int(how_many)
            if self.crewnecks < 0:
                self.crewnecks = 0
            print('Okay, those items have been removed!')
        if remove_item.lower() == 'h':
            how_many = input('How many Hoodies are you looking to remove?\nAmt: ')
            self.hoodies -= int(how_many)
            if self.hoodies < 0:
                self.hoodies = 0
            print('Okay, those items have been removed!')

    def view_cart(self):
        print('\nOkay, let\'s take a look!')
        print('Your Cart')
        print('T-Shirts:', self.t_shirts)
        print('Long Sleeve Tees:', self.long_sleeve_tees)
        print('Crewnecks:', self.crewnecks)
        print('Hoodies:', self.hoodies)

def pan_text():
    eduardo_s_cart = Cart(0, 0, 0, 0)
    print('\n--Welcome to Panacea Textile Co.--')

    while True:
        ans = input('\nWhat would you like to do today?\nShop("s") - View Cart("v") - Add/Remove Item("i") - Finish Shopping("f")\nEnter Here: ')

        if ans == 's':
            eduardo_s_cart.shop()
        
        elif ans == 'v':
            eduardo_s_cart.view_cart()

        elif ans == 'i':
            print('\nWould you like to add("a") or remove("r") items from your cart?')
            aor = input('Enter here: ')
            if aor == 'a':
                eduardo_s_cart.add()
            elif aor == 'r':
                eduardo_s_cart.sub()

        elif ans == 'f':
            print('\nHere\'s your receipt!')
            print(eduardo_s_cart.__dict__)
            print('\nThank you for shopping with Panacea Textile, we hope to see you again soon!')
            break

pan_text()
