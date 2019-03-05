from distutils.core import setup
from spotquant.measurespots import header

setup( name = 'measre lifetimes' ,
		version = str( header( printit = False ) ),
		description = 'Utilities to quantify trajectories lifetimes' ,
		author = 'Andrea Picco',
		author_email = 'andrea.picco@unige.ch',
		url = 'https://github.com/apicco/CtrlLifetimes',
		download_url = 'https://github.com/apicco/CtrlLifetimes.git',
		packages = [ 'ctrlifetimes' ],
		license = 'The software is distributed under the terms of the GNU General Public License Version 3, June 2007. Trajalign is a free software and comes with ABSOLUTELY NO WARRANTY.'
		)
