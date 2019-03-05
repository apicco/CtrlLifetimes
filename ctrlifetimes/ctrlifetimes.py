from trajalign.traj import Traj
from trajalign.average import load_directory
from trajalign.average import nanMAD as MAD
from matplotlib import pyplot as plt
from scipy import stats
import numpy as np

def measure_average_lifetime( list_of_trajectories , min_cutoff = 3 , max_cutoff = 125 ):

	lifetimes = []

	for element in list_of_trajectories :

		if ( element.frames()[ 0 ] > min_cutoff ) & ( element.frames()[ len( element ) - 1 ] < max_cutoff ) :

			lifetimes.append( element.lifetime() )

	return lifetimes

# load all the trajectories identified by pattern in path which do not exceed max_frame (which marks end of movie, or significant photobleaching)

abp1 = load_directory(
		#path = '../Trajectories/130404_mky0154_DW/' ,
		path = '../Trajectories/130409_mky0154_DW/' ,
		pattern = 'W1data' ,
		comment_char = '%' ,
		dt = 0.2715 ,
		t_unit = 's' ,
		coord_unit = 'pxl' ,
		frames = 0 ,
		coord = ( 1 , 2 ) ,
		f = 3 ,
		protein = 'Abp1-mCherry' 
		)

abp1_lifetimes = measure_average_lifetime( abp1 )
abp1_lifetime_mean = [ np.mean( abp1_lifetimes ) , np.std( abp1_lifetimes ) / np.sqrt( len( abp1_lifetimes ) ) ]
abp1_lifetime_median = [ np.nanmedian( abp1_lifetimes ) , MAD( abp1_lifetimes ) / np.sqrt( len( abp1_lifetimes ) ) ]

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
abp1_with_sla1_lifetime_mean = [ np.mean( abp1_with_sla1_lifetimes ) , np.std( abp1_with_sla1_lifetimes ) / np.sqrt( len( abp1_with_sla1_lifetimes ) ) ]
abp1_with_sla1_lifetime_median = [ np.nanmedian( abp1_with_sla1_lifetimes ) , MAD( abp1_with_sla1_lifetimes ) / np.sqrt( len( abp1_with_sla1_lifetimes ) ) ]

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
abp1_with_myo3_lifetime_mean = [ np.mean( abp1_with_myo3_lifetimes ) , np.std( abp1_with_myo3_lifetimes ) / np.sqrt( len( abp1_with_myo3_lifetimes ) ) ]
abp1_with_myo3_lifetime_median = [ np.nanmedian( abp1_with_myo3_lifetimes ) , MAD( abp1_with_myo3_lifetimes ) / np.sqrt( len( abp1_with_myo3_lifetimes ) ) ]

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
abp1_with_myo5_lifetime_mean = [ np.mean( abp1_with_myo5_lifetimes ) , np.std( abp1_with_myo5_lifetimes ) / np.sqrt( len( abp1_with_myo5_lifetimes ) ) ]
abp1_with_myo5_lifetime_median = [ np.nanmedian( abp1_with_myo5_lifetimes ) , MAD( abp1_with_myo5_lifetimes ) / np.sqrt( len( abp1_with_myo5_lifetimes ) ) ]

print( abp1_lifetime_mean )
print( abp1_with_sla1_lifetime_mean )
print( abp1_with_myo3_lifetime_mean )
print( abp1_with_myo5_lifetime_mean )

print( abp1_lifetime_median )
print( abp1_with_sla1_lifetime_median )
print( abp1_with_myo3_lifetime_median )
print( abp1_with_myo5_lifetime_median )

print( 't-test ind')

print( stats.ttest_ind( abp1_lifetimes , abp1_with_sla1_lifetimes ) )
print( stats.ttest_ind( abp1_lifetimes , abp1_with_myo3_lifetimes ) )
print( stats.ttest_ind( abp1_lifetimes , abp1_with_myo5_lifetimes ) )
print( stats.ttest_ind( abp1_with_sla1_lifetimes , abp1_with_myo3_lifetimes ) )
print( stats.ttest_ind( abp1_with_sla1_lifetimes , abp1_with_myo5_lifetimes ) )
print( stats.ttest_ind( abp1_with_myo3_lifetimes , abp1_with_myo5_lifetimes ) )

f , ( ( sla1 , myo3 ) , ( myo5 , abp1 ) ) = plt.subplots( 2 , 2 , gridspec_kw = { 'height_ratios' : [ 1 , 1 ] } , figsize = ( 11 , 11 ) )

sla1.hist( abp1_with_sla1_lifetimes )
myo3.hist( abp1_with_myo3_lifetimes )
myo5.hist( abp1_with_myo5_lifetimes )
abp1.hist( abp1_lifetimes )

plt.subplot( sla1 )
plt.title( "Abp1-mCherry, Sla1-GFP")
plt.xlabel( "Abp1-mCherry lifetime (s)" )
plt.ylabel( "Frequency" )

plt.subplot( myo3 )
plt.title( "Abp1-mCherry, Myo3-GFP")
plt.xlabel( "Abp1-mCherry lifetime (s)" )
plt.ylabel( "Frequency" )

plt.subplot( myo5 )
plt.title( "Abp1-mCherry, Myo5-GFP")
plt.xlabel( "Abp1-mCherry lifetime (s)" )
plt.ylabel( "Frequency" )

plt.subplot( abp1 )
plt.title( "Abp1-mCherry alone")
plt.xlabel( "Abp1-mCherry lifetime (s)" )
plt.ylabel( "Frequency" )

f.savefig( 'hist.pdf' )

g , ( barplot ) = plt.subplots( 1 , 1 , gridspec_kw = { 'height_ratios' : [ 1 , 1 ] } , figsize = ( 7 , 11 ) )

barplot.bar( [ 1 ,2 ,3 ,4 ] , [ abp1_lifetime_median[ 0 ] , abp1_with_sla1_lifetime_median[ 0 ] ,  abp1_with_myo3_lifetime_median[ 0 ] , abp1_with_myo5_lifetime_median[ 0 ] ] , yerr = [ abp1_lifetime_median[ 1 ] , abp1_with_sla1_lifetime_median[ 1 ] ,  abp1_with_myo3_lifetime_median[ 1 ] , abp1_with_myo5_lifetime_median[ 1 ] ] , color = 'grey' , ecolor = 'black' )

plt.subplot( barplot )
plt.text( 1.4 , 1 , "n="+str( len( abp1_lifetimes ) ) , horizontalalignment='center' )
plt.text( 2.4 , 1 , "n="+str( len( abp1_with_sla1_lifetimes ) ) , horizontalalignment='center' )
plt.text( 3.4 , 1 , "n="+str( len( abp1_with_myo3_lifetimes ) ) , horizontalalignment='center' )
plt.text( 4.4 , 1 , "n="+str( len( abp1_with_myo5_lifetimes ) ) , horizontalalignment='center' )
plt.ylabel( "Abp1-mCherry lifetime (s)" ) 
barplot.set_xticks([ 1.4 ,2.4,3.4,4.4])
barplot.set_xticklabels(['Abp1-mCherry','Abp1-mCherry\nSla1-GFP', 'Abp1-mCherry\nMyo3-GFP', 'Abp1-mCherry\nMyo5-GFP'])

g.savefig( 'plot_with_Abp1.pdf' )

h , ( barplot ) = plt.subplots( 1 , 1 , gridspec_kw = { 'height_ratios' : [ 1 , 1 ] } , figsize = ( 7 , 11 ) )

barplot.bar( [ 1 ,2 ,3 ] , [ abp1_with_sla1_lifetime_median[ 0 ] ,  abp1_with_myo3_lifetime_median[ 0 ] , abp1_with_myo5_lifetime_median[ 0 ] ] , yerr = [ abp1_with_sla1_lifetime_median[ 1 ] ,  abp1_with_myo3_lifetime_median[ 1 ] , abp1_with_myo5_lifetime_median[ 1 ] ] , color = 'grey' , ecolor = 'black' )

plt.subplot( barplot )
plt.text( 1.4 , 1 , "n="+str( len( abp1_with_sla1_lifetimes ) ) , horizontalalignment='center' )
plt.text( 2.4 , 1 , "n="+str( len( abp1_with_myo3_lifetimes ) ) , horizontalalignment='center' )
plt.text( 3.4 , 1 , "n="+str( len( abp1_with_myo5_lifetimes ) ) , horizontalalignment='center' )
plt.ylabel( "Abp1-mCherry lifetime (s)" ) 
barplot.set_xticks([ 1.4 ,2.4,3.4 ])
barplot.set_xticklabels(['Abp1-mCherry\nSla1-GFP', 'Abp1-mCherry\nMyo3-GFP', 'Abp1-mCherry\nMyo5-GFP'])

h.savefig( 'plot.pdf' )
