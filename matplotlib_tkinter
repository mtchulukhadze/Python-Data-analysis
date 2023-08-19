import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk
from tkinter import Scale
from numpy.random import randn

df = pd.DataFrame(randn(500, 4), columns=['mon', 'tues', 'wed', 'thurs'])

fig, ax = plt.subplots()
gridsize = 15
color_map = 'YlGnBu'

fig.set_size_inches(10, 7)

# ტკინტერის ფანჯარა
root = tk.Tk()
root.title("Hexbin Plot")
root.geometry("1024x768")


def update_plot(val):
    global gridsize, color_map
    gridsize = int(val) if int(val) > 0 else 1
    ax.clear()  # წინა გრინდის ზომის წაშლა და განახლებულის ჩასმა
    if gridsize > 0:
        hexplot = df.plot(x='mon', y='thurs', kind='hexbin', gridsize=gridsize, cmap=color_map, mincnt=0, ax=ax)
        hexplot.set_title('Hexbin Plot')
    else:
        hexplot = df.plot(x='mon', y='thurs', kind='hexbin', cmap='YlGnBu', ax=ax, alpha=0.7)
        hexplot.set_title('Scatter Plot')

    hexplot.set_xlabel('x')
    hexplot.set_ylabel('y')
    canvas.draw()
    if gridsize > 1:
        axes = hexplot.axes
        axes.collections[0].colorbar.remove()


def update_color_map(event):
    global color_map
    color_map = color_var.get()
    update_plot(gridsize)


# ფერის ფანჯარა
color_var = tk.StringVar(root)
color_var.set(color_map)
color_label = tk.Label(root, text="Color")
color_label.pack()
color_combobox = ttk.Combobox(root, textvariable=color_var, values=plt.colormaps())
color_combobox.bind("<<ComboboxSelected>>", update_color_map)
color_combobox.pack()

# სლაიდერი
slider_label = tk.Label(root, text="Hexagon Radius")
slider_label.pack()
slider = Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, length=200, width=20,
               sliderlength=20, sliderrelief=tk.RAISED,
               troughcolor='lightgray',
               command=update_plot)

slider.set(gridsize)
slider.pack()

# საინიციალიზაციო პლოტი
hexplot = df.plot(x='mon', y='thurs', kind='hexbin', gridsize=gridsize, cmap='YlGnBu', mincnt=0, ax=ax)
hexplot.set_title('Hexbin Plot')
hexplot.set_xlabel('x')
hexplot.set_ylabel('y')

# ქოლორბარის იგნორირება
axes = hexplot.axes
axes.collections[0].colorbar.remove()

# პლოტის ინიციალიზაცია ტკინტერში
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

tk.mainloop()
