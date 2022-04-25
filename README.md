# Dissertation - Please read in raw format for better clarity.
This is a Repository compiling all my Data and Code from my adventures through my Dissertation.


Please note, all code used for exploratory data analysis was provided by Stuart Grieve. Github: https://github.com/sgrieve


Data used in this study is sourced from multiple sources, for ease of access I have listed data used below, along with the corresponding links for download/ original author:

TAM-hydrology simulation output (full_phys.hydro.k5e-5.y231-240,241-250), 
Authors: Lora, Juan; Faulk, Sean; Mitchell, Jonathan; Milly, Chris. 
Link: https://doi.org/10.5281/zenodo.3473571

Titan Global Channels (global_channels.shp),
Creator: Julia Miller
Link: Available from author upon request.

Titan Cassini SAR - HiSAR Global Mosaic 351m v1 (gwarped to Titan2000 coordinate system),
Creator: NASA
Link: https://astrogeology.usgs.gov/search/details/Titan/Cassini/Global-Mosaic/Titan_SAR_HiSAR_MosaicThru_T104_Jan2015_clon180_128ppd/cub

All analysis preformed, and all results obtained, are formed from the data stated above.


This repository contains an archive of all data analysis. To run the code in the .ipynb files, you will have to run them through Jupyter Notebook. This is most easily done by downloading anaconda, and downloading the appropriate repositories.

This video is a easy tutorial: https://www.youtube.com/watch?v=syijLJ3oQzU

Various libaries which are being used (imported at the beginning of files) may have to be downloading in anaconda before successfully executing commands in file.



Breakdown of files available:

Tokunaga Analysis-A1~L1
Info: These files use tokunaga_fns.py to calculate the R2, a, c values for the fluvial network.
Dependencies: tokunaga_fns.py, north and south folders in the same path location as the Analysis files.
Library Dependencies: tokunaga_fns, numpy, matplotlib.pyplot

North and South Folders
Info: Contain .csv files with the breakdown of fluvial networks and their indiviual horton orderings and tokunaga indicies.
Dependencies: N/A
Library Dependencies: N/A

Precipitation Data Folder
Info: Contains full_phys.hydro.k5e-5.y231-240,241-250 simulation outputs used to measure precipitation rates on Titan.
Dependencies: N/A
Library Dependencies: N/A

Research Question 1
Info: Data Analysis defining TSS, second part explores Tokunaga parameter distribution.
Dependencies: RQ1.csv, TSS Threshold Value (0.1), Goodness of Fit from the Tokunaga Analysis.ipynb analysis
Library Dependencies: numpy, matplotlib.pyplot, pandas, matplotlib.patches, matplotlib.lines 

Research Question 2
Info: Plots latitude as a function of the c parameter, correlation analysis also included.
Dependencies:RQ1.csv, a and c values
Library Dependencies: numpy, matplotlib.pyplot, pandas, matplotlib.patches, matplotlib.lines 

Precipitation Extraction:
Info: Extraction of precipitation combining the 2 files, conversion to 1-Titan-year average, extraction of corresponding precipitation values for each fluvial network, creation of correlation graph at different confidence thresholds for precipitation and c parameter.
Dependencies: full_phys.hydro.k5e-5.y231-240,241-250
Library Dependencies: netCDF4, scipy.io, numpy, cartopy, cartopy.feature, cartopy.crs, matplotlib.pyplot, xarray, metpy.cbook, numpy, matplotlib.pyplot, pandas, seaborn, matplotlib.patches, matplotlib.lines, sklearn.linear_model, scipy

Enjoy ;)
