
#functions
#adjust these later to minimize opening and saving of JSON file so that you're not using cpu unnecessarily

def load_user_data():
   with open('userdata.json', 'r') as file:
       database = json.load(file)
       return database

def save_user_data(data):
    with open('userdata.json', 'w') as file:
        json.dump(data, file, indent=4)

def print_welcome_statement():
    print("\nWelcome to Apollo- We're excited to connect you with other music makers!")
    print("To start building your circle, we'll need to build your profile")

def add_user():
    name = input("\nWhat is your name? ")
    age = input("\nWhat is your age ")
    role = input("\nPlease describe your role in the music industry in a few sentences: ")
    years_experience = input("\nHow many years of experience do you have in the music industry? ")
    genre = input("\nWhat genre(s) do you work in primarily? ")
    link = input("\nPlease include links to your work: ")

    user_database = load_user_data()
    if name not in user_database:
        user_database[name] = {
            "age": int(age),
            "role": role,
            "years of experience": int(years_experience),
            "genre": genre,
            "link": link
        }
        save_user_data(user_database)
    else:
        return

def main():
    print_welcome_statement()
    add_user()

if __name__ == "__main__":
    main()
