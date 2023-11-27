"""
Opgave "GUI step 1":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2010.png

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import tkinter as tk

padx = 15
pady = 5

main_window = tk.Tk()
main_window.title("my first GUI")
main_window.geometry("400x150")

lf = tk.LabelFrame(main_window, text="Container")
lf.grid(row=1, column=1, padx=padx, pady=pady)

idtext = tk.Label(lf, text="id")
idtext.grid(row=1, column=1, padx=padx, pady=pady)

entry = tk.Entry(lf, width=3)
entry.grid(row=2, column=1, padx=padx, pady=pady)

button = tk.Button(lf, text="Create")
button.grid(row=3, column=1, padx=padx, pady=pady)

if __name__ == "__main__":
    main_window.mainloop()
