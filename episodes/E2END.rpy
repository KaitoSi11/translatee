#
label E2END:
    # Say whatever we need to say
    $renpy.pause(2.5)
    show mcInt with dissolve:
        xalign 0.5
        yalign 0.1
        yoffset 135
        
    "Hello, {i}ACE Academy{/i} Steam Early Access supporters!"
    "Thank you for playing episode 2! {w}We hope you enjoyed it."
    "We love to hear and incorporate player feedback into development, so please feel free to let us know your thoughts on the discussion board or in a review on Steam!"
    "Thanks again. {w}We hope to see you in the next episode of ACE Academy~!"
    
    hide mcInt with dissolve
    "NOTE: If you wish to continue without starting over for the next episode, please follow these instructions:"
    "Make a save slot now! {w}Please use this when the next episode is released."
    "Thank you and see you next time~!"
    
    #return
    "Welcome back to ACE Academy - Episode 3."
    "If all went well, it should have loaded your game just fine."
    "Please keep in mind there are a lot of variables and it is possible some save files {i}may{/i} become unstable."
    "If you run into any issues, please let us know on the forums."
    "Enjoy!"
    
    scene black with fade
    
    jump E3D1S1
