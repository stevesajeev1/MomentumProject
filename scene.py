from manim import *

# set-ExecutionPolicy Unrestricted

# Definition of Momentum
class Definition(Scene):
    def construct(self):
        title = Text("Momentum", font_size=100)
        self.play(Write(title), run_time=3)
        self.play(title.animate.scale(0.5).move_to(UP * 3.5))
        definition = Text("The momentum of an object is the product of its mass and its velocity. It is a vector quantity.", font_size=25).next_to(title, DOWN * 4)
        definition[38:42].set_color(BLUE)
        definition[48:56].set_color(BLUE)
        self.play(AddTextLetterByLetter(definition), run_time=7)
        equation = MathTex(r"\overrightarrow{p}=", r"m", r"\cdot", r"\overrightarrow{v}", font_size=50).next_to(definition, DOWN * 3)
        mass = definition[38:42].copy()
        velocity = definition[48:56].copy()
        self.play(FadeIn(equation[0]))
        self.play(Transform(mass, equation[1]), FadeIn(equation[2]))
        self.play(Transform(velocity, equation[3]))
        self.wait()
        units = Tex("Its units are ", r"$kg\frac{m}{s}$", " or ", r"$Ns$", font_size=50).next_to(equation, DOWN * 4)
        self.play(Create(units))
        self.wait(3)

# Impulse-Momentum Theory Definition
class ImpulseMomentum(Scene):
    def construct(self):
        title = Text("Impulse-Momentum Theorem", font_size=70)
        self.play(Write(title), run_time=3)
        self.play(title.animate.scale(5/7).move_to(UP * 3.5))
        definition = Text("The change in momentum of an object is equal to the impulse applied on it.", font_size=25).next_to(title, DOWN * 4)
        definition[3:19].set_color(BLUE)
        definition[31:36].set_color(YELLOW)
        definition[41:48].set_color(GREEN)
        derivation = Text("It can be derived from Newton's Second Law of Motion.", font_size=25).next_to(definition, DOWN * 2)
        equation = MathTex(r"\overrightarrow{F}", r"=", r"m", r"\overrightarrow{a}", font_size=50).next_to(derivation, DOWN * 5)
        acceleration = MathTex(r"\overrightarrow{F}", r"=", r"m", r"\frac{\Delta v}{\Delta t}", font_size=50).move_to(equation)
        simplification = MathTex(r"\overrightarrow{F}", r"=", r"\frac{m\Delta v}{\Delta t}", font_size=50).move_to(acceleration)
        momentum = MathTex(r"\overrightarrow{F}", r"=", r"\frac{\Delta p}{\Delta t}", font_size=50).move_to(simplification)
        self.play(AddTextLetterByLetter(definition), run_time=5)
        self.play(AddTextLetterByLetter(derivation), FadeIn(equation), run_time=3)
        self.wait(0.5)
        accelerationExplained = MathTex(r"(\overrightarrow{a}=\frac{\Delta\overrightarrow{v}}{\Delta t})", font_size=30).set_opacity(0.5).next_to(equation, DOWN * 3)
        self.play(FadeIn(accelerationExplained), TransformMatchingTex(equation, acceleration))
        self.wait(2)
        simplificationExplained = Text(r"(Move m to the numerator)", font_size=20).set_opacity(0.5).move_to(accelerationExplained)
        self.play(FadeTransform(accelerationExplained, simplificationExplained), ReplacementTransform(acceleration[2:], simplification[2]))
        self.clear()
        self.add(title, definition, derivation, simplification, simplificationExplained)
        self.wait(2)
        momentumExplained = MathTex(r"(m\Delta\overrightarrow{v}=\Delta\overrightarrow{p})", font_size=30).set_opacity(0.5).move_to(simplificationExplained)
        self.play(FadeTransform(simplificationExplained, momentumExplained), TransformMatchingTex(simplification, momentum))
        self.wait(2)
        finalExplained = Text(r"(Rearrange the equation for momentum)", font_size=20).set_opacity(0.5).move_to(momentumExplained)
        time = MathTex(r"\Delta t").move_to(momentum[2]).shift(DOWN * 0.31)
        finalRHS = MathTex(r"\Delta\overrightarrow{p}").move_to(momentum[2])
        self.add(time)
        path = ArcBetweenPoints(time.get_center(), finalRHS.get_center() + LEFT * 1.35, angle=-PI/2)
        self.play(FadeTransform(momentumExplained, finalExplained), MoveAlongPath(time, path), FadeTransform(momentum[2], finalRHS), momentum[0].animate.shift(LEFT*0.5), run_time=1.5)
        self.wait(2)
        impulseBox = SurroundingRectangle(Group(momentum[0], time)).set_color(GREEN)
        impulseText = Text("Impulse", font_size=20).next_to(Group(momentum[0], time), DOWN).set_color(GREEN)
        self.play(Create(impulseBox), FadeIn(impulseText), FadeOut(finalExplained))
        self.wait()
        momentumBox = SurroundingRectangle(finalRHS).set_color(BLUE)
        momentumText = Text("Momentum", font_size=20).next_to(finalRHS, DOWN).set_color(BLUE)
        self.play(Create(momentumBox), FadeIn(momentumText))
        self.wait(2)
        application = Text("This means that the area under a force-time graph is equal to impulse.", font_size=25).next_to(equation, DOWN * 5)
        application[16:41].set_color(BLUE)
        application[43:48].set_color(YELLOW)
        application[50:57].set_color(GREEN)
        self.play(AddTextLetterByLetter(application))
        self.wait()

# Impulse-Momentum Theory Graph
class ImpulseMomentumGraph(Scene):
    def calcArea(self, min, max):
        return -(max**2 * (110 * max**4 - 1836 * max**3 + 2895 * max**2 + 82740 * max - 377640)/10080) - -(min**2 * (110 * min**4 - 1836 * min**3 + 2895 * min**2 + 82740 * min - 377640)/10080)

    def construct(self):
        title = Text("Impulse-Momentum Theorem", font_size=50).move_to(UP * 3.5)
        self.add(title)
        ax = Axes(
            x_range=[0, 8], 
            y_range=[-20, 60, 10], 
            x_axis_config={"numbers_to_include": np.arange(0, 8, 1)},
            y_axis_config={"numbers_to_include": np.arange(-20, 60, 10)}
        ).next_to(title, DOWN * 0.5).scale(0.7)
        labels = ax.get_axis_labels(x_label="t (s)", y_label=MathTex(r"\overrightarrow{F} (N)"))
        self.play(FadeIn(ax, labels))
        force_graph = ax.plot(lambda x: -11/168 * x**5 + 51/56 * x**4 - 193/168 * x**3 - 197/8 * x**2 + 1049/14 * x, x_range=[0, 8], use_smoothing=False, color=GREEN)
        self.play(Create(force_graph), run_time=5, rate_func=linear)
        self.wait()
        t = ValueTracker(0)
        # integral of force_graph equation
        momentum = MathTex(r"\overrightarrow{F}\Delta t = \Delta\overrightarrow{p} = ", font_size=40).shift(DOWN * 2.6)
        decimal = DecimalNumber(0, num_decimal_places=1, unit="N s", font_size=40).next_to(momentum, RIGHT)
        decimal.add_updater(lambda d: d.set_value(self.calcArea(0, t.get_value())))
        area = always_redraw(lambda: ax.get_area(force_graph, x_range=[0, t.get_value()], color=BLUE, opacity=0.5))
        area1 = DecimalNumber(self.calcArea(0, 3.939), num_decimal_places=1, unit="N s", font_size=35).move_to(force_graph.get_center() + LEFT * 2.4 + UP * 0.5)
        area2 = DecimalNumber(self.calcArea(3.939, 6.613), num_decimal_places=1, unit="N s", font_size=30).move_to(force_graph.get_center() + RIGHT * 1.3 + DOWN * 1.55)
        area3 = DecimalNumber(self.calcArea(6.613, 8), num_decimal_places=1, unit="N s", font_size=25).move_to(force_graph.get_center() + RIGHT * 3.7 + DOWN * 0.55)
        self.play(FadeIn(area, momentum, decimal))
        self.wait()
        self.play(t.animate.set_value(3.939), run_time=5, rate_func=linear)
        self.play(FadeIn(area1, run_time=1), t.animate.set_value(6.613), run_time=5, rate_func=linear)
        self.play(FadeIn(area2, run_time=1), t.animate.set_value(8), run_time=5, rate_func=linear)
        self.play(FadeIn(area3, run_time=1))
        self.wait(11)

# Conservation of momentum
class ConservationMomentum(Scene):
    def construct(self):
        title = Text("Conservation of Momentum", font_size=70)
        self.play(Write(title), run_time=3)
        self.play(title.animate.scale(5/7).move_to(UP * 3.5))
        definition = Text("The total momentum of any closed, isolated system is a constant.", font_size=25).next_to(title, DOWN * 5)
        definition[21:36].set_color(YELLOW)
        definition[45:53].set_color(BLUE)
        equation = MathTex(r"\Sigma \overrightarrow{p_{initial}} = \Sigma \overrightarrow{p_{final}}", font_size=50).next_to(definition, DOWN * 3)
        self.play(AddTextLetterByLetter(definition), run_time=5)
        self.play(FadeIn(equation))
        self.wait()
        application = Text("This means that momentum is conserved in ALL isolated collisions, including both inelastic and elastic collisions.", font_size=20).next_to(equation, DOWN * 5)
        application[34:37].set_color(YELLOW)
        self.play(AddTextLetterByLetter(application), run_time=7)
        self.wait(3)

# Collisions
class Collisions(Scene):
    def construct(self):
        title = Text("Collisions", font_size=100)
        self.play(Write(title), run_time=3)
        self.play(title.animate.scale(0.5).move_to(UP * 3.5))
        definition = Text("There are two types of collisions: inelastic and elastic.", font_size=25).next_to(title, DOWN * 4)
        definition[29:38].set_color(BLUE)
        definition[41:48].set_color(GREEN)
        self.play(AddTextLetterByLetter(definition), run_time=3)
        self.wait()
        inelastic = Text("- Perfectly Inelastic Collision: Kinetic energy is not conserved in the collision and objects stick together.", font_size=20).next_to(definition, DOWN * 2)
        inelasticEquation = MathTex(r"m_1v_{1, i} + m_2v_{2, i} = (m_1 + m_2)v_f", font_size=40).next_to(inelastic, DOWN)
        inelastic[1:28].set_color(BLUE)
        inelastic[44:56].set_color(YELLOW)
        inelastic[73:93].set_color(YELLOW)
        elastic = Text("- Perfectly Elastic Collision: Kinetic energy is conserved in the collision and objects \"bounce\" off eachother.", font_size=20).next_to(inelasticEquation, DOWN * 2)
        elasticEquation1 = MathTex(r"m_1v_{1, i} + m_2v_{2, i} = m_1v_{1, f} + m_2v_{2, f}", font_size=40).next_to(elastic, DOWN)
        elasticEquation2 = MathTex(r"\frac{1}{2}m_1v_{1, i}^2 + \frac{1}{2}m_2v_{2, i}^2 = \frac{1}{2}m_1v_{1, f}^2 + \frac{1}{2}m_2v_{2, f}^2", font_size=40).next_to(elasticEquation1, DOWN)
        elastic[1:26].set_color(GREEN)
        elastic[42:51].set_color(YELLOW)
        elastic[75:95].set_color(YELLOW)
        self.play(AddTextLetterByLetter(inelastic), run_time=7)
        self.wait()
        self.play(FadeIn(inelasticEquation))
        self.wait(3)
        self.play(AddTextLetterByLetter(elastic), run_time=7)
        self.wait()
        self.play(FadeIn(elasticEquation1))
        self.wait(2)
        self.play(FadeIn(elasticEquation2))
        self.wait()
    
# Inelastic Collision
class Inelastic(Scene):
    def construct(self):
        title = Text("Inelastic Collision", font_size=50).move_to(UP * 3.5)
        self.add(title)
        object1 = Square(side_length=1, fill_opacity=1, fill_color=RED).next_to(title, DOWN * 5).shift(LEFT * 4)
        label1 = always_redraw(lambda: Text("1", font_size=30).move_to(object1.get_center()))
        object2 = Square(side_length=1, fill_opacity=1, fill_color=PURPLE).next_to(title, DOWN * 5)
        label2 = always_redraw(lambda: Text("2", font_size=30).move_to(object2.get_center()))
        self.play(DrawBorderThenFill(object1))
        self.play(FadeIn(label1))
        self.play(DrawBorderThenFill(object2))
        self.play(FadeIn(label2))
        self.wait()
        velocity1initial = always_redraw(lambda: Arrow(buff=0, start=object1.get_center() + RIGHT * 0.1, end=object1.get_center() + RIGHT * 1.6, stroke_width=4, max_tip_length_to_length_ratio=0.2).set_color(BLUE))
        self.add(velocity1initial)
        self.play(object1.animate.move_to(object2).shift(LEFT * 1), run_time=2, rate_func=linear)
        self.remove(velocity1initial)
        velocity1final = always_redraw(lambda: Arrow(buff=0, start=object1.get_center() + RIGHT * 0.1, end=object1.get_center() + RIGHT * 0.85, stroke_width=4, max_tip_length_to_length_ratio=0.4).set_color(GREEN))
        velocity2final = always_redraw(lambda: Arrow(buff=0, start=object2.get_center() + RIGHT * 0.1, end=object2.get_center() + RIGHT * 0.85, stroke_width=4, max_tip_length_to_length_ratio=0.4).set_color(GREEN))
        self.add(velocity1final, velocity2final)
        self.play(object1.animate.shift(RIGHT * 4), object2.animate.shift(RIGHT * 4), run_time=4, rate_func=linear)
        self.play(FadeOut(object1, object2, velocity1final, velocity2final, label1, label2), run_time=2)
        velocity1initial.clear_updaters()
        velocity1final.clear_updaters()
        velocity2final.clear_updaters()
        object1.shift(LEFT * 4)
        object2.shift(LEFT * 4)
        label1.shift(LEFT * 4)
        label2.shift(LEFT * 4)
        initial = Text("Initial:", font_size=30).move_to(ORIGIN).shift(LEFT * 1.5)
        self.play(FadeIn(object1, object2, label1, label2, velocity1initial, initial))
        self.wait()
        initialMomentum = velocity1initial.copy()
        self.play(initialMomentum.animate.next_to(initial, RIGHT), run_time=2)
        self.wait()
        self.play(FadeOut(object1, object2, label1, label2, velocity1initial))
        object1.shift(RIGHT * 4)
        object2.shift(RIGHT * 4)
        label1.shift(RIGHT * 4)
        label2.shift(RIGHT * 4)
        final = Text("Final:", font_size=30).move_to(ORIGIN + DOWN).shift(LEFT * 1.5)
        self.play(FadeIn(object1, object2, label1, label2, velocity1final, velocity2final, final))
        self.wait()
        finalMomentum1 = velocity1final.copy()
        finalMomentum2 = velocity2final.copy()
        self.play(finalMomentum1.animate.next_to(initial, RIGHT + DOWN * 3), finalMomentum2.animate.next_to(initial, RIGHT * 4 + DOWN * 3), run_time=3)
        self.wait()
        self.play(FadeOut(object1, object2, label1, label2, velocity1final, velocity2final))
        self.wait()
        comparison = VGroup(initial, initialMomentum, final, finalMomentum1, finalMomentum2)
        self.play(comparison.animate.scale(1.25).shift(UP * 2.5))
        verticalLine1 = DashedLine(start=initialMomentum.get_corner(UL), end=finalMomentum1.get_corner(DL))
        verticalLine2 = DashedLine(start=initialMomentum.get_corner(UR), end=finalMomentum2.get_corner(DR))
        self.play(Create(verticalLine1), run_time=2)
        self.play(Create(verticalLine2), run_time=2)
        self.wait()
        momentumConserved = Text("Momentum is conserved!", font_size=25).next_to(comparison, DOWN * 2.25)
        velocity1 = MathTex(r"v_0", font_size=20).set_color(BLUE).move_to(initialMomentum.get_center() + UP * 0.1)
        velocity2 = MathTex(r"\frac{v_0}{2}", font_size=20).set_color(GREEN).move_to(finalMomentum1.get_center() + UP * 0.25 + LEFT * 0.1)
        velocity3 = MathTex(r"\frac{v_0}{2}", font_size=20).set_color(GREEN).move_to(finalMomentum2.get_center() + UP * 0.25 + LEFT * 0.1)
        momentumConserved[8:10].set_color(YELLOW)
        momentumEquation = MathTex(r"`\begin{gathered}m_1v_{1, i} + m_2v_{2, i} = (m_1 + m_2)v_f\\ m_1v_0 = (m_1 + m_2)v_f \end{gathered}`", font_size=25).set_opacity(0.5).next_to(momentumConserved, DOWN)
        self.play(AddTextLetterByLetter(momentumConserved))
        self.play(FadeIn(velocity1, velocity2, velocity3, momentumEquation), run_time=2)
        self.wait(2)
        initialKinetic = MathTex(r"K_0 = \frac{1}{2}m{v_1}^2", font_size=35).next_to(momentumEquation, DOWN * 1.5)
        substitutedInitialKinetic = MathTex(r"K_0 = \frac{1}{2}m", r"{v_0}", r"^2", font_size=35).next_to(momentumEquation, DOWN * 1.5)
        substitutedInitialKinetic[1].set_color(BLUE)
        finalKinetic = MathTex(r"K_f = \frac{1}{2}m{v_1}^2 + \frac{1}{2}m{v_2}^2", font_size=35).next_to(initialKinetic, DOWN)
        substitutedFinalKinetic = MathTex(r"K_f = \frac{1}{2}m", r"{\frac{v_0}{2}}", r"^2 + \frac{1}{2}m", r"{\frac{v_0}{2}}", r"^2", font_size=35).next_to(initialKinetic, DOWN * 1.25)
        substitutedFinalKinetic[1].set_color(GREEN)
        substitutedFinalKinetic[3].set_color(GREEN)
        completeFinalKinetic = MathTex(r"K_f = \frac{1}{4}m", r"{v_0}", r"^2", font_size=35).next_to(initialKinetic, DOWN * 1.25)
        completeFinalKinetic[1].set_color(GREEN)
        self.play(FadeIn(initialKinetic, finalKinetic), run_time=2)
        self.wait()
        self.play(TransformMatchingTex(initialKinetic, substitutedInitialKinetic))
        self.wait(2)
        self.play(Create(SurroundingRectangle(substitutedInitialKinetic, color=BLUE)))
        self.wait(2)
        self.play(TransformMatchingTex(finalKinetic, substitutedFinalKinetic))
        self.wait(3)
        self.play(TransformMatchingTex(substitutedFinalKinetic, completeFinalKinetic))
        self.wait(2)
        self.play(Create(SurroundingRectangle(completeFinalKinetic, color=GREEN)))
        self.wait(2)
        kineticConserved = Text("Kinetic Energy is not conserved!", font_size=25).next_to(completeFinalKinetic, DOWN)
        kineticConserved[13:18].set_color(YELLOW)
        self.play(AddTextLetterByLetter(kineticConserved))
        self.wait()

# Elastic Collision
class Elastic(Scene):
    def construct(self):
        title = Text("Elastic Collision", font_size=50).move_to(UP * 3.5)
        self.add(title)
        object1 = Square(side_length=1, fill_opacity=1, fill_color=RED).next_to(title, DOWN * 5).shift(LEFT * 4)
        label1 = always_redraw(lambda: Text("1", font_size=30).move_to(object1.get_center()))
        object2 = Square(side_length=1, fill_opacity=1, fill_color=PURPLE).next_to(title, DOWN * 5)
        label2 = always_redraw(lambda: Text("2", font_size=30).move_to(object2.get_center()))
        self.play(DrawBorderThenFill(object1))
        self.play(FadeIn(label1))
        self.play(DrawBorderThenFill(object2))
        self.play(FadeIn(label2))
        self.wait()
        velocity1initial = always_redraw(lambda: Arrow(buff=0, start=object1.get_center() + RIGHT * 0.1, end=object1.get_center() + RIGHT * 1.6, stroke_width=4, max_tip_length_to_length_ratio=0.2).set_color(BLUE))
        self.add(velocity1initial)
        self.play(object1.animate.move_to(object2).shift(LEFT * 1), run_time=2, rate_func=linear)
        self.remove(velocity1initial)
        velocity2final = always_redraw(lambda: Arrow(buff=0, start=object2.get_center() + RIGHT * 0.1, end=object2.get_center() + RIGHT * 1.6, stroke_width=4, max_tip_length_to_length_ratio=0.2).set_color(GREEN))
        self.add(velocity2final)
        self.play(object2.animate.shift(RIGHT * 4), run_time=2, rate_func=linear)
        self.play(FadeOut(object1, object2, velocity2final, label1, label2), run_time=2)
        velocity1initial.clear_updaters()
        velocity2final.clear_updaters()
        object2.shift(LEFT * 4)
        label2.shift(LEFT * 4)
        initial = Text("Initial:", font_size=30).move_to(ORIGIN).shift(LEFT * 1.5)
        self.play(FadeIn(object1, object2, label1, label2, velocity1initial, initial))
        self.wait()
        initialMomentum = velocity1initial.copy()
        self.play(initialMomentum.animate.next_to(initial, RIGHT), run_time=2)
        self.wait()
        self.play(FadeOut(object1, object2, label1, label2, velocity1initial))
        object2.shift(RIGHT * 4)
        label2.shift(RIGHT * 4)
        final = Text("Final:", font_size=30).move_to(ORIGIN + DOWN).shift(LEFT * 1.5)
        self.play(FadeIn(object1, object2, label1, label2, velocity2final, final))
        self.wait()
        finalMomentum = velocity2final.copy()
        self.play(finalMomentum.animate.next_to(initial, RIGHT + DOWN * 3), run_time=3)
        self.wait()
        self.play(FadeOut(object1, object2, label1, label2, velocity2final))
        self.wait()
        comparison = VGroup(initial, initialMomentum, final, finalMomentum)
        self.play(comparison.animate.scale(1.25).shift(UP * 2.5))
        verticalLine1 = DashedLine(start=initialMomentum.get_corner(UL), end=finalMomentum.get_corner(DL))
        verticalLine2 = DashedLine(start=initialMomentum.get_corner(UR), end=finalMomentum.get_corner(DR))
        self.play(Create(verticalLine1), run_time=2)
        self.play(Create(verticalLine2), run_time=2)
        self.wait()
        momentumConserved = Text("Momentum is conserved!", font_size=25).next_to(comparison, DOWN * 2.25)
        velocity1 = MathTex(r"v_0", font_size=20).set_color(BLUE).move_to(initialMomentum.get_center() + UP * 0.1)
        velocity2 = MathTex(r"v_0", font_size=20).set_color(GREEN).move_to(finalMomentum.get_center() + UP * 0.1)
        momentumConserved[8:10].set_color(YELLOW)
        momentumEquation = MathTex(r"`\begin{gathered}m_1v_{1, i} + m_2v_{2, i} = m_1v_{1, f} + m_2v_{2, f}\\ m_1v_0 = m_2v_f \end{gathered}`", font_size=25).set_opacity(0.5).next_to(momentumConserved, DOWN)
        self.play(AddTextLetterByLetter(momentumConserved))
        self.play(FadeIn(velocity1, velocity2, momentumEquation), run_time=2)
        self.wait(2)
        initialKinetic = MathTex(r"K_0 = \frac{1}{2}m{v_1}^2", font_size=35).next_to(momentumEquation, DOWN * 1.5)
        substitutedInitialKinetic = MathTex(r"K_0 = \frac{1}{2}m", r"{v_0}", r"^2", font_size=35).next_to(momentumEquation, DOWN * 1.5)
        substitutedInitialKinetic[1].set_color(BLUE)
        finalKinetic = MathTex(r"K_f = \frac{1}{2}m{v_1}^2", font_size=35).next_to(initialKinetic, DOWN)
        substitutedFinalKinetic = MathTex(r"K_f = \frac{1}{2}m", r"{v_0}", r"^2", font_size=35).next_to(initialKinetic, DOWN * 1.25)
        substitutedFinalKinetic[1].set_color(GREEN)
        self.play(FadeIn(initialKinetic, finalKinetic), run_time=2)
        self.wait()
        self.play(TransformMatchingTex(initialKinetic, substitutedInitialKinetic))
        self.wait(2)
        self.play(Create(SurroundingRectangle(substitutedInitialKinetic, color=BLUE)))
        self.wait(2)
        self.play(TransformMatchingTex(finalKinetic, substitutedFinalKinetic))
        self.wait(2)
        self.play(Create(SurroundingRectangle(substitutedFinalKinetic, color=GREEN)))
        self.wait(2)
        kineticConserved = Text("Kinetic Energy is conserved!", font_size=25).next_to(substitutedFinalKinetic, DOWN)
        kineticConserved[13:15].set_color(YELLOW)
        self.play(AddTextLetterByLetter(kineticConserved))
        self.wait()

# Credits
class Credits(Scene):
    def construct(self):
        title = Text("Credits", font_size=100)
        self.play(Write(title), run_time=3)
        self.play(title.animate.scale(0.5).move_to(UP * 3.5))
        steveText = Text("Steve Sajeev", font_size=70, color=BLUE)
        steveRole = Text("Animations, Project Planner", font_size=20).next_to(steveText, DOWN * 0.8)
        steve = VGroup(steveText, steveRole)
        self.play(FadeIn(steveText))
        self.play(Circumscribe(steveText, Circle))
        self.play(AddTextLetterByLetter(steveRole))
        self.wait()
        self.play(steve.animate.shift(LEFT * 12))
        amritText = Text("Amrit Vignesh", font_size=70, color=YELLOW)
        amritRole = Text("Voiceover/Script of Overview of Momentum + Elastic Collision, Editing", font_size=20).next_to(amritText, DOWN * 0.8)
        amrit = VGroup(amritText, amritRole)
        self.play(FadeIn(amritText))
        self.play(Circumscribe(amritText, Circle))
        self.play(AddTextLetterByLetter(amritRole))
        self.wait()
        self.play(amrit.animate.shift(RIGHT * 12))
        pranavText = Text("Pranav Eada", font_size=70, color=GREEN)
        pranavRole = Text("Voiceover/Script of Conservation of Momentum, Collisions, and Inelastic Collision", font_size=20).next_to(pranavText, DOWN * 0.8)
        pranav = VGroup(pranavText, pranavRole)
        self.play(FadeIn(pranavText))
        self.play(Circumscribe(pranavText, Circle))
        self.play(AddTextLetterByLetter(pranavRole))
        self.wait()
        self.play(pranav.animate.shift(UP * 12))
        sharonText = Text("Sharon Sajeev", font_size=70, color=PURPLE)
        sharonRole = Text("Voiceover/Script of Impulse-Momentum Theory and Graph", font_size=20).next_to(sharonText, DOWN * 0.8)
        sharon = VGroup(sharonText, sharonRole)
        self.play(FadeIn(sharonText))
        self.play(Circumscribe(sharonText, Circle))
        self.play(AddTextLetterByLetter(sharonRole))
        self.wait()
        self.play(sharon.animate.shift(DOWN * 12))
        steve.scale(0.6)
        amrit.scale(0.6)
        pranav.scale(0.6)
        sharon.scale(0.6)
        stevePath = ArcBetweenPoints(steve.get_center(), title.get_center() + DOWN * 1.5, angle=2 * PI/4)
        amritPath = ArcBetweenPoints(amrit.get_center(), title.get_center() + DOWN * 3, angle= -5 * PI/4)
        pranavPath = ArcBetweenPoints(pranav.get_center(), title.get_center() + DOWN * 4.5, angle=-PI)
        sharonPath = ArcBetweenPoints(sharon.get_center(), title.get_center() + DOWN * 6, angle=PI)
        self.play(MoveAlongPath(steve, stevePath))
        self.play(MoveAlongPath(amrit, amritPath))
        self.play(MoveAlongPath(pranav, pranavPath))
        self.play(MoveAlongPath(sharon, sharonPath))
        code = Text("(Animation code found at https://github.com/stevesajeev1/MomentumProject)", font_size=20).set_opacity(0.5).next_to(sharon, DOWN)
        self.play(FadeIn(code))
        self.wait()