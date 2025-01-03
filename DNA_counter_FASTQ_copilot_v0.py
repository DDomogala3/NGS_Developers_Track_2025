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
    file_path = filedialog.askopenfilename(filetypes=[("FASTQ files", "*.fastq"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            sequences = []
            while True:
                header = file.readline().strip()  # Read the header line (starts with '@')
                if not header:
                    break  # End of file
                sequence = file.readline().strip()  # Read the sequence line
                file.readline()  # Skip the '+' line
                file.readline().strip()  # Skip the quality score line
                
                sequences.append(sequence)
            # Join all sequences into one string for counting
            text = ''.join(sequences)
            label.config(text="A: %s T: %s G: %s C: %s" % DNA_count(text))

window = tk.Tk()
window.title("DNA Base Counter")

button_open = tk.Button(window, text="Open FASTQ File", command=open_file)
button_open.pack()

label = tk.Label(window, text="A: 0 T: 0 G: 0 C: 0")
label.pack()

window.mainloop()
