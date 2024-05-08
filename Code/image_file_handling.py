from PIL import Image #Image hangling library
orb_type = "2s"

def open_orbital_image(orb_type):
    dir_name = "Rendered_orbitals_EXAMPLES\\"
    try:
        filename = str(orb_type + "_rendered_orbital.png") #Creating file name
        print(filename)
        pic_file = Image.open(dir_name+filename)
        return pic_file
    except:
        print("Error: No file found")
    return

pic_file = open_orbital_image(orb_type)
pic_file.show()
