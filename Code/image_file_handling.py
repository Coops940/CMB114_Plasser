from PIL import Image
from datetime import date #Imports to create individul name for saved plots
from datetime import datetime

def open_orbital_image(orb_type):
    dir_name = "Rendered_orbitals_EXAMPLES\\"
    try:
        filename = str(dir_name+orb_type + "_rendered_orbital.png") #Creating file name
        pic_file = Image.open(filename)
        #pic_file = pic_file.resize((300,300),Image.ANTIALIAS)
        return pic_file, filename
    except:
        print("Error: No file found")
    return

def create_filename(orb_type, plot_type):
    return (orb_type +"_"+ plot_type +"_"+ str(date.today()) + '_' + str(datetime.now().strftime("%H-%M-%S")))

def save_plot(plot, orb_type, plot_type):
    filename = create_filename(orb_type, plot_type)
    plot.savefig(filename+".png", dpi = 65)
    return filename+".png"

def open_plot_image(filename):
    pic_file = Image.open(filename)
    #pic_file = pic_file.resize((300,300),Image.ANTIALIAS)
    return pic_file
