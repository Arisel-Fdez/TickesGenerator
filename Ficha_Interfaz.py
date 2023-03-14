import tkinter as tk
import string
import random


def generate_tickets():
    number_of_tickets = int(num_tickets_entry.get())
    ticket_length = int(ticket_length_entry.get())
    time_limit = time_limit_entry.get()
    profile = profile_entry.get()
    comment = comment_entry.get()
    price = price_entry.get()

    with open(f"{comment}.pdf", "w") as f:
        generator_text.insert(tk.END, "/ip hotspot user\n")
        for x in range(number_of_tickets):
            code = (''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(ticket_length)))
            doc = (f"add server=hotspot1 name={code} limit-uptime={time_limit} profile={profile} comment={comment}\n")
            a = ("---------------------------------FdezNet-Fichas---------------------------------\n")
            ficha = (f"PIN: {code} | Tiempo: {comment} | Precio: ${price} | FdezNet Residencial: XXXXXXXXXX\n")
            b = ("--------------------------------Internet-ilimitado------------------------------\n")
            f.write(a)
            f.write(ficha)
            f.write(b)

            generator_text.insert(tk.END, doc)


def copy_to_clipboard():
    data = generator_text.get("1.0", 'end-1c')
    root_clipboard = tk.Tk()
    root_clipboard.withdraw()
    root_clipboard.clipboard_clear()
    root_clipboard.clipboard_append(data)
    root_clipboard.update()
    root_clipboard.destroy()


root = tk.Tk()
root.title("Generador de Tickets")

num_tickets_label = tk.Label(root, text="Cantidad de tickets:")
num_tickets_entry = tk.Entry(root)

ticket_length_label = tk.Label(root, text="Longitud del PIN:")
ticket_length_entry = tk.Entry(root)

profile_label = tk.Label(root, text="Perfil del ticket:")
profile_entry = tk.Entry(root)

time_limit_label = tk.Label(root, text="Límite de tiempo:")
time_limit_entry = tk.Entry(root)


comment_label = tk.Label(root, text="Comentario del ticket:")
comment_entry = tk.Entry(root)

price_label = tk.Label(root, text="Precio por ticket:")
price_entry = tk.Entry(root)

generate_btn = tk.Button(root, text="Generar", command=generate_tickets)

num_tickets_label.pack()
num_tickets_entry.pack()

ticket_length_label.pack()
ticket_length_entry.pack()

time_limit_label.pack()
time_limit_entry.pack()

profile_label.pack()
profile_entry.pack()

comment_label.pack()
comment_entry.pack()

price_label.pack()
price_entry.pack()

generate_btn.pack()

generator_frame = tk.Frame(root, width=300, height=250)
generator_frame.pack_propagate(0)
generator_frame.pack(side=tk.BOTTOM)

generator_label = tk.Label(generator_frame, text="Tickets Generados:", font=('Arial Black',12))
generator_label.pack(side = tk.TOP, pady=10)

generator_scroll = tk.Scrollbar(generator_frame)
generator_scroll.pack(side = tk.RIGHT,fill=tk.Y)

generator_text = tk.Text(generator_frame, wrap=tk.WORD,width=35,height=10, yscrollcommand=generator_scroll.set)
generator_text.pack(side=tk.LEFT, padx=10)

generator_scroll.config(command=generator_text.yview)

copy_btn = tk.Button(root, text="Copiar", command=copy_to_clipboard)
copy_btn.pack(side=tk.BOTTOM)


root.mainloop()
