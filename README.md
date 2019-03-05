# CtrlLifetimes
Measure protein lifetimes in endocytic patches in yeasts from trajectories acquired from microscopy movies.

#Example
	from ctrlifetimes.ctrlifetimes import ctrlifetimes as clt
	from ctrlifetimes.ctrlifetimes import barplot 
	
	x = ( 
			clt( path = 'foo.path/protein1/' , dt = 0.2725 , how = 'median' , protein_name = 'Protein1' , pattern = 'foo.txt' ) ,
			clt( path = 'foo.path/protein2/' , dt = 0.2725 , how = 'median' , protein_name = 'Protein2' , pattern = 'foo.txt' ) ,
			clt( path = 'foo.path/protein3/' , dt = 0.2725 , how = 'median' , protein_name = 'Protein3' , pattern = 'foo.txt' ) ,
			clt( path = 'foo.path/protein4/' , dt = 0.2725 , how = 'median' , protein_name = 'Protein4' , pattern = 'foo.txt' ) 
			)
	
	barplot( x , filename = 'foo.pdf', figsize = ( 6 , 5 ) , ylabel = 'Lifetime (s)' )
