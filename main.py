import time
from snake import Snake, Sscreen
from food import Food
from scoreboard import Scoreboard


def main():
    Screen = Sscreen()
    s = Snake()
    f = Food()
    sb = Scoreboard()
    # Command Snake
    Screen.screen1.listen()
    Screen.screen1.onkey(s.left, "Left")
    Screen.screen1.onkey(s.up, "Up")
    Screen.screen1.onkey(s.right, "Right")
    Screen.screen1.onkey(s.down, "Down")
    # end of command snake

    game_is_on = True
    while game_is_on:
        Screen.screen1.update()
        time.sleep(0.1)

        s.move()

        # Detect food
        if s.head.distance(f) < 15:
            f.refersh()
            s.extend()
            sb.increase_score()
        # end of detect food

        # Detect wall
        if s.head.xcor() >= 361 or s.head.xcor() <= -361 or s.head.ycor() >= 250 or s.head.ycor() <= -250:
            sb.reset()
            s.reset()
        # end of detect wall

        # Detect tail
        for segment in s.segment[1:]:
            if s.head.distance(segment) < 17:
                sb.reset()
                s.reset()

        # end of detect the tail
    Screen.screen1.exitonclick()


if __name__ == "__main__":
    main()
