import tkinter as tk
from tkinter import ttk
import random

# Color code dictionary
color_code = {
    "black": (0, 1, None, 250),
    "brown": (1, 10, 1, 100),
    "red": (2, 100, 2, 50),
    "orange": (3, 1000, None, 15),
    "yellow": (4, 10000, None, 25),
    "green": (5, 100000, 0.5, 20),
    "blue": (6, 1000000, 0.25, 10),
    "violet": (7, 10000000, 0.1, 5),
    "grey": (8, 100000000, 0.05, 1),
    "white": (9, 1000000000, None, None),
    "gold": (-1, 0.1, 5, None),
    "silver": (-2, 0.01, 10, None)
}

# Function to calculate resistor value
def calculate_resistor_value(colors, num_bands):
    first_value = color_code[colors[0]][0]
    second_value = color_code[colors[1]][0]
    temp_coefficient = None
    tolerance = 20
    if num_bands == 4:
        power = color_code[colors[2]][1]
        value = (10 * first_value + second_value) * power
        tolerance = color_code[colors[3]][2]
    elif num_bands == 5:
        third_value = color_code[colors[2]][0]
        power = color_code[colors[3]][1]
        value = (100 * first_value + second_value * 10 + third_value) * power
        tolerance = color_code[colors[4]][2]
    else:
        third_value = color_code[colors[2]][0]
        power = color_code[colors[3]][1]
        value = (100 * first_value + second_value * 10 + third_value) * power
        tolerance = color_code[colors[4]][2]
        temp_coefficient = color_code[colors[5]][3]
    return value, tolerance, temp_coefficient

# Function to check game answer
def check_game_answer():
    band1_color = random_band1_color.get()
    band2_color = random_band2_color.get()
    band3_color = random_band3_color.get()
    band4_color = random_band4_color.get()
    band5_color = random_band5_color.get()
    band6_color = random_band6_color.get()

    try:
        resistor_value, tolerance, _ = calculate_resistor_value([band1_color, band2_color, band3_color, band4_color, band5_color, band6_color], 6)
        user_resistance = int(resistance_entry.get())
        user_tolerance = int(tolerance_entry.get())

        if user_resistance == resistor_value and user_tolerance == tolerance:
            result_label.configure(text="Correct answer!")
        else:
            result_label.configure(text="Wrong answer. Try again.")
    except KeyError:
        result_label.configure(text="Invalid color entered.")

# Function to generate random band colors
def generate_random_colors():
    random_band1_color.set(random.choice(list(color_code.keys())))
    random_band2_color.set(random.choice(list(color_code.keys())))
    random_band3_color.set(random.choice(list(color_code.keys())))
    random_band4_color.set(random.choice(list(color_code.keys())))
    random_band5_color.set(random.choice(list(color_code.keys())))
    random_band6_color.set(random.choice(list(color_code.keys())))

window = tk.Tk()
window.title("Resistor Color Code Calculator and Game")
window.geometry("400x400")

tab_control = ttk.Notebook(window)

# Resistance Calculator tab
calculator_tab = ttk.Frame(tab_control)
tab_control.add(calculator_tab, text="Resistance Calculator")

resistor_frame = ttk.LabelFrame(calculator_tab, text="Calculate Resistance Value")
resistor_frame.pack(padx=20, pady=20)

num_bands_label = ttk.Label(resistor_frame, text="Number of Bands:")
num_bands_label.grid(row=0, column=0, padx=5, pady=5, sticky="W")

num_bands_combo = ttk.Combobox(resistor_frame, values=[4, 5, 6], state="readonly")
num_bands_combo.grid(row=0, column=1, padx=5, pady=5)
num_bands_combo.current(0)

band1_label = ttk.Label(resistor_frame, text="Band 1 color:")
band1_label.grid(row=1, column=0, padx=5, pady=5, sticky="W")

band1_combo = ttk.Combobox(resistor_frame, values=list(color_code.keys()), state="readonly")
band1_combo.grid(row=1, column=1, padx=5, pady=5)
band1_combo.current(0)

band2_label = ttk.Label(resistor_frame, text="Band 2 color:")
band2_label.grid(row=2, column=0, padx=5, pady=5, sticky="W")

band2_combo = ttk.Combobox(resistor_frame, values=list(color_code.keys()), state="readonly")
band2_combo.grid(row=2, column=1, padx=5, pady=5)
band2_combo.current(0)

band3_label = ttk.Label(resistor_frame, text="Band 3 color:")
band3_label.grid(row=3, column=0, padx=5, pady=5, sticky="W")

band3_combo = ttk.Combobox(resistor_frame, values=list(color_code.keys()), state="readonly")
band3_combo.grid(row=3, column=1, padx=5, pady=5)
band3_combo.current(0)

band4_label = ttk.Label(resistor_frame, text="Band 4 color:")
band4_label.grid(row=4, column=0, padx=5, pady=5, sticky="W")

band4_combo = ttk.Combobox(resistor_frame, values=list(color_code.keys()), state="readonly")
band4_combo.grid(row=4, column=1, padx=5, pady=5)
band4_combo.current(0)

band5_label = ttk.Label(resistor_frame, text="Band 5 color:")
band5_label.grid(row=5, column=0, padx=5, pady=5, sticky="W")

band5_combo = ttk.Combobox(resistor_frame, values=list(color_code.keys()), state="readonly")
band5_combo.grid(row=5, column=1, padx=5, pady=5)
band5_combo.current(0)

band6_label = ttk.Label(resistor_frame, text="Band 6 color:")
band6_label.grid(row=6, column=0, padx=5, pady=5, sticky="W")

band6_combo = ttk.Combobox(resistor_frame, values=list(color_code.keys()), state="readonly")
band6_combo.grid(row=6, column=1, padx=5, pady=5)
band6_combo.current(0)

result_button = ttk.Button(resistor_frame, text="Calculate", command=lambda: calculate_resistor_value())
result_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

result_label = ttk.Label(resistor_frame, text="")
result_label.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

# Game tab
game_tab = ttk.Frame(tab_control)
tab_control.add(game_tab, text="Color Code Game")

game_frame = ttk.LabelFrame(game_tab, text="Color Code Game")
game_frame.pack(padx=20, pady=20)

random_band1_color = tk.StringVar(value="")
random_band2_color = tk.StringVar(value="")
random_band3_color = tk.StringVar(value="")
random_band4_color = tk.StringVar(value="")
random_band5_color = tk.StringVar(value="")
random_band6_color = tk.StringVar(value="")

band1_color_label = ttk.Label(game_frame, text="Band 1 color:")
band1_color_label.grid(row=0, column=0, padx=5, pady=5, sticky="W")

band1_color_entry = ttk.Entry(game_frame, textvariable=random_band1_color, state="readonly")
band1_color_entry.grid(row=0, column=1, padx=5, pady=5)

band2_color_label = ttk.Label(game_frame, text="Band 2 color:")
band2_color_label.grid(row=1, column=0, padx=5, pady=5, sticky="W")

band2_color_entry = ttk.Entry(game_frame, textvariable=random_band2_color, state="readonly")
band2_color_entry.grid(row=1, column=1, padx=5, pady=5)

band3_color_label = ttk.Label(game_frame, text="Band 3 color:")
band3_color_label.grid(row=2, column=0, padx=5, pady=5, sticky="W")

band3_color_entry = ttk.Entry(game_frame, textvariable=random_band3_color, state="readonly")
band3_color_entry.grid(row=2, column=1, padx=5, pady=5)

band4_color_label = ttk.Label(game_frame, text="Band 4 color:")
band4_color_label.grid(row=3, column=0, padx=5, pady=5, sticky="W")

band4_color_entry = ttk.Entry(game_frame, textvariable=random_band4_color, state="readonly")
band4_color_entry.grid(row=3, column=1, padx=5, pady=5)

band5_color_label = ttk.Label(game_frame, text="Band 5 color:")
band5_color_label.grid(row=4, column=0, padx=5, pady=5, sticky="W")

band5_color_entry = ttk.Entry(game_frame, textvariable=random_band5_color, state="readonly")
band5_color_entry.grid(row=4, column=1, padx=5, pady=5)

band6_color_label = ttk.Label(game_frame, text="Band 6 color:")
band6_color_label.grid(row=5, column=0, padx=5, pady=5, sticky="W")

band6_color_entry = ttk.Entry(game_frame, textvariable=random_band6_color, state="readonly")
band6_color_entry.grid(row=5, column=1, padx=5, pady=5)

random_colors_button = ttk.Button(game_frame, text="Generate Random Colors", command=generate_random_colors)
random_colors_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

resistance_label = ttk.Label(game_frame, text="Resistance:")
resistance_label.grid(row=7, column=0, padx=5, pady=5, sticky="W")

resistance_entry = ttk.Entry(game_frame)
resistance_entry.grid(row=7, column=1, padx=5, pady=5)

tolerance_label = ttk.Label(game_frame, text="Tolerance:")
tolerance_label.grid(row=8, column=0, padx=5, pady=5, sticky="W")

tolerance_entry = ttk.Entry(game_frame)
tolerance_entry.grid(row=8, column=1, padx=5, pady=5)

check_answer_button = ttk.Button(game_frame, text="Check Answer", command=check_game_answer)
check_answer_button.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

tab_control.pack(expand=1, fill="both")

window.mainloop()
