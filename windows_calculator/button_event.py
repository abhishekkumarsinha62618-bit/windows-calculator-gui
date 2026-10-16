#importing module
import tkinter as tk

#creating an empty gui
root=tk.Tk()

#fun
def test(event):
    button_text=event.widget.cget('text')
    print('Button',button_text, 'is pressed')

#properties
root.geometry('200x200')

#Adding 2 buttons
button_1=tk.Button(root,text='1',width=5,height=2,)

#right click event--> 'Button-3'
#left click event-->'Button-1'
#Scroll button click event-->'Button-2'
button_1.bind('<Button-1>',test)
button_1.pack()

button_2=tk.Button(root,text='2',width=5,height=2)

#right click event--> 'Button-3'
button_2.bind('<Button-3>',test)
button_2.pack()



#continuous display
root.mainloop()