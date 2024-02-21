def make_pizza(*topings):
    print(topings)
    for toping in topings:
        print(toping)
vani = make_pizza("mushroom","onion","tomato")
ankitha = make_pizza("mushroom","pineapple","paneer","tomato")
bindu = make_pizza("mushroom","pineapple","paneer","seetcorn")


def make_pizza_base(*topings,base):
    print(topings,base)
    for toping in topings:
        print(toping)
vani = make_pizza_base("mushroom","onion","tomato",base="thin")

# def make_pizza_base(*topings,*base): *args will appear only once
