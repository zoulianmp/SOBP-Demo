# sobpplot.py

# Plot SOBP generated by Geant4 (CSV format).

import g4score
import matplotlib as mpl
mpl.use('Agg')
import pylab as pl

def sobpplot(fname):

    x,x2,d = g4score.getxz(fname) 

    title = 'Proton Spread-out Bragg Peak'
    xlabel = 'Depth (mm)'
    ylabel = 'Dose (arbitrary units)'    

    ## Add light grey grid
    pl.figure()
    ax=pl.axes()
    ax.set_axisbelow(True)
    pl.grid(color='lightgrey', zorder=20)

    pl.title(title,weight='bold')
    pl.xlabel(xlabel)
    pl.ylabel(ylabel)

    # Plot out to 140 mm
    x = x[:141]     # Use with Geant4.9.4
    #x = x2[:141]   # Use with Geant4.9.3 
    d = d[:141]

    pl.plot(x,d,linewidth=2)
    pl.savefig('sobp-demo.png')

if __name__ == '__main__':
    import sys

    fname = sys.argv[1]
    sobpplot(fname)
    
