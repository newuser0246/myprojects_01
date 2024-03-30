def load_favorites():
    try:
        with open('favorites.txt', 'r') as f:
            favorites = f.read().splitlines()
    except FileNotFoundError:
        favorites = []
    return favorites

def save_favorites(favorites):
    with open('favorites.txt', 'w') as f:
        for city in favorites:
            f.write(city + '\n')
        

def add_favorite(city):
    favorites = load_favorites()
    if city not in favorites:
        favorites.append(city)
        save_favorites(favorites)
        print(f"{city} added to favorites.")
    else:
        print(f"{city} is already in favorites.")

def display_favorites():
    favorites = load_favorites()
    if favorites:
        print("Your favorite cities:")
        for city in favorites:
            print("-", city)
    else:
        print("You have no favorite cities yet.")

def delete_favorites(city):
    favorites = load_favorites()
    if city in favorites:
        favorites.remove(city)
        save_favorites(favorites)
        print(f"{city} is deleted from favorites.")
    else:
        print(f"{city} Not Found in favorites.")

def delete_all():
    favorites = load_favorites()
    favorites.clear()
    save_favorites(favorites)
    print("All Cities are deleted from favorites.")

def main():
    while True:
        print("\n1. Add city to favorites")
        print("2. Delete city from favorites")
        print("3. Display favorite cities")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            city = str(input("Enter the city you want to add to favorites: "))
            add_favorite(city)
        elif choice == '2':
            is_all = int(input("Enter '1' if you want to delete all the cities (empty the list), else Enter '0': "))
            if is_all == 1:
                delete_all()
            else:
                city = str(input("Enter the city you want to delete from favorites: "))
                delete_favorites(city)

        elif choice == '3':
            display_favorites()
        elif choice == '4':
            print("Exiting from favorites ...\n\n")
            break
        else:
            print("\n Invalid choice. Please try again.")

if __name__ == "__main__":
    main()