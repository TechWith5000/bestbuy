import store
from products import Product
from store import Store

def start():
    '''Shows the menu to the user'''
    print("     Store menu\n"
          "     __________")
    print("1. List all products in store\n"
          "2. Show total amount in store\n"
          "3. Make an order\n"
          "4. Quit")
def main():
    '''Runs the program, handles user input'''
    # setup initial stock of inventory
    product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]
    best_buy = Store(product_list)
    products_var = best_buy.get_all_products()


    while True:
        start()
        user_choice = input("Please enter a number: ")

        if user_choice == "1":
            # testing is_active for products in the shop
            #for product in products_var:
                #print(product.is_active())
            #print(products_var)
            for i, product in enumerate(products_var, start=1):
                print(f" {i}. {product.show()}")
            print("")

        if user_choice == "2":
            print(best_buy.get_total_quantity())

        if user_choice == "3":
            shopping_list = []
            order_running = True
            while order_running:
                print("------")
                for i, product in enumerate(products_var, start=1):
                    print(f" {i}. {product.show()}")
                print("------\n")
                print("When you want to finish order, enter empty text.")

                while True:
                    product_choice = input("Which product # do you want?")
                    # check whether user quits the order
                    if product_choice == "":
                        order_running = False
                        break # break the inner while loop
                    # check whether index is in the range of available products_var
                    if int(product_choice) > len(products_var) or int(product_choice) < 1:
                        print(f"# {product_choice} is not a valid product")
                        continue

                    product_amount = input("What amount do you want?")
                    # check whether user quits the order
                    if product_amount == "":
                        order_running = False
                        break # break the inner while loop


                    try:
                        # convert user input to an index
                        selected_product_index = int(product_choice) - 1
                        selected_product = products_var[selected_product_index]
                        product_amount = int(product_amount)

                        # add tuple (product, amount) to shopping list, if amount available
                        if product_amount <= selected_product.get_quantity():
                            shopping_list.append((selected_product, product_amount))
                            print("Product added to list!")
                        else:
                            print(f"Only {selected_product.get_quantity()} available")
                            continue


                    except ValueError:
                        print("Error adding product!")
                        continue

                # check if the outer loop terminates and the inner loop therefore should terminate as well
                if not order_running:
                    break

            try:
                total_price = best_buy.order(shopping_list)
                print(f"***********\n Order made! Total payment: {total_price}")

            except ValueError:
                print("Not enough products_var in stock, please make your order again with a smaller amount.")
                continue

            # update the product list after each order
            products_var = best_buy.get_all_products()

        if user_choice == "4":
            break



if __name__ == "__main__":
    main()