import os

class Window:

    def print_window(self):
        self._clear_window()
        window = ""
        window += "************************************************************\n"
        window += "*                       JEU DU PENDU                       *\n"
        window += "*  mot à trouver : XXXXXXXX    nom du joueur : XXXXXXXXXX  *\n"
        window += "*                                                          *\n"
        window += "*  coups restants : X                     points : XXXXXX  *\n"
        window += "*                                                          *\n"
        window += "*  lettres déjà testées :                                  *\n"
        window += "*                                                          *\n"
        window += "*  abcdefghijklmnopqrstuvwxyz                              *\n"
        window += "*                                                          *\n"
        window += "************************************************************\n"
        print(window)
    
    def _clear_window(self):
        os.system('cls')
        os.system('clear')
    
w = Window()
w.print_window()