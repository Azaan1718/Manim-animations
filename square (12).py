from manim import *
class Creation3(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 10, 2],
            x_length=10,
            y_length=5,
            axis_config={"color": WHITE}
        )
        labels = axes.get_axis_labels()
        self.play(Create(axes), Write(labels))

        x_tracker = ValueTracker(7)

        rect = always_redraw(lambda: Rectangle(width=x_tracker.get_value(), height=1/x_tracker.get_value()).move_to(axes.c2p(0, 0), aligned_edge=DL))
        self.add(rect)

        trace = TracedPath(lambda: rect.get_corner(UR), stroke_color=YELLOW, stroke_width=4)
        self.add(trace)

        self.play(x_tracker.animate.set_value(2), run_time=5)
        
        self.wait()

        