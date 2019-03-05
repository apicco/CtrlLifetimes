# CtrlLifetimes

Measure protein lifetimes in endocytic patches in yeasts from trajectories acquired from microscopy movies.

##How to

_ctrlifetimes( path , dt , how , protein\_name , pattern , cutoff = ( 1 , np.inf ) , comment\_char = '%' , t\_unit = 's' , coord\_unit = 'pxl' , frames = 0 , coord = ( 1 , 2 ) , f = 3 )_ meaures the lifetimes of the '.txt' trajectories in 'path' and outputs a dictionary that is composed by the \'average\', a tuple with the average and its sem, \'lifetimes\', which is the entire datset of lifetimes measured between the 'cutoff', and 'name', a string that names the protein. The input values in ctrlifetimes are input values mostly for 'load\_data' (see the [trajalgin](http://apicco.github.io/trajectory_alignment/) distribution). 
cutoff' is used to exclude the early and last frames of a movie as trajectories that start or end there are likely to be truncated. 

##Example

	from ctrlifetimes.ctrlifetimes import ctrlifetimes as clt
	from ctrlifetimes.ctrlifetimes import barplot 
	
	x = ( 
			clt( path = 'foo.path/protein1/' , dt = 0.2725 , how = 'median' , protein_name = 'Protein1' , pattern = 'foo.txt' ) ,
			clt( path = 'foo.path/protein2/' , dt = 0.2725 , how = 'median' , protein_name = 'Protein2' , pattern = 'foo.txt' ) ,
			clt( path = 'foo.path/protein3/' , dt = 0.2725 , how = 'median' , protein_name = 'Protein3' , pattern = 'foo.txt' ) ,
			clt( path = 'foo.path/protein4/' , dt = 0.2725 , how = 'median' , protein_name = 'Protein4' , pattern = 'foo.txt' ) 
			)
	
	barplot( x , filename = 'foo.pdf', figsize = ( 6 , 5 ) , ylabel = 'Lifetime (s)' )
