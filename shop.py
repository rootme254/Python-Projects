'''
This is a shopping list like ile inatumiwa in jumia the online shopping
Create a class called ShoppingCart.

Create a constructor that has no arguments and sets the total attribute to zero, and initializes an empty dict attribute named items.

Create a method add_item that requires item_name, quantity and price arguments. This method should add the cost of the added items to the current value of total. It should also add an entry to the items dict such that the key is the item_name and the value is the quantity of the item.

Create a method remove_item that requires similar arguments as add_item. It should remove items that have been added to the shopping cart and are not required. This method should deduct the cost of these items from the current total and also update the items dict accordingly. If the quantity of items to be removed exceeds current quantity in cart, assume that all entries of that item are to be removed.

Create a method checkout that takes in cash_paid and returns the value of balance from the payment. If cash_paid is not enough to cover the total, return Cash paid not enough.

Create a class called Shop that has a constructor which initializes an attribute called quantity at 100.

Make sure Shop inherits from ShoppingCart.

In the Shop class, override the remove_item method, such that calling Shop's remove_item with no arguments decrements quantity by one.

'''

class ShoppingCart (object):


      
     def __init__(self):

          self.total = 0
          self.items = {}

          

     def add_item(self,item_name ,quantity ,price):

         self.total =self.total + price
         self.items[item_name]=quantity



   
     def remove_item(self,item_name ,quantity,price):

          
          del self.items[item_name]
          self.total = self.total - price
          value=0
          
          for k,v in self.items.items():
               value += v
               
          if (quantity > value ):

               self.items.clearAll()



     def checkout(self,cash_paid):

          if (cash_paid < self.total):

               print ("Cash paid not enough ")
          else:
               self.balance= cash_paid - self.total
               print ("Total amount for the goods below ",self.total)
               print (self.items)
               print ("The arrears after payment is ",self.balance)



     def show_details(self):

          print  (self.items)

               

class Shop(ShoppingCart):
     
     '''If you wanted the constructor to be handled by the ->>
        super constructor
        super.(ShoppingCart,self).__init__(item_name ,quantity ,price)
     '''

     def __init__(self):

          self.quantity=100

    #Overriding the remove_item
     def remove_item(self):

          self.quantity =- 1
          

sh=ShoppingCart()
sh.add_item("Cars",30,3452.34)
sh.add_item("Computer",20,3452.34)
sh.add_item("Movies",20,34523.34)
sh.add_item("Papers",10,1000)
sh.remove_item("Papers",10,1000)
sh.show_details()

sh.checkout(80000)



         
    
