import random
import noise
from PIL import Image
import argparse

"""
========================
Argument commande line
========================
"""
parser = argparse.ArgumentParser(description='Program to generate a PNG representing a 2D procedural world using the Perlin noise algorithm')
parser.add_argument('-n', '--name',
                    help='String : PNG\'s name for the map. Default : map.png',
                    action="store",
                    default="map.png"
                    )
parser.add_argument('-i', '--image',
                    help='int : Size of image (x,x). Default : 512',
                    action="store",
                    default=512,
                    type=int
                    )
parser.add_argument('-s', '--seed',
                    help='int : seed to create a map .Between (0-1000)',
                    action="store",
                    default=0,
                    type=int,
                    )
parser.add_argument('-sc', '--scale',
                    help='int : Choose the Scale of the map. Lower Number will extend the map. Default : 130',
                    action="store",
                    default=130,
                    type=int
                    )
parser.add_argument('-o', '--octaves',
                    help='int : Level of details in the map. Default : 7',
                    action="store",
                    default=7,
                    type=int
                    )
parser.add_argument('-l', '--lacunarity',
                    help='float : Level of details by octave. Default : 1.9',
                    action="store",
                    default=1.9,
                    type=float
                    )

parser.add_argument('-p', '--persistence',
                    help='float : Octave contribution rate for the map. Default : 0.35',
                    action="store",
                    default=0.35,
                    type=float
                    )

args = parser.parse_args()

"""
====================
End of command line
====================
"""

"""Code explanation 
We will realize a perlin noise, which is a random but coherent generation 
No big disturbance, with a continuity 

We will use a noise function that will allow us to do this. In 2D
"""

#Name of the output image
image_filepath = args.name


#Writing the parameters for our world
scale = args.scale              #The size of our map (the larger the value the more zoomed in map, and vice versa)
octaves = args.octaves          #Level of detail of the map
lacunarity = args.lacunarity    #Level of detail per octave
persistence = args.persistence  #Influences the octaves (how much each octave contributes to the overall shape)
if(args.seed != 0):
    seed = args.seed
else :
    seed = random.randint(0,700) #Seed for the creation map

#Color of our world
sea = (66,110,225)
ocean = (0,48,143)
plains = (36,135,32)
beach = (240,210,172)
forest = (0,77,13)
mountains = (140,140,140)
snow = (255,255,255)

#Image size 
size = (args.image,args.image)

#Creation of the image
image = Image.new(mode="RGB", size=size)

def set_color(x,y,image,value):
    if value < -0.1*127.0+128 :
        image.putpixel((x,y),ocean)
    elif value < 0.01*127.0+128:
        image.putpixel((x,y),sea)
    elif value < 0.08*127.0+128:
        image.putpixel((x,y),beach)
    elif value < 0.20*127.0+128:
        image.putpixel((x,y),plains)
    elif value < 0.35*127.0+128 :
        image.putpixel((x,y),forest)
    elif value < 0.43*127.0+128:
        image.putpixel((x,y),mountains)
    elif value < 1*127.0+128:
        image.putpixel((x,y),snow)


#We browse all the pixels of the image
for x in range(size[0]):
    for y in range(size[1]):
        value = noise.pnoise2(x/scale, 
                              y/scale,
                              octaves=octaves,
                              persistence=persistence,
                              lacunarity = lacunarity,
                              repeatx=size[0], #The repetition of the generated shape in x, here the shape is the size of the image which no repetition
                              repeaty=size[1], #The repetition of the generated shape in y
                              base=seed
                              )*127.0+128
        set_color(x,y,image,value)        
image.save(image_filepath)







    
    
    