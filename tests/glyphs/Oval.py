import numpy as np

from bokeh.document import Document
from bokeh.models import ColumnDataSource, DataRange1d, Plot, LinearAxis, Grid
from bokeh.models.glyphs import Oval
from bokeh.plotting import show

N = 9
x = np.linspace(-2, 2, N)
y = x**2

source = ColumnDataSource(dict(x=x, y=y))

xdr = DataRange1d(sources=[source.columns("x")])
ydr = DataRange1d(sources=[source.columns("y")])

plot = Plot(
    title=None, x_range=xdr, y_range=ydr, plot_width=300, plot_height=300,
    h_symmetry=False, v_symmetry=False, min_border=0, toolbar_location=None)

glyph = Oval(x="x", y="y", width=0.4, height=0.6, angle=-0.7, fill_color="#1d91d0")
plot.add_glyph(source, glyph)

xaxis = LinearAxis()
plot.add_layout(xaxis, 'below')

yaxis = LinearAxis()
plot.add_layout(yaxis, 'left')

plot.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
plot.add_layout(Grid(dimension=1, ticker=yaxis.ticker))

doc = Document()
doc.add(plot)

show(plot)