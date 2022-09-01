product={"jablka":
             {"price":4.99,
              "quantity":100
                },
         "gruszki":{
             "price":5.99,
             "quantity": 150,
                }
         }

def upgrade_quantity(choice, new_quantity):
    product[choice]["quantity"]=product[choice]["quantity"]-new_quantity
    if new_quantity>product[choice]["quantity"]:
        print("Nie mamy tyle na stanie")

    print(product[choice]["quantity"])



def price(choice, new_quantity):
    return new_quantity*product[choice]["price"]







