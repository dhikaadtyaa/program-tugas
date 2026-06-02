import tkinter as tk
from tkinter import messagebox, ttk
import threading
import time

# ======================================
# DFA VISUALIZER
# ======================================

class DFAVisualizer:
    def __init__(self, canvas):
        self.canvas = canvas
        self.states = []

    def create_states(self, names):

        self.canvas.delete("all")
        self.states.clear()

        x = 30

        for i, name in enumerate(names):

            circle = self.canvas.create_oval(
                x, 40,
                x + 80, 120,
                fill="#CBD5E1",
                width=3
            )

            self.canvas.create_text(
                x + 40,
                80,
                text=name,
                font=("Segoe UI", 8, "bold"),
                width=70
            )

            self.states.append(circle)

            if i < len(names) - 1:
                self.canvas.create_line(
                    x + 80,
                    80,
                    x + 120,
                    80,
                    arrow=tk.LAST,
                    width=2
                )

            x += 130

    def set_state(self, index, color):

        self.canvas.itemconfig(
            self.states[index],
            fill=color
        )

        self.canvas.update()

# ======================================
# VALIDASI
# ======================================

def validasi_npm(npm):

    langkah = []

    if len(npm) != 10:
        langkah.append("✗ NPM harus 10 digit")
        return False, langkah

    langkah.append("✓ Panjang NPM sesuai")

    if not npm.isdigit():
        langkah.append("✗ NPM hanya boleh angka")
        return False, langkah

    langkah.append("✓ Semua karakter angka")
    langkah.append("✓ NPM valid")

    return True, langkah

def validasi_email(email):

    langkah = []

    if "@" not in email:
        langkah.append("✗ Simbol @ tidak ditemukan")
        return False, langkah

    langkah.append("✓ Username ditemukan")
    langkah.append("✓ Simbol @ ditemukan")

    bagian = email.split("@")

    if len(bagian) != 2:
        langkah.append("✗ Format email salah")
        return False, langkah

    if "." not in bagian[1]:
        langkah.append("✗ Domain tidak memiliki titik")
        return False, langkah

    langkah.append("✓ Domain ditemukan")
    langkah.append("✓ Ekstensi domain ditemukan")
    langkah.append("✓ Email valid")

    return True, langkah

def validasi_hp(hp):

    langkah = []

    if not hp.startswith("08"):
        langkah.append("✗ Nomor harus diawali 08")
        return False, langkah

    langkah.append("✓ Awalan 08 sesuai")

    if len(hp) < 10:
        langkah.append("✗ Nomor terlalu pendek")
        return False, langkah

    langkah.append("✓ Panjang nomor sesuai")

    if not hp.isdigit():
        langkah.append("✗ Nomor HP hanya boleh angka")
        return False, langkah

    langkah.append("✓ Semua karakter angka")
    langkah.append("✓ Nomor HP valid")

    return True, langkah

# ======================================
# GUI
# ======================================

root = tk.Tk()
root.title("Registrasi Mahasiswa DFA")
root.geometry("1200x800")
root.configure(bg="#0F172A")

# ======================================
# HEADER
# ======================================

header = tk.Frame(
    root,
    bg="#1E293B",
    height=90
)

header.pack(fill="x")

tk.Label(
    header,
    text="🎓 SISTEM REGISTRASI MAHASISWA BERBASIS DFA",
    bg="#1E293B",
    fg="white",
    font=("Segoe UI", 22, "bold")
).pack(pady=(10,0))

tk.Label(
    header,
    text="Implementasi Deterministic Finite Automata",
    bg="#1E293B",
    fg="#CBD5E1",
    font=("Segoe UI", 10)
).pack()

# ======================================
# MAIN FRAME
# ======================================

main = tk.Frame(root, bg="#0F172A")
main.pack(fill="both", expand=True, padx=15, pady=15)

# ======================================
# PANEL KIRI
# ======================================

left = tk.Frame(
    main,
    bg="white",
    width=350
)

left.pack(side="left", fill="y", padx=(0,10))
left.pack_propagate(False)

tk.Label(
    left,
    text="FORM REGISTRASI",
    bg="white",
    fg="#2563EB",
    font=("Segoe UI",14,"bold")
).pack(pady=15)

def add_field(label):

    tk.Label(
        left,
        text=label,
        bg="white",
        font=("Segoe UI",10,"bold")
    ).pack(anchor="w", padx=15)

    e = tk.Entry(
        left,
        font=("Segoe UI",11)
    )

    e.pack(
        fill="x",
        padx=15,
        pady=5
    )

    return e

entry_nama = add_field("Nama Mahasiswa")
entry_npm = add_field("NPM")
entry_email = add_field("Email")
entry_hp = add_field("Nomor HP")

# ======================================
# PANEL KANAN
# ======================================

right = tk.Frame(
    main,
    bg="white"
)

right.pack(
    side="right",
    fill="both",
    expand=True
)

status_dfa = tk.Label(
    right,
    text="Status DFA : Menunggu Input",
    bg="white",
    fg="#2563EB",
    font=("Segoe UI",11,"bold")
)

status_dfa.pack(pady=10)

progress = ttk.Progressbar(
    right,
    length=700,
    mode="determinate"
)

progress.pack(pady=5)

canvas = tk.Canvas(
    right,
    width=850,
    height=180,
    bg="white",
    highlightthickness=0
)

canvas.pack()

visual = DFAVisualizer(canvas)

hasil = tk.Text(
    right,
    height=15,
    bg="#111827",
    fg="#E5E7EB",
    insertbackground="white",
    font=("Consolas",10)
)

hasil.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=15
)

# ======================================
# ANIMASI DFA
# ======================================

def animasi(valid):

    states = [
        "Mulai",
        "NPM",
        "Email",
        "@",
        "Domain",
        "HP",
        "Final"
    ]

    visual.create_states(states)

    progress["value"] = 0

    for i in range(len(states)):

        visual.set_state(i, "#22C55E")

        progress["value"] = (
            (i + 1) / len(states)
        ) * 100

        root.update()

        time.sleep(0.4)

    if not valid:

        visual.set_state(
            len(states)-1,
            "#EF4444"
        )

# ======================================
# PROSES
# ======================================

def proses():

    nama = entry_nama.get()

    npm_ok, npm_log = validasi_npm(
        entry_npm.get()
    )

    email_ok, email_log = validasi_email(
        entry_email.get()
    )

    hp_ok, hp_log = validasi_hp(
        entry_hp.get()
    )

    valid = (
        npm_ok and
        email_ok and
        hp_ok
    )

    threading.Thread(
        target=animasi,
        args=(valid,),
        daemon=True
    ).start()

    hasil.delete("1.0", tk.END)

    hasil.insert(
        tk.END,
        "===== HASIL VALIDASI DFA =====\n\n"
    )

    for item in npm_log:
        hasil.insert(tk.END, item + "\n")

    hasil.insert(
        tk.END,
        "\n"
    )

    for item in email_log:
        hasil.insert(tk.END, item + "\n")

    hasil.insert(
        tk.END,
        "\n"
    )

    for item in hp_log:
        hasil.insert(tk.END, item + "\n")

    hasil.insert(
        tk.END,
        "\n-----------------------------\n"
    )

    if valid:

        status_dfa.config(
            text="Status DFA : ACCEPTED ✓",
            fg="#22C55E"
        )

        hasil.insert(
            tk.END,
            f"\nMahasiswa : {nama}\n"
            "STATUS : VALID\n"
        )

        messagebox.showinfo(
            "Berhasil",
            "Registrasi berhasil!"
        )

    else:

        status_dfa.config(
            text="Status DFA : REJECTED ✗",
            fg="#EF4444"
        )

        hasil.insert(
            tk.END,
            "\nSTATUS : TIDAK VALID\n"
        )

        messagebox.showerror(
            "Gagal",
            "Data tidak valid!"
        )

def reset_form():

    for e in [
        entry_nama,
        entry_npm,
        entry_email,
        entry_hp
    ]:
        e.delete(0, tk.END)

    hasil.delete(
        "1.0",
        tk.END
    )

    canvas.delete("all")

    progress["value"] = 0

    status_dfa.config(
        text="Status DFA : Menunggu Input",
        fg="#2563EB"
    )

# ======================================
# BUTTON
# ======================================

btn_frame = tk.Frame(
    left,
    bg="white"
)

btn_frame.pack(
    pady=20
)

tk.Button(
    btn_frame,
    text="DAFTAR",
    bg="#2563EB",
    fg="white",
    width=12,
    font=("Segoe UI",11,"bold"),
    command=proses
).pack(side="left", padx=5)

tk.Button(
    btn_frame,
    text="RESET",
    bg="#EF4444",
    fg="white",
    width=12,
    font=("Segoe UI",11,"bold"),
    command=reset_form
).pack(side="left", padx=5)

root.mainloop()