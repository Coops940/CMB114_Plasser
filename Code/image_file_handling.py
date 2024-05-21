#Imports libraries used
from PIL import Image
from datetime import date #Imports to create individul name for saved plots
from datetime import datetime

def open_orbital_image(orb_type):
    """
    Opens the rendered image file for the orb_type selected.
    """
    dir_name = "Rendered_orbitals_EXAMPLES\\"
    try: #Try.. Except... used for error handling
        #Determines the filename (as all file systemically name) from orb_type
        filename = str(dir_name+orb_type + "_rendered_orbital.png") #Creating file name
        #Opens image file
        pic_file = Image.open(filename)
        #returns image file and filename
        return pic_file, filename
    except:
        #Produces error message
        print("Error: No file found")
    return

def create_filename(orb_type, plot_type):
    """
    Creates a individual file name for plot using orb_type, plot_type and current date and time when run
    """
    return (orb_type +"_"+ plot_type +"_"+ str(date.today()) + '_' + str(datetime.now().strftime("%H-%M-%S")))

def save_plot(plot, orb_type, plot_type):
    """
    Saves plots as .png with an appropriate filename
    """
    filename = create_filename(orb_type, plot_type)
    #Saves plot at specified quality
    plot.savefig(filename+".png", dpi = 65)
    return filename+".png" #Returns filename

def open_plot_image(filename):
    """
    Opens plot of orb_type using filename given
    """
    pic_file = Image.open(filename)
    #Returns picture file
    return pic_file
