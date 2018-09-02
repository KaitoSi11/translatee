label E1END:
    # Say whatever we need to say
    $renpy.pause(2.5)
    show mcInt with dissolve:
        xalign 0.5
        yalign 0.1
        yoffset 135
        
    "Hello, {i}ACE Academy{/i} Steam Early Access supporters!"
    "This is a message just for you and will be removed from future builds of the game."
    "Thank you for playing the Steam Early Access build of ACE Academy. {w}We hope you enjoyed it."
    "We're very excited for the next episode coming soon!"
    "You'll be able to play it just by updating your game client when it releases."
    "Thanks again. {w}We hope to see you in the next episode of ACE Academy~!"
    
    hide mcInt with dissolve
    "NOTE: If you wish to continue without starting over for the next episode, please follow these instructions:"
    "Make a save slot now! {w}Please use this when the next episode is released."
    "Thank you and see you next time~!"
    
    "Hello, I see you are loading your original save file from Episode 1!"
    "We've upgraded a lot of the back-end stuff which unfortunately rendered previous saves as unstable. :("
    "That being said, this part of the game can NEVER be accessed! Which means that only a select handful of people will ever see this!"
    "We'd like to give you guys a special treat, so please write down the passcode {b}E1END{/b}."
    "On release, we'll have a passcode screen where you will be able to retrieve you super special gift using that code!"
    "Anyways that's all for now. We hope you enjoy episode 2 and beyond. :D"
    "Oh, let me go ahead and return you to the main menu."
    "Right..."
    "About..."
    "Now! (Goodbye~)"
    
    #return
    
    jump E2D1S1
