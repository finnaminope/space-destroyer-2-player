@namespace
class SpriteKind:
    P2 = SpriteKind.create()
    PROJECTILE_EMMITTER = SpriteKind.create()

def on_player2_button_b_pressed():
    BLAST_WAVE(False, True)
controller.player2.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player2_button_b_pressed)

def on_combos_attach_combo():
    blockSettings.write_number("SID", 0)
controller.combos.attach_combo("U D U D", on_combos_attach_combo)

def on_player2_button_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . 
                    . . . . . . . . 
                    . . . . . . . . 
                    . . . . . . . . 
                    . . . 2 2 . . . 
                    . . . 2 2 . . . 
                    . . . 2 2 . . . 
                    . . . 2 2 . . .
        """),
        SHIP2,
        0,
        -140)
    projectile.start_effect(effects.cool_radial, 100)
controller.player2.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player2_button_a_pressed)

def on_combos_attach_combo2():
    global gonna_die
    gonna_die = 0
controller.combos.attach_combo("ba", on_combos_attach_combo2)

def on_combos_attach_combo3():
    game.splash("POINTS SPENT:", " " + ("" + str(SPENT)))
controller.combos.attach_combo("a+b", on_combos_attach_combo3)

def on_combos_attach_combo4():
    global gonna_die
    gonna_die = 1
controller.combos.attach_combo("ab", on_combos_attach_combo4)

def on_on_overlap(sprite3, otherSprite3):
    scene.camera_shake(4, 500)
    otherSprite3.destroy(effects.spray)
    sprite3.start_effect(effects.fire, 200)
    if DRAW_SCORE == 0:
        info.change_life_by(-1)
    else:
        info.change_score_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    scene.camera_shake(4, 500)
    otherSprite.destroy(effects.spray)
    sprite.start_effect(effects.fire, 200)
    if DRAW_SCORE == 0:
        info.change_life_by(-1)
    else:
        info.change_score_by(-1)
sprites.on_overlap(SpriteKind.P2, SpriteKind.enemy, on_on_overlap2)

def on_player2_disconnected():
    SHIP2.destroy()
controller.player2.on_event(ControllerEvent.DISCONNECTED, on_player2_disconnected)

def PANIC(ERROR_CODE: number, DESC: str, CRASH: bool):
    if CRASH:
        game.splash("ERROR: " + str(ERROR_CODE) + " DESC: " + DESC)
        game.reset()
    else:
        game.splash("ERROR: " + str(ERROR_CODE) + " DESC: " + DESC)
    console.log_value("ERROR: " + DESC + " ERROR CODE:", ERROR_CODE)

def on_life_zero():
    INCEREMENT_SID__END_GAME()
info.on_life_zero(on_life_zero)

def on_player1_button_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . 
                    . . . . . . . . 
                    . . . . . . . . 
                    . . . . . . . . 
                    . . . 7 7 . . . 
                    . . . 7 7 . . . 
                    . . . 7 7 . . . 
                    . . . 7 7 . . .
        """),
        ship,
        0,
        -140)
    projectile.start_effect(effects.cool_radial, 100)
controller.player1.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player1_button_a_pressed)

def on_combos_attach_combo5():
    blockSettings.write_number("SID", na_n)
controller.combos.attach_combo("D U D U", on_combos_attach_combo5)

def on_on_overlap3(sprite2, otherSprite2):
    sprite2.destroy()
    otherSprite2.destroy(effects.spray)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap3)

def on_player2_connected():
    global SHIP2
    if _2_PLAYER == 1:
        SHIP2 = sprites.create(img("""
                . . . . . . . c d . . . . . . . 
                            . . . . . . . c d . . . . . . . 
                            . . . . . . . c d . . . . . . . 
                            . . . . . . . c b . . . . . . . 
                            . . . . . . . f f . . . . . . . 
                            . . . . . . . c 2 . . . . . . . 
                            . . . . . . . f f . . . . . . . 
                            . . . . . . . e 2 . . . . . . . 
                            . . . . . . e e 4 e . . . . . . 
                            . . . . . . e 2 4 e . . . . . . 
                            . . . . . c c c e e e . . . . . 
                            . . . . e e 2 2 2 4 e e . . . . 
                            . . c f f f c c e e f f e e . . 
                            . c c c c e e 2 2 2 2 4 2 e e . 
                            c c c c c c e e 2 2 2 4 2 2 e e 
                            c c c c c c e e 2 2 2 2 4 2 e e
            """),
            SpriteKind.P2)
        controller.player2.move_sprite(SHIP2, 100, 100)
        SHIP2.bottom = 120
        SHIP2.set_stay_in_screen(True)
        info.set_life(6)
controller.player2.on_event(ControllerEvent.CONNECTED, on_player2_connected)

def on_player1_button_b_pressed():
    if BLAST_WAVE_ENABLED == True:
        BLAST_WAVE(True, True)
controller.player1.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player1_button_b_pressed)

def on_combos_attach_special_code():
    
    def on_start_cutscene():
        global _2_PLAYER, SPENT, DRAW_SCORE, BLAST_WAVE_ENABLED
        story.show_player_choices("EXIT MENUE", "USE 2 PLAYER", "POINT CONVERTER", "MORE")
        if story.check_last_answer("USE 2 PLAYER"):
            _2_PLAYER = 1
        if story.check_last_answer("POINT CONVERTER"):
            info.change_life_by(info.score())
            SPENT += info.score()
            info.set_score(info.score() - info.life() + 1)
        if story.check_last_answer("MORE"):
            story.show_player_choices("EXIT MENUE", "SAVE OPTIONS", "GET CONSOLE", "OTHER")
            if story.check_last_answer("SAVE OPTIONS"):
                story.show_player_choices("EXIT MENUE", "", "SAVE SCORE", "LOAD SAVE")
                if story.check_last_answer("SAVE SCORE"):
                    blockSettings.write_number("SAVED SCORE", info.score())
                if story.check_last_answer("LOAD SAVED SCORE"):
                    info.set_score(blockSettings.read_number("SAVED SCORE"))
            if story.check_last_answer("OTHER"):
                story.show_player_choices("EXIT MENUE", "SCORE OR LIFE", "ENABLE SIMULATOR FEATURES")
                if story.check_last_answer("SCORE OR LIFE"):
                    story.show_player_choices("EXIT MENUE", "SCORE", "LIFE")
                    if story.check_last_answer("SCORE"):
                        DRAW_SCORE = 1
                        info.change_score_by(1)
                    if story.check_last_answer("LIFE"):
                        DRAW_SCORE = 0
                elif story.check_last_answer("ENABLE SIMULATOR FEATURES"):
                    game.splash("WARNING: THIS MAY BADLY LAG YOUR GAME ON ARCADE DEVICES")
                    if game.ask("ARE YOU SHURE"):
                        BLAST_WAVE_ENABLED = True
                        game.splash("SIM FEATURES ENABLED")
    story.start_cutscene(on_start_cutscene)
    
controller.combos.attach_special_code(on_combos_attach_special_code)

def INCEREMENT_SID__END_GAME():
    blockSettings.write_number("SID", blockSettings.read_number("SID") + 1)
    game.over(False)
def BLAST_WAVE(_1_OR_2: bool, TXT_DISPLAY: bool):
    global textSprite, SCREEN_PROGRESS, mySprite, projectile2
    if BLAST_WAVE_ENABLED:
        if TXT_DISPLAY:
            textSprite = textsprite.create("DEATH RAY!! ACTIVE")
            textSprite.set_position(70, 50)
        if _1_OR_2:
            SCREEN_PROGRESS = 0
            mySprite = sprites.create(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . .
                """),
                SpriteKind.PROJECTILE_EMMITTER)
            mySprite.set_position(0, ship.y)
            for index in range(scene.screen_width()):
                projectile2 = sprites.create_projectile_from_sprite(img("""
                        . . . . . . . . 
                                            . . . . . . . . 
                                            . . . . . . . . 
                                            . . . . . . . . 
                                            . . . 7 . . . . 
                                            . . . 7 . . . . 
                                            . . . 7 . . . . 
                                            . . . 7 . . . .
                    """),
                    mySprite,
                    0,
                    -140)
                mySprite.set_position(SCREEN_PROGRESS, ship.y)
                SCREEN_PROGRESS += 1
            projectile2.start_effect(effects.cool_radial, 100)
            if TXT_DISPLAY:
                pause(1000)
                textSprite.destroy()
        else:
            SCREEN_PROGRESS = 0
            mySprite = sprites.create(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . .
                """),
                SpriteKind.PROJECTILE_EMMITTER)
            mySprite.set_position(0, SHIP2.y)
            for index2 in range(scene.screen_width()):
                projectile2 = sprites.create_projectile_from_sprite(img("""
                        . . . . . . . . 
                                            . . . . . . . . 
                                            . . . . . . . . 
                                            . . . . . . . . 
                                            . . . 7 7 . . . 
                                            . . . 7 7 . . . 
                                            . . . 7 7 . . . 
                                            . . . 7 7 . . .
                    """),
                    mySprite,
                    0,
                    -140)
                mySprite.set_position(SCREEN_PROGRESS, SHIP2.y)
                SCREEN_PROGRESS += 1
            projectile2.start_effect(effects.cool_radial, 100)
            if TXT_DISPLAY:
                pause(1000)
                textSprite.destroy()
    else:
        PANIC(1,
            "ATTEMPT TO RENDER DEATH RAY RESULTED IN BAD VAR RETURN BOOL",
            True)

def on_combos_attach_combo6():
    global gonna_die
    if game.ask("DEBUG CRASH GAME?", "THIS WILL CRASH YOUR GAME"):
        gonna_die = 0
        for index3 in range(5):
            BLAST_WAVE(True, True)
controller.combos.attach_combo("D D U U", on_combos_attach_combo6)

projectile2: Sprite = None
mySprite: Sprite = None
SCREEN_PROGRESS = 0
textSprite: TextSprite = None
_2_PLAYER = 0
DRAW_SCORE = 0
SPENT = 0
SHIP2: Sprite = None
projectile: Sprite = None
ship: Sprite = None
BLAST_WAVE_ENABLED = False
gonna_die = 0
GAME_SPEED = 500
IMPORT_SCORE = 0
gonna_die = 1
BLAST_WAVE_ENABLED = False
asteroids = [sprites.space.space_small_asteroid1,
    sprites.space.space_small_asteroid0,
    sprites.space.space_asteroid0,
    sprites.space.space_asteroid1,
    sprites.space.space_asteroid4,
    sprites.space.space_asteroid3]
ship = sprites.create(img("""
        . . . . . . . c d . . . . . . . 
            . . . . . . . c d . . . . . . . 
            . . . . . . . c d . . . . . . . 
            . . . . . . . c b . . . . . . . 
            . . . . . . . f f . . . . . . . 
            . . . . . . . c 7 . . . . . . . 
            . . . . . . . f f . . . . . . . 
            . . . . . . . 8 7 . . . . . . . 
            . . . . . . 8 8 5 6 . . . . . . 
            . . . . . . 8 7 5 6 . . . . . . 
            . . . . . c c c 6 6 6 . . . . . 
            . . . . 8 8 7 7 7 5 6 6 . . . . 
            . . 8 f f f c c 6 6 f f 6 6 . . 
            . 8 8 8 8 6 6 7 7 7 7 5 7 6 6 . 
            8 8 8 8 8 8 6 6 7 7 7 5 7 7 6 6 
            8 8 8 8 8 8 6 6 7 7 7 7 5 7 6 6
    """),
    SpriteKind.player)
ship.set_stay_in_screen(True)
ship.bottom = 120
controller.player1.move_sprite(ship, 100, 100)
info.set_life(3)
effects.star_field.start_screen_effect()

def on_update_interval():
    global projectile
    if gonna_die == 1:
        projectile = sprites.create_projectile_from_side(asteroids[randint(0, len(asteroids) - 1)], 0, 75)
        projectile.set_kind(SpriteKind.enemy)
        projectile.x = randint(10, 150)
game.on_update_interval(GAME_SPEED, on_update_interval)

def on_on_update():
    if info.score() == 0 and DRAW_SCORE == 1:
        INCEREMENT_SID__END_GAME()
game.on_update(on_on_update)

def on_update_interval2():
    if GAME_SPEED <= 100:
        BLAST_WAVE(True, False)
game.on_update_interval(2000, on_update_interval2)

def on_forever():
    console.log_value("TDY", controller.dy(50))
    console.log_value("TDX", controller.dx(50))
    if controller.A.is_pressed():
        console.log_value("A BOTTON PRESSED", 1)
    else:
        console.log_value("A BOTTON PRESSED", 0)
    if controller.B.is_pressed():
        console.log_value("B BOTTON PRESSED", 1)
    else:
        console.log_value("B BOTTON PRESSED", 0)
    console.log_value("SID", blockSettings.read_number("SID"))
forever(on_forever)

def on_forever2():
    print(blockSettings.read_number("SID"))
forever(on_forever2)
