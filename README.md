<h1 align="center">2D World Generator</h1>

<h2 align="center">Explanation</h2>
<p>This program allows you to generate png images of a 2D procedural world. Thanks to Perlin's noise </p>
<p align = center>
<img src="./Assets/example.png?raw=true" alt="Image Of a procedural world" height=200 width=200 text-align="center">
<img src="./Assets/example2.png?raw=true" alt="Image Of a procedural world" height=200 width=200 text-align="center">
</p>
<h1></h1>

<h2 align="center">How to use it? </h2>
<h3 >Requirements</h3>
<ul>
    <li>Python 3.x.x  </li>
    <li>Noise (pip install noise) </li>
    <li>Pillow (pip install Pillow) </li>
</ul>


<h3> Working </h3>
<p> Just run the program, it will generate an image in the image directory </p>

<h1></h1>

<h2 align="center">Arguments for the command line</h2>
<ul>
    <li>
        <span color="grey">--name<span> : Changes the name of the generated image
    </li>
    <li>
        <span color="grey">--image<span> : Changes the size of the image. Default (512,512)
    </li>
    <li>
        <span color="grey">--seed<span> : Seed of the world. (To get the same map)
    </li>
    <li>
        <p><span color="grey">--scale<span> : Change the scale of a world. By default it is 130. If you choose smaller it will enlarge the map and vice versa. <br> Example with 2 maps, having the same seed but not the same Scale.</p>
        <p align="center">
        <img src="./Assets/example_Scale.png" alt="Example Scale" width=130>
        <img src="./Assets/example_Scale2.png" alt="Example Scale" width=130>
        </p>
    </li>
    <li>
        <p><span color="grey">--octaves <span>:
        Level of detail that the map will include. By default it is 7. The fewer octaves there are, the less detail there will be on the map <br> Example of 2 maps with the same seed, but not the same number of Octaves
        </p>
        <p align="center">
        <img src="./Assets/example_Octave.png" alt="Example Octave" width=130>
        <img src="./Assets/example_Octave2.png" alt="Example Octave" width=130>
        </p>
    </li>
    <li>
        <p><span color="grey">--lacunarity <span>:
        Level of detail by octave. By default it is 1.9. The fewer lacunarity there are, the less detail there will by Octave (Very efficient to increase both - Lacunarity & Octave) <br> Example of 2 maps with the same seed, but not the same Lacunarity
        </p>
        <p align="center">
        <img src="./Assets/example_Lacunarity.png" alt="Example Lacunarity" width=130>
        <img src="./Assets/example_Lacunarity2.png" alt="Example Lacunarity" width=130>
        </p>
    </li>
    <li>
        <p><span color="grey">--persistence <span>:
        Octave contribution rate for the map. By default it is 0.35. The fewer persistence there are, less will contribute the octaves to the generation of the map <br> Example of 2 maps with the same seed, but not the same Persistence
        </p>
        <p align="center">
        <img src="./Assets/example_Persistence.png" alt="Example Lacunarity" width=130>
        <img src="./Assets/example_Persistence2.png" alt="Example Lacunarity" width=130>
        </p>
    </li>
</ul>
<h1></h1>
<h2 align="center">Idea ?</h2>
<p>If you have any ideas to improve this program, don't hesitate to submit it! And if you have any questions, don't hesitate to contact me </p>
<h1></h1>

<h2 align="center">Have fun! </h2>
