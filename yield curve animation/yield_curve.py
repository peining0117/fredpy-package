import dateutil
import fredpy as fp
import matplotlib.pyplot as plt
import matplotlib.dates as dts
import numpy as np

fp.api_key = fp.load_api_key('fred_api_key.txt')

# date example: '1981-01-14'

def yc(date,all_yields=None):

	yields=[]
	if all_yields == None:
		y1m= fp.series('DTB4WK')
		y3m= fp.series('DTB3')
		y6m= fp.series('DTB6')
		y1 = fp.series('DGS1')
		y5 = fp.series('DGS5')
		y10= fp.series('DGS10')
		y20= fp.series('DGS20')
		y30= fp.series('DGS30')

		all_yields = [y1m,y3m,y6m,y1,y5,y10,y20,y30] 

	for n,x in enumerate(all_yields):
		'''A doc string.'''
		try:
			index = x.dates.index(date)
			yields.append(x.data[index])	
		except ValueError:
			index = -1000
			yields.append('NaN')
	yields= np.array(yields)
	y2    = yields.astype(np.double)
	ymask = np.isfinite(y2)
	mat   = np.array([0,1,2,2.5,4,5,5.5,6])
	d1    = dateutil.parser.parse(date)
	d_str = d1.strftime('%B %d, %Y')
	
	return d_str, mat,yields,ymask