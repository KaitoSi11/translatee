#
label E4END:
    stop music fadeout 2
    show mcInt with dissolve:
        xalign 0.5
        yalign 0.1
        yoffset 135
        

    "Thank you for playing ACE! {w}We hope you enjoyed it."
    "We love to hear and incorporate player feedback into future projects, so please feel free to let us know your thoughts on the discussion boards or in a Steam review!"
    "With that formality out of the way, whew, what a ride it's been! For our original supports, thank you so much for sticking with us."
    "For new players, welcome to the PixelFade family!"
    "While the adventure of ACE stops here for now, PixelFade is always exploring new options! Please feel free to check out what we are up to at {a=http://pixelfade.com}pixelfade.com{/a}!"
    "Thanks again!"
    scene black with Dissolve(2.0)
    $renpy.pause()
    "..."
    "Still here?"
    "There's nothing else!"
    "This isn't a Marvelle movie where you get a special hidden teaser."
    $renpy.pause()
    "...I get the feeling I just set an expectation that we {i}will{/i} have something after all this text."
    "<_<"
    ">_>"
    "Look, I got nothing, so stop trying, okay?"
    "Just press escape, or right click that mouse button and be on your merry way."
    $renpy.pause()
    "..."
    "Really? Still here?"
    "O_O"
    "o_o"
    "._."
    "Okay, {i}maybe{/i} I might have something to share..."

    "...Are you ready?"
    "Here goes...!"
    
    play music "audio/music/Raycrash (GAME VERSION).ogg" fadein .5
    scene cg GEAR aludian poster at Shake(None, 4, dist=20)
    "{color=#ff0000}ACE{/color} {color=#00ccff}ACADEMY{/color}: {color=#ffff00}SUPERNOVA{/color}"
    stop music
    scene black
    $renpy.pause(.20)
    "Sorry, that's not actually a thing."
    "Though I will say that mock reveal somehow ended up looking pretty cool, LOL."
    "For realsies though, we are excited about the next visual novel currently in development! Check out {a=http://pixelfade.com}pixelfade.com{/a} for details!"
    "Thanks again for playing! {w}:D"
    "Goodbye!"
    
    $renpy.pause()
    menu:
        "Goodbye!":
            return
            
        "The game ends here for real?":
            "Your Inner Thought" "HOLD ON PIXELFADE."
            "?!"
            "Your Inner Thought" "DID YOU REALLY JUST END THE GAME LIKE THAT?"
            "Yes--"
            "Your Inner Thought" "NO, NOT ACCEPTABLE."
            "D:! We're sorry... {w}ACE is a crowd funded project and we did our best given our resources!"
            "Actually, the length ended up almost twice as long than what we initially planned! We stretched out as long as we could! >_<"
            "Your Inner Thought" "SO IF YOU HAD MORE RESOURCES, I COULD HAVE HAD A LONGER GAME?"
            "Indeed! As an indie team, your support will directly impact the scope of our projects... including future ones!"
            "Your Inner Thought" "ALRIGHT, I'M MODERATELY INTERESTED, HOW DO I HELP?"
            "Please feel free to check us out on {a=https://www.patreon.com/pixelfade}Patreon{/a}!"
            "Alternatively, we'll be crowdfunding our next project in the near future... please consider pledging then!"
            "Your Inner Thought" "OKAY, THANKS FOR THE INFO."
            "No problem {color=#FFBF00}[pfirst]{/color}. Thanks for your consideration and understanding!"
            "Have a great day! {w}:D"
            
            
    return
