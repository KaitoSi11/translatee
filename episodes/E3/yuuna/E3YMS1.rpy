#
label E3YMS1:
    
    #Afternoon
    
    $ yuuOut = "Cooking"
    $ yuuHairF = "cooking"
    $ yuuHairB = yuuHairF
    
    "I was browsing a list of clubs and classes earlier and ACE offers a cooking club. I remember Nikki mocking me, saying I should join when she first started her club, but maybe that isn't such a bad idea."
    "The look on her face would be priceless if I offered to cook and it was edible. {w}I'll go check it out."
    
    stop music fadeout 5
    stop ambient fadeout 3
    scene black with fade
    play ambient "audio/ambience/Kitchen Cooking.ogg" fadein 3
    scene bg campus auditorium day with fade
    
    "The cooking class is held in the culinary building. I enter a classroom filled with multiple cooking stations already set up with ingredients. It kind of reminds me of a chemistry lab, but with stoves and ovens."
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 3
    
    "In the corner of the room, I spot Yuuna and claim the station beside her."
    show yuuna neu at cc with dissolve
    pf "Hey Yuuna."
    show exclamation:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    show yuuna cur
    "She blinks in surprise."
    show yuuna hap
    voice "audio/voice/E3/Free/YM/S1/yuuna/1.ogg"
    ym "Oh hey! Are you part of the cooking club?"
    pf "No, I'm just dropping in today."
    show yuuna smi
    voice "audio/voice/E3/Free/YM/S1/yuuna/2.ogg"
    ym "Me too. What brings you here?"
    pf "I'd like to make a meal for Nikki."
    
    if E2YMS3_Completed == 1 or day >= 3:
        show yuuna hap
        voice "audio/voice/E3/Free/YM/S1/yuuna/3.ogg"
        ym "That's really nice of you. I'm sure she'll appreciate it."
        pf "I hope so! She's a wiz in the kitchen."
    
    else:
        show yuuna cur
        voice "audio/voice/E3/Free/YM/S1/yuuna/4.ogg"
        ym "Nikki?"
        pf "Oh, she's my younger sister."
        show yuuna sur
        voice "audio/voice/E3/Free/YM/S1/yuuna/5.ogg"
        ym "I didn't know you have a sister!"
        pf "Yup. She loves to cook, but I thought maybe I'd give her a break and make her something instead."
        show yuuna hap
        "Yuuna smiles."
        voice "audio/voice/E3/Free/YM/S1/yuuna/6.ogg"
        ym "You sound like a really thoughtful big brother."
        
    show yuuna smi
    pf "What about you? What brings you here?"
    voice "audio/voice/E3/Free/YM/S1/yuuna/7.ogg"
    ym "Since I quit the SBA, I've got a lot of extra time so I've been trying out some of the other clubs ACE offers."
    
    if E2YMS4_Completed == 0:
        pf "When did you quit the SBA?"
        show yuuna neu
        voice "audio/voice/E3/Free/YM/S1/yuuna/8.ogg"
        ym "Right around when I got Dasshu as your sponsor."
        "Her voice holds the edge of finality. It's clear she doesn't want to talk about this further."
    
    pf "Anything catch your interest?"
    show yuuna hap
    voice "audio/voice/E3/Free/YM/S1/yuuna/9.ogg"
    ym "A couple, but I'm still weighing my options. Besides, it's fun trying new things!"
    hide yuuna with dissolve
    "The student instructor arrives and everyone breaks away from their conversations to stand at their stations."
    show professorM2 extra at cc with dissolve:
        xzoom -1
    voice "audio/voice/E3/Free/YM/S1/sprof1/1.ogg"
    sprof1 "Welcome, everyone!"
    "He goes into a short message explaining who he is and the rules and structure of the club."
    voice "audio/voice/E3/Free/YM/S1/sprof1/2.ogg"
    sprof1 "Now that that's out of the way- today, we will be learning how to make Kasutera. If you haven't already done so, please put on your aprons."
    "I slip off my blazer and tie the apron around my waist."
    voice "audio/voice/E3/Free/YM/S1/sprof1/3.ogg"
    sprof1 "First, we will preheat the oven to 160 degrees, and don't forget to line your pan with parchment paper."
    "Isn't that a little low? {w}Oh right, it's in Celsius."
    voice "audio/voice/E3/Free/YM/S1/sprof1/4.ogg"
    sprof1 "For our dry ingredients we will have 1 cup and 2 ½ tablespoons of bread flour and 1 cup of sugar. The wet ingredients will have 6 eggs and 5 tablespoons of honey diluted with 2 ½ tablespoons of water."
    hide professorM2 with dissolve
    
    $ E3YMS1_Correct = 0
    
    "At least there aren't that many ingredients. As instructed, I measure out the ingredients. {w}Wait, I forgot to preheat the oven! What temperature should it be?"
    
    #QTE
    $ qtebase = 3
    $ qtetotal = qtebase
    $ t_var = qtetotal
    show screen timer_scr(place="E3YMS1_Degrees")
    
    menu:
        "140 degrees.":
            $ renpy.hide_screen ("timer_scr")
            "I preheat the oven to 140 degrees."
    
        "150 degrees.":
            $ renpy.hide_screen ("timer_scr")
            "I preheat the oven to 150 degrees."
    
        "160 degrees." if MCStory != 2:
            $ E3YMS1_Correct += 1
            $ renpy.hide_screen ("timer_scr")
            "I preheat the oven to 160 degrees."
        
        "{color=#00ff00}{b}160 degrees.{/b}{/color}" if MCStory == 2:
            $ E3YMS1_Correct += 1
            $ renpy.hide_screen ("timer_scr")
            "I preheat the oven to 160 degrees."
    
        "170 degrees.":
            $ renpy.hide_screen ("timer_scr")
            "I preheat the oven to 170 degrees."
    
        "180 degrees.":
            label E3YMS1_Degrees:
                $ renpy.hide_screen ("timer_scr")
                "I preheat the oven to 180 degrees."
    
    "The instructor continues to provide instructions and I follow as best as I can."
    $ persistent.gpix[66][0] = 1
    $ persistent.gpix[67][0] = 1
    $ persistent.gpix[68][0] = 1
    show cg yuuna cooking 1 with dissolve:
        xzoom 0.5
        yzoom 0.5
    "While whisking the eggs, my gaze wanders over to Yuuna. She's carefully pouring flour into her measuring cup and leveling it off before dumping it in the bowl. Her tongue sticks out slightly as she concentrates."
    show cg yuuna cooking 2 with dissolve
    "I try to hold back a chuckle, when she glances at me. There's a smudge of flour on her cheek, and I can't hold back my smile."
    show cg yuuna cooking 3 with dissolve
    "She matches my grin, before turning back to her ingredients."
    show cg yuuna cooking 1 with dissolve
    
    "I refocus on my own station and add the sugar. The only thing left is to add the honey. How much water do I use to dilate the honey?"
    
    $ qtebase = 3
    $ qtetotal = qtebase
    $ t_var = qtetotal
    show screen timer_scr(place="E3YMS1_Water")
    
    menu:
        "1 ½ teaspoons":
            label E3YMS1_Water:
                $ renpy.hide_screen ("timer_scr")
                "I add 1 ½ teaspoons of water."
    
        "1 ½ tablespoons.":
            $ renpy.hide_screen ("timer_scr")
            "I add 1 ½ tablespoons of water."
    
        "2 tablespoons.":
            $ renpy.hide_screen ("timer_scr")
            "I add 2 tablespoons of water."
    
        "2 ½ teaspoons.":
            $ renpy.hide_screen ("timer_scr")
            "I add 2 ½ teaspoons of water."
    
        "2 ½ tablespoons." if MCStory != 2:
            $ E3YMS1_Correct += 1
            $ renpy.hide_screen ("timer_scr")
            "I add 2 ½ tablespoons of water."
            
        "{color=#00ff00}{b}2 ½ tablespoons.{/b}{/color}" if MCStory == 2:
            $ E3YMS1_Correct += 1
            $ renpy.hide_screen ("timer_scr")
            "I add 2 ½ tablespoons of water."
            
    voice "audio/voice/E3/Free/YM/S1/sprof1/5.ogg"
    sprof1 "Once you add the last of your flour, mix the ingredients until combined. Be careful not to overmix!"
    voice "audio/voice/E3/Free/YM/S1/sprof1/6.ogg"
    sprof1 "Pour the batter into your pan and let it bake for 35 minutes."
    
    "As instructed, I add the last of my flour to the mixture and continue to mix it. What counts as over mixing anyway? How do I know if I've mixed just the right amount or too much? {w}Using my wooden spoon, I poke around to see if there are any flour chunks still left. {w}Nope. {w}I guess that means my batter is ready to go in the oven."
    
    "I set the timer for…"
    
    #QTE
    $ qtebase = 3
    $ qtetotal = qtebase
    $ t_var = qtetotal
    show screen timer_scr(place="E3YMS1_Timer")
    
    menu:
        "20 minutes.":
            label E3YMS1_Timer:
                $ renpy.hide_screen ("timer_scr")
                "...20 minutes."
    
        "25 minutes.":
            $ renpy.hide_screen ("timer_scr")
            "...25 minutes."
    
        "30 minutes.":
            $ renpy.hide_screen ("timer_scr")
            "...30 minutes."
    
        "35 minutes." if MCStory != 2:
            $ E3YMS1_Correct += 1
            $ renpy.hide_screen ("timer_scr")
            "...35 minutes."
            
        "{color=#00ff00}{b}35 minutes.{/b}{/color}" if MCStory == 2:
            $ E3YMS1_Correct += 1
            $ renpy.hide_screen ("timer_scr")
            "...35 minutes."
    
        "40 minutes.":
            $ renpy.hide_screen ("timer_scr")
            "...40 minutes."
    
    "Now just to wait and see."
    scene black with fade
    #time pass
    $renpy.pause(1)
    #fade in
    scene bg campus auditorium day with fade
    
    "Once my timer dings, I carefully remove the cake from the oven. It baked unevenly so some of the side is spilling over the pan. I think it might be a little darker on one side too. Does that mean it's burned? I guess only one way to find out."
    "I pry it out of the pan and put it on my plate. Some of the edges got stuck to the parchment paper when I removed it so there are patches of yellow exposed under the darkish brown layer."
    
    "Yuuna carefully sets her cake on her plate. It's a perfect loaf with a golden brown top and light yellow sides. {w}She glances over at my cake and hides her smile with a cough."
    "The instructor begins his taste test in my row at the back of the classroom. He reaches me before Yuuna."
    
    show professorM2 extra at r2 with dissolve:
        xzoom -1
        
    voice "audio/voice/E3/Free/YM/S1/sprof1/7.ogg"
    sprof1 "Hm, it didn't quite come out the way you expected, did it? But, let's see how it tastes."
    
    "He puts a forkful of cake in his mouth."
    
    if E3YMS1_Correct == 3:
        "His eyes light up in a smile."
        show note:
            xoffset 1040
            yoffset 5
            xzoom .75
            yzoom .75
        voice "audio/voice/E3/Free/YM/S1/sprof1/8.ogg"
        sprof1 "This is absolutely delightful!"
        pf "Really?"
        voice "audio/voice/E3/Free/YM/S1/yuuna/10.ogg"
        ym "Let me try!"
        show yuuna sur at l2 with dissolve
        "Yuuna stands right beside me, staring curiously at my cake. {w}She tries a small piece."
        show heart:
            xoffset 365
            yoffset 100
            xzoom .75
            yzoom .75
        show yuuna hap
        voice "audio/voice/E3/Free/YM/S1/yuuna/11.ogg"
        ym "Oh wow! This is so good!"
        "I beam. Nikki is going to be so surprised!"
    
    elif E3YMS1_Correct > 0:
        "He chews thoughtfully."
        show storm:
            xoffset 1040
            yoffset 5
            xzoom .75
            yzoom .75
        voice "audio/voice/E3/Free/YM/S1/sprof1/9.ogg"
        sprof1 "Hm, it's not quite right. There's something a little off about the taste and texture."
        "I must have gotten some of the measurements wrong. Next time I'll pay more attention to the recipe."
        show yuuna smi at l2 with dissolve
        "Yuuna smiles."
        voice "audio/voice/E3/Free/YM/S1/yuuna/12.ogg"
        ym "That's not bad for a first try."
    
    else:
        "His face is a blank mask as he swallows. {w}Uh oh, I know that expression all too well."
        show drop:
            xoffset 1040
            yoffset 5
            xzoom .75
            yzoom .75
        voice "audio/voice/E3/Free/YM/S1/sprof1/10.ogg"
        sprof1 "Practice makes perfect."
        show yuuna smi at l2 with dissolve
        "Yuuna smiles encouragingly."
        voice "audio/voice/E3/Free/YM/S1/yuuna/13.ogg"
        ym "I'm sure you'll get it next time."
        "I sigh."
        
    show yuuna neu
    "The instructor stops at Yuuna's station next."
    voice "audio/voice/E3/Free/YM/S1/sprof1/11.ogg"
    sprof1 "This is a beautiful cake! I can't wait to see how it tastes."
    show yuuna hap
    "Yuuna's face lights up in anticipation as the instructor takes a bite."
    stop music fadeout 5
    show yuuna smi
    show dots:
        xoffset 1040
        yoffset 5
        xzoom .75
        yzoom .75
    "He pauses, straining to keep his face calm, then gulps heavily."
    voice "audio/voice/E3/Free/YM/S1/yuuna/14.ogg"
    ym "How is it?"
    "Her voice trembles with hope."
    show yuuna neu
    show drop:
        xoffset 1040
        yoffset 5
        xzoom .75
        yzoom .75
    "The instructor's voice is hoarse as he chokes out his next words."
    play music "audio/music/Sneaking About (GAME VERSION).ogg" fadein 5
    voice "audio/voice/E3/Free/YM/S1/sprof1/12.ogg"
    sprof1 "Practice makes perfect."
    show yuuna sur
    voice "audio/voice/E3/Free/YM/S1/yuuna/15.ogg"
    ym "W-What?"
    pf "Let me try."
    show yuuna wor
    "I take a bite."
    ### VOICE - didn't have a file for this one, but #14 is the same... I guess?
    voice "audio/voice/E3/Free/YM/S1/yuuna/14.ogg"
    ym "How is it?"
    
    "It's like if sugar and plaster had a baby together and let it sit out in the sun until every drop of moisture was baked out of it."
    
    
    menu:
        "How do I put this nicely…":
            pf "Practice makes perfect."
            show shocked:
                xoffset 365
                yoffset 100
                xzoom .75
                yzoom .75
            show yuuna sur
            voice "audio/voice/E3/Free/YM/S1/yuuna/16.ogg"
            ym "Again?!"
    
        "It doesn't taste how it looks.":
            pf "Well, at least you've still got your looks."
            show question:
                xoffset 365
                yoffset 100
                xzoom .75
                yzoom .75
            show yuuna ske
            voice "audio/voice/E3/Free/YM/S1/yuuna/17.ogg"
            ym "Excuse me?"
            pf "The cake! I mean at least the cake {i}looks{/i} delicious… even though it's not."
    
        "I wish I could un-taste this.":
            pf "This is not good."
            show crying:
                xoffset 365
                yoffset 100
                xzoom .75
                yzoom .75
            show yuuna sad
            voice "audio/voice/E3/Free/YM/S1/yuuna/18.ogg"
            ym "What?"
            
    show yuuna wor
    voice "audio/voice/E3/Free/YM/S1/yuuna/19.ogg"
    ym "Can it really be so bad?"
    "Yuuna grabs her fork and stuffs a piece in her mouth. She grimaces, then sighs deeply."
    show yuuna dis
    voice "audio/voice/E3/Free/YM/S1/yuuna/20.ogg"
    ym "Practice does make perfect."
    stop music fadeout 3
    hide professorM2 with dissolve
    show yuuna sad at cc with dissolve
    "The instructor moves on to another station while Yuuna pouts at her rejected cake."
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 3
    pf "Well, aside from the result of your baking, what did you think of this class?"
    show drop:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    show yuuna hap
    voice "audio/voice/E3/Free/YM/S1/yuuna/21.ogg"
    ym "It was fun! But surprisingly challenging…"
    show yuuna thi
    "She glances at her cake again and mutters under her breath."
    voice "audio/voice/E3/Free/YM/S1/yuuna/22.ogg"
    ym "Where did I go wrong?"
    pf "You going to stick with this as your new extra curricular activity?"
    show yuuna neu
    voice "audio/voice/E3/Free/YM/S1/yuuna/23.ogg"
    ym "Mmm, I don't know. I want to keep checking out other clubs."
    pf "Makes sense."
    show yuuna smi
    voice "audio/voice/E3/Free/YM/S1/yuuna/24.ogg"
    ym "It looks like other students are tasting each other's cakes. You want to try some?"
    pf "Sure."
    
    #fade black
    scene black with fade
    "Yuuna and I walk around the room and try some of the other cakes with varying results. Once we tasted all of them, we head out."
    
    # end
    $ E3YMS1_Completed = 1
    
