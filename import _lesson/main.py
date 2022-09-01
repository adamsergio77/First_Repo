from shop.products import upgrade_quantity
from shop.products import price
from shop.order import make_new_oreder
from shop.products import product


def beginin():
    while True:
        print("Witaj w wirtualnym sklepie \nWybierz z ponizszych pozycji \n\t- jablka\n\t- gruszki\n\t- winogorna\n Jesli chcesz zakonczy dodawanie produktow wcisnij x")
        choice = (input("wybierz produkt: "))
        if choice=="x":
            break

        if choice not in product.keys():
            print("Produktu nie ma na liscie\nZacznijmy od poczatku\n")
            continue
        new_quantity = int(input("Wybierz ilosc"))
        if new_quantity>product[choice]["quantity"]:
            print(f"Nie ma tyle na stanie, ilosc na magazynie wynisi {product[choice]['quantity']}\nZacznijmy od poczatku\n")
            continue

        upgrade_quantity(choice,new_quantity)
        price_of_order=price(choice,new_quantity)
        new_oreder=make_new_oreder(choice,new_quantity,(f"{price_of_order:0.2f}"))





if __name__=='__main__':
    beginin()