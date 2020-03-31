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
        self.button_frame.grid(row=2)
        self.frame_attachment = ttk.Frame(self.fenetre)
        self.frame_attachment.grid(row=3)

    def open_file(self):
        """Ajoute une pièce jointe"""
        filename = askopenfilename(title="Ouvrir le fichier")
        if filename:
            self.list_attachment.append(filename)
            self.maj_frame_attachment()

    def delete_file(self):
        """Supprime une pièce jointe"""
        if self.list_attachment != []:
            self.list_attachment.pop()
            self.maj_frame_attachment()
        if self.list_attachment == []:
            self.button_delete.config(state=tk.DISABLED)

    def maj_frame_attachment(self):
        """Met à jour le frame des pièces jointes"""
        self.frame_attachment.destroy()
        self.frame_attachment = ttk.Frame(self.fenetre)
        for filename in self.list_attachment:
            ttk.Label(self.frame_attachment,
                      text=filename.split("/")[-1]).pack()
        self.frame_attachment.grid(row=3)
        self.button_delete.config(state=tk.NORMAL)
