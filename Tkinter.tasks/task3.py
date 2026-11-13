import tkinter as tk

root = tk.Tk()
root.title("Кнопка и обработчик")
root.geometry("400x250")

def change_text():
    label.config(text="Задание выполнено!")

label = tk.Label(
    root,
    text="Нажмите кнопку",
    font=("Arial", 16)
)
label.pack(pady=30)

button = tk.Button(
    root,
    text="Выполнить",
    command=change_text,
    font=("Arial", 12)
)
button.pack(pady=10)

root.mainloop()
