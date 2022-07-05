namespace SpriteKind {
    export const P2 = SpriteKind.create()
    export const PROJECTILE_EMMITTER = SpriteKind.create()
}
controller.player2.onButtonEvent(ControllerButton.B, ControllerButtonEvent.Pressed, function () {
    BLAST_WAVE(false, true)
})
controller.combos.attachCombo("U D U D", function () {
    blockSettings.writeNumber("SID", 0)
})
controller.player2.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
        . . . . . . . . 
        . . . . . . . . 
        . . . . . . . . 
        . . . . . . . . 
        . . . 2 2 . . . 
        . . . 2 2 . . . 
        . . . 2 2 . . . 
        . . . 2 2 . . . 
        `, SHIP2, 0, -140)
    projectile.startEffect(effects.coolRadial, 100)
})
controller.combos.attachCombo("ba", function () {
    gonna_die = 0
})
controller.combos.attachCombo("a+b", function () {
    game.splash("POINTS SPENT:", " " + ("" + SPENT))
})
controller.combos.attachCombo("ab", function () {
    gonna_die = 1
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite3, otherSprite3) {
    scene.cameraShake(4, 500)
    otherSprite3.destroy(effects.spray)
    sprite3.startEffect(effects.fire, 200)
    if (DRAW_SCORE == 0) {
        info.changeLifeBy(-1)
    } else {
        info.changeScoreBy(-1)
    }
})
sprites.onOverlap(SpriteKind.P2, SpriteKind.Enemy, function (sprite, otherSprite) {
    scene.cameraShake(4, 500)
    otherSprite.destroy(effects.spray)
    sprite.startEffect(effects.fire, 200)
    if (DRAW_SCORE == 0) {
        info.changeLifeBy(-1)
    } else {
        info.changeScoreBy(-1)
    }
})
controller.player2.onEvent(ControllerEvent.Disconnected, function () {
    SHIP2.destroy()
})
function PANIC (ERROR_CODE: number, DESC: string, CRASH: boolean) {
    if (CRASH) {
        game.splash("ERROR: " + ERROR_CODE + " DESC: " + DESC)
        game.reset()
    } else {
        game.splash("ERROR: " + ERROR_CODE + " DESC: " + DESC)
    }
    console.logValue("ERROR: " + DESC + " ERROR CODE:", ERROR_CODE)
}
info.onLifeZero(function () {
    INCEREMENT_SID__END_GAME()
})
controller.player1.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
        . . . . . . . . 
        . . . . . . . . 
        . . . . . . . . 
        . . . . . . . . 
        . . . 7 7 . . . 
        . . . 7 7 . . . 
        . . . 7 7 . . . 
        . . . 7 7 . . . 
        `, ship, 0, -140)
    projectile.startEffect(effects.coolRadial, 100)
})
controller.combos.attachCombo("D U D U", function () {
    blockSettings.writeNumber("SID", 1)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite2, otherSprite2) {
    sprite2.destroy()
    otherSprite2.destroy(effects.spray)
    info.changeScoreBy(1)
})
controller.player2.onEvent(ControllerEvent.Connected, function () {
    if (_2_PLAYER == 1) {
        SHIP2 = sprites.create(img`
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
            `, SpriteKind.P2)
        controller.player2.moveSprite(SHIP2, 100, 100)
        SHIP2.bottom = 120
        SHIP2.setStayInScreen(true)
        info.setLife(6)
    }
})
controller.player1.onButtonEvent(ControllerButton.B, ControllerButtonEvent.Pressed, function () {
    if (BLAST_WAVE_ENABLED == true) {
        BLAST_WAVE(true, true)
    }
})
controller.combos.attachSpecialCode(function () {
    story.startCutscene(function () {
        story.showPlayerChoices("EXIT MENUE", "USE 2 PLAYER", "POINT CONVERTER", "MORE")
        if (story.checkLastAnswer("USE 2 PLAYER")) {
            _2_PLAYER = 1
        }
        if (story.checkLastAnswer("POINT CONVERTER")) {
            info.changeLifeBy(info.score())
            SPENT += info.score()
            info.setScore(info.score() - info.life() + 1)
        }
        if (story.checkLastAnswer("MORE")) {
            story.showPlayerChoices("EXIT MENUE", "SAVE OPTIONS", "GET CONSOLE", "OTHER")
            if (story.checkLastAnswer("SAVE OPTIONS")) {
                story.showPlayerChoices("EXIT MENUE", "", "SAVE SCORE", "LOAD SAVE")
                if (story.checkLastAnswer("SAVE SCORE")) {
                    blockSettings.writeNumber("SAVED SCORE", info.score())
                }
                if (story.checkLastAnswer("LOAD SAVE")) {
                    info.setScore(blockSettings.readNumber("SAVED SCORE"))
                }
            }
            if (story.checkLastAnswer("OTHER")) {
                story.showPlayerChoices("EXIT MENUE", "SCORE OR LIFE", "ENABLE SIMULATOR FEATURES")
                if (story.checkLastAnswer("SCORE OR LIFE")) {
                    story.showPlayerChoices("EXIT MENUE", "SCORE", "LIFE")
                    if (story.checkLastAnswer("SCORE")) {
                        DRAW_SCORE = 1
                        info.changeScoreBy(1)
                    }
                    if (story.checkLastAnswer("LIFE")) {
                        DRAW_SCORE = 0
                    }
                } else if (story.checkLastAnswer("ENABLE SIMULATOR FEATURES")) {
                    game.splash("WARNING: THIS MAY BADLY LAG YOUR GAME ON ARCADE DEVICES")
                    if (game.ask("ARE YOU SHURE")) {
                        BLAST_WAVE_ENABLED = true
                        game.splash("SIM FEATURES ENABLED")
                    }
                }
            }
        }
    })
})
function INCEREMENT_SID__END_GAME () {
    blockSettings.writeNumber("SID", blockSettings.readNumber("SID") + 1)
    game.over(false)
}
function BLAST_WAVE (_1_OR_2: boolean, TXT_DISPLAY: boolean) {
    if (BLAST_WAVE_ENABLED) {
        if (TXT_DISPLAY) {
            textSprite = textsprite.create("DEATH RAY!! ACTIVE")
            textSprite.setPosition(70, 50)
        }
        if (_1_OR_2) {
            SCREEN_PROGRESS = 0
            mySprite = sprites.create(img`
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
                `, SpriteKind.PROJECTILE_EMMITTER)
            mySprite.setPosition(0, ship.y)
            for (let index = 0; index < scene.screenWidth(); index++) {
                projectile2 = sprites.createProjectileFromSprite(img`
                    . . . . . . . . 
                    . . . . . . . . 
                    . . . . . . . . 
                    . . . . . . . . 
                    . . . 7 . . . . 
                    . . . 7 . . . . 
                    . . . 7 . . . . 
                    . . . 7 . . . . 
                    `, mySprite, 0, -140)
                mySprite.setPosition(SCREEN_PROGRESS, ship.y)
                SCREEN_PROGRESS += 1
            }
            projectile2.startEffect(effects.coolRadial, 100)
            if (TXT_DISPLAY) {
                pause(1000)
                textSprite.destroy()
            }
        } else {
            SCREEN_PROGRESS = 0
            mySprite = sprites.create(img`
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
                `, SpriteKind.PROJECTILE_EMMITTER)
            mySprite.setPosition(0, SHIP2.y)
            for (let index = 0; index < scene.screenWidth(); index++) {
                projectile2 = sprites.createProjectileFromSprite(img`
                    . . . . . . . . 
                    . . . . . . . . 
                    . . . . . . . . 
                    . . . . . . . . 
                    . . . 7 7 . . . 
                    . . . 7 7 . . . 
                    . . . 7 7 . . . 
                    . . . 7 7 . . . 
                    `, mySprite, 0, -140)
                mySprite.setPosition(SCREEN_PROGRESS, SHIP2.y)
                SCREEN_PROGRESS += 1
            }
            projectile2.startEffect(effects.coolRadial, 100)
            if (TXT_DISPLAY) {
                pause(1000)
                textSprite.destroy()
            }
        }
    } else {
        PANIC(1, "ATTEMPT TO RENDER DEATH RAY RESULTED IN BAD VAR RETURN BOOL", true)
    }
}
controller.combos.attachCombo("D D U U", function () {
    if (game.ask("DEBUG CRASH GAME?", "THIS WILL CRASH YOUR GAME")) {
        gonna_die = 0
        BLAST_WAVE(true, true)
    }
})
let projectile2: Sprite = null
let mySprite: Sprite = null
let SCREEN_PROGRESS = 0
let textSprite: TextSprite = null
let _2_PLAYER = 0
let DRAW_SCORE = 0
let SPENT = 0
let SHIP2: Sprite = null
let projectile: Sprite = null
let ship: Sprite = null
let BLAST_WAVE_ENABLED = false
let gonna_die = 0
let GAME_SPEED = 500
let IMPORT_SCORE = 0
gonna_die = 1
BLAST_WAVE_ENABLED = false
let asteroids = [
sprites.space.spaceSmallAsteroid1,
sprites.space.spaceSmallAsteroid0,
sprites.space.spaceAsteroid0,
sprites.space.spaceAsteroid1,
sprites.space.spaceAsteroid4,
sprites.space.spaceAsteroid3
]
ship = sprites.create(img`
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
    `, SpriteKind.Player)
ship.setStayInScreen(true)
ship.bottom = 120
controller.player1.moveSprite(ship, 100, 100)
info.setLife(9)
effects.starField.startScreenEffect()
game.onUpdateInterval(GAME_SPEED, function () {
    if (gonna_die == 1) {
        projectile = sprites.createProjectileFromSide(asteroids[randint(0, asteroids.length - 1)], 0, 75)
        projectile.setKind(SpriteKind.Enemy)
        projectile.x = randint(10, 150)
    }
})
game.onUpdate(function () {
    if (info.score() == 0 && DRAW_SCORE == 1) {
        INCEREMENT_SID__END_GAME()
    }
})
game.onUpdateInterval(2000, function () {
    if (GAME_SPEED <= 100) {
        BLAST_WAVE(true, false)
    }
})
forever(function () {
	
})
forever(function () {
	
})
