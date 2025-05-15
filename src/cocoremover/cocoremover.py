import os
import glob
import io
import requests
import logging
import warnings
import statistics
import math
from pathlib import Path
from importlib import resources

import numpy as np
import pandas as pnd


        
def cocoremover(args, logger): 
    
    
    # adjust out folder path
    while args.output.endswith('/'):
        args.output = args.output[:-1]
    
        
    strain_to_df = collect_raw_data(logger, args.input, args.plates, args.replicates, args.discarding)
    if type(strain_to_df) == int: return 1


    strain_to_df = data_preprocessing(logger, strain_to_df)
    if type(strain_to_df) == int: return 1


    strain_to_fitdf = curve_fitting(logger, args.output, strain_to_df, args.auc)
    if type(strain_to_fitdf) == int: return 1


    response = plot_plates(logger, args.output, strain_to_df, strain_to_fitdf, args.noynorm, args.auc)
    if response==1: return 1
    
        
    return 0