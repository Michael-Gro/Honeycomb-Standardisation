This is generally the code used for the paper.

meth-.. is short for method..

meth-1 is the code for Layer Growth
meth-2 is the code for Vertex Displacement
meth-3 is the code for Voronoi Expansion

select-vertices can be used to generate Pointsets from Pictures
associate-threads can be used to make these Pointsets ordered into threads (list of points) for further processing

meth-4.ipynb is the code for processing code produced with meth-2, meth-3 or from manual selection
meth-1 includes large parts optimized from meth-4

To generate structures please follow and debug the existing scripts.
For evaluating and correcting the structures meth-4 (or the end of meth-1) is required.
Depending on how methods are set up the base inputs for the correction have to be manipulated heavily, like the start point for sweeping over the lists, that has to be done by hand.
this can be partially avoided by cutting a larger section from the left and the right of the structures instead of chosing the "correct" point (skipping an entire iteration)
