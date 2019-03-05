from trajalign.traj import Traj
from trajalign.average import load_directory
from trajalign.average import nanMAD as MAD
from matplotlib import pyplot as plt
from scipy import stats
import numpy as np

def measure_lifetimes( list_of_trajectories , min_cutoff = 3 , max_cutoff = 125 ):

	#measure_lifetimes of the trajectories in the list

	lifetimes = []

	for element in list_of_trajectories :

		if ( element.frames()[ 0 ] > min_cutoff ) & ( element.frames()[ len( element ) - 1 ] < max_cutoff ) :

			lifetimes.append( element.lifetime() )

	return lifetimes

def average_lifetime( l , how ) :

	#average the lifetime of the trajectories

	if how == 'mean' or how == 'Mean' :

		a = [ np.mean( l ) , np.std( l ) / np.sqrt( len( l ) ) ]

	elif how == 'median' or how == 'Median' :
		
		a = [ np.nanmedian( l ) , MAD( l ) / np.sqrt( len( l ) ) ]

	else : 

		print( 'how must be either [mM]ean or [mM]edian' )

	return a 

def ctrlifetimes( path , dt , how , protein_name , cutoff = ( - np.inf , np.inf ) , pattern = 'W1data' , comment_char = '%' , t_unit = 's' , coord_unit = 'pxl' , frames = 0 , coord = ( 1 , 2 ) , f = 3 ) :

	#wrapper to load the trajectories and compute their average_lifetime

	l = load_directory( 
			path = path , 
			pattern = pattern ,
			comment_char = comment_char , 
			dt = dt ,
			t_unit = t_unit , 
			frames = frames ,
			coord = coord ,
			coord_unit = coord_unit ,
			f = f , 
			protein = protein_name
			)

	ml = measure_lifetimes( l , min_cutoff = cutoff[ 0 ] , max_cutoff = [ 1 ] )
	 
	al = average_lifetime( ml , how )

	return( { 'average' : al , 'lifetimes' : ml , 'name' : protein_name } )

def barplot( l , filename , figsize ) :

	# l is a list of ctralifetimes outputs

	g , ( barplot ) = plt.subplots( 1 , 1 , gridspec_kw = { 'height_ratios' : [ 1 , 1 ] } , figsize = figsize )

	barplot.bar( [ i + 1 for i in len( l ) ] , [ i[ 'average' ][ 0 ] for i in l ] , yerr = [ i[ 'average' ][ 1 ] for i in l ] , color = 'grey' , ecolor = 'black' )

	plt.subplot( barplot )
	xaxt = []
	for i in  range( len( l ) ):

		plt.text( i + 1.4 , 1 , "n=" + str( len( l[ i ][ 'lifetimes' ] ) ) , horizontalalignment = 'center' )
		xaxt.append( i + 1.4 )

	plt.ylabel( "Abp1-mCherry lifetime (s)" ) 
	barplot.set_xticks( xaxt )
	barplot.set_xticklabels( [ i[ 'name' ] for i in l ] )

	g.savefig( filename )
