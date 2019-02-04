from trajalign.traj import Traj
from trajalign.average import load_directory
from trajalign.average import nanMAD as MAD
import numpy as np

def measure_average_lifetime( list_of_trajectories ):

	lifetimes = []

	for element in list_of_trajectories :

		lifetimes.append( element.lifetime() )

	return lifetimes

# load all the trajectories identified by pattern in path which do not exceed max_frame (which marks end of movie, or significant photobleaching)

abp1_with_sla1 = load_directory(
		path = '../Trajectories/140506_3074/' ,
		pattern = 'W1data.txt$' ,
		comment_char = '%' ,
		dt = 0.2715 ,
		t_unit = 's' ,
		coord_unit = 'pxl' ,
		frames = 0 ,
		coord = ( 1 , 2 ) ,
		f = 3 ,
		protein = 'Abp1-mCherry' 
		)

abp1_with_sla1_lifetimes = measure_average_lifetime( abp1_with_sla1 )
abp1_with_sla1_lifetime_mean = [ np.mean( abp1_with_sla1_lifetimes ) , np.std( abp1_with_sla1_lifetimes ) ]
abp1_with_sla1_lifetime_median = [ np.nanmedian( abp1_with_sla1_lifetimes ) , MAD( abp1_with_sla1_lifetimes ) ]

abp1_with_myo3 = load_directory(
		path = '../Trajectories/160601_3459/' ,
		pattern = 'W1data.txt$' ,
		comment_char = '%' ,
		dt = 0.2715 ,
		t_unit = 's' ,
		coord_unit = 'pxl' ,
		frames = 0 ,
		coord = ( 1 , 2 ) ,
		f = 3 ,
		protein = 'Abp1-mCherry'
		)

abp1_with_myo3_lifetimes = measure_average_lifetime( abp1_with_myo3 )
abp1_with_myo3_lifetime_mean = [ np.mean( abp1_with_myo3_lifetimes ) , np.std( abp1_with_myo3_lifetimes ) ]
abp1_with_myo3_lifetime_median = [ np.nanmedian( abp1_with_myo3_lifetimes ) , MAD( abp1_with_myo3_lifetimes ) ]

abp1_with_myo5 = load_directory(
		path = '../Trajectories/160601_3151/' ,
		pattern = 'W1data.txt$' ,
		comment_char = '%' ,
		dt = 0.2715 ,
		t_unit = 's' ,
		coord_unit = 'pxl' ,
		frames = 0 ,
		coord = ( 1 , 2 ) ,
		f = 3 ,
		protein = 'Abp1-mCherry'
		)

abp1_with_myo5_lifetimes = measure_average_lifetime( abp1_with_myo5 )
abp1_with_myo5_lifetime_mean = [ np.mean( abp1_with_myo5_lifetimes ) , np.std( abp1_with_myo5_lifetimes ) ]
abp1_with_myo5_lifetime_median = [ np.nanmedian( abp1_with_myo5_lifetimes ) , MAD( abp1_with_myo5_lifetimes ) ]

print( abp1_with_sla1_lifetime_mean )
print( abp1_with_myo3_lifetime_mean )
print( abp1_with_myo5_lifetime_mean )

print( abp1_with_sla1_lifetime_median )
print( abp1_with_myo3_lifetime_median )
print( abp1_with_myo5_lifetime_median )

