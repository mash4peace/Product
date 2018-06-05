from product_viewer import Product, show_products, Book, Movie, show_product
def main():
    print("The Product Viewer program! ")
    print()
    products = (Product('Stanley 13 Ounces Wood Hammer', 12.99, 62),
                Book("The Big Short", 15.95, 34, "Micheal Lewis"),
                Movie("The Holly Grail - DVD", 14.99, 68, 1975))
    show_products(products)

    while True:
        number = int(input("Enter product number: "))
        print()

        product = products[number-1]
        show_product(product)


        choice = input("Continue ? (y/n)")
        print()
        if choice != 'y':
            break
main()