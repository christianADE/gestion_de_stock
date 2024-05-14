'''
la partie a executer premierement... pour acceder a l'interface
'''

from tkinter import Tk
from tkinter import Frame
from tkinter import Menu
from tkinter import Message

from categorie.views import CategorieView
from produits.views import ProduitView

class Main:

    def __init__(self):
        self.root = Tk()
        self.root.geometry('710x607')
        self.root.title('GESTON DE STOCK')

        self.frame_produit = None
        self.frame_categorie = None

        self.menu = Menu(self.root)
        self.root['menu'] = self.menu

        self.menu.add_command(label='Categorie', command=self.show_categorie)
        self.menu.add_command(label='Produit', command=self.show_produit)
        Message(self.root, text='Gestionnaire de Stock').grid(row=0, column=0, columnspan=4)
        self.root.mainloop()

    def show_categorie(self):
        if self.frame_categorie is None:
            self.frame_categorie = Frame(self.root)
            self.frame_categorie.grid(row=0, column=0) #afficher les categorie
            if self.frame_produit is not None:
                self.frame_produit.grid_forget() # retirer la page des produits
            self.frame_produit = None
            CategorieView(self.frame_categorie)

    def show_produit(self):
        if self.frame_produit is None:
            self.frame_produit = Frame(self.root)
            self.frame_produit.grid(row=0, column=0)
            if self.frame_categorie is not None:
                self.frame_categorie.forget()
            self.frame_categorie = None
            ProduitView(self.frame_produit)

if __name__ == "__main__":
   

    Main()




    