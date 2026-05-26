
def expense_tracker():
    print("--- DecodeLabs Expense Tracker ---")
    print("Enter your expenses one by one.")
    print("Type 'done' when you are finished to see the total.\n")

    total_spent=0.0

    while True:
        user_input=input("Enter expense amount or done: ").strip().lower()

        if user_input=="done":
            break

        try:
            expense=float(user_input)

            total_spent+=expense
            print(f"Current total expense ${total_spent:.2f}")
        except ValueError:

            print("Invalid input please enter a valid input in integer or type done!")

        
    print("-"*30,"\n")
    print(f"Final Total Expense :${total_spent:.2f}\n")
    print("-"*30,"\n")




expense_tracker()
      