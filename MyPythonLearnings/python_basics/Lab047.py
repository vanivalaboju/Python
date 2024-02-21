def makepizza(*toppings, base="Wheat"):
    print(toppings, base)
    for topping in toppings:
        print(topping)
    return toppings, base


vani_v, vani_k = makepizza("onion", "tomato", "sweetcorn")
pramod = makepizza("onion", "tomato", "sweetcorn", base="thin crust")
print(vani_v)
print(vani_k)
print(pramod)