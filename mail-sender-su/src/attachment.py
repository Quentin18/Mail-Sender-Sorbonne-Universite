"""
Mail sender Sorbonne Université
Gestion des pièces jointes
Quentin Deschamps, 2020
"""
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename


class Attachment:
    """Gestion des pièces jointes"""
    def __init__(self, fenetre):
        self.list_attachment = []
        self.fenetre = fenetre
        self.button_frame = ttk.Frame(self.fenetre)
        self.button_attachment = ttk.Button(self.button_frame,
                                            text="Joindre un fichier",
                                            command=self.open_file)
        self.button_attachment.grid(row=0, column=0)
        self.button_delete = ttk.Button(self.button_frame,
                                        text="Supprimer",
                                        command=self.delete_file)
        self.button_delete.grid(row=0, column=1)
        self.button_delete.config(state=tk.DISABLED)
        self.button_frame.grid(row=2, padx=5, pady=5)
        self.listbox_attachment = tk.Listbox(self.fenetre, height=4, width=50)
        self.listbox_attachment.grid(row=3)

    def open_file(self):
        """Ajoute une pièce jointe"""
        filename = askopenfilename(title="Ouvrir le fichier")
        if filename:
            self.list_attachment.append(filename)
            self.listbox_attachment.insert(tk.END, filename.split("/")[-1])
            self.button_delete.config(state=tk.NORMAL)

    def delete_file(self):
        """Supprime une pièce jointe"""
        filename = self.listbox_attachment.get(tk.ACTIVE)
        # if not filename:
        #     filename = self.list_attachment[-1]
        index = self.listbox_attachment.get(0, tk.END).index(filename)
        self.list_attachment.pop(index)
        self.listbox_attachment.delete(index)
        if self.list_attachment == []:
            self.button_delete.config(state=tk.DISABLED)
