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

def ctrlifetimes( path , dt , how , protein_name , pattern , cutoff = ( 1 , np.inf ) , comment_char = '%' , t_unit = 's' , coord_unit = 'pxl' , frames = 0 , coord = ( 1 , 2 ) , f = 3 ) :

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

	ml = measure_lifetimes( l , min_cutoff = cutoff[ 0 ] , max_cutoff = cutoff[ 1 ] )
	al = average_lifetime( ml , how )

	return( { 'average' : al , 'lifetimes' : ml , 'name' : protein_name } )

def significance( c1 , c2 ) :

	p = stats.mannwhitneyu( c1[ 'lifetimes' ] , c2[ 'lifetimes' ] )

	print( 'H0: the distribution of ' + c1[ 'name' ] + ' is equal to the distribution of ' + c2[ 'name' ] + '. P value = ' + str( p[ 1 ] ) )

	return p 

def barplot( l , filename , figsize , ylabel , reference = [ ] , x_rotation = 0 ) :

	# l is a list of ctralifetimes outputs
	# it can be that a user inputs a tuple instead
	l = list( l ) 

	g , ( barplot ) = plt.subplots( 1 , 1 , gridspec_kw = { 'height_ratios' : [ 1 ] , 'width_ratios' : [ 1 ] } , figsize = figsize )

	#reference (f), if present,  is the first bar
	if len( reference ) : 
		
		bplt_x = [ 0 ] + [ i + 1 for i in range( len( l ) ) ]
		bplt_y = [ reference[ 'average' ][ 0 ] ] + [ i[ 'average' ][ 0 ] for i in l ]
		bplt_yerr = [ reference[ 'average' ][ 1 ] ] + [ i[ 'average' ][ 1 ] for i in l ]
		bplt_names = [ reference[ 'name' ] ] + [ i[ 'name' ] for i in l ]

	else :

		bplt_x = [ i + 1 for i in range( len( l ) ) ]
		bplt_y = [ i[ 'average' ][ 0 ] for i in l ]
		bplt_yerr = [ i[ 'average' ][ 1 ] for i in l ]
		bplt_names = [ i[ 'name' ] for i in l ]

	barplot.bar( bplt_x , bplt_y , yerr = bplt_yerr , color = 'grey' , ecolor = 'black' )

	plt.subplot( barplot )
	
	xaxt = [ 0 ]

	plt.text( 0 , 1 , "n=" + str( len( reference[ 'lifetimes' ] ) ) , horizontalalignment = 'center' )

	for i in  range( len( l ) ):
		
		xaxt.append( i + 1 )

		plt.text( i + 1 , 1 , "n=" + str( len( l[ i ][ 'lifetimes' ] ) ) , horizontalalignment = 'center' )

	plt.ylabel( ylabel ) 
	barplot.set_xticks( xaxt )
	barplot.set_xticklabels( bplt_names , rotation = x_rotation )

	g.savefig( filename )

def write_csv( path , data ) :

	"""
	write_csv: write the lifetimes in the result dictionary outputs of ctrlifetimes, inputed as a tuple, into a csv file named path.
	The path includes the file name but not .csv, which is added automatically by the script
	""" 
	
	f = open( path + '.csv' , "w" )

	header = ""
	data_len = []
	l = len( data )

	for i in range( l ) : 

		header = header + data[ i ][ 'name' ] + "," 
		data_len.append( len( data[ i ][ 'lifetimes' ] ) )
	
	f.write( header )
	f.write( "\n" )

	m = max( data_len )  
	
	for i in range( m ) :

		line = ""

		for ii in range( l ) :
	
			try :
	
				line = line + str( data[ ii ][ 'lifetimes' ][ i ] ) + "," 
	
			except :
	
				line = line + "" + ","

		f.write( line )
		f.write( "\n" )
	
	f.close()

	
	
	

