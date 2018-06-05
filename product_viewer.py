from objects import Product, Book, Movie
def show_products(products):
    print("Products".upper())
    for i in range(len(products)):
        product = products[i]
        print(str(i +1)+ ". " + product.getDiscription())
    print()

def show_product(product):
    print("Product Data".upper())
    print("Name:        ", product.name)
    if isinstance(product, Book):
        print("Author:  ", product.author)
    if isinstance(product, Movie):
        print("Year:       ", product.year)

    print("Discount price: {:.2f}".format(product.getDiscountPrice()))
    print()

