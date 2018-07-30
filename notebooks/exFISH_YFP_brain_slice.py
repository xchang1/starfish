#!/usr/bin/env python
# coding: utf-8
#
# EPY: stripped_notebook: {"metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}, "language_info": {"codemirror_mode": {"name": "ipython", "version": 3}, "file_extension": ".py", "mimetype": "text/x-python", "name": "python", "nbconvert_exporter": "python", "pygments_lexer": "ipython3", "version": "3.6.5"}}, "nbformat": 4, "nbformat_minor": 2}

# EPY: START markdown
# # Reproduce Allen smFISH results with Starfish
# 
# This notebook walks through a work flow that reproduces the smFISH result for one field of view using the starfish package. 
# EPY: END markdown

# EPY: START code
from starfish.io import Stack
from starfish.image import ImageStack
from starfish.constants import Indices
import os
# EPY: END code

# EPY: START code
experiment_json = 'https://dmf0bdeheu4zf.cloudfront.net/20180730/exFISH/YFP_brain_slice/fov_001/experiment.json'
# EPY: END code

# EPY: START markdown
# Load the Stack object, which while not well-named right now, should be thought of as an access point to an "ImageDataSet". In practice, we expect the Stack object or something similar to it to be an access point for _multiple_ fields of view. In practice, the thing we talk about as a "TileSet" is the `Stack.image` object. The data are currently stored in-memory in a `numpy.ndarray`, and that is where most of our operations are done. 
# 
# The numpy array can be accessed through Stack.image.numpy\_array (public method, read only) or Stack.image.\_data (read and write)
# EPY: END markdown

# EPY: START code
from starfish.codebook import Codebook
codebook = Codebook.from_json('https://dmf0bdeheu4zf.cloudfront.net/20180730/exFISH/YFP_brain_slice/fov_001/experiment.json')
codebook
# EPY: END code

# EPY: START markdown
# We're ready now to load the experiment into starfish and take a look at the data (This experiment is big, it takes a few minutes):
# EPY: END markdown

# EPY: START code
s = Stack.from_experiment_json(experiment_json)
import warnings
with warnings.catch_warnings():
    warnings.simplefilter('ignore', FutureWarning)
    s.image.show_stack({Indices.CH: 0}, rescale=True)
# EPY: END code
