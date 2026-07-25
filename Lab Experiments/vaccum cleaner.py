
def vacuum_cleaner(location, state):
    print("Vacuum is placed in Room", location)
    print("Room A:", state[0], " | Room B:", state[1])   
    if location == "A":
        if state[0] == "Dirty":
            print("Room A is Dirty. Cleaning Room A...")
            state[0] = "Clean"
        else:
            print("Room A is already Clean.")
        location = "B"
        if state[1] == "Dirty":
            print("Room B is Dirty. Cleaning Room B...")
            state[1] = "Clean"
        else:
            print("Room B is already Clean.")

    elif location == "B":
        if state[1] == "Dirty":
            print("Room B is Dirty. Cleaning Room B...")
            state[1] = "Clean"
        else:
            print("Room B is already Clean.")
        location = "A"
        if state[0] == "Dirty":
            print("Room A is Dirty. Cleaning Room A...")
            state[0] = "Clean"
        else:
            print("Room A is already Clean.")
    print("\nFinal State: Room A:", state[0], "| Room B:", state[1])
vacuum_cleaner("A", ["Dirty", "Clean"])
