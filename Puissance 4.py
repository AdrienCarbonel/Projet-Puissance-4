import tkinter as tk
import random as rd 

joueur1 = input("Entrez le nom du joueur 1 : ")
joueur2 = input("Entrez le nom du joueur 2 : ")

tour_counter = 0

starter = rd.choice((str(joueur1),str(joueur2)))
tour = starter



'''if starter == joueur1:
    tour_counter = 0
elif starter == joueur2:
    tour_counter = 1'''



def round():
    if tour_counter % 2 == 0:
        tour = joueur1
        label.configure(text ="C'est au tour de" + str(tour))
        label.configure(text ="C'est au tour de" + str(tour))
    elif tour_counter % 2 == 1:
        tour = joueur2
        label(text = "C'est au tour de" + str(tour))
    
         
    
     

grid_height, grid_width = 7, 7

taille_case_height, taille_case_width = 1080/grid_height, 1920/grid_width

plateau = [[0]*grid_width for j in range(grid_height)]
size_modif = 2
shift_x = 50
shift_y = 30

# Différentes fonctions
def afficher_cercle_jaune(event):
        """Fonction permettant d'afficher un cercle jaune"""
        global cercle_jaune, tour_counter
        x, y = event.x, event.y
        cercle_jaune = canevas.create_oval(x,y,(x+50),(y+50),fill="yellow",width=2, outline="yellow")
        tour_counter += 1
        label3.config(text= "tours  :" + str(tour_counter))
        if tour_counter % 2 == 0:
            tour = joueur1
            label.config(text ="C'est au tour de : " + str(tour))
        if tour_counter % 2 == 1:
            tour = joueur2
            label.config(text = "C'est au tour de : " + str(tour))

        
    

def afficher_cercle_rouge(event):
    """Fonction permettant d'afficher un cercle rouge"""
    global cercle_rouge, tour_counter
    x, y = event.x, event.y
    cercle_rouge = canevas.create_oval(x,y,(x+50),(y+50),fill="red",width=2, outline="red")
    tour_counter += 1
    label3.config(text= "tours  :" + str(tour_counter))
    if tour_counter % 2 == 0:
        tour = joueur1
        label.config(text ="C'est au tour de : " + str(tour))
    if tour_counter % 2 == 1:
        tour = joueur2
        label.config(text = "C'est au tour de : " + str(tour))


    
    
def annuler_cercle_rouge():
    canevas.delete(cercle_rouge)


def annuler_cercle_jaune():
    canevas.delete(cercle_jaune)

       
def deplacement1():
    for i in range(len(plateau)):
        if plateau[7][i] == 0:
            if tour == joueur1:    
                plateau[7][i] = 1
            elif tour == joueur2:
                plateau[7][i] = -1

''''def detection_cord():'''

def update(event):
    global tour_counter
    tour_counter += 1
    
    

   
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
label = tk.Label(fenetre, text= "C'est au tour de : " + str(tour))
label3 = tk.Label(text= "Tour : " + str(tour_counter))


# Boutons
bouton = tk.Button(fenetre,text="Supprimer un cercle rouge",bg="blue",fg="yellow",font=("helvetica","20","italic"),command=annuler_cercle_rouge)
bouton2 = tk.Button(fenetre,text="Supprimer un cercle jaune",bg="blue",fg="yellow",font=("helvetica","20","italic"),command= annuler_cercle_jaune)


# Création de la Grille
x = 0
y = 0
for i in range(max(grid_height,grid_width)+1):
    canevas.create_line(x/size_modif+shift_x,shift_y,x/size_modif+shift_x,1080/size_modif+shift_y,fill="blue",width=2)
    canevas.create_line(shift_x,y/size_modif+shift_y,1920/size_modif+shift_x,y/size_modif+shift_y,fill="blue",width=2)
    x += taille_case_width
    y += taille_case_height




# Placement des Widgets
bouton2.grid()
bouton.grid()
canevas.grid()

label.place(x= 800, y= 800)
label3.place(x= 500, y= 800)



canevas.bind('<Button-1>', afficher_cercle_jaune)
canevas.bind('<Button-3>', afficher_cercle_rouge)

fenetre.mainloop()



