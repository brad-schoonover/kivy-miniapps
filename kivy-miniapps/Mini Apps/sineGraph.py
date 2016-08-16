import itertools
from math import sin, cos, pi
from kivy.utils import get_color_from_hex as rgb
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from myKivyGarden import MeshLinePlot, Graph, Plot
from kivy.clock import Clock


class TestApp(App):

    def build(self):
        b = BoxLayout(orientation='vertical')
        self.title = "Moving Sine Wave"

        # example of a custom theme
        colors = itertools.cycle([
            rgb('7dac9f'), rgb('dc7062'), rgb('66a8d4'), rgb('e5b060')])
        graph_theme = {
            'label_options': {
                'color': rgb('444444'),  # color of tick labels and titles
                'bold': True},
            'background_color': rgb('f8f8f2'),  # back ground color of canvas
            'tick_color': rgb('808080'),  # ticks and grid
            'border_color': rgb('808080')}  # border drawn around each graph

        graph = Graph(
            xlabel='t',
            ylabel='Y=sin(wt+a)',
            x_ticks_minor=5,
            x_ticks_major=25,
            y_ticks_major=1,
            y_grid_label=True,
            x_grid_label=True,
            padding=5,
            xlog=False,
            ylog=False,
            x_grid=True,
            y_grid=True,
            xmin=-50,
            xmax=50,
            ymin=-1,
            ymax=1,
            **graph_theme)


        plot = MeshLinePlot(color=next(colors))
        plot.points = [(x / 10., sin(x / 50.)) for x in range(-500, 501)]
        graph.add_plot(plot)
        self.plot = plot  # this is the moving graph, so keep a reference

        plot2 = MeshLinePlot(color=next(colors))
        plot2.points = [(x / 10., sin(x / 50.)) for x in range(-500, 501)]
        graph.add_plot(plot2)
        self.plot2 = plot2

        Clock.schedule_interval(self.update_points, 1 / 60.)

        b.add_widget(graph)

        return b


    def update_points(self, *args):
        self.plot.points = [(x / 10., sin(-Clock.get_time() + x / 50.)) for x in range(-500, 501)]
        self.plot2.points = [(x / 10., sin(1-Clock.get_time() + x / 50.)) for x in range(-500, 501)]

if __name__ == "__main__":
    TestApp().run()
