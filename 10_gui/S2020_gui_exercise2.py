""" Opgave "GUI step 2":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2020.png

Genbrug din kode fra "GUI step 1".

GUI-strukturen bør være som følger:
    main window
        labelframe
            frame
                labels and entries
            frame
                buttons

Funktionalitet:
    Klik på knappen "clear entry boxes" sletter teksten i alle indtastningsfelter (entries).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import tkinter as tk

def clear_all_entries():
    entry.delete(0, tk.END)
    weight.delete(0, tk.END)
    destentry.delete(0, tk.END)
    Wentry.delete(0, tk.END)

padx = 15
pady = 5

main_window = tk.Tk()
main_window.title("my first GUI")
main_window.geometry("400x150")

# ==== labels and entries ====

lf = tk.LabelFrame(main_window, text="Container")
lf.grid(row=1, column=1, padx=padx, pady=pady)

entry_frame = tk.Frame(lf)
entry_frame.grid(row=1, column=1)

idtext = tk.Label(entry_frame, text="id")
idtext.grid(row=1, column=1, padx=padx, pady=pady)

entry = tk.Entry(entry_frame, width=3)
entry.grid(row=2, column=1, padx=padx, pady=pady)

weighttext = tk.Label(entry_frame, text="Weight")
weighttext.grid(row=1, column=2, padx=padx, pady=pady)

weight = tk.Entry(entry_frame, width=6)
weight.grid(row=2, column=2, padx=padx, pady=pady)

destinationtext = tk.Label(entry_frame, text="destination")
destinationtext.grid(row=1, column=3, padx=padx, pady=pady)

destentry = tk.Entry(entry_frame, width=12)
destentry.grid(row=2, column=3, padx=padx, pady=pady)

Weathetext = tk.Label(entry_frame, text="Weather")
Weathetext.grid(row=1, column=4, padx=padx, pady=pady)

Wentry = tk.Entry(entry_frame, width=10)
Wentry.grid(row=2, column=4, padx=padx, pady=pady)

# ==== buttons ====

button_frame = tk.Frame(lf)
button_frame.grid(row=2, column=1)

button = tk.Button(button_frame, text="Create")
button.grid(row=3, column=1, padx=padx, pady=pady)

button1 = tk.Button(button_frame, text="Update")
button1.grid(row=3, column=2, padx=padx, pady=pady)

button2 = tk.Button(button_frame, text="Delete")
button2.grid(row=3, column=3, padx=padx, pady=pady)

button3 = tk.Button(button_frame, text="Clear Entry Boxes", command=clear_all_entries)
button3.grid(row=3, column=4, padx=padx, pady=pady)

if __name__ == "__main__":
    main_window.mainloop()
