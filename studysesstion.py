import json
user_sessions = {}
session ={}
def show__menu():
        print("╔══════════════════════════════╗")
        print("║      STUDY TRACKER 📚            ")
        print("╚══════════════════════════════╝")
        choice =input('1.➕ Add session\n2.👀 View sessions\n3.🗑️  remove session\n4.🍅 Start Pomodoro\n5.🖥️  exit\nchoose a number; ')
        return choice
def save_data():
    with open("data.json", "w") as file:
        json.dump(session, file)
def load_data():
    global session

    with open("data.json", "r") as file:
        session = json.load(file)
load_data()                
def add():
    new_session=input('what session you want to add? ')
    duration = int(input("How many minutes do you want to study? "))
    session[new_session]=duration
    save_data()
    print(f"{new_session}: {duration} mins added to the list successfully")
def view():
    print(session)
load_data()
def save_users():
    with open("users.json", "w") as file:
        json.dump(user_sessions, file)


def load_users():
    global user_sessions

    try:
        with open("users.json", "r") as file:
            data = json.load(file)

            user_sessions = {
                int(user_id): sessions
                for user_id, sessions in data.items()
            }

    except FileNotFoundError:
        user_sessions = {}
def start_pomodoro():
   import pomodoro
   pomodoro.Pomodoro(25)
def remove():
    subject = input("What session do you want to remove? ")

    if subject in session:
        del session[subject]
        save_data()
        print(f"{subject} removed successfully.")
    else:
        print("Session not found.")
if __name__ == "__main__":
    load_data()

    while True:
        choice = show__menu()

        if choice == '1':
            add()

        elif choice == '2':
            view()

        elif choice == '3':
            remove()

        elif choice == '4':
            start_pomodoro()

        elif choice == '5':
            break

        else:
            print("The number is not valid")




