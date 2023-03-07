import tkinter as tk
import random as rd 

joueur1 = input("Entrez le nom du joueur 1 : ")
joueur2 = input("Entrez le nom du joueur 2 : ")


score = 0
starter = rd.choice((str(joueur1),str(joueur2)))
tour = starter
tour_counter = 0


'''if starter == joueur1:
    tour_counter = 0
elif starter == joueur2:
    tour_counter = 1'''



def round():
    if (tour_counter % 2 == 0):
        tour = joueur1
        label.config(text ="C'est au tour de :    " + str(tour))
    elif (tour_counter % 2 == 1):
        tour = joueur2
        label.config(text= "C'est au tour de :    " + str(tour))
    
         
    
     

grid_height, grid_width = 7, 7

taille_case_height, taille_case_width = 1080/grid_height, 1920/grid_width

plateau = [[0]*grid_width for j in range(grid_height)]
size_modif = 2
shift_x = 50
shift_y = 30

# Différentes fonctions
def affiche_cercle(event):
    """ Fonction permettant d'afficher un cercle rouge ou jaune selon la parité de la variable tour_counter """
    global cercle, tour_counter
    x = event.x
    y = event.y
    if (tour_counter % 2 == 0):
        cercle = canevas.create_oval(x,y,(x+50),(y+50),width=2,fill="yellow",outline="yellow")
        label3.config(text="Tour :      " + str(tour_counter))
    if (tour_counter % 2 == 1):
        cercle = canevas.create_oval(x,y,(x+50),(y+50),width=2,fill="red",outline="red")
        label3.config(text="Tour :      " + str(tour_counter))
    tour_counter += 1
    round()
        
    
def supprimer_cercle():
    if (tour_counter % 2 == 0):
        canevas.delete(cercle)
    if (tour_counter % 2 == 1):
        canevas.delete(cercle)
       
def deplacement1():
    for i in range(len(plateau)):
        if plateau[7][i] == 0:
            if tour == joueur1:    
                plateau[7][i] = 1
            elif tour == joueur2:
                plateau[7][i] = -1

''''def detection_cord():'''


    
    

   
# Création de la fenêtre
fenetre = tk.Tk()   
fenetre.title("Un jeu de Puissance 4")  # Titre
fenetre.geometry("1920x1080") # Dimension de la fenêtre
fenetre.state("zoomed")



# Canevas 
canevas = tk.Canvas(bg="white",width=1920,height=1080)


# Différents Labels 
label_joueur1 = tk.Label(fenetre,text=joueur1 + "  :",font=("Times New Roman","20","italic"),bg="white")
label_joueur2 = tk.Label(fenetre,text=joueur2 + "  :",font=("Times New Roman","20","italic"),bg="white")
label_score_joueur1 = tk.Label(fenetre,text= str(score),font=("Times New Roman","20","italic"),bg="white")
label_score_joueur2 = tk.Label(fenetre,text= str(score),font=("Times New Roman","20","italic"),bg="white")
label = tk.Label(fenetre, text= "C'est au tour de :    " + str(tour),bg="white",font=("Times New Roman","20"))
label3 = tk.Label(fenetre,text= "Tour :      " + str(tour_counter),bg="white",font=("Times New Roman","20"))


# Bouton pour supprimer un cercle
suppression_cercle = tk.Button(fenetre,text="Supprimer un cercle",command= supprimer_cercle,bg="red",fg="yellow",height=3,font=("Times New Roman","20","italic"))


# Création de la Grille
x = 0
y = 0
for i in range(max(grid_height,grid_width)+1):
    canevas.create_line(x/size_modif+shift_x,shift_y,x/size_modif+shift_x,1080/size_modif+shift_y,fill="blue",width=2)
    canevas.create_line(shift_x,y/size_modif+shift_y,1920/size_modif+shift_x,y/size_modif+shift_y,fill="blue",width=2)
    x += taille_case_width
    y += taille_case_height




# Placement des Widgets
label.place(x=1200,y=700)
label3.place(x=1200,y=650)
suppression_cercle.place(x=500,y=650)
label_joueur1.place(x=1200,y=100)
label_joueur2.place(x=1200,y=400)
label_score_joueur1.place(x=1300,y=100)
label_score_joueur2.place(x=1300,y=400)
canevas.grid()





canevas.bind('<Button-1>', affiche_cercle)


fenetre.mainloop()



