import tkinter as tk
from tkinter import ttk

# Color palette
BG_COLOR = "#a8e6cf"
FG_COLOR = "#ff8b94"
FONT_COLOR = "#222f5b"

def open_simple_interest_window():
    new_window = tk.Toplevel(window)
    new_window.title("Simple Interest Calculator")
    new_window.geometry("400x350")
    new_window.configure(bg=BG_COLOR)

    def on_button_click():
        x_input = entry_principle.get()
        y_input = entry_interest_rate.get()
        z_input = entry_time.get()

        if x_input.isdigit() and y_input.isdigit():
            x = float(x_input)
            y = float(y_input)
            z = float(z_input)

            result = (x * y * z) / 100
            result2 = x + result

            result_label.config(text=f"Interest will be: {result}", fg=FG_COLOR)
            result_label2.config(text=f"Total amount will be: {result2}", fg=FG_COLOR)

        else:
            result_label.config(text="Invalid input. Please enter numbers.", fg=FG_COLOR)
            result_label2.config(text="Invalid input. Please enter numbers.", fg=FG_COLOR)

    label_principle = tk.Label(new_window, text="Enter the principle amount:", bg=BG_COLOR, fg=FONT_COLOR,
                               font=("Helvetica", 12, "bold"))
    label_principle.pack()

    entry_principle = tk.Entry(new_window, width=30, bg="#d2d2d2", fg=FONT_COLOR, font=("Helvetica", 12, "bold"))
    entry_principle.pack(pady=10)

    label_interest_rate = tk.Label(new_window, text="Enter the annual interest rate:", bg=BG_COLOR, fg=FONT_COLOR,
                                   font=("Helvetica", 12, "bold"))
    label_interest_rate.pack()

    entry_interest_rate = tk.Entry(new_window, width=30, bg="#d2d2d2", fg=FONT_COLOR, font=("Helvetica", 12, "bold"))
    entry_interest_rate.pack(pady=10)

    label_time = tk.Label(new_window, text="Enter the time in years:", bg=BG_COLOR, fg=FONT_COLOR,
                          font=("Helvetica", 12, "bold"))
    label_time.pack()

    entry_time = tk.Entry(new_window, width=30, bg="#d2d2d2", fg=FONT_COLOR, font=("Helvetica", 12, "bold"))
    entry_time.pack(pady=10)

    button = tk.Button(new_window, text="Calculate", command=on_button_click, bg=FONT_COLOR, fg=BG_COLOR)
    button.pack(pady=10)

    result_label = tk.Label(new_window, text="", bg=BG_COLOR, fg=FONT_COLOR, font=("Helvetica", 12, "bold"))
    result_label.pack(pady=10)

    result_label2 = tk.Label(new_window, text="", bg=BG_COLOR, fg=FONT_COLOR, font=("Helvetica", 12, "bold"))
    result_label2.pack(pady=10)

def open_compound_interest_window():
    new_window = tk.Toplevel(window)
    new_window.title("Compound Interest Calculator")
    new_window.geometry("400x350")
    new_window.configure(bg=BG_COLOR)

    def on_button_click_ci():
        p_input = (entry_principle1.get())
        r_input = (entry_interest_rate1.get())
        t_input = (entry_time1.get())

        if p_input.isdigit() and r_input.isdigit():
            p = float(p_input)
            r1 = float(r_input)
            t = float(t_input)

            r = r1 / 100

            ci1 = (p * (1 + r) ** t) - p

            ci = int(ci1)
            total_amount = ci + p

            result_label3.config(text=f"Interest will be: {ci}", fg=FG_COLOR)
            result_label4.config(text=f"Total amount will be: {total_amount}", fg=FG_COLOR)

        else:
            result_label3.config(text="Invalid input. Please enter numbers.", fg=FG_COLOR)
            result_label4.config(text="Invalid input. Please enter numbers.", fg=FG_COLOR)

    label_principle1 = tk.Label(new_window, text="Enter the principle amount:", bg=BG_COLOR, fg=FONT_COLOR,
                                font=("Helvetica", 12, "bold"))
    label_principle1.pack()

    entry_principle1 = tk.Entry(new_window, width=30, bg="#d2d2d2", fg=FONT_COLOR, font=("Helvetica", 12, "bold"))
    entry_principle1.pack(pady=10)

    label_interest_rate1 = tk.Label(new_window, text="Enter the annual interest rate:", bg=BG_COLOR, fg=FONT_COLOR,
                                    font=("Helvetica", 12, "bold"))
    label_interest_rate1.pack()

    entry_interest_rate1 = tk.Entry(new_window, width=30, bg="#d2d2d2", fg=FONT_COLOR, font=("Helvetica", 12, "bold"))
    entry_interest_rate1.pack(pady=10)

    label_time1 = tk.Label(new_window, text="Enter the time in years:", bg=BG_COLOR, fg=FONT_COLOR,
                           font=("Helvetica", 12, "bold"))
    label_time1.pack()

    entry_time1 = tk.Entry(new_window, width=30, bg="#d2d2d2", fg=FONT_COLOR, font=("Helvetica", 12, "bold"))
    entry_time1.pack(pady=10)

    button2 = tk.Button(new_window, text="Calculate", command=on_button_click_ci, bg=FONT_COLOR, fg=BG_COLOR)
    button2.pack(pady=10)

    result_label3 = tk.Label(new_window, text="", bg=BG_COLOR, fg=FONT_COLOR, font=("Helvetica", 12, "bold"))
    result_label3.pack(pady=10)

    result_label4 = tk.Label(new_window, text="", bg=BG_COLOR, fg=FONT_COLOR, font=("Helvetica", 12, "bold"))
    result_label4.pack(pady=10)

def submit_button_click():
    selected_option = dropdown.get()

    if selected_option == "Simple interest":
        open_simple_interest_window()
    elif selected_option == "Compound interest":
        open_compound_interest_window()

window = tk.Tk()
window.title("Loan Calculator")
window.geometry("400x300")
window.configure(bg=BG_COLOR)

label = tk.Label(window, text="Hello\n Welcome to the Loan Calculator", bg=BG_COLOR, fg=FONT_COLOR,
                 font=("Helvetica", 12, "bold"))
label.pack(pady=20)

options = ["Simple interest", "Compound interest"]
selected_option = tk.StringVar(value=options[0])
dropdown = ttk.Combobox(window, values=options, textvariable=selected_option)
dropdown.pack(pady=10)

button = tk.Button(window, text="Submit", bg=FONT_COLOR, fg=BG_COLOR, font=("Helvetica", 10, "bold"),
                   command=submit_button_click)
button.pack(pady=10)

window.mainloop()
