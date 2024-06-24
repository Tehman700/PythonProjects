import turtle
import tkinter
import random
import time
from main_menu_buttons import Button            # FOR THE FOUR BUTTONS
import pygame
from background_music import Music              # FOR BACKGROUND MUSIC
from players import Player,Points
from bullets import Bullet

## ALL THIS BELOW IS FOR THE SCREEN CREATING 
scr = turtle.Screen()
scr.setup(900,600)
scr.title("STREET GANG SHOOTING GAME")
# scr.addshape('user_shooter.gif')
scr.addshape('car3.gif')

scr.bgpic("mainmenu.png")
scr.tracer(0)






# FOR BACKGROUND MUSIC 

Music.playing()

# FOR THE FOUR BUTTONS BY MAKING OBJECTS FROM CLASSES AND SETTING DIFFERENT PARAMETERS FOR EACH BUTTON ALONG X AND Y AXIS
# BECASE TURTLE HAS NO BUILT-IN BUTTON METHOD SO WE USED THIS JUGAAR


easy_button = Button((235-45, 55-15),(270-36,57-10),'EASY')
medium_button = Button((235-45, -20-15),(250-36,-17-10),'MEDIUM')
hard_button = Button((235-45, -95-15),(270-36,-93-10),'HARD')
info_button = Button((235-45, -170-15),(230-36,-167-10),'HOW TO PLAY', letter_size=18)



def clicking(x,y):
    if (235 - 45) < x < (235 + 45) and (55 - 15) < y < (55 + 15):
        scr.clear()
        easy_setup()
    if (235 - 45) < x < (235+45) and (-20-15) < y < (-20+15):
        scr.clear()
        medium_setup()
    if (235 - 45) < x < (235 + 45) and (-95-15) < y < (-95+15):
        scr.clear()
        hard_setup()
    if (235 - 45) < x < (235 + 45) and (-170-15) < y < (-170+15):
        scr.clear()
        information()
    

def easy_setup():
    from turtle import Screen
    import tkinter
    import random
    import time
    from main_menu_buttons import Button            # FOR THE FOUR BUTTONS
    import pygame
    from background_music import Music              # FOR BACKGROUND MUSIC
    from players import Player,Points
    from bullets import Bullet
    from demo import Car



    # I AM CREATING THIS AGAIN BECAUSE INTIALLY BULLET SPEED WAS NOT BEING CONTROLLED BY
    # ME AND WHEN I MADE SOME LITTLE CHANGES THE SPEED WAS INCREASED BUT I MISSED THE PART WHERE IT HAPPENED
    # SO LOL NOW THIS IS WHY IT IS LONG HEHEHEHEH


    scr = Screen()
    scr.setup(width=900, height=600)
    scr.bgpic('shooting_area.png')
    scr.tracer(0)
    points = Points()
    car = Car()


    computer = Player('user_shooter.gif',(-400,0))
    user = Player('computer_shooter.gif',(400,0))
    bullets_user = []
    bullets_comp = []
    scr.onkeypress(user.up,'Up')
    scr.onkeypress(user.down, 'Down')
    scr.onkeypress(user.left, 'Left')
    scr.onkeypress(user.right,'Right')
    scr.onkeypress(computer.up,'w')
    scr.onkeypress(computer.down,'s')
    scr.onkeypress(computer.comp_right,'d')
    scr.onkeypress(computer.comp_left,'a')
    scr.update()

    def shoot_bullet_comp():
        bull_comp = Bullet(computer.player.position(),10,0)
        bullets_comp.append(bull_comp)
        Music.gun_shot()


    def shoot_bullet():
        bull_user1 = Bullet(user.player.position(),-10,0)
        bullets_user.append(bull_user1)
        Music.gun_shot()

    def shoot_burst():
        bull_user1 = Bullet(user.player.position(),-10,0)
        bullets_user.append(bull_user1)

        bull_user2 = Bullet(user.player.position(),-10,0)
        bullets_user.append(bull_user2)

    def burst_fire():
        shoot_burst()
        time.sleep(0.1)
        shoot_burst()
    def display_timer():
        turtle.clear()

        # Calculate current time
        current_time = int(time.time() - start_time)

        # agay use krna prh rha tha as a parmater so it though empty is good
        m = ""


        # Calculate remaining time
        remaining_time = max(0, 120 - current_time)

        # Display the remaining time
        turtle.penup()
        turtle.goto(0, 210)
        turtle.write(f"Time left: {remaining_time} seconds", align="center", font=("Courier", 20, "bold"))
        turtle.pendown()

        # POP UP FOR EVERY TIMER STOP

        if current_time >= 120:
            turtle.clear()
            scr.clear()
            result(m)
            return
       
        # Call the function again after 1 second
        turtle.ontimer(display_timer, 1000)

    turtle.speed(0)
    turtle.hideturtle()
    turtle.Screen().bgcolor("lightblue")

    start_time = time.time()

    display_timer()



    # RESULT FUNCITON DISPLAYS ALL THE RESULTS

    def result(m):
        scr.bgpic("result_background.png")
        
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(0, -67)
        writer.write(m, align="center", font=("Arial", 34, "bold"))

        with open('points.txt', 'r') as file:
            numbers = file.readlines()
            first = int(numbers[0].strip())
            second = int(numbers[1].strip())

        if first> second:
            result_m = f"Shayan Won with {first} Points"
        elif first< second:
            result_m = f"Tehman Won with {second} Points"
        else:
            result_m = "OH NO IT'S A DRAW"
        result(result_m)
        
        





    scr.onkey(shoot_bullet,'f')
    scr.onkey(shoot_bullet_comp,'space')
    scr.onkey(burst_fire, 'b')
    scr.listen()

    def boundary_check(bullet):
        x, y = bullet.bullet.position()
        # FOR CHECKING THE BOUNDARY AT EDGES
        if x > scr.window_width() // 2 or x < -scr.window_width() // 2 or y > scr.window_height() // 2 or y < -scr.window_height() // 2:
            bullet.bullet.hideturtle()
            # Music.men_shot()
            return False
        return True

    game = True
    bullet_speed = 0.0001  



    # ALL BULLET SHOTTING AND MECHANISM WHERE IT IS BEING REMOVED FROM THE LIST, WHEN IT REACHES AT THE END
    # OTHERWISE THE LIST IS APPENDED AGAIN AND AGAIN AND SPEED REDUCES FOT BULLET

    while game:
        time.sleep(bullet_speed)
        scr.update()
        
        for b in bullets_user[:]:
            b.bullet_moving()
            if not boundary_check(b):
                bullets_user.remove(b)
            if b.bullet.distance(computer.player) < 20:
                bullets_user.remove(b)
                b.bullet.hideturtle()
                Music.men_shot()
                points.increase_user_score()
                with open('points.txt', 'r') as file:
                    numbers = file.readlines()
                    second = int(numbers[0].strip())
                    if second > 5:
                        result()
                scr.update()


        for c in bullets_comp[:]:
            c.bullet_moving()
            if not boundary_check(c):
                bullets_comp.remove(c)
            if c.bullet.distance(user.player) < 20:
                bullets_comp.remove(c)
                c.bullet.hideturtle()
                Music.men_shot()
                points.increase_comp_score()
                scr.update()

        
        scr.update()











    scr.exitonclick()






    






def medium_setup():
    from turtle import Screen
    import tkinter
    import random
    import time
    from main_menu_buttons import Button            # FOR THE FOUR BUTTONS
    import pygame
    from background_music import Music              # FOR BACKGROUND MUSIC
    from players import Player,Points
    from bullets import Bullet
    from final import Car


    scr = Screen()
    scr.setup(width=900, height=600)
    scr.bgpic('shooting_area.png')
    scr.tracer(0)
    points = Points()
    car = Car()


    computer = Player('user_shooter.gif',(-400,0))
    user = Player('computer_shooter.gif',(400,0))
    bullets_user = []
    bullets_comp = []
    scr.onkeypress(user.up,'Up')
    scr.onkeypress(user.down, 'Down')
    scr.onkeypress(user.left, 'Left')
    scr.onkeypress(user.right,'Right')
    scr.onkeypress(computer.up,'w')
    scr.onkeypress(computer.down,'s')
    scr.onkeypress(computer.comp_right,'d')
    scr.onkeypress(computer.comp_left,'a')
    scr.update()

    def shoot_bullet_comp():
        bull_comp = Bullet(computer.player.position(),10,0)
        bullets_comp.append(bull_comp)
        Music.gun_shot()


    def shoot_bullet():
        bull_user1 = Bullet(user.player.position(),-10,0)
        bullets_user.append(bull_user1)
        Music.gun_shot()

    def shoot_burst():
        bull_user1 = Bullet(user.player.position(),-10,0)
        bullets_user.append(bull_user1)

        bull_user2 = Bullet(user.player.position(),-10,0)
        bullets_user.append(bull_user2)

    def burst_fire():
        shoot_burst()
        time.sleep(0.1)
        shoot_burst()
    def display_timer():
        # Clear previous content
        turtle.clear()

        current_time = int(time.time() - start_time)
        m = ""
        remaining_time = max(0, 60 - current_time)

        turtle.penup()
        turtle.goto(0, 210)
        turtle.write(f"Time left: {remaining_time} seconds", align="center", font=("Courier", 20, "bold"))
        turtle.pendown()

        if current_time >= 60:
            turtle.clear()
            scr.clear()
            result(m)
            return
       
        turtle.ontimer(display_timer, 1000)

    turtle.speed(0)
    turtle.hideturtle()
    turtle.Screen().bgcolor("lightblue")

    start_time = time.time()

    display_timer()

    def result(m):
        scr.bgpic("result_background.png")
        
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(0, -67)
        writer.write(m, align="center", font=("Arial", 34, "bold"))

        with open('points.txt', 'r') as file:
            numbers = file.readlines()
            first = int(numbers[0].strip())
            second = int(numbers[1].strip())

        if first> second:
            result_m = f"Shayan Won with {first} Points"
        elif first< second:
            result_m = f"Tehman Won with {second} Points"
        else:
            result_m = "OH NO IT'S A DRAW"
        result(result_m)
        
        





    scr.onkey(shoot_bullet,'f')
    scr.onkey(shoot_bullet_comp,'space')
    scr.onkey(burst_fire, 'b')
    scr.listen()

    def boundary_check(bullet):
        x, y = bullet.bullet.position()
        if x > scr.window_width() // 2 or x < -scr.window_width() // 2 or y > scr.window_height() // 2 or y < -scr.window_height() // 2:
            bullet.bullet.hideturtle()
            # Music.men_shot()
            return False
        return True

    game = True
    car_speed = 1  # Adjust car speed here
    bullet_speed = 0.0001  # Adjust bullet speed here

    while game:
        time.sleep(bullet_speed)
        scr.update()
        car.create()
        car.moving(car_speed)
        
        for b in bullets_user[:]:
            b.bullet_moving()
            if not boundary_check(b):
                bullets_user.remove(b)
            if b.bullet.distance(computer.player) < 20:
                bullets_user.remove(b)
                b.bullet.hideturtle()
                Music.men_shot()
                points.increase_user_score()
                with open('points.txt', 'r') as file:
                    numbers = file.readlines()
                    second = int(numbers[0].strip())
                    if second > 5:
                        result()
                scr.update()

            # COLLSIOON WITH CARS FOR IF DETECTED THEN DETUCT ONE POINT AND ALSO REMOVE THAT CAR FROM LIST OR I MEAN ROAD
            for c in car.all_cars[:]:
                if b.bullet.distance(c) < 20:
                    bullets_user.remove(b)
                    b.bullet.hideturtle()
                    car.all_cars.remove(c)
                    c.hideturtle()
                    points.decrease_user_score()  # Decrease user score if their bullet hits the car

        for c in bullets_comp[:]:
            c.bullet_moving()
            if not boundary_check(c):
                bullets_comp.remove(c)
            if c.bullet.distance(user.player) < 20:
                bullets_comp.remove(c)
                c.bullet.hideturtle()
                Music.men_shot()
                points.increase_comp_score()
                scr.update()

            for car_instance in car.all_cars[:]:
                if c.bullet.distance(car_instance) < 20:
                    bullets_comp.remove(c)
                    c.bullet.hideturtle()
                    car.all_cars.remove(car_instance)
                    car_instance.hideturtle()
                    points.decrease_comp_score()  # Decrease computer score if their bullet hits the car

        scr.update()











    scr.exitonclick()
































def hard_setup():
    from turtle import Screen
    import tkinter
    import random
    import time
    from main_menu_buttons import Button            # FOR THE FOUR BUTTONS
    import pygame
    from background_music import Music              # FOR BACKGROUND MUSIC
    from players import Player,Points
    from bullets import Bullet
    from demo import Car, Down


    scr = Screen()
    scr.setup(width=900, height=600)
    scr.bgpic('shooting_area.png')
    scr.tracer(0)
    points = Points()
    car = Car()
    down_car = Down()


    computer = Player('user_shooter.gif',(-400,0))
    user = Player('computer_shooter.gif',(400,0))
    bullets_user = []
    bullets_comp = []
    scr.onkeypress(user.up,'Up')
    scr.onkeypress(user.down, 'Down')
    scr.onkeypress(user.left, 'Left')
    scr.onkeypress(user.right,'Right')
    scr.onkeypress(computer.up,'w')
    scr.onkeypress(computer.down,'s')
    scr.onkeypress(computer.comp_right,'d')
    scr.onkeypress(computer.comp_left,'a')
    scr.update()

    def shoot_bullet_comp():
        bull_comp = Bullet(computer.player.position(),10,0)
        bullets_comp.append(bull_comp)
        Music.gun_shot()


    def shoot_bullet():
        bull_user1 = Bullet(user.player.position(),-10,0)
        bullets_user.append(bull_user1)
        Music.gun_shot()

    def shoot_burst():
        bull_user1 = Bullet(user.player.position(),-10,0)
        bullets_user.append(bull_user1)

        bull_user2 = Bullet(user.player.position(),-10,0)
        bullets_user.append(bull_user2)

    def burst_fire():
        shoot_burst()
        time.sleep(0.1)
        shoot_burst()
    def display_timer():
        turtle.clear()

        current_time = int(time.time() - start_time)
        m = ""
        remaining_time = max(0, 60 - current_time)

        turtle.penup()
        turtle.goto(0, 210)
        turtle.write(f"Time left: {remaining_time} seconds", align="center", font=("Courier", 20, "bold"))
        turtle.pendown()

        if current_time >= 60:
            turtle.clear()
            scr.clear()
            result(m)
            return
       
        turtle.ontimer(display_timer, 1000)

    turtle.speed(0)
    turtle.hideturtle()
    turtle.Screen().bgcolor("lightblue")

    start_time = time.time()

    display_timer()

    def result(m):
        scr.bgpic("result_background.png")
        
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(0, -67)
        writer.write(m, align="center", font=("Arial", 34, "bold"))

        with open('points.txt', 'r') as file:
            numbers = file.readlines()
            first = int(numbers[0].strip())
            second = int(numbers[1].strip())

        if first> second:
            result_m = f"Shayan Won with {first} Points"
        elif first< second:
            result_m = f"Tehman Won with {second} Points"
        else:
            result_m = "OH NO IT'S A DRAW"
        result(result_m)
        
        





    scr.onkey(shoot_bullet,'f')
    scr.onkey(shoot_bullet_comp,'space')
    scr.onkey(burst_fire, 'b')
    scr.listen()

    def boundary_check(bullet):
        x, y = bullet.bullet.position()
        if x > scr.window_width() // 2 or x < -scr.window_width() // 2 or y > scr.window_height() // 2 or y < -scr.window_height() // 2:
            bullet.bullet.hideturtle()
            # Music.men_shot()
            return False
        return True

    game = True
    car_speed = 1  # Adjust car speed here
    bullet_speed = 0.0001  # Adjust bullet speed here

    while game:
        time.sleep(bullet_speed)
        scr.update()
        car.create('car1.gif',(-70, -300))
        car.create('car2.gif',(-200,-300))
        down_car.create_down('car3.gif',(200,300))
        down_car.create_down('car4.gif',(70,300))
        down_car.moving_down(car_speed)
        car.moving(car_speed)
        
        for b in bullets_user[:]:
            b.bullet_moving()
            if not boundary_check(b):
                bullets_user.remove(b)
            if b.bullet.distance(computer.player) < 20:
                bullets_user.remove(b)
                b.bullet.hideturtle()
                Music.men_shot()
                points.increase_user_score()
                with open('points.txt', 'r') as file:
                    numbers = file.readlines()
                    second = int(numbers[0].strip())
                    if second > 5:
                        result()
                scr.update()
            for d in down_car.all_down[:]:
                if b.bullet.distance(d) < 20:
                    bullets_user.remove(b)
                    b.bullet.hideturtle()
                    down_car.all_down.remove(d)
                    d.hideturtle()
                    points.decrease_user_score()
            for c in car.all_cars[:]:
                if b.bullet.distance(c) < 20:
                    bullets_user.remove(b)
                    b.bullet.hideturtle()
                    car.all_cars.remove(c)
                    c.hideturtle()
                    points.decrease_user_score()  # Decrease user score if their bullet hits the car

        for c in bullets_comp[:]:
            c.bullet_moving()
            if not boundary_check(c):
                bullets_comp.remove(c)
            if c.bullet.distance(user.player) < 20:
                bullets_comp.remove(c)
                c.bullet.hideturtle()
                Music.men_shot()
                points.increase_comp_score()
                scr.update()

            # Check collision with cars
            for car_instance in car.all_cars[:]:
                if c.bullet.distance(car_instance) < 20:
                    bullets_comp.remove(c)
                    c.bullet.hideturtle()
                    car.all_cars.remove(car_instance)
                    car_instance.hideturtle()
                    points.decrease_comp_score()  # Decrease computer score if their bullet hits the car
            for carii in down_car.all_down[:]:
                if c.bullet.distance(carii) < 20:
                    bullets_comp.remove(c)
                    c.bullet.hideturtle()
                    down_car.all_down.remove(carii)
                    carii.hideturtle()
                    points.decrease_comp_score()
        scr.update()











    scr.exitonclick()




def information():
    from turtle import Screen


    scr = Screen()
    scr.setup(width=1920, height=1080)
    scr.bgpic('game_manual.png')



turtle.onscreenclick(clicking,1)
turtle.listen()

turtle.done()
scr.exitonclick()