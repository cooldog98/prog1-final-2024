class All_process:
    class run_ball:
        import ball
        import random
        def __init__(self, num_ball:int = 5, speed:int = 0, trace:int = 0, time_speed:int = 2):
            import turtle
            self.num_ball = num_ball
            self.speed = speed
            self.trace = trace
            self.time_speed = time_speed
            self.canvas_width = turtle.screensize()[0]
            self.canvas_height = turtle.screensize()[1]


        # def turtle_detall(self):
        #     import turtle
        #     canvas_width = turtle.screensize()[0]
        #     canvas_height = turtle.screensize()[1]
        #     print(canvas_width, canvas_height)

        def num_of_ball(self, xpos, ypos, vx, vy):
            import turtle
            import random
            ball_radius = 0.05 * self.canvas_width
            turtle.colormode(255)
            xpos = []
            ypos = []
            vx = []
            vy = []
            ball_color = []
            for i in range(self.num_ball):
                xpos.append(random.uniform(-1 * self.canvas_width + ball_radius, self.canvas_width - ball_radius))
                ypos.append(random.uniform(-1 * self.canvas_height + ball_radius, self.canvas_height - ball_radius))
                vx.append(10 * random.uniform(-1.0, 1.0))
                vy.append(10 * random.uniform(-1.0, 1.0))
                ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                return xpos, ypos, vx, vy, ball_color

        @property
        def draw_border(self):
            import turtle
            turtle.penup()
            turtle.goto(-(self.canvas_width), -(self.canvas_height))
            turtle.pensize(10)
            turtle.pendown()
            turtle.color((0, 0, 0))
            for i in range(2):
                turtle.forward(2 * self.canvas_width)
                turtle.left(90)
                turtle.forward(2 * self.canvas_height)
                turtle.left(90)

        def while_true(self):
            import turtle
            import ball
            while (True):
                turtle.clear()
                self.run_ball.draw_border
                for i in range(self.num_ball):
                    ball.draw_ball(self.ball_color[i], 0.05 * self.canvas_width, self.xpos[i], self.ypos[i])
                    ball.move_ball(i, self.xpos, self.ypos, self.vx, self.vy, self.time_speed)
                    ball.update_ball_velocity(i, self.xpos, self.ypos, self.vx, self.vy, self.canvas_width,
                                              self.canvas_height, 0.05 * self.canvas_width)
                turtle.update()

    import turtle
    turtle.done()

    class seven_segments_proc:

        def __init__(self):
            pass

        def init(my_turtle, color):
            import turtle
            turtle.speed(0)
            turtle.tracer(0)
            turtle.hideturtle()
            turtle.colormode(255)

            my_turtle.color(color)
            my_turtle.penup()
            my_turtle.setheading(0)
            my_turtle.goto(0, 0)
            my_turtle.pensize(10)

        def draw_0(my_turtle, digit):
            if digit == 0:
                my_turtle.goto(-50, 100)
                my_turtle.pendown()
                my_turtle.forward(100)
                my_turtle.right(90)
                my_turtle.forward(100)
                my_turtle.forward(100)
                my_turtle.right(90)
                my_turtle.forward(100)
                my_turtle.right(90)
                my_turtle.forward(100)
                my_turtle.forward(100)
                my_turtle.right(90)
                my_turtle.penup()

        def draw_1(my_turtle, digit):
            if digit == 1:
                my_turtle.goto(50, 100)
                my_turtle.pendown()
                my_turtle.right(90)
                my_turtle.forward(100)
                my_turtle.forward(100)
                my_turtle.left(90)
                my_turtle.penup()

        def draw_2(my_turtle, digit):
            if digit == 2:
                my_turtle.goto(-50, 100)
                my_turtle.pendown()
                my_turtle.forward(100)
                my_turtle.right(90)
                my_turtle.forward(100)
                my_turtle.right(90)
                my_turtle.forward(100)
                my_turtle.left(90)
                my_turtle.forward(100)
                my_turtle.left(90)
                my_turtle.forward(100)
                my_turtle.penup()

        def draw_3(my_turtle, digit):
            if digit == 3:
                my_turtle.goto(-50, 100)
                my_turtle.pendown()
                my_turtle.forward(100)
                my_turtle.right(90)
                my_turtle.forward(100)
                my_turtle.right(90)
                my_turtle.forward(100)
                my_turtle.forward(-100)
                my_turtle.left(90)
                my_turtle.forward(100)
                my_turtle.right(90)
                my_turtle.forward(100)
                my_turtle.left(90)
                my_turtle.left(90)
                my_turtle.penup()

        def draw_4(my_turtle, digit):
            if digit == 4:
                my_turtle.goto(-50, 100)
                my_turtle.pendown()
                my_turtle.right(90)
                my_turtle.forward(100)
                my_turtle.left(90)
                my_turtle.forward(100)
                my_turtle.left(90)
                my_turtle.forward(100)
                my_turtle.forward(-100)
                my_turtle.forward(-100)
                my_turtle.right(90)
                my_turtle.penup()

        def draw_5(my_turtle, digit):
            if digit == 5:
                my_turtle.goto(-50, 100)
                my_turtle.pendown()
                my_turtle.forward(100)
                my_turtle.forward(-100)
                my_turtle.right(90)
                my_turtle.forward(100)
                my_turtle.left(90)
                my_turtle.forward(100)
                my_turtle.right(90)
                my_turtle.forward(100)
                my_turtle.right(90)
                my_turtle.forward(100)
                my_turtle.left(90)
                my_turtle.left(90)
                my_turtle.penup()

        def draw_6(my_turtle, digit):
            if digit == 6:
                # draw(my_turtle, 5)

                my_turtle.goto(-50, 0)
                my_turtle.pendown()
                my_turtle.right(90)
                my_turtle.forward(100)
                my_turtle.left(90)
                my_turtle.penup()

        def draw_7(my_turtle, digit):
            if digit == 7:
                my_turtle.goto(-50, 100)
                my_turtle.pendown()
                my_turtle.forward(100)
                my_turtle.forward(-100)
                draw(my_turtle, 1)

        def draw_8(my_turtle, digit):
            if digit == 8:
                draw(my_turtle, 0)
                my_turtle.goto(-50, 0)
                my_turtle.pendown()
                my_turtle.forward(100)
                my_turtle.penup()

            if digit == 9:
                draw(my_turtle, 5)
                my_turtle.goto(50, 100)
                my_turtle.pendown()
                my_turtle.right(90)
                my_turtle.forward(100)
                my_turtle.left(90)
                my_turtle.penup()

        def clear(my_turtle):
            my_turtle.clear()

        def my_delay(dt):
            import time
            start = time.time()
            while time.time() - start < dt:
                pass

        Tom = turtle.Turtle()
        tom_color = (255, 0, 0)
        init(Tom, tom_color)
        delay_in_seconds = 0.2
        while True:
            for i in range(0, 10):
                clear(Tom)
                draw(Tom, i)
                my_delay(delay_in_seconds)
                turtle.update()

        turtle.done()
