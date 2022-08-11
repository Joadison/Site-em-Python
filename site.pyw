import time
import os
import time
import datetime, random
from tkinter import ttk
from tkinter import *
from tkhtmlview import HTMLLabel


root = Tk()
root.title('CATI WEB')
root.geometry('700x480')
root.minsize(700,480)
root.maxsize(700,480)
#root.configure(background='#71a6ff')


#######################################################
my_label = HTMLLabel(root, html="""
     <h3>LINKS</h3>
     <ul>
        <li><a href='tjnet/'>Portal TJCE</a></li>
        <li><a href='#'>TJNET</a></li>
        <li><a href='#'>SAJADM</a></li>
        <li><a href='#'>SEEU</a></li>
        <li><a href='#'>CATINET</a></li>
    </ul>
    <h3>PROGRAMAS</h3>
    <ul>
        <li><a href='#'>SAJPG e SG</a></li>
        <li><a href='#'>PJE</a></li>
        <li><a href='#'>Assinador CPA</a></li>
        <li><a href='#'>PDF24</a></li>
        <li><a href='#'>TEST</a></li>
    </ul>
    """)
my_label.pack(pady=20, padx=20)


root.mainloop()

