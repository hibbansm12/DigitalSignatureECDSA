import customtkinter as ctk
from tkinter import filedialog, messagebox
from digital_signature import DigitalSignature

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Aplikasi Digital Signature dengan ECDSA")
        self.geometry("600x400")

        self.ds = DigitalSignature()

        # Membuat judul aplikasi
        self.title_label = ctk.CTkLabel(self, text="Aplikasi Digital Signature", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=10)

        # Membuat deskripsi aplikasi
        self.description_label = ctk.CTkLabel(self, text="Gunakan aplikasi ini untuk membuat dan memverifikasi tanda tangan digital menggunakan ECDSA.", wraplength=500, justify="center")
        self.description_label.pack(pady=10)

        # Tombol untuk menghasilkan kunci
        self.generate_keys_button = ctk.CTkButton(self, text="Generate Keys", command=self.generate_keys)
        self.generate_keys_button.pack(pady=10)

        # Tombol untuk menandatangani file
        self.sign_file_button = ctk.CTkButton(self, text="Sign File", command=self.sign_file)
        self.sign_file_button.pack(pady=10)

        # Label untuk menampilkan nama file yang dipilih
        self.file_label = ctk.CTkLabel(self, text="File yang dipilih: Tidak ada", anchor="w")
        self.file_label.pack(pady=5, fill="x", padx=20)

        # Tombol untuk memverifikasi tanda tangan
        self.verify_signature_button = ctk.CTkButton(self, text="Verify Signature", command=self.verify_signature)
        self.verify_signature_button.pack(pady=10)

        # Label instruksi
        self.instructions_label = ctk.CTkLabel(self, text="Instruksi:\n1. Generate keys\n2. Sign a file\n3. Verify a file signature", justify="left")
        self.instructions_label.pack(pady=20, fill="x", padx=20)

    def generate_keys(self):
        result = self.ds.generate_keys()
        messagebox.showinfo("Sukses", result)

    def sign_file(self):
        file_path = filedialog.askopenfilename(title="Pilih file untuk ditandatangani")
        if not file_path:
            return
        
        self.file_label.configure(text=f"File yang dipilih: {file_path}")

        result = self.ds.sign_file(file_path)
        messagebox.showinfo("Sukses", result)

    def verify_signature(self):
        file_path = filedialog.askopenfilename(title="Pilih file untuk diverifikasi")
        if not file_path:
            return

        self.file_label.configure(text=f"File yang dipilih: {file_path}")

        result = self.ds.verify_signature(file_path)
        messagebox.showinfo("Hasil Verifikasi", result)

# Menjalankan aplikasi
if __name__ == "__main__":
    app = App()
    app.mainloop()
