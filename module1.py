

shop = {"shirt" : 450, "pant" : 700, "belt" : 300, "cap" :200, "specs" :700,
             "sandal" : 600, "shoes" : 800}


customer =input("which product you want to know the price ? ")


if customer == "shoes":
    print(shop["shoes"])
elif customer == "belt":
    print(shop["belt"])
elif customer == "shirt":
    print(shop["shirt"])
elif customer == "sandal":
    print(shop["sandal"])
elif customer == "cap":
    print(shop["cap"])
elif customer == "spec":
    print(shop["spec"])
elif customer == "pant":
    print(shop["pant"])

else:
    print("NO PRODUCT AVAILABLE")





