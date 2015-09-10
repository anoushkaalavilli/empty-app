from ggame import App
myapp = App()
myapp.run()
from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 0.3)
black = Color(0x000000, 1.0)
thinline = LineStyle(1, black)
rectangle = RectangleAsset(1000, 200, thinline, blue)
Sprite(rectangle)
myapp = App()
myapp.run()