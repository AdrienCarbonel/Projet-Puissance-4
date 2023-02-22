import tkinter as tk
import random as rd 

joueur1 = input("Entrez le nom du joueur 1 :  ")
joueur2 = input("Entrez le nom du joueur 2 : ")




""" Partie Graphique du Puissance 4 """


grid_height, grid_width = 7, 7

taille_case_height, taille_case_width = 1080/grid_height, 1920/grid_width

plateau = [[0]*grid_width for j in range(grid_height)]
size_modif = 2
shift_x = 50
shift_y = 30

# Différentes fonctions
def afficher_cercle_jaune(event):
        """Fonction permettant d'afficher un cercle jaune"""
        x, y = event.x, event.y
        canevas.create_oval(x,y,(x+50),(y+50),fill="yellow",width=2, outline="yellow")
        
    
    

def afficher_cercle_rouge(event):
    """Fonction permettant d'afficher un cercle rouge"""
    x, y = event.x, event.y
    canevas.create_oval(x,y,(x+50),(y+50),fill="red",width=2, outline="red")
    
    



    
       
        
def annuler_coup():
    "Fonction qui permet d'annuler le coup précédemment joué"
    i = 0
    if afficher_cercle_rouge:
       canevas.delete(canevas.create_oval(x,y,(x+50),(y+50),fill="red",width=2, outline="red"))
    elif afficher_cercle_jaune:
       canevas.delete(canevas.create_oval(x,y,(x+50),(y+50),fill="yellow",width=2, outline="yellow"))

    

   
# Création de la fenêtre
fenetre = tk.Tk()   
fenetre.title("Un jeu de Puissance 4")  # Titre
fenetre.geometry("1920x1080") # Dimension de la fenêtre




# Canevas 
canevas = tk.Canvas(bg="white",width=1920,height=1080)

canevas.create_text(1200,100,text=joueur1 + "  :",font=("Times New Roman","20","italic"))
canevas.create_text(1200,400,text=joueur2 + "  :",font=("Times New Roman","20","italic"))
canevas.create_text(1300,100,text="0",font=("Times New Roman","20","italic"))
canevas.create_text(1300,400,text="0",font=("Times New Roman","20","italic"))


# Boutons
bouton = tk.Button(fenetre,text="Annuler le coup",bg="blue",fg="yellow",font=("helvetica","20","italic"),command=annuler_coup)


# Création de la Grille
x = 0
y = 0
for i in range(max(grid_height,grid_width)+1):
    canevas.create_line(x/size_modif+shift_x,shift_y,x/size_modif+shift_x,1080/size_modif+shift_y,fill="blue",width=2)
    canevas.create_line(shift_x,y/size_modif+shift_y,1920/size_modif+shift_x,y/size_modif+shift_y,fill="blue",width=2)
    x += taille_case_width
    y += taille_case_height




# Placement des Widgets
bouton.grid()
canevas.grid()


canevas.bind('<Button-3>', afficher_cercle_rouge)
canevas.bind('<Button-1>', afficher_cercle_jaune)


fenetre.mainloop()

""" Partie Logique du Puissance 4 """






