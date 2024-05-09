from tkinter import *

n=2
l=2

def run(orb_type, plot_type):
    print(orb_type, plot_type)

class elements: 
    """
    General class with all attributes and functions for any element in tkinter
    """
    def __init__(self, window, geo, colour, co_ords):
        self.height = geo[1]
        self.width = geo[0]
        self.colour = colour
        self.window = window
        self.co_ords = co_ords
        self.font = "Arial Rounded MT Bold"
        self.fontsize = 14
    
    def build_canvas(self): 
        """
        Creates canvas from general attributes
        """
        _canvas = Canvas(output_window, bg = self.colour, width = self.width, height = self.height)
        _canvas.pack()
        _canvas.place(y = self.co_ords[1], x = self.co_ords[0])
        
class label(elements):
    """
    Daughter class for elements - extra attributes and functions specifc to labels
    """
    def __init__(self, window, geo, colour, co_ords, text):
        elements.__init__(self, window, geo, colour, co_ords)
        self.text = text
    
    def build(self): 
        """
        Builds label
        """
        _label = Label(self.window, text = self.text, width = self.width, height = self.height, bg = self.colour, font = (self.font , str(self.fontsize)))
        _label.pack()
        _label.place(y = self.co_ords[1], x = self.co_ords[0])

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
        user_input = StringVar()
        user_input.set(self.options[0])
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
        
#Creates input window GUIs
input_window = Tk()
input_window.geometry("550x450")
input_window.title("INPUT WINDOW")
input_window.configure(bg = 'DarkSeaGreen3')

output_window = Tk()
output_window.geometry("600x500")
output_window.title("OUTPUT WINDOW")
output_window.configure(bg = 'DarkSeaGreen4')

orb_label = label(input_window, [45,2] , 'DarkSeaGreen3', [10,10], "PICK THE ORBITAL TYPE:")
represent_label = label(input_window, [45,2] , 'DarkSeaGreen3', [10,150], "PICK THE REPRESENTATION TYPE:")
orb_choice = dropdown(input_window, [25,3], 'white smoke', [160, 75], ["1_s", "2_s", "2_p"])
represent_choice = dropdown(input_window, [25,3], 'white smoke', [160, 225], ["1D", "2D", "RENDERING"])
generate_button = button(input_window, [15,3], "ghost white", [210, 350], "GENERATE", lambda: run(orb_type.get(), plot_type.get()))

orb_label.build()
represent_label.build()
orb_type = orb_choice.build()
plot_type = represent_choice.build()
generate_button.build()


graphics_box = elements(output_window, [550,300], 'white smoke', [25,25])
pqnumber_label = label(output_window, [30,1] , 'DarkSeaGreen3', [25,350], (f"Principle Quantum Number:{n:>12.0f}"))
amnumber_label = label(output_window, [30,1] , 'DarkSeaGreen3', [25,375], (f"Angular Momentum Number:{l:>10.0f}"))
graphics_box.build_canvas()
pqnumber_label.build()
amnumber_label.build()

input_window.mainloop()

print(orb_type.get(), plot_type.get())