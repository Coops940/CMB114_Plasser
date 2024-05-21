#import matplotlib.pyplot as plt
import gui
import calculations_and_plots
import image_file_handling
import hybrid_plots
def break_orbital(orb_type):
    """
    Functions breaks down orbital type input to components
    """
    atomic_am_dic = {"s":0, "p": 1}
    
    orb_broken = orb_type.split("_")
    return orb_broken[0], atomic_am_dic[orb_broken[1]]


def collect_inputs(orb_type, plot_type, canvas):
    if plot_type.upper() == "RENDERING":
        img_file, filename = image_file_handling.open_orbital_image(orb_type)
    else:
        orb_broken = orb_type.split("_")
        print(orb_broken)
        if orb_broken[0] == "1" or orb_broken[0] == "2":
            n, l = break_orbital(orb_type)
            plot = calculations_and_plots.plot_orbitals(int(n), int(l), 0, 10, plot_type)
        else:
            plot = hybrid_plots.hybrid_plot_orbitals(orb_type, 0, 10, plot_type)
        filename = image_file_handling.save_plot(plot, orb_type, plot_type)
        plot.show()
        img_file = image_file_handling.open_plot_image(filename)
        #img_file.show()
    gui.update_graphic_box(canvas, filename)



#gui