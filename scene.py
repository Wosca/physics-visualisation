from manim import *

class ProjectileRunUp(Scene):
    def construct(self):
        # Define the ledge (1m above the ground)
        ledge = Line(start=[-3, 1, 0], end=[0, 1, 0], color=WHITE)
        ground = Line(start=[-3, -0.1, 0], end=[5, -0.1, 0], color=GREEN)
        self.play(Create(ledge), Create(ground))
        
        # Create a ball (the projectile) starting from the left
        ball = Dot(point=[-3, 1.2, 0], color=RED)
        self.play(FadeIn(ball))
        
        # Animation: Ball runs up to the edge of the ledge
        run_up_distance = 3  # Distance from the start point to the edge
        run_up_speed = 1  # Speed in m/s
        run_up_time = run_up_distance / run_up_speed

        self.play(ball.animate.move_to([0, 1.2, 0]), run_time=run_up_time)
        
        # Define the motion path for the projectile after leaving the ledge
        g = 9.8  # Acceleration due to gravity in m/s^2
        initial_speed = 2  # Horizontal speed in m/s
        height_of_ledge = 1  # Ledge height in meters

        # Time to hit the ground: solving for y = 0 when y(t) = height_of_ledge - (1/2) * g * t^2
        fall_time = np.sqrt(2 * height_of_ledge / g)

        # Horizontal distance traveled: x = initial_speed * fall_time
        horizontal_distance = initial_speed * fall_time

        # Trajectory for falling motion
        def get_projectile_trajectory(t):
            x = initial_speed * t  # Horizontal velocity remains constant
            y = 1.2 - 0.5 * g * t**2  # Vertical position with gravity (start at 1.2m)
            return np.array([x, y, 0])

        trajectory = ParametricFunction(
            lambda t: get_projectile_trajectory(t),
            t_range=[0, fall_time], color=YELLOW
        )
        
        # Animate the ball along the trajectory after falling off the ledge
        self.play(Create(trajectory))
        self.play(MoveAlongPath(ball, trajectory, run_time=fall_time))

        # Display the horizontal distance traveled
        distance_text = MathTex(f"\\text{{Distance traveled: }} {horizontal_distance:.2f} \\text{{m}}")
        distance_text.to_edge(UP)
        self.play(Write(distance_text))

        # Fade out
        self.play(FadeOut(ball, ledge, ground, trajectory, distance_text))

