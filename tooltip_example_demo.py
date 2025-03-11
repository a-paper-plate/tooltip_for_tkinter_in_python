import tkinter as tk
from tooltip import ToolTip


#initializing the window (necessary for tkinter)
window = tk.Tk()
window.geometry("800x800")
window.title("example of tool tip")
window.configure(bg='#18181b')






#creating a button that the tooltip will be applied to 
# (it can be anything but I'm just using a button here for an example)
button=tk.Button(window,height=20,width=20,bg='#333')
button.grid(column=1,row=1)










#creating a frame for the tool tip to use
tooltip_one_frame=tk.Frame(window,background="#222",name="tooltip",borderwidth=10)


#creating and applying a label to the tool tip
tooltip_one_label=tk.Label(tooltip_one_frame,text="tooltip 1 text")
tooltip_one_label.grid(column=1,row=1)


#creating and applying a button to the tooltip
tooltip_one_button_one=tk.Button(tooltip_one_frame,height=5,width=5,bg='#0f0',command=lambda:print("tooltip button 1"))
tooltip_one_button_one.grid(column=1,row=2)









# Generating a tooltip for the button using tooltip_one_frame as the ToolTip overlay and setting root to window allowing you to deselect(Close the window) by clicking anywhere 
# But you can only open up the tooltip by MB-1 clicking (right clicking) on the button
first_tooltip=ToolTip(root=window, widget=button,tooltip_window=tooltip_one_frame)
print(first_tooltip)




# creating a button with the master being the tooltip itself instead of the frame showing that you don't need to call it directly(the frame) but can call the tooltip itself if you prefer
tooltip_one_button_two=tk.Button(master=first_tooltip,height=5,width=5,bg='#00f',command=lambda:print("tooltip button 2"))
tooltip_one_button_two.grid(column=1,row=3)







#I don't know why you'd want to do this but it does allow you to have a tooltip on a tooltip



# Creating a second frame for inner tooltip but it is still the child of window instead of the first tooltip 
# because it would be visually clipped based off the borders of the first tooltip if you were to child it to said tooltip
Frame_for_tooltip_two=tk.Frame(master=window,background="#555",name="test_tooltip",borderwidth=10)


# Creating a button to be applied to the second tooltip For an example of customizability
# I'm also making it red to make it visually distinct from the first button
tooltip_tooltip_button=tk.Button(Frame_for_tooltip_two, height=5, width=5, bg='#f00',command=lambda:print("tooltip_2"))
tooltip_tooltip_button.grid(column=1,row=2)



#Applying the tooltip to the first tooltip using the second frame(tooltip_test_frame)
second_tooltip=ToolTip(root = window , widget = first_tooltip , tooltip_window = Frame_for_tooltip_two)








#(also necessary for tkinter)
window.mainloop()