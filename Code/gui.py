#imports libraries and other python scripts used
from tkinter import *
import main

#Sets defaults for output window
n=0
l=0

def generate(orb_type, plot_type, canvas, pqn_label, amn_label):
    """
    Function updates gui output window and calls function in main.py
    """
    print(orb_type, plot_type)
    #If orb_type can't be broken into n and l (meaning atomic orbital) then runs exception handling
    #Updates gui output window
    if orb_type.split("_")[0].isnumeric():
        n, l = main.break_orbital(orb_type)
    else:
        n = "2"
        l = main.calculate_hybrid_l(orb_type)
    amn_label.config(text = f"Angular Momentum Number:{l:>8.2f}")
    pqn_label.config(text = f"Principle Quantum Number:{n:>13s}")
    #Calls function in main.py 
    main.collect_inputs(orb_type, plot_type, canvas)
    return 

class elements: 
    """
    General class with all attributes and functions for any element in tkinter
    """
    def __init__(self, window, geo, colour, co_ords):
        #Assigns all attributes give through __init__ function
        self.height = geo[1]
        self.width = geo[0]
        self.colour = colour
        self.window = window
        self.co_ords = co_ords
        self.font = "Segoe UI Semibold"
        self.fontsize = 14
    
    def build_canvas(self): 
        """
        Creates canvas from general attributes
        """
        #Builds using tkinter 
        _canvas = Canvas(self.window, bg = self.colour, width = self.width, height = self.height)
        _canvas.grid(row = 0, column = 0, rowspan = 10, columnspan = 5)
        #Allows canvas to hold images
        _canvas.create_image(-10, -10, anchor = "w")
        _canvas.pack()
        #Places canvas in specific position 
        _canvas.place(y = self.co_ords[1], x = self.co_ords[0])
        return _canvas #return canvas so can be updated
        
class label(elements):
    """
    Daughter class for elements - extra attributes and functions specifc to labels
    """
    def __init__(self, window, geo, colour, co_ords, text):
        #Assigns attributes using elements parent class and additional attributes
        elements.__init__(self, window, geo, colour, co_ords)
        self.text = text
    
    def build(self): 
        """
        Builds label
        """
        _label = Label(self.window, text = self.text, width = self.width, height = self.height, bg = self.colour, font = (self.font , str(self.fontsize)))
        _label.pack()
        _label.place(y = self.co_ords[1], x = self.co_ords[0])
        return _label #Retuns _label so labels can be updated 

class dropdown(elements):
    """
    Daughter class for elements - extra attributes and functions specifc to dropdown menus
    """
    def __init__(self, window, geo, colour, co_ords, options):
        elements.__init__(self, window, geo, colour, co_ords)
        self.options = options
    
    def build(self):
        """
        Builds downdown menu
        """
        #Creates variable to hold user current selection in 
        user_input = StringVar()
        user_input.set(self.options[0]) #Sets default as first element in options list
        _dropdown = OptionMenu(self.window, user_input, *self.options)
        _dropdown.config(width = self.width, height = self.height, bg = self.colour, font = (self.font , str(self.fontsize-4)))
        _dropdown.pack()
        _dropdown.place(y = self.co_ords[1], x = self.co_ords[0])
        return user_input
    
class button(elements): 
    """
    Daughter class for elements - extra attributes and functions specifc to button
    """
    def __init__(self, window, geo, colour, co_ords, text, function):
        elements.__init__(self, window, geo, colour, co_ords)
        self.text = text
        self.function = function
    
    def build(self): 
        """
        Builds button
        """    
        _button = Button(self.window, text = self.text,bg= self.colour, width = self.width, height = self.height, font = (self.font , str(self.fontsize-4)), command= self.function)
        _button.pack()
        _button.place(y = self.co_ords[1], x = self.co_ords[0])

def update_graphic_box(graphic_box, pic_file):
    """
    Function to upadte the contents of a canvas
    """
    #Opens image file foramtted for tkinter
    img = PhotoImage(file = pic_file, master = output_window)
    graphic_box.create_image(0, 0, image = img, anchor= "nw")
    graphic_box.image=img
    return

#Creates input and output window GUIs
input_window = Tk()
input_window.geometry("550x450")
input_window.title("INPUT WINDOW")
input_window.configure(bg = 'DarkSeaGreen3')

output_window = Tk()
output_window.geometry("600x700")
output_window.title("OUTPUT WINDOW")
output_window.configure(bg = 'DarkSeaGreen4')
#Creates widgets in output window
graphics_box = elements(output_window, [550,500], 'white smoke', [25,25])
pqnumber_label = label(output_window, [30,1] , 'DarkSeaGreen3', [25,550], (f"Principle Quantum Number:{n:>13.0f}"))
amnumber_label = label(output_window, [30,1] , 'DarkSeaGreen3', [25,575], (f"Angular Momentum Number:{l:>10.0f}"))
#Builds widgets in output window
graphic_box_built = graphics_box.build_canvas()
pqnumber_label_built = pqnumber_label.build()
amnumber_label_built = amnumber_label.build()
#Creates widgets in input window
orb_label = label(input_window, [45,2] , 'DarkSeaGreen3', [10,10], "PICK THE ORBITAL TYPE:")
represent_label = label(input_window, [45,2] , 'DarkSeaGreen3', [10,150], "PICK THE REPRESENTATION TYPE:")
orb_choice = dropdown(input_window, [25,3], 'white smoke', [160, 75], ["1_s", "2_s", "2_p", "s_p", "s_p_2", "s_p_3"])
represent_choice = dropdown(input_window, [25,3], 'white smoke', [160, 225], ["1D", "2D", "RENDERING"])
generate_button = button(input_window, [15,3], "ghost white", [210, 350], "GENERATE", lambda: generate(orb_type.get(), plot_type.get(), graphic_box_built, pqnumber_label_built, amnumber_label_built))
#Builds widgets in input window
orb_label.build()
represent_label.build()
orb_type = orb_choice.build()
plot_type = represent_choice.build()
generate_button.build()

input_window.mainloop() #Runs windows on mainloop, checking for actions
output_window.mainloop()