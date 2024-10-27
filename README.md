This is generally the code used for the paper.

meth-.. is short for method..

meth-1.ipynb is the code for Layer Growth <br>
meth-2.ipynb is the code for Vertex Displacement <br>
meth-3.ipynb is the code for Voronoi Expansion <br>

select-vertices.py can be used to generate Pointsets from Pictures <br>
associate-threads.py can be used to make these Pointsets ordered into threads (list of points) for further processing

meth-4.ipynb is the code for processing code produced with meth-2, meth-3 or from manual selection <br>
meth-1 includes large parts optimized from meth-4

To generate structures please follow and debug the existing scripts. <br>
For evaluating and correcting the structures meth-4 (or the end of meth-1) is required. <br>
Depending on how methods are set up the base inputs for the correction have to be manipulated heavily, like the start point for sweeping over the lists, that has to be done by hand. <br>
this can be partially avoided by cutting a larger section from the left and the right of the structures instead of chosing the "correct" point (skipping an entire iteration)
