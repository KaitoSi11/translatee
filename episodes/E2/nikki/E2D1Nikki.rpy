#
label E2D1Nikki:
    
    "I punch in Nikki's phone number and wait for her to answer."
    play sound "audio/sfx/Technology/Phone Dial.ogg"
    $renpy.pause(2.5)
    play sound2 "audio/sfx/Technology/Phone Answer.ogg"
    $renpy.pause(2)
    voice "audio/voice/E2/D1/Nikki/1.ogg"
    sf "Hey, what's up?"
    pf "Hi Nikki, I'm pretty much done here, so was just checking to see if you needed a ride home. I know Kaito's out again so maybe we can do something fun… like go to a movie?" 
    voice "audio/voice/E2/D1/Nikki/2.ogg"
    sf "Wouldn't you rather go with your girlfriend?"
    pf "I don't have a girlfriend!"
    "Nikki laughs."
    voice "audio/voice/E2/D1/Nikki/3.ogg"
    sf "I wouldn't say that so loudly."
    "I glance at the students walking past giving me strange looks. Oops."
    voice "audio/voice/E2/D1/Nikki/4.ogg"
    sf "Anyway, I guess you'll be seeing that movie alone because I already made plans with my friends tonight." 

    menu:
        "Alright, see you later then.":
            pf "Okay, have fun. I'll see if anybody else is free."
            voice "audio/voice/E2/D1/Nikki/5.ogg"
            sf "Sounds like a plan. Bye!"
            pf "Bye."
            "The line goes dead as Nikki hangs up."
    
        "I'll join you.":
            pf "Why don't we all hang out together?"
            voice "audio/voice/E2/D1/Nikki/6.ogg"
            sf "I don't think so."
            pf "Why not? Your friends love me!"
            voice "audio/voice/E2/D1/Nikki/7.ogg"
            sf "Yeah, that's exactly why I said no."
            pf "Are you worried that they like me more than you?"
            voice "audio/voice/E2/D1/Nikki/8.ogg"
            sf "As if that were possible! Don't you have your own friends you can hang out with? It's weird that you're trying to hang out with mine."
            pf "Yeah, I guess."
            voice "audio/voice/E2/D1/Nikki/9.ogg"
            sf "Good, go bother one of them. See ya!"
            "She hangs up before I can reply." 
    
        "Really? What kind of plans?":
            pf "Oh… What are you guys doing?"
            voice "audio/voice/E2/D1/Nikki/10.ogg"
            sf "Just hanging out."
            pf "How long will you be? Maybe later we can--"
            voice "audio/voice/E2/D1/Nikki/11.ogg"
            sf "Umm, bro..."
            "I pause. What am I doing? I can see Nikki any time at home."
            pf "Actually, I think I'm going to call up one of my friends instead."
            voice "audio/voice/E2/D1/Nikki/12.ogg"
            sf "Good idea."
            "I hear someone call Nikki's name on the other end of the phone." 
            voice "audio/voice/E2/D1/Nikki/13.ogg"
            sf "Sorry, I have to go now. Have fun with whatever you decide to do!" 
            "The line goes dead before I can even say goodbye. When did my little sister become more popular than me?"
    
    "With a shrug, I think about who else I can call."
    $ E2FreeTime_CalledNikki = 1
    jump E2FreeTime
