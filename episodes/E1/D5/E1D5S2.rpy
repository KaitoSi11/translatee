label E1D5S2:


"I pull out my phone and start browsing technology articles."
"There's one about a new simulator at a nearby arcade. The game gives us a chance to check out prototypes that aren't tested or distributed yet. Plus the weaponry sounds wicked! It would be worth taking a look." 
"I grab my bike and head to the arcade." 

label E1D5S2_ArcadeConvergence:

stop ambient fadeout 1.5
stop music fadeout 1.5
scene black with fade
$renpy.pause(1.0)


play ambient "audio/ambience/Arcade.ogg" fadein 3
play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 3
$renpy.pause(1.5)

scene bg activity arcade day with fade

"It looks busy, but most of the people are crowded around one particular simulator, watching an intense match." 
"In the rightmost seat, there's a gelatinous looking guy about my age. He's got a determined look on his chubby face and shouts a string of non-stop taunts and insults at his opposing player." 

"The machine dings as his most recent challenger is knocked out in a few short minutes." 
show gosunerd extra at cc with dissolve
voice "audio/voice/E1/D5/S2/GosuArcade/1.ogg"
fk "Hahaha! Another one bites the dust! Who's next?" 
"His eyes scan the surrounding crowd, but no one steps forward." 

menu: 
    "I'll take a crack at it!" :
        pf "Looks like fun! I could have a go." 
        show gosunerd extra with dissolve:
            xzoom -1
        $renpy.pause(.25)
        "His gaze falls on me and narrows as he gives me a once over." 
        voice "audio/voice/E1/D5/S2/GosuArcade/2.ogg"
        fk "It's your funeral." 
        pf "Can't we just have a friendly game?" 
        voice "audio/voice/E1/D5/S2/GosuArcade/3.ogg"
        fk "Says the loser." 
        pf "What ever happened to sportsmanship?" 
        voice "audio/voice/E1/D5/S2/GosuArcade/4.ogg"
        fk "Sit down and I'll show you."

    "Only the best player around.":
        pf "I'll be next. The game is calling to me." 
        show gosunerd extra with dissolve:
            xzoom -1
        $renpy.pause(.25)
        voice "audio/voice/E1/D5/S2/GosuArcade/5.ogg"
        fk "Calling for you to lose." 
        pf "I can only hear calls to win. That must be for you."
        voice "audio/voice/E1/D5/S2/GosuArcade/6.ogg"
        fk "I don't lose!" 
        pf "There's always a first for everything." 

    "I'm next.": 
        pf "My turn." 
        show gosunerd extra with dissolve:
            xzoom -1
        $renpy.pause(.25)
        voice "audio/voice/E1/D5/S2/GosuArcade/7.ogg"
        fk "Your turn to lose." 
        pf "We'll see." 
        "He opens his mouth to retort but I give him a hard glare." 
        pf "Are we talking or playing?" 
        voice "audio/voice/E1/D5/S2/GosuArcade/8.ogg"
        fk "Playing!" 

    "Don't challenge him.":
        hide gosunerd extra with dissolve
        "I didn't come here to feed the trolls. I came here to practice."
        "After finding an empty simulator station, I start a game."
        stop music fadeout 3.0
        stop ambient fadeout 3.0
        scene black with fade
        scene bg battleground night with fade
        show mc mech at bl with dissolve:
            xzoom -1
        show arM neu at br with dissolve
        $renpy.pause(2.5)
        #Gameplay (EASIER THAN CHALLENGING TROLL, BUT LESSER ITEMS)
        $ enemy = "arM"
        $ mode = "default"
        $ context = "E1D5S2_SoloComplete"
        
        $ mcEnergyMax = 200
        $ mcEnergy = 200
        $ enemyHPMax = 125
        $ enemyHP = 125
        
        $ survived = 0
        $ E1D5S2Score = 0
        $ E1D5S2_SoloWon = 0
        # Default means using all possilbe moves. Use 'survived' to add to this sequence's score
        play music "audio/music/Fight Song 1 (GAME VERSION).ogg"
        $ qtebase = 10
        $ qtereaction = qteath + qtetrack + qtebase
        $ qtetotal = qtereaction
        $ t_var = qtereaction
        
        show screen battle_screen
        #show screen timer_scrReaction(place="E1D5S2_SoloComplete")
        jump qte_game
        label E1D5S2_SoloComplete:
        $ E1D5S2Score = survived
        #if you score really high, you'll get a good item
        #if you score low, you'll get a mediocre item.
        if enemyHP < 0:
            $ E1D5S2_SoloWon = 1
                
        $renpy.pause(2.5)
        $ renpy.hide_screen ("battle_screen")
        scene black with fade
        play ambient "audio/ambience/Arcade.ogg" fadein 3
        play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 3
        $renpy.pause(1.5)
        scene bg activity arcade day with fade
        "I shut down the simulator."
        $ E1D5S2Score = survived
        if (E1D5S2_SoloWon == 1):
            "Heh, still got it."

        else:
            "Hm, guess it's a good thing I came here to practice."

        "Exiting the simulator, I glance around the arcade. There's still a group of people crowded around the annoying guy, who's still baiting the group with taunts."
        "I've had enough practice for one day and don't feel like listening to him, so I head out of the arcade and go home."
        stop music fadeout 3.0
        stop ambient fadeout 3.0
        scene black with fade

        $renpy.pause(1.0)
        jump E1D5S7


        
hide gosunerd extra with dissolve
"He turns back to the simulator. I take my place and boot up the screen." 
stop music fadeout 3.0
stop ambient fadeout 3.0

scene black with fade
scene bg battleground night with fade
show mc mech at bl with dissolve:
    xzoom -1
show arM neu at br with dissolve
$renpy.pause(2.5)
#Game Play
play music "audio/music/Fight Song 1 (GAME VERSION).ogg" fadein 2
$ enemy = "arM"
$ mode = "default"
$ context = "E1D5S2_DuelComplete"

$ mcEnergyMax = 200
$ mcEnergy = 200
$ enemyHPMax = 150
$ enemyHP = 150

$ survived = 0
$ qtebase = 10
$ qtereaction = qteath + qtetrack + qtebase
$ qtetotal = qtereaction
$ t_var = qtereaction

$ E1D5S2Score = 0
$ E1D5S2_ArcadeMatchWon = 0
# Default means using all possilbe moves. Use 'survived' to add to this sequence's score
show screen battle_screen
#show screen timer_scrReaction(place="E1D5S2_DuelComplete")
jump qte_game
label E1D5S2_DuelComplete:
$ E1D5S2Score = survived
#If you score really high, you'll get a great item
#if you score low, you get nothing
if enemyHP < 0:
    $ E1D5S2_ArcadeMatchWon = 1
$ E1D5S2Score = survived
$renpy.pause(2.5)
$ renpy.hide_screen ("battle_screen")
scene black with fade
if (E1D5S2_ArcadeMatchWon == 1):

    play ambient "audio/ambience/Arcade.ogg" fadein 3
    play music "audio/music/Rivals (GAME VERSION).ogg" fadein 3
    $renpy.pause(1.5)
    
    scene bg activity arcade day with fade
    
    "My screen lights up with flashing words indicating me as the winner." 
    
    show exclamation:
        xoffset 720
        yoffset 70
        xzoom .75
        yzoom .75
    show gosunerd extra at cc with dissolve
    voice "audio/voice/E1/D5/S2/GosuArcade/9.ogg"
    fk "No! That's not fair!" 

    menu: 
        "I just got lucky.": 
            "I can't help but grin as I turn towards him." 
            pf "Beginner's luck, I guess." 
            hide gosunerd extra with dissolve
            "He mumbles something I can't quite make out before pushing back from the simulator and storming off. The crowd cheers for my win… {w}Or his loss. {w}It's hard to tell which." 

        "This is what a champion looks like.": 
            pf "You look like a guy who just got his ass handed to him."
            "He narrows his eyes and crosses his thick arms over his chest."
            show vein:
                xoffset 720
                yoffset 70
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D5/S2/GosuArcade/10.ogg"
            fk "You must have cheated!" 
            pf "No need to cheat when you're this good." 
            voice "audio/voice/E1/D5/S2/GosuArcade/11.ogg"
            fk "I'm reporting you for cheating. No one can beat me at this game!" 
            hide gosunerd extra with dissolve
            "The cheering crowd drowns out his half-hearted threat, and he storms away in a huff. I wave after him." 
            pf "Better luck next time!" 

        "Game over.":
            "I look at him but say nothing." 
            "His face has gone beet red and his eyes narrow to slits. I start to leave when he stops me."
            voice "audio/voice/E1/D5/S2/GosuArcade/12.ogg"
            show vein:
                xoffset 720
                yoffset 70
                xzoom .75
                yzoom .75
            fk "Where do you think you're going? We aren't done here!"
            "I glance back at the flashing \"End\" screen."
            pf "Yes, we are."
            hide gosunerd extra with dissolve
            "Then I walk away and leave him to his protests."


    "Slowly, the crowd begins to disperse. The angry nerd is nowhere to be found." 

else:

    play ambient "audio/ambience/Arcade.ogg" fadein 3
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 3
    $renpy.pause(1.5)

    scene bg activity arcade day with fade
    
    show gosunerd extra at cc with dissolve
    "His screen dings obnoxiously, naming him as the winner. {w}He grins smugly." 
    voice "audio/voice/E1/D5/S2/GosuArcade/13.ogg"
    fk "Hmph, guess you're all talk, loser!" 

    menu: 
        "Good Game.":
            pf "Good match." 
            show gosunerd extra:
                xzoom -1
                easein .45 xoffset 325
            "I offer him a congratulatory pat on the shoulder, but he slides away from me."
            voice "audio/voice/E1/D5/S2/GosuArcade/14.ogg"
            fk "Don't touch me, scrub. Your \"bad\" is probably contagious."
            "I pat him anyway and he jerks violently away."
            show vein:
                xoffset 1000
                yoffset 70
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D5/S2/GosuArcade/15.ogg"
            fk "Stop it! You're ruining my mojo!"
            "I shrug, and step away from the simulator."

        "I let you win.":
            pf "You're just lucky I went easy on you." 
            voice "audio/voice/E1/D5/S2/GosuArcade/16.ogg"
            fk "I don't need luck when I'm this skilled." 
            pf "Oh yeah? Play me again and we'll see." 
            "He laughs a nasally guffaw. It reminds me of a choking donkey."
            voice "audio/voice/E1/D5/S2/GosuArcade/17.ogg"
            fk "Haha! No way! I'm not gonna waste any more time on a n00b like you."

        "...":
            "Silently, I turn to leave." 
            voice "audio/voice/E1/D5/S2/GosuArcade/18.ogg"
            fk "Guess you're not such a big shot after all." 
            "Shrugging off his words, I slip out of the simulator."
            voice "audio/voice/E1/D5/S2/GosuArcade/19.ogg"
            fk "Well, aren't you going to say something?"
            "Once he realises I'm not going to answer he tries again."
            voice "audio/voice/E1/D5/S2/GosuArcade/20.ogg"
            fk "You're just upset that you're a loser!" 
            "This guy talks too much."

    show gosunerd extra:
        xzoom 1
        easein .45 xoffset 0
    "He glances around."
    voice "audio/voice/E1/D5/S2/GosuArcade/21.ogg"
    fk "Who's next?"
    "The crowd shuffles in silence while I walk away."
    hide gosunerd extra with dissolve

$renpy.pause(.5)
"I do a quick circle around the arcade, but none of the other games catch my interest. Exiting the building, I find my bike and drive home."


stop music fadeout 3.0
stop ambient fadeout 3.0
scene black with fade

$renpy.pause(1.0)


jump E1D5S7