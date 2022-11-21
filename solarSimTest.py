import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
import matplotlib.pyplot as plt
import math
import itertools




class Menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("480x300")
        self.title('Solar System Creator')

        self.planetSelector=('Earthlike','Marslike','Mercurylike',
        'Venuslike','Jupiterlike','Saturnlike','Uranuslike','Neptunelike')
        self.planetOption = tk.StringVar(self)
        self.planetOption2 = tk.StringVar(self)
        self.planetOption3 = tk.StringVar(self)
        self.planetOption4 = tk.StringVar(self)
        self.planetOption5 = tk.StringVar(self)
        self.planetNumOption = tk.IntVar(self)
        self.planetGrav = tk.IntVar(self)
        self.planetGrav2 = tk.IntVar(self)
        self.planetGrav3 = tk.IntVar(self)
        self.planetGrav4 = tk.IntVar(self)
        self.planetGrav5 = tk.IntVar(self)
        self.createWidgets()
        self.planetNumOption.set(0)

    def createWidgets(self):
        paddings = {'padx':5,'pady':5}
        label = ttk.Label(self, text='Select how many planets in this solar system (up to 5):')
        label.grid(column=0,row=0,sticky=tk.W,**paddings)
        planetNumSel = ttk.Button(self,text='Add a planet',command=self.planetNum)
        planetNumSel.grid(column=1,row=0,sticky=tk.W,**paddings)
        self.planetCount = 0
        simGenerate = ttk.Button(self,text='Generate simulation',command=self.simGen)
        simGenerate.grid(column=1,row=6,sticky=tk.W,**paddings)
    
    def planetNum(self,*args):
        self.planetCount = self.planetCount + 1
        label = ttk.Label(self, text='Planet 1 mass:')
        label.grid(column=0,row=1,sticky=tk.W)
        # planetsToAdd = ttk.OptionMenu(self,self.planetOption,self.planetSelector[0],*self.planetSelector,command = self.planets)
        # planetsToAdd.grid(column=0,row=1,sticky=tk.W)
        planetSlider = tk.Scale(self, from_=10, to=60,orient='horizontal',variable=self.planetGrav)
        planetSlider.set(35)
        planetSlider.grid(column=1,row=1,sticky=tk.W)
        if self.planetCount == 2:
            label = ttk.Label(self, text='Planet 2 mass:')
            label.grid(column=0,row=2,sticky=tk.W)
            # planetsToAdd2 = ttk.OptionMenu(self,self.planetOption2,self.planetSelector[0],*self.planetSelector,command = self.planets)
            # planetsToAdd2.grid(column=0,row=2,sticky=tk.W)
            planetSlider2 = tk.Scale(self, from_=10, to=60,orient='horizontal',variable=self.planetGrav2)
            planetSlider2.set(35)
            planetSlider2.grid(column=1,row=2,sticky=tk.W)
        elif self.planetCount == 3:
            label = ttk.Label(self, text='Planet 3 mass:')
            label.grid(column=0,row=3,sticky=tk.W)
            # planetsToAdd3 = ttk.OptionMenu(self,self.planetOption3,self.planetSelector[0],*self.planetSelector,command = self.planets)
            # planetsToAdd3.grid(column=0,row=3,sticky=tk.W)
            planetSlider3 = tk.Scale(self, from_=10, to=60,orient='horizontal',variable=self.planetGrav3)
            planetSlider3.set(35)
            planetSlider3.grid(column=1,row=3,sticky=tk.W)
        elif self.planetCount == 4:
            label = ttk.Label(self, text='Planet 4 mass:')
            label.grid(column=0,row=4,sticky=tk.W)
            # planetsToAdd4 = ttk.OptionMenu(self,self.planetOption4,self.planetSelector[0],*self.planetSelector,command = self.planets)
            # planetsToAdd4.grid(column=0,row=4,sticky=tk.W)
            planetSlider4 = tk.Scale(self, from_=10, to=60,orient='horizontal',variable=self.planetGrav4)
            planetSlider4.set(35)
            planetSlider4.grid(column=1,row=4,sticky=tk.W)
        elif self.planetCount == 5:
            label = ttk.Label(self, text='Planet 5 mass:')
            label.grid(column=0,row=5,sticky=tk.W)
            # planetsToAdd5 = ttk.OptionMenu(self,self.planetOption5,self.planetSelector[0],*self.planetSelector,command = self.planets)
            # planetsToAdd5.grid(column=0,row=5,sticky=tk.W)
            planetSlider5 = tk.Scale(self, from_=10, to=60,orient='horizontal',variable=self.planetGrav5)
            planetSlider5.set(35)
            planetSlider5.grid(column=1,row=5,sticky=tk.W)
        else:
            pass
    def planetAdd(self,*args):
        planetsToAdd = ttk.OptionMenu(self,self.planetOption,self.planetSelector[0],*self.planetSelector,command = self.planets)
        planetsToAdd.grid(column=0,row=1,sticky=tk.W)
    def planets(self,*args):
        pass
    def simGen(self,*args):
        global numOfPlanets
        numOfPlanets = self.planetCount
        if numOfPlanets == 1:
            global planet1Mass
            planet1Mass = self.planetGrav.get()
        elif numOfPlanets == 2:
            global planet2Mass
            planet1Mass = self.planetGrav.get()
            planet2Mass = self.planetGrav2.get()
        elif numOfPlanets == 3:
            global planet3Mass
            planet1Mass = self.planetGrav.get()
            planet2Mass = self.planetGrav2.get()
            planet3Mass = self.planetGrav3.get()
        elif numOfPlanets == 4:
            global planet4Mass
            planet1Mass = self.planetGrav.get()
            planet2Mass = self.planetGrav2.get()
            planet3Mass = self.planetGrav3.get()
            planet4Mass = self.planetGrav4.get()
        elif numOfPlanets == 5:
            global planet5Mass
            planet1Mass = self.planetGrav.get()
            planet2Mass = self.planetGrav2.get()
            planet3Mass = self.planetGrav3.get()
            planet4Mass = self.planetGrav4.get()
            planet5Mass = self.planetGrav5.get()
        else:
            pass
        self.destroy()
        pass
class SolarSystem:

    def __init__(self,size,projection_2d=False):
        self.size = size
        self.projection_2d = projection_2d
        self.bodies = []

        self.fig, self.ax = plt.subplots(
            1,
            1,
            subplot_kw={"projection":"3d"},
            figsize = (self.size / 50, self.size / 50),
        )
        self.fig.tight_layout()
        if self.projection_2d:
            self.ax.view_init(10, 0)
        else:
            self.ax.view_init(0, 0)
    def add_body(self,body):
        self.bodies.append(body)

    def update_all(self):
        self.bodies.sort(key=lambda item: item.position[0])
        for body in self.bodies:
            body.move()
            body.draw()

    def draw_all(self):
        self.ax.set_xlim((-self.size / 2, self.size / 2 ))
        self.ax.set_ylim((-self.size / 2, self.size / 2 ))
        self.ax.set_zlim((-self.size / 2, self.size / 2 ))
        if self.projection_2d:
            self.ax.xaxis.set_ticklabels([])
            self.ax.yaxis.set_ticklabels([])
            self.ax.zaxis.set_ticklabels([])
        else:
            self.ax.axis(False)
        plt.pause(0.001)
        self.ax.clear()

    def calculateAllBodyInteractions(self):
        bodiesCopy = self.bodies.copy()
        for idx, first in enumerate(bodiesCopy):
            for second in bodiesCopy[idx + 1:]:
                first.accelerateDueToGravity(second)

class SolarSystemBody:
    min_display_size = 10
    display_log_base = 1.3

    def __init__(self,solar_system,mass,position = (0,0,0),velocity = (0,0,0),):
        self.solar_system = solar_system
        self.mass = mass
        self.position = position
        self.velocity = Vector(*velocity)
        self.display_size = max(
            math.log(self.mass,self.display_log_base),self.min_display_size,
        )
        self.colour = 'black'
        self.solar_system.add_body(self)
    def move(self):
        self.position = (
            self.position[0] + self.velocity[0],
            self.position[1] + self.velocity[1],
            self.position[2] + self.velocity[2],
        )
    def draw(self):
        self.solar_system.ax.plot(
            *self.position,
            marker ="o",
            markersize=self.display_size+self.position[0]/30,
            color=self.colour
        )
        if self.solar_system.projection_2d:
            self.solar_system.ax.plot(
                self.position[0],
                self.position[1],
                -self.solar_system.size / 2,
                marker="o",
                markersize=self.display_size / 2,
                color=(.5, .5, .5),
            )
    def accelerateDueToGravity(self,other):
        distance = Vector(*other.position) - Vector(*self.position)
        distance_mag = distance.get_magnitude()
        force_mag = self.mass * other.mass / (distance_mag ** 2)
        force = distance.normalize() * force_mag
        reverse = 1
        for body in self, other:
            acceleration = force/body.mass
            body.velocity += acceleration * reverse
            reverse = -1

class Sun(SolarSystemBody):
    def __init__(self, solar_system, mass=10_000,position=(0,0,0),velocity=(0,0,0),):
        super(Sun, self).__init__(solar_system, mass, position, velocity)
        self.colour = 'yellow'

class Planet(SolarSystemBody):
    colours = itertools.cycle([(1,0,0),(0,1,0),(0,0,1)])
    def __init__(self,solar_system,mass=10,position=(0,0,0),velocity=(0,0,0),):
        super(Planet, self).__init__(solar_system,mass,position,velocity)
        self.colour = next(Planet.colours)


class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        elif item == 2:
            return self.z
        else:
            raise IndexError("There are only three elements in the vector")
    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
        )
    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
        )
    def __mul__(self, other):
        if isinstance(other, Vector):  # Vector dot product
            return (
                self.x * other.x
                + self.y * other.y
                + self.z * other.z
            )
        elif isinstance(other, (int, float)):  # Scalar multiplication
            return Vector(
                self.x * other,
                self.y * other,
                self.z * other,
            )
        else:
            raise TypeError("operand must be Vector, int, or float")
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(
                self.x / other,
                self.y / other,
                self.z / other,
            )
        else:
            raise TypeError("operand must be int or float")
    def get_magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    def normalize(self):
        magnitude = self.get_magnitude()
        return Vector(
            self.x / magnitude,
            self.y / magnitude,
            self.z / magnitude,
        )
        
        
        


if __name__=="__main__":
    app = Menu()
    app.mainloop()
    solar_system = SolarSystem(400,projection_2d=True)
    sun = Sun(solar_system)

    if numOfPlanets == 1:


        planets = (Planet(solar_system,mass=planet1Mass,position=(150,50,0),velocity=(0,5,5),))
    elif numOfPlanets == 2:
        planets = (Planet(solar_system,mass=planet1Mass,position=(150,50,0),velocity=(0,5,5),),
            Planet(solar_system,mass=planet2Mass,position=(100,-50,150),velocity=(5,0,0)
        )
        )
    elif numOfPlanets == 3:
        planets = (Planet(solar_system,mass=planet1Mass,position=(150,50,0),velocity=(0,5,5),),
            Planet(solar_system,mass=planet2Mass,position=(100,50,150),velocity=(0,5,0),),
            Planet(solar_system,mass=planet3Mass,position=(50,-150,50),velocity=(0,0,5)
            )
            )
    elif numOfPlanets == 4:
        planets = (Planet(solar_system,mass=planet1Mass,position=(150,50,0),velocity=(0,5,5),),
            Planet(solar_system,mass=planet2Mass,position=(100,50,150),velocity=(0,5,0),),
            Planet(solar_system,mass=planet3Mass,position=(50,-150,50),velocity=(0,0,5),),
            Planet(solar_system,mass=planet4Mass,position=(0,100,100),velocity=(0,3,4)))
    elif numOfPlanets == 5:
        planets = (Planet(solar_system,mass=planet1Mass,position=(150,50,0),velocity=(0,5,5),),
            Planet(solar_system,mass=planet2Mass,position=(100,50,150),velocity=(0,5,0),),
            Planet(solar_system,mass=planet3Mass,position=(50,-150,50),velocity=(0,0,5),),
            Planet(solar_system,mass=planet4Mass,position=(0,100,100),velocity=(0,3,4),),
            Planet(solar_system,mass=planet5Mass,position=(50,-50,0),velocity=(0,3,1)))      
            
    while True:
        solar_system.calculateAllBodyInteractions()
        solar_system.update_all()
        solar_system.draw_all()
