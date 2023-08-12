import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_event():
    clear_screen()
    print("Create a New Event\n")
    event_name = input("Enter the name of the event: ")
    event_folder = event_name.replace(" ", "_")

    if not os.path.exists(event_folder):
        os.makedirs(event_folder)

    text_file_path = os.path.join(event_folder, event_name + ".txt")

    participants = []
    num_participants = int(input("Enter the number of participants: "))
    for _ in range(num_participants):
        participant = input(f"Enter participant #{len(participants)+1} name: ")
        participants.append(participant)

    participants.sort()

    sponsors = []
    num_sponsors = int(input("Enter the number of sponsors: "))
    for _ in range(num_sponsors):
        sponsor = input(f"Enter sponsor #{len(sponsors)+1} name: ")
        sponsors.append(sponsor)

    sponsors.sort()

    total_budget = float(input("Enter the total budget for the event: "))

    with open(text_file_path, "w") as text_file:
        text_file.write(f"Event: {event_name}\n\n")
        text_file.write("Participants:\n")
        text_file.write("\n".join(participants))
        text_file.write("\n\nSponsors:\n")
        text_file.write("\n".join(sponsors))
        text_file.write(f"\n\nTotal Budget: ${total_budget}")

    clear_screen()
    print("Event details have been successfully stored.\n")

def fetch_event_details():
    clear_screen()
    print("Fetch Event Details\n")
    event_name = input("Enter the name of the event to fetch details: ")
    event_folder = event_name.replace(" ", "_")
    text_file_path = os.path.join(event_folder, event_name + ".txt")

    if os.path.exists(text_file_path):
        with open(text_file_path, "r") as text_file:
            event_details = text_file.read()
            clear_screen()
            print("Event Details:\n")
            print(event_details)
    else:
        clear_screen()
        print("Error: No such event file found.\n")

def advanced_menu():
    while True:
        clear_screen()
        print("Advanced Menu:")
        print("1. List all events")
        print("2. Search for an event")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_all_events()
        elif choice == "2":
            search_for_event()
        elif choice == "3":
            clear_screen()
            print("Returning to main menu.\n")
            break
        else:
            clear_screen()
            print("Invalid choice. Please select a valid option.\n")

def list_all_events():
    clear_screen()
    print("List of All Events\n")

    event_folders = [folder for folder in os.listdir() if os.path.isdir(folder)]
    events = [event.replace("_", " ") for event in event_folders]

    if events:
        print("Available events:")
        for i, event in enumerate(events, start=1):
            print(f"{i}. {event}")
    else:
        print("No events found.")

    input("\nPress Enter to return to the advanced menu.")

def search_for_event():
    clear_screen()
    print("Search for an Event\n")
    event_name = input("Enter the name of the event to search for: ")
    event_folder = event_name.replace(" ", "_")
    text_file_path = os.path.join(event_folder, event_name + ".txt")

    if os.path.exists(text_file_path):
        with open(text_file_path, "r") as text_file:
            event_details = text_file.read()
            clear_screen()
            print("Event Details:\n")
            print(event_details)
    else:
        clear_screen()
        print("Error: No such event file found.\n")

    input("\nPress Enter to return to the advanced menu.")

def main():
    clear_screen()
    print("Welcome to the Event Management System!")

    while True:
        print("\nMain Menu:")
        print("1. Create a new event")
        print("2. Fetch details of an existing event")
        print("3. Advanced Menu")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_event()
        elif choice == "2":
            fetch_event_details()
        elif choice == "3":
            advanced_menu()
        elif choice == "4":
            clear_screen()
            print("Exiting the program. Goodbye!\n")
            break
        else:
            clear_screen()
            print("Invalid choice. Please select a valid option.\n")

if __name__ == "__main__":
    main()
