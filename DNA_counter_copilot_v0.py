import tkinter as tk
from tkinter import filedialog

def DNA_count(text):
    A = 0
    T = 0
    G = 0
    C = 0
    for i in text:
        if i == "A":
            A += 1
        elif i == "T":
            T += 1
        elif i == "G":
            G += 1
        elif i == "C":
            C += 1
        else:
            pass
    return A, T, G, C

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("FASTA files", "*.fasta"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            # Skip the first line if it is a header (starts with '>')
            lines = file.readlines()
            if lines[0].startswith('>'):
                lines = lines[1:]
            text = ''.join(lines).replace('\n', '')
            label.config(text="A: %s T: %s G: %s C: %s" % DNA_count(text))

window = tk.Tk()
window.title("DNA Base Counter")

button_open = tk.Button(window, text="Open FASTA File", command=open_file)
button_open.pack()

label = tk.Label(window, text="A: 0 T: 0 G: 0 C: 0")
label.pack()

window.mainloop()
