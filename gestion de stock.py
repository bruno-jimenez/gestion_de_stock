from tkinter import *


#[--------------------------------]
#      management fontion
#[--------------------------------]

def add_product():
     pass

def add_categorie():
    pass    

def del_product():
    pass

def del_categorie():
    pass

def edit_product():
    pass

def edit_categorie():
    pass

def select_product():
    pass

def select_categorie():
    pass

#[--------------------------------]
#  create the tkinter interface
#[--------------------------------]

root = Tk()
root.title("Product stock overview")

# Création des widgets pour le tableau de bord
titre_label = Label(root, text="Product stock")
ajouter_bouton = Button(root, text="Add product", command=add_product)
supprimer_bouton = Button(root, text=" Del product ", command=del_product)

# Placement des widgets dans la fenêtre
titre_label.pack()
ajouter_bouton.pack()
supprimer_bouton.pack()

# Boucle principale Tkinter
root.mainloop()