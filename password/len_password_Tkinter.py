#coding:utf-8
from tkinter import *

# la fontion qui permet de compter les caracteres
def compter():
    password = entry.get()
    result = len(password)
    re = str(result)
    entry2.delete( 0, END )
    entry2.insert( 0,result )
    if result >=1 :
        aa = "caractères"
    else :
        aa = "caractère"
    with open( "Nombres_de_caractères.txt", "a+" ) as file:
        file.write(" Il y a " + re + " " +  aa + " dans le mot de passe " + password + "\n")
        file.close()

def effacer():
    entry2.delete( 0, END )
    entry.delete( 0, END )
#  window
window = Tk()
window.title( "Compteur de mot de passe " )
window.geometry( "1080x720" )
window.minsize( 720, 360 )
window.config( background='#2C2323' )
# frame
frame = Frame( window, bg='#2C2323' )

# image
width = 300
height = 300
image = PhotoImage( file='images.png' ).zoom(20).subsample( 32 )
canvas = Canvas( frame, width=width, height=height, bg='#60108E', bd=0, highlightthickness=0 )
canvas.create_image( width / 2, height / 2, image=image )
canvas.grid( row=0, column=0, sticky=W )

frame2 = Frame( frame, bg='#2C2323' )
frame3 = Frame( frame, bg='#2C2323' )
# titre
label = Label( frame2, text=" Compteur de mot de passe ", font="Bahnschrift, 20", bg='#2C2323', fg='white' )
label.pack()

# champ
entry = Entry( frame2, font="Bahnschrift, 20", bg='#2C2323', fg='white' )
entry.pack(fill=X)
# champ ou le nombre sera entrez
entry2 = Entry( frame3, font="Bahnschrift, 20", bg='#2C2323', fg='white', bd=0, highlightthickness=0 )
entry2.pack()

# bouton
button = Button( frame2, text=" Compter ", font="Bahnschrift, 20", bg='#2C2323', fg='white', command=compter )
button.pack(fill=X)
# bouton effacer
buttoneffacer = Button( frame2, text=" Effacer ", font="Bahnschrift, 20", bg='#2C2323', fg='white', command=effacer )
buttoneffacer.pack(fill=X)
# afficher la frame
frame2.grid( row=0, column=1, sticky=W )
frame3.grid( row=0, column=1, sticky=N )
frame.pack( expand=YES )

# menu
menu = Menu(window)
menu_bar = Menu(menu, tearoff=0, bg= 'white')
menu_bar.add_command(label="Quitter", command=window.quit)
menu_bar.add_command(label="Compter", command=compter)

menu.add_cascade(label="Fichier", menu=menu_bar, font='blue')
window.config(menu=menu)

window.mainloop()
