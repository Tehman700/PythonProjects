


    while is_ggg:
        time.sleep(speed_increase)
        scr.update()
        barrr.create()
        barrr.moving()


        if tim.ycor() > 280:
            scoreboard.increase()
            tim.setposition(0,-280)
            speed_increase -=0.01
            time.sleep(speed_increase)
            scoreboard.check_highscore()
            

        for eacg in barrr.all_bars:
            if eacg.distance(tim) < 20:
                tim.setposition(0,-280)
                scoreboard.drrr()
                speed_increase = 0.1
                time.sleep(speed_increase)
                scoreboard.check_highscore()
            
            