import tkinter as tk

# Différentes fonctions


def afficher_cercle_jaune(event):
        """Fonction permettant d'afficher un cercle jaune"""
        x, y = event.x, event.y
        canevas.create_oval(x,y,(x+50),(y+50),fill="yellow",width=2, outline="yellow")
    

def afficher_cercle_rouge(event):
    """Fonction permettant d'afficher un cercle rouge"""
    x, y = event.x, event.y
    canevas.create_oval(x,y,(x+50),(y+50),fill="red",width=2, outline="red")
# Création de la fenêtre

fenetre = tk.Tk()  # Création de la fenêtre 
fenetre.title("Un jeu de Puissance 4")  #Titre
fenetre.geometry("1920x1080") # Dimension de la fenêtre
# Canevas

canevas = tk.Canvas(bg="white",width=1920,height=1080)
# Placement des widgets

canevas.grid()
canevas.bind('<Button-3>', afficher_cercle_rouge)
canevas.bind('<Button-1>', afficher_cercle_jaune)





fenetre.mainloop() #Boucle Principale


