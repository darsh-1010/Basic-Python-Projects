import random
import tkinter as tk
from tkinter import ttk, messagebox

class IRCTCApp:
    def __init__(self, root):
        self.root = root
        self.root.title("IRCTC Ticket Booking")
        self.root.geometry("600x500")
        self.root.configure(bg="#f7f5e6")

        self.create_widgets()

    def create_widgets(self):
        # Header
        header_label = tk.Label(self.root, text="Welcome to the IRCTC", bg="#f7f5e6", fg="#52658f",
                                font=("Arial", 16, "bold"))
        header_label.pack(pady=20)

        # Menu Options
        menu_label = tk.Label(self.root, text="Select an option:", bg="#f7f5e6", fg="#333a56", font=("Arial", 12))
        menu_label.pack()

        options = ["Schedule", "Book Tickets"]
        self.selected_option = tk.StringVar(value=options[0])
        dropdown = ttk.Combobox(self.root, values=options, textvariable=self.selected_option)
        dropdown.pack(pady=10)

        submit_button = tk.Button(self.root, text="Submit", bg="#333a56", fg="#f7f5e6", font=("Arial", 10, "bold"),
                                  command=self.handle_submission)
        submit_button.pack(pady=10)

    def handle_submission(self):
        selected_option = self.selected_option.get()

        if selected_option == "Schedule":
            self.show_schedule()
        elif selected_option == "Book Tickets":
            self.open_book_tickets_window()

    def show_schedule(self):
        schedule_window = tk.Toplevel(self.root)
        schedule_window.title("Train Schedule")
        schedule_window.geometry("500x400")
        schedule_window.configure(bg="#e8e8e8")

        schedule_label = tk.Label(schedule_window, text="Train Schedule", bg="#e8e8e8", fg="#333a56",
                                  font=("Arial", 14, "bold"))
        schedule_label.pack(pady=10)

        # Train schedule details
        schedule_text = "From\tTo\tTime\t    Train\t          Duration\n" \
                        "Baroda\tAjmer\t1PM-8PM\t   BR-AJ-SL\t     8 Hours\n" \
                        "Patna\tDelhi\t9PM-11AM\t PA-DL-AC\t   14 Hours\n" \
                        "Mumbai\tBhuj\t10AM-8PM\t MU-BH-SF\t  10 Hours\n" \
                        "Ajmer\tDelhi\t6AM-10AM\t AL-DE-Gl\t      4 Hours\n" \
                        "Patna\tOrissa\t1AM-11PM\t PA-OR-AC1\t11 Hours\n" \
                        "Ajmer\tPatna\t6AM-11PM\t AJ-PA-RC\t   17 Hours"

        schedule_text_widget = tk.Text(schedule_window, wrap="word", height=10, width=50, font=("Arial", 10))
        schedule_text_widget.insert("1.0", schedule_text)
        schedule_text_widget.config(state="disabled")
        schedule_text_widget.pack(pady=10)

        submit_button = tk.Button(schedule_window, text="Submit", bg="#333a56", fg="#f7f5e6",
                                  font=("Arial", 10, "bold"),
                                  command=lambda: schedule_window.destroy())
        submit_button.pack(pady=10)

    def open_book_tickets_window(self):
        book_tickets_window = tk.Toplevel(self.root)
        book_tickets_window.title("Book Tickets")
        book_tickets_window.geometry("600x500")
        book_tickets_window.configure(bg="#433f3f")

        ticket_booking_app = TicketBookingApp(book_tickets_window)

class TicketBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Trains window ")
        self.root.geometry("600x750")
        self.root.configure(bg="#f7f5e6")

        self.train_var = tk.StringVar()
        self.class_var = tk.StringVar()

        self.create_new_widgets()

    def create_new_widgets(self):
        # Header
        header_label = tk.Label(self.root, text="Book Tickets", bg="#f7f5e6", fg="#52658f",
                                font=("Arial", 16, "bold"))
        header_label.pack(pady=20)

        # Ticket Booking Form
        self.source_label = tk.Label(self.root, text="Source Station:", bg="#f7f5e6", font=("Arial", 12))
        self.source_label.pack()
        self.source_entry = tk.Entry(self.root)
        self.source_entry.pack(pady=5)

        self.destination_label = tk.Label(self.root, text="Destination:", bg="#f7f5e6", font=("Arial", 12))
        self.destination_label.pack()
        self.destination_entry = tk.Entry(self.root)
        self.destination_entry.pack(pady=5)

        self.passenger_label = tk.Label(self.root, text="Number of Passengers:", bg="#f7f5e6", font=("Arial", 12))
        self.passenger_label.pack()
        self.passenger_entry = tk.Entry(self.root)
        self.passenger_entry.pack(pady=5)

        self.full_name_label = tk.Label(self.root, text="Full name of a passenger (one only):", bg="#f7f5e6", font=("Arial", 12))
        self.full_name_label.pack()
        self.full_name_entry = tk.Entry(self.root)
        self.full_name_entry.pack(pady=5)

        self.age_label = tk.Label(self.root, text="Enter your age", bg="#f7f5e6", font=("Arial", 12))
        self.age_label.pack()
        self.age_entry = tk.Entry(self.root)
        self.age_entry.pack(pady=5)

        self.phone_label = tk.Label(self.root, text="Phone number (One only)", bg="#f7f5e6", font=("Arial", 12))
        self.phone_label.pack()
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.pack(pady=5)

        self.email_label = tk.Label(self.root, text="Email Address:", bg="#f7f5e6", font=("Arial", 12))
        self.email_label.pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack(pady=5)

        self.aadhar_label = tk.Label(self.root, text="Enter Aadhar card number ", bg="#f7f5e6", font=("Arial", 12))
        self.aadhar_label.pack()
        self.aadhar_entry = tk.Entry(self.root)
        self.aadhar_entry.pack(pady=5)

        self.date_label = tk.Label(self.root, text="Travel Date (DD-MM-YYYY):", bg="#f7f5e6", font=("Arial", 12))
        self.date_label.pack()
        self.date_entry = tk.Entry(self.root)
        self.date_entry.pack(pady=5)

        # Dropdowns for Train and Class options
        self.create_dropdown("Select Train", ["Baroda-Ajmer", "Patna-Delhi", "Mumbai-Bhuj", "Ajmer-Delhi", "Patna-Orissa", "Ajmer-Patna"], self.train_var)
        self.create_dropdown("Select Class", ["Generel", "Sleeper", "AC-2 TIER", "AC-1 TIER", "LUXURY"], self.class_var)

        self.book_button = tk.Button(self.root, text="Book Tickets", bg="#333a56", fg="#f7f5e6",
                                      font=("Arial", 10, "bold"), command=self.book_tickets)
        self.book_button.pack(pady=10)

    def create_dropdown(self, label_text, options, variable):
        label = tk.Label(self.root, text=label_text, bg="#f7f5e6", font=("Arial", 12))
        label.pack()
        dropdown = ttk.Combobox(self.root, values=options, textvariable=variable)
        dropdown.pack(pady=5)

    def book_tickets(self):
        source = self.source_entry.get()
        destination = self.destination_entry.get()
        num_passengers = self.passenger_entry.get()
        full_name = self.full_name_entry.get()
        age =self.age_entry.get()
        phone_number =self.phone_entry.get()
        email = self.email_entry.get()
        aadhar = self.aadhar_entry.get()
        date = self.date_entry.get()
        travel_date = self.date_entry.get()
        selected_train = self.train_var.get()
        selected_class = self.class_var.get()
        pnr_number = random.randint(1000000000, 9999999999)
        trip_code = random.randint(1, 99)

        train_options = {
            'Baroda-Ajmer': 680,
            'Patna-Delhi': 1350,
            'Mumbai-Bhuj': 980,
            'Ajmer-Delhi': 860,
            'Patna-Orissa': 1520,
            'Ajmer-Patna': 1800
        }

        class_options = {
            'Generel': 200,
            'Sleeper': 300,
            'AC-2 TIER': 600,
            'AC-1 TIER': 900,
            'LUXURY': 1500
        }

        basic_fare = train_options[selected_train] + class_options[selected_class]
        total_fare = basic_fare * int(num_passengers)

        ticket_info = (
            f"____________________E-TICKET____________________\n"
            f"PNR NUMBER: {pnr_number}\n"
            f"DATE: {date}\n"
            f"TRIP CODE: c{trip_code}\n"
            f"TRAIN: {selected_train}\n"
            f"CLASS: {selected_class}\n"
            f"JOURNEY FROM: {source}\n"
            f"JOURNEY TO: {destination}\n"
            f"No of Passengers: {num_passengers}\n"
            f"Full name of a passenger (one only): {full_name}\n"
            f"Phone no: {phone_number}\n"
            f"AGE: {age}\n"
            f"Aadhar NO: {aadhar}\n"
            f"EMAIL-ID: {email}\n"
            f"The Amount successfully paid is: {total_fare}/-\n"
            f"*************************NOTE*****************************\n"
            f"Trip code can be used to get seat number(s) at the source station.\n"
            f"It will also be forwarded to the registered email after the final chart\n"
            f"Thank you for choosing IRCTC"
        )

        messagebox.showinfo(
            "Payment Success",
            f"The payment is successful RS {total_fare}/-. Your Ticket is Printed Below"
        )

        try:
            num_passengers = self.passenger_entry.get()
        except ValueError:
            messagebox.showerror("Error", "Number of passengers must be an integer.")
            return

        if not all([source, destination, email, travel_date, selected_train, selected_class]):
            messagebox.showerror("Error", "Please fill in all the required fields.")
            return


        self.show_ticket_window(ticket_info)

    def show_ticket_window(self, ticket_info):
        ticket_window = tk.Toplevel(self.root)
        ticket_window.geometry("500x600")
        tk.Label(ticket_window, text="Ticket Information", font=("Helvetica", 16, "bold")).pack(pady=10)
        ticket_text = tk.Text(ticket_window, height=20, width=60)
        ticket_text.pack(padx=20, pady=10)
        ticket_text.insert(tk.END, ticket_info)
        ticket_text.config(state=tk.DISABLED)  # Disable text editing

if __name__ == "__main__":
    root = tk.Tk()
    app = IRCTCApp(root)
    root.mainloop()
