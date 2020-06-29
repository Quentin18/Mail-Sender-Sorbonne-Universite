"""
The ``attachments`` module manages attachments.
It uses the ``askopenfilenames`` function from the
``tkinter.filedialog`` module.

.. module:: attachments
    :synopsis: Manage attachments.

.. moduleauthor:: Quentin Deschamps <quentindeschamps18@gmail.com>

"""
import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilenames


class Attachments:
    """Manage attachments."""
    def __init__(self, window, button_frame):
        self.attachments = []
        self.window = window
        self.button_frame = button_frame

        # Listbox
        self.frame_listbox = ttk.Frame(self.window)
        self.label_listbox = ttk.Label(self.frame_listbox,
                                       text='Pièces jointes')
        self.listbox_attachments = tk.Listbox(self.frame_listbox,
                                              height=2, width=60)
        self.label_listbox.grid(row=0)
        self.listbox_attachments.grid(row=1)
        self.frame_listbox.grid(row=4, padx=10, pady=10)

        # Button
        self.button_attachments = ttk.Button(self.button_frame,
                                             text='Joindre un fichier',
                                             command=self.attach_files)
        self.button_attachments.grid(row=0, column=1, padx=5, pady=5)
        self.button_delete = ttk.Button(self.button_frame,
                                        text='Supprimer',
                                        command=self.delete_file)
        self.button_delete.grid(row=0, column=2, padx=5, pady=5)
        self.button_delete.config(state=tk.DISABLED)

    def attach_files(self):
        """Add attachments."""
        attachments = askopenfilenames(
            initialdir='.', title='Joindre les fichiers',
            filetypes=[
                ('all files', '.*'),
                ('pdf files', '.pdf'),
                ('zip files', '.zip'),
                ('png files', '.png')
            ]
        )
        for filename in attachments:
            if filename not in self.attachments:
                self.attachments.append(filename)
                self.listbox_attachments.insert(
                    tk.END, os.path.basename(filename))
                self.button_delete.config(state=tk.NORMAL)

    def delete_file(self):
        """Delete attachments."""
        filename = self.listbox_attachments.get(tk.ACTIVE)
        index = self.listbox_attachments.get(0, tk.END).index(filename)
        self.attachments.pop(index)
        self.listbox_attachments.delete(index)
        if self.attachments == []:
            self.button_delete.config(state=tk.DISABLED)
