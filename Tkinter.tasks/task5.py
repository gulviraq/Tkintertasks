import tkinter as tk

root = tk.Tk()
root.title("Форма ввода данных")
root.geometry("450x300")

def show_data():
    name = entry_name.get()
    age = entry_age.get()

    if name == "" or age == "":
        result.config(text="Заполните все поля!", fg="red")
    else:
        result.config(
            text=f"{name}, вам {age} лет",
            fg="green"
        )

def clear_form():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    result.config(text="")
    entry_name.focus_set()

tk.Label(root, text="Имя:").grid(row=0, column=0, padx=10, pady=10)

entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Возраст:").grid(row=1, column=0, padx=10, pady=10)

entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1, padx=10, pady=10)

tk.Button(
    root,
    text="Показать данные",
    command=show_data
).grid(row=2, column=0, pady=15)

tk.Button(
    root,
    text="Очистить",
    command=clear_form
).grid(row=2, column=1, pady=15)

result = tk.Label(root, text="", font=("Arial", 12))
result.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
