import tkinter as tk

root = tk.Tk()
root.title("Информация")
root.geometry("500x300")

title = tk.Label(
    root,
    text="Информационная карточка",
    font=("Arial", 18, "bold"),
    fg="blue"
)
title.pack(pady=20)

name = tk.Label(
    root,
    text="ФИО: Асылбекова Гульвира",
    font=("Arial", 14),
    fg="black"
)
name.pack(pady=10)

group = tk.Label(
    root,
    text="Группа: 3ПО-324",
    font=("Arial", 14),
    fg="green"
)
group.pack(pady=10)

subject = tk.Label(
    root,
    text="Дисциплина: Программное обеспечение",
    font=("Arial", 14),
    fg="purple"
)
subject.pack(pady=10)

root.mainloop()
