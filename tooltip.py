import tkinter as tk
class ToolTip:
    ...
class ToolTip:
    instances:ToolTip=[]
    def __init__(self,root,widget,tooltip_window:tk.Frame|ToolTip|None=None,generate_mouse_controls:bool=True, force_MB1_deletion:bool=False)-> tk.Frame|None:
        """will generate tkinter.Frame for the tooltip if not given one"""
        # this almost isn't necessary but it is used for moving the tool tip to the right position
        self.root=root


        #will generate a frame if not given one otherwise we'll use the one that was passed in
        if tooltip_window==None:
            self.tooltip_container = tk.Frame(root,name="tooltip")
        else:
            self.tooltip_container=tooltip_window


        #saves widget for later use
        self.widget = widget


        #appends this object to a list that is accessible by all other tooltips
        ToolTip.instances.append(self)


        #generates Mouse controls if not told to do otherwise
        if generate_mouse_controls:
            if not force_MB1_deletion:
                root.bind('<Button-1>', self.hide_this_tooltip,add="+")
            self.widget.bind('<Button-3>', self.show_tooltip,add="+")


        #makes sure the tooltip is shown above the object it's assigned to and will print any exception that it gets
        try:
            self.tooltip_container.lift(widget)
        except Exception as e:
            print(e)




    def __call__(self):
        return self.tooltip_container

    def is_widget_inside(self,widget, container)->bool:
        """Check if 'widget' is inside 'container' at any level, including if the 'widget' IS the 'container'"""
        #checks if the widget is the container and returns true otherwise it continues
        if widget==container:
            return True
        

        # Traverse up the widget hierarchy
        parent = widget.master
        while parent:  
            if parent == container:
                return True
            parent = parent.master


        # the widget is not the container or inside the container
        return False 


    def show_tooltip(self, event)-> None:
        """Enables rendering of the tooltip and moves it to the current Mouse position"""
        self.tooltip_container.place(x=event.widget.winfo_rootx()-self.root.winfo_rootx()+event.x, y=event.widget.winfo_rooty()-self.root.winfo_rooty()+event.y)




    def hide_this_tooltip(self,event)-> None:
        """Disables rendering of this tooltip"""
        if not self.is_widget_inside(event.widget,self.tooltip_container):
            self.tooltip_container.place_forget()

    def hide_all_tooltips(self)-> None:
        """Disables rendering of all tooltips"""
        for tooltip in ToolTip.instances:
            tooltip.tooltip_window.place_forget()


    #used for putting a tooltip on a tooltip (again I don't know why you would do this but it's here)
    def bind(self,button,func,add=""):
        self.tooltip_container.bind(button, func,add=add)
        