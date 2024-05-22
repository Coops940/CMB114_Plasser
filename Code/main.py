#imports addtiona python scripts
import gui
import calculations_and_plots
import image_file_handling
import hybrid_plots

def calculate_hybrid_l(orb_type):
    if orb_type == "s_p":
        return ((0.5*1) + (0.5*2))
    elif orb_type == "s_p_2":
        return ((0.33*1) + (0.66*2))
    elif orb_type == "s_p_3":
        return ((0.25*1) + (0.75*2))
    else:
        print("Error: Unknown hybrid orbital")

def break_orbital(orb_type):
    """
    Functions breaks down orbital type to components n and l
    """
    atomic_am_dic = {"s":0, "p": 1}
    orb_broken = orb_type.split("_")
    return orb_broken[0], atomic_am_dic[orb_broken[1]]


def collect_inputs(orb_type, plot_type, canvas):
    """
    Takes inputs from the gui and handles running
    """
    #Compares plot_type to see if RENDERING was selected
    if plot_type.upper() == "RENDERING":
        #Calls function to open pre-rendered image of selected orbital
        img_file, filename = image_file_handling.open_orbital_image(orb_type)
    else:
        #Checks the orb_type to determine if the user selected an atomic or hybirdied orbital
        orb_broken = orb_type.split("_")
        if orb_broken[0] == "1" or orb_broken[0] == "2":
            #Plots atomic orbital by calling function
            n, l = break_orbital(orb_type)
            plot = calculations_and_plots.plot_orbitals(int(n), int(l), 0, 10, plot_type)
        else:
            #Plots hybridised orbital by calling function
            plot = hybrid_plots.hybrid_plot_orbitals(orb_type, 0, 10, plot_type)
        #Calls function to saves the plot and return file name
        filename = image_file_handling.save_plot(plot, orb_type, plot_type)
        plot.show() #Prints plot to shell
        #Opens the image file that was saved as .png and stores in variable using function
        img_file = image_file_handling.open_plot_image(filename)
    #Upadates gui
    gui.update_graphic_box(canvas, filename)