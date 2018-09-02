label E1D5S1:


play ambient "audio/ambience/Morning.ogg" fadein 3
play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 3
$renpy.pause(1.5)

scene bg homekaito myroom day with fade

"The soft chirping of birds gradually awaken me from my slumber. My muscles scream as I push myself up in bed. It looks like being out of live matches for a while has taken its toll. Still, the pain is a reminder of a well played battle, which is comforting."

pf "9:00 AM."

"With a yawn, I crawl out of bed and ready myself for the day."

stop ambient fadeout 2.0
scene black with fade
$renpy.pause(.5)
scene bg homekaito main day with fade

"I head downstairs expecting to see Nikki."

pf "Hey--"

"No ones here. Weird. I pull out my phone and see a text message from her."

"{i}Hey! I'm going out with some friends for breakfast and then shopping. I was going to tell you in person but you were still sleeping by the time I was heading out, lazybones. =3={/i}"
"{i}Kaito also said he's heading out to an emergency meeting. I know how useless you are when it comes to breakfast, so open the fridge and check the second row. TTYL! ^w^{/i}"

pf "Useless?! Grrr..."

"Opening the fridge, I'm greeted with the most delicious-looking egg salad sandwich I've ever seen."

pf "Damnit Nikki, always making it impossible to stay mad at you."

"I bring the sandwich to the table along with a poured glass of juice. I wonder what I should do today…"


label E1D5S1_WeekendChoiceSelection:

menu:
    #"Practice on my own.":
    #    $ E1D5S1_EventAlone = 1
    #    jump E1D5S2
        
    "Work on the history project with Yuuna.":
        $ E1D5S1_EventYuuna = 1
        jump E1D5S3
        
    "Ask Kaori about team strategies.":
        $ E1D5S1_EventKaori = 1
        jump E1D5S4
        
    "Hang out with Shou." if (E1D5S6_MayuNoThanksLoop == 0):
        $ E1D5S1_EventShou = 1
        jump E1D5S5
        
    "See what Mayu is up to." if (E1D5S6_MayuNoThanksLoop == 0):
        $ E1D5S1_EventMayu = 1
        jump E1D5S6
        
        
        