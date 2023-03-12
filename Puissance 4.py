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


    
         
    
     

grid_height, grid_width = 7, 7

taille_case_height, taille_case_width = 1080/grid_height, 1920/grid_width

plateau = [[0]*grid_width for j in range(grid_height)]
size_modif = 2
shift_x = 50
shift_y = 30

# Différentes fonctions

def coordonnees(event):
    print("J'ai cliqué aux coordonnées    :",event.x,event.y)

    


def deplacement():
    canevas.move(cercle,0,3.10*taille_case_height-0.75*taille_case_height)
    fenetre.after(200000000000000000,deplacement)

def round():
    global tour_counter
    """ Fonction qui détermine si c'est le tour du joueur 1 ou celui de joueur 2 selon la parité de la variable tour_counter """
    if (tour_counter % 2 == 0):
        tour_counter += 1
        tour = joueur1
        label.config(text ="C'est au tour de :    " + str(tour))
    elif (tour_counter % 2 == 1):
        tour_counter += 1
        tour = joueur2
        label.config(text= "C'est au tour de :    " + str(tour))
        




def affiche_cercle(event):
    """ Fonction permettant d'afficher un cercle rouge ou jaune selon la parité de la variable tour_counter """
    global cercle, tour_counter, x1, y1
    x1 = event.x
    y1 = event.y
    if (tour_counter % 2 == 0):
        cercle = canevas.create_oval(x1,y1,(x1+50),(y1+50),width=2,fill="yellow",outline="yellow")
        label3.config(text="Tour :      " + str(tour_counter))
        print(canevas.coords(cercle))
    elif (tour_counter % 2 == 1):
        cercle = canevas.create_oval(x1,y1,(x1+50),(y1+50),width=2,fill="red",outline="red")
        label3.config(text="Tour :      " + str(tour_counter))
        print(canevas.coords(cercle))
    deplacement()
    placement_cercle()
    round()
    
    
        
    
def supprimer_cercle():
    """ Fonction permettant de supprimer le dernier cercle qui a été créé """
    global tour_counter
    if (tour_counter % 2 == 0):
        if (tour == joueur1):
            canevas.delete(cercle)
            tour_counter -= 1
            label.config(text= "C'est au tour de :    " + str(tour))
    if (tour_counter % 2 == 1):
        canevas.delete(cercle)
        tour_counter -= 1
        label.config(text= "C'est au tour de :    " + str(tour))
        

    

def update():
    global tour_counter
    if supprimer_cercle() == True:
        tour_counter -= 1
        label.config(text= "C'est au tour de :    " + str(tour))

def placement_cercle():
    """ Fonction permettant de placer un 1 ou -1 ( selon si le cercle est rouge ou jaune ) à l'indice i,j de plateau """
    if (52 <= canevas.coords(cercle)[2] <= 185) and (492 <= canevas.coords(cercle)[3] <= 569) and (tour_counter % 2 == 0):
        plateau[6][0] = 1
    elif (52 <= canevas.coords(cercle)[2] <= 185) and (492 <= canevas.coords(cercle)[3] <= 569) and (tour_counter % 2 == 1):
        plateau[6][0] = -1
    elif (187 <= canevas.coords(cercle)[2] <= 324) and (492 <= canevas.coords(cercle)[3] <= 569) and (tour_counter % 2 == 0):
        plateau[6][1] = 1
    elif (187 <= canevas.coords(cercle)[2] <= 324) and (493 <= canevas.coords(cercle)[3] <= 569) and (tour_counter % 2 == 1):
        plateau[6][1] = -1
    elif (326 <= canevas.coords(cercle)[2] <= 460) and (493 <= canevas.coords(cercle)[3] <= 569) and (tour_counter % 2 == 0):
        plateau[6][2] = 1
    elif (326 <= canevas.coords(cercle)[2] <= 460) and (493 <= canevas.coords(cercle)[3] <= 569) and (tour_counter % 2 == 1):
        plateau[6][2] = -1
    elif (461 <= canevas.coords(cercle)[2] <= 596) and (493 <= canevas.coords(cercle)[3] <= 569) and (tour_counter % 2 == 0):
        plateau[6][3] = 1
    elif (461 <= canevas.coords(cercle)[2] <= 596) and (493 <= canevas.coords(cercle)[3] <= 569) and (tour_counter % 2 == 1):
        plateau[6][3] = -1
    elif (599 <= canevas.coords(cercle)[2] <= 734) and (493 <= canevas.coords(cercle)[3] <= 569) and (tour_counter % 2 == 0):
        plateau[6][4] = 1
    elif (599 <= canevas.coords(cercle)[2] <= 734) and (493 <= canevas.coords(cercle)[3] <= 569) and (tour_counter % 2 == 1):
        plateau[6][4] = -1
    elif (737 <= canevas.coords(cercle)[2] <= 872) and (493 <= canevas.coords(cercle)[3] <= 569) and (tour_counter % 2 == 0):
        plateau[6][5] = 1
    elif (737 <= canevas.coords(cercle)[2] <= 872) and (493 <= canevas.coords(cercle)[3] <= 569) and (tour_counter % 2 == 1):
        plateau[6][5] = -1
    elif (874 <= canevas.coords(cercle)[2] <= 1009) and (493 <= canevas.coords(cercle)[3] <= 569) and (tour_counter % 2 == 0):
        plateau[6][6] = 1
    elif (874 <= canevas.coords(cercle)[2] <= 1009) and (493 <= canevas.coords(cercle)[3] <= 569) and (tour_counter % 2 == 1):
        plateau[6][6] = -1
    elif (50 <= canevas.coords(cercle)[2] <= 187) and (414 <= canevas.coords(cercle)[3] <= 492) and (tour_counter % 2 == 0):
        plateau[5][0] = 1
    elif (50 <= canevas.coords(cercle)[2] <= 187) and (414 <= canevas.coords(cercle)[3] <= 492) and (tour_counter % 2 == 1):
        plateau[5][0] = -1
    elif (187 <= canevas.coords(cercle)[2] <= 324) and (414 <= canevas.coords(cercle)[3] <= 492) and (tour_counter % 2 == 0):
        plateau[5][1] = 1
    elif (187 <= canevas.coords(cercle)[2] <= 324) and (414 <= canevas.coords(cercle)[3] <= 492) and (tour_counter % 2 == 1):
        plateau[5][1] = -1
    elif (324 <= canevas.coords(cercle)[2] <= 461) and (414 <= canevas.coords(cercle)[3] <= 492) and (tour_counter % 2 == 0):
        plateau[5][2] = 1
    elif (324 <= canevas.coords(cercle)[2] <= 461) and (414 <= canevas.coords(cercle)[3] <= 492) and (tour_counter % 2 == 1):
        plateau[5][2] = -1
    elif (461 <= canevas.coords(cercle)[2] <= 597) and (414 <= canevas.coords(cercle)[3] <= 492) and (tour_counter % 2 == 0):
        plateau[5][3] = 1
    elif (461 <= canevas.coords(cercle)[2] <= 597) and (414 <= canevas.coords(cercle)[3] <= 492) and (tour_counter % 2 == 1):
        plateau[5][3] = -1
    elif (598 <= canevas.coords(cercle)[2] <= 735) and (414 <= canevas.coords(cercle)[3] <= 492) and (tour_counter % 2 == 0):
        plateau[5][4] = 1
    elif (598 <= canevas.coords(cercle)[2] <= 735) and (414 <= canevas.coords(cercle)[3] <= 492) and (tour_counter % 2 == 1):
        plateau[5][4] = -1
    elif (737 <= canevas.coords(cercle)[2] <= 873) and (414 <= canevas.coords(cercle)[3] <= 492) and (tour_counter % 2 == 0):
        plateau[5][5] = 1 
    elif (737 <= canevas.coords(cercle)[2] <= 873) and (414 <= canevas.coords(cercle)[3] <= 492) and (tour_counter % 2 == 1):
        plateau[5][5] = -1
    elif (873 <= canevas.coords(cercle)[2] <= 1009) and (414 <= canevas.coords(cercle)[3] <= 492) and (tour_counter % 2 == 0):
        plateau[5][6] = 1
    elif (873 <= canevas.coords(cercle)[2] <= 1009) and (414 <= canevas.coords(cercle)[3] <= 492) and (tour_counter % 2 == 1):
        plateau[5][6] = -1
    print(plateau)
        


"""def deplacement():
    canevas.move(cercle,0,3*taille_case_height)
    for i in range(len(plateau)-1,0,-1):
        for j in range(len(plateau)):
            if (plateau[i][j] == 1) or (plateau[i][j] == -1):
                canevas.move(cercle,0,3*taille_case_height-0.57*i*taille_case_height)
                print(i,j)"""
            
    




    
    

   
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

label_score_joueur1 = tk.Label(fenetre,text= '  ' + str(score),font=("Times New Roman","20","italic"),bg="white")

label_score_joueur2 = tk.Label(fenetre,text= '  ' + str(score),font=("Times New Roman","20","italic"),bg="white")

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
canevas.bind("<Button-3>", coordonnees)
fenetre.mainloop()



