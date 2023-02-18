import tkinter as tk

# Différentes fonctions


def afficher_cercle(event):
        canevas.create_oval((),fill= "blue")
# Création de la fenêtre

fenetre = tk.Tk()
fenetre.title("Un jeu de Puissance 4")
fenetre.geometry("1920x1080")
# Canevas

canevas = tk.Canvas(bg="white",width=1920,height=1080)
# Placement des widgets
canevas.grid()
canevas.bind('<Button-1>', afficher_cercle)
fenetre.mainloop()


