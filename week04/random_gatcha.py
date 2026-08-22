import random

import tkinter as tk

def random_gatcha():

	number = random.randint(0, 1)
	if number == 0:
		result = "Na Yeonsu"
	elif number == 1:
		result = "Song Hyunsuk"
	result_label.config(text=f"{result}")

window = tk.Tk()

window.title("Random Gatcha")

window.geometry("400x300")

title_label = tk.Label(window, text="Random Gatcha", font=("Arial", 20))

title_label.pack(pady=30)

result_label = tk.Label(window, text="?", font=("Arial", 40))
result_label.pack(pady=20)

pick_button = tk.Button(window, text="Random Gatcha", font=("Arial", 15), command = random_gatcha)
pick_button.pack(pady=20)

window.mainloop()
