from products import Product
from store import Store

def start():
    '''shows the menu to the user'''
    print("     Store menu\n"
          "     __________")
    print("1. List all products in store\n"
          "2. Show total amount in store\n"
          "3. Make an order\n"
          "4. Quit")
def main():
    # setup initial stock of inventory
    product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]
    best_buy = Store(product_list)
    products = best_buy.get_all_products()


    while True:
        start()
        user_choice = input("Please enter a number: ")

        if user_choice == "1":
            for i, product in enumerate(products, start=1):
                print(f" {i}. {product.show()}")
            print("")

        if user_choice == "2":
            print(best_buy.get_total_quantity())

        if user_choice == "3":
            shopping_list = []
            order_running = True
            while order_running:
                print("------")
                for i, product in enumerate(products, start=1):
                    print(f" {i}. {product.show()}")
                print("------\n")
                print("When you want to finish order, enter empty text.")

                while True:
                    product_choice = input("Which product # do you want?")

                    if product_choice == "":
                        order_running = False
                        break # break the inner while loop

                    product_amount = input("What amount do you want?")
                    if product_amount == "":
                        order_running = False
                        break # break the inner while loop

                    try:
                        # convert user input to an index
                        selected_product_index = int(product_choice) - 1
                        selected_product = products[selected_product_index]
                        product_amount = int(product_amount)
                        shopping_list.append((selected_product, product_amount))
                        print("Product added to list!")

                    except ValueError:
                        print("Error adding product!")
                        continue

                # check if the outer loop terminates and the inner loop therefore should terminate as well
                if not order_running:
                    break

            print(f"***********\n Order made! Total payment: {best_buy.order(shopping_list)}")


        if user_choice == "4":
            break

        else:
            continue


if __name__ == "__main__":
    main()