#
label E2D5VB:
    
    "I spot Valerie in the kitchen with some guy. Her body is pressed up against him as she whispers something in his ear. The guy perks up, nods, then rushes out of the kitchen and towards the hallway. {w}With a huge grin on her face, Valerie notices me and comes over. Her hips move alluringly with her walk, but she seems a tad unsteady on her feet."
    show valerie mis b3 at cc with dissolve
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO36.ogg"
    vb "Hey, you."
    pf "Who was that guy?"
    show valerie thi b3 at cc
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO37.ogg"
    vb "Oh, I don't know."
    pf "Really? Because you seemed kind of close--"
    show valerie mis b3 at cc
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO38.ogg"
    vb "Forget about him. He's not important."
    show valerie ske b3 at cc
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO39.ogg"
    vb "The better question is: what's a guy like you doing in a place like this?"
    pf "Just getting a drink."
    show valerie hap b3 at cc
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO40.ogg"
    vb "Oh yeah?"
    "She giggles and leans in closer to me."
    show valerie mis b3 at cc
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO41.ogg"
    vb "I might have had a drink too."
    
    if E2VBS3_Completed == 1:
        pf "Uh, aren't you still underage?"
        voice "audio/voice/E2/D5/VB/ValerieE2D5REDO42.ogg"
        vb "Maybe."
        pf "You shouldn't be drinking."
        show valerie hap b3 at cc
        voice "audio/voice/E2/D5/VB/ValerieE2D5REDO43.ogg"
        vb "Oops. Well, it's a little too late for that."
    
        if MCStory == 3:
            "Actually, the more I study her, the more I can see her \"drunkeness\" is an act. I wonder why she's doing it, so I'll play along."
    
    else:
        menu:
            "Aren't you underage?":
                pf "How old are you again?"
                voice "audio/voice/E2/D5/VB/ValerieE2D5REDO44.ogg"
                vb "19."
                pf "You can't drink here! You're still underage."
                show valerie ske b3 at cc
                "Valerie waves a hand dismissively."
                voice "audio/voice/E2/D5/VB/ValerieE2D5REDO45.ogg"
                vb "It's okay. I've already been drinking legally for a full year back in France. It's not my fault the age limit here is higher than it is at home."
                pf "Still, you should be careful."
                show valerie hap b3 at cc
                "She giggles and pats my arm."
                show note:
                    xoffset 720
                    yoffset 125
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E2/D5/VB/ValerieE2D5REDO46.ogg"
                vb "It's cute that you're worried about me."
                pf "U-Um, yeah…"
                "Her hand is as warm as my cheeks."
    
            "Just one?":
                "I put my drink back down on the counter and study her."
                pf "You sure that's all you've had?"
                show valerie ske b3 at cc
                voice "audio/voice/E2/D5/VB/ValerieE2D5REDO47.ogg"
                vb "Of course! I think I'd know if I've had more."
                # shake? might split line
                "Valerie takes another step towards me and wobbles on her heel. {w}She stumbles, and falls into my arms."
                show exclamation:
                    xoffset 720
                    yoffset 125
                    xzoom .75
                    yzoom .75
                show valerie sur b3 at cc
                voice "audio/voice/E2/D5/VB/ValerieE2D5REDO48.ogg"
                vb "Oh!"
                show valerie cur b3 at cc
                "Her hands linger on my arms as a blush creeps up her cheeks."
                show valerie smi b3 at cc
                voice "audio/voice/E2/D5/VB/ValerieE2D5REDO49.ogg"
                vb "Wow, you're strong."
                "I grin and subtly flex as I help her back to her feet."
                pf "Careful."
                show valerie hap b3 at cc
                "She giggles again."
                voice "audio/voice/E2/D5/VB/ValerieE2D5REDO50.ogg"
                vb "Okay, I might have had more than just one drink."
    
            "Looks like one is all you need.":
                pf "Well, it seems like you've had enough anyway."
                show valerie dis b3 at cc
                "She pouts."
                voice "audio/voice/E2/D5/VB/ValerieE2D5REDO51.ogg"
                vb "Aww, don't be like that. The party's only just getting started!"
                "I shrug and take a sip from my drink. As I bring it back down, Valerie takes the cup from me and also takes a sip."
                pf "Hey!"
    
                if E2D5S4_Drink == "Water":
                    show valerie ske b3 at cc
                    "She gives me a weird look."
                    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO52.ogg"
                    vb "You aren't drinking anything?"
                    pf "I am. Water."
                    show valerie hap b3 at cc
                    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO53.ogg"
                    vb "Hm…"
    
                else:
                    show valerie hap b3 at cc
                    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO54.ogg"
                    vb "Good choice. It seems like you know how to enjoy yourself at a party too."
                    pf "I suppose."
    
            "{color=#00ff00}{b}She's lying.{/b}{/color}" if MCStory == 3:
                "I have no idea why she's pretending to be drunk, but she looks as sober as can be. Her intelligent eyes watch me closely, and I think she's trying to gauge my reaction to her drunken facade."
                "I suppose I'll play along and see where she's going with this."
                "Raising my drink, I take a sip."
                pf "I suppose I need to catch up to you."
                show valerie hap b3 at cc
                "She giggles, pleased."
                
    show valerie neu b2 at cc with dissolve
    "Someone nearly bumps into us as they reach for a drink. Valerie frowns."
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO55.ogg"
    vb "C'mon, let's go find someplace else to talk. It's too busy in here."
    hide valerie with dissolve
    "She grabs my hand and leads me to the living room. The couch is surprisingly empty, so Valerie plops down and pats the space beside her. I oblige her and sit down."
    show valerie ner b1 at cc with dissolve
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO56.ogg"
    vb "I hope you're not still angry with me."
    pf "Huh? Angry about what?"
    show valerie neu b1 at cc
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO57.ogg"
    vb "About your core."
    pf "Oh. {w}No, I'm not angry."
    show valerie smi b1 at cc
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO58.ogg"
    vb "Good, because now that I'm your engineer you're going to be seeing a lot more of me."
    pf "Oh yeah?"
    show valerie hap b1 at cc
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO59.ogg"
    vb "Of course. Somebody needs to make sure that your core gets a lot of tender loving care."
    pf "Hey! I give it a lot of TLC!"
    show valerie mis b1 at cc
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO60.ogg"
    vb "I'll bet you do."
    pf "Huh?"
    show valerie ske b1 at cc
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO61.ogg"
    vb "I meant someone besides you."
    show valerie smi b1 at cc
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO62.ogg"
    vb "Someone with a gentler touch, who knows how to treat it right."
    pf "You don't know anything about my core."
    show valerie mis b1 at cc
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO63.ogg"
    vb "Well, I'd like to."
    "Suddenly I'm aware of how close she is to me. She puts a hand on my arm."
    show note:
        xoffset 720
        yoffset 125
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO64.ogg"
    vb "I'd like the chance to get to know it intimately…"
    pf "Um…"
    show valerie smi b1 at cc
    stop music fadeout 3
    stop ambient fadeout 3
    "She closes the gap between us, and I feel her soft skin on me. Her breath tickles my ear as she whispers."
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO65.ogg"
    vb "Do you know where Shou's room is?"
    
    if E2SSS2_Completed == 1:
        pf "Yeah."
    
    else:
        pf "No."
        show valerie ske b1 at cc
        voice "audio/voice/E2/D5/VB/ValerieE2D5REDO66.ogg"
        vb "You know where the bedrooms are?"
        "I think I remember seeing the hallway leading towards them, and nod."
        show valerie mis b1 at cc
        voice "audio/voice/E2/D5/VB/ValerieE2D5REDO67.ogg"
        vb "Shou's room is on the first level, third door on the right."
        pf "Okay…"
        
    show valerie mis b1 at cc
    show heart:
        xoffset 720
        yoffset 125
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO68.ogg"
    vb "Go there. Wait for me on the bed… I'll be right behind you."
    
    menu:
        "It would be wrong to say yes.":
            # some kind of sprite movement?
            show valerie cur b1 at cc with dissolve
            "Gently, I push her away from me and shake my head."
            pf "I can't. I'm sorry."
            "Her eyes are wide in surprise."
            show question:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            show valerie cur b1 at cc
            voice "audio/voice/E2/D5/VB/ValerieE2D5REDO69.ogg"
            vb "How come?"
            pf "I'm sorry. It wouldn't be right to take advantage of you when you aren't thinking straight."
            show valerie hap b1 at cc
            voice "audio/voice/E2/D5/VB/ValerieE2D5REDO70.ogg"
            vb "My mind couldn't be more clear."
            pf "You might think that, but you've had a few drinks and alcohol always clouds minds."
            show valerie mis b1 at cc
            voice "audio/voice/E2/D5/VB/ValerieE2D5REDO71.ogg"
            vb "Trust me, this is what I want."
            "I shake my head again."
            pf "I'm sorry."
            show valerie dis b1 at cc
            "She pouts."
            show valerie neu b1 at cc
            voice "audio/voice/E2/D5/VB/ValerieE2D5REDO72.ogg"
            vb "I see."
            show valerie smi b1 at cc
            "But even though she's pouting, she doesn't seem that upset. In fact, she almost seems to like my answer."
    
        "Hell yeah!":
            "Is this a dream or real life?"
            pf "Why don't you come with me?"
            show valerie hap b1 at cc
            voice "audio/voice/E2/D5/VB/ValerieE2D5REDO73.ogg"
            vb "I'm going to freshen up first, but I promise you won't be disappointed."
            pf "Okay."
            hide valerie with dissolve
            "With some reluctance I pull away from her lingering touch and head towards the hall. Glancing back, Valerie also stands and blows a kiss at me."
            scene black with fade
            "With renewed energy, I hurry to Shou's room and find the door unlocked. I check to make sure no one is watching, and crack open the door before slipping inside the dark room."
            # lower or stop ambient volume?
            stop music fadeout 3
            "As I search for the light, I pull off my shirt and begin to unbutton my pants."
            voice "audio/voice/E2/D5/VB/fbro1/1.ogg"
            "Mystery Voice" "What took so long, babe? Come on the bed."
            play music "audio/music/Baka! (GAME VERSION).ogg" fadein 3
            "I freeze. Unless Valerie's got the worst cold in the world, I'm pretty sure that was just a man who spoke. {w}Understanding dawns on me."
            pf "We've been played, man."
            voice "audio/voice/E2/D5/VB/fbro1/2.ogg"
            fbro1 "... Shou? Is that you?"
            pf "Nope."
            voice "audio/voice/E2/D5/VB/fbro1/3.ogg"
            fbro1 "Get your own room, man! This one's occupied."
            pf "Bro, she's not coming."
            voice "audio/voice/E2/D5/VB/fbro1/4.ogg"
            fbro1 "What?"
            pf "Valerie."
            voice "audio/voice/E2/D5/VB/fbro1/5.ogg"
            fbro1 "How do you know… who the hell are you?"
            pf "Just another sucker for a cute blonde."
            "There's an uncomfortable silence as I fix my pants and search blindly for the shirt I dropped on the floor. {w}A light right now would really help, but I know I do not want to see the sight on the bed."
            voice "audio/voice/E2/D5/VB/fbro1/6.ogg"
            fbro1 "Well, crap."
            pf "Yeah."
            "I find my shirt and pull it on. Then I hear the shuffle of moving fabrics as the guy gets off the bed."
            pf "I'm going to go now while we're both still anonymous. But let us never speak of this again. Ever."
            voice "audio/voice/E2/D5/VB/fbro1/7.ogg"
            fbro1 "As far as I'm concerned this never happened."
            "I open the door a crack and slip back into the hallway. {w}Valerie got me good. I should have known that sounded too good to be true…"
            # ambient queue, if
            scene bg campus dorm night with fade
            "As I return to the party, Valerie approaches me with a big grin on her face."
            show valerie hap b1 at cc with dissolve
            voice "audio/voice/E2/D5/VB/ValerieE2D5REDO74.ogg"
            vb "Was that everything you imagined and more?"
            pf "I don't know what you're talking about."
            show valerie mis b1 at cc
            voice "audio/voice/E2/D5/VB/ValerieE2D5REDO75.ogg"
            vb "Sure you don't."
            show note:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            $renpy.pause(1)
            hide valerie with dissolve
            "She laughs and winks before walking away."
            "I can't believe I fell for that…"
            scene black with fade
            stop music fadeout 5
            "Shaking away any lingering thoughts of the incident, I rejoin the party and spend the rest of the night dancing."
            jump E2D5VB_End
    
        "No thanks.":
            pf "Sorry, but I'll have to pass."
            show valerie ske b1 at cc
            "Her brow is furrowed in confusion."
            voice "audio/voice/E2/D5/VB/ValerieE2D5REDO76.ogg"
            vb "Why?"
            pf "Shou is my friend and the thought of violating his room like that doesn't appeal to me."
            show valerie mis b1 at cc
            "She feigns innocence."
            voice "audio/voice/E2/D5/VB/ValerieE2D5REDO77.ogg"
            vb "What do you mean? What exactly do you think we'd be doing in there?"
            pf "Yeah, I'm not playing this game."
            show valerie smi b1 at cc
            voice "audio/voice/E2/D5/VB/ValerieE2D5REDO78.ogg"
            vb "Hm."
            "But she grins anyway, like she's pleased I refused."
    
        "{color=#00ff00}{b}It's a trap.{/b}{/color}" if MCStory == 3:
            pf "No."
            show valerie cur b1 at cc
            "She blinks at my abrupt answer."
            voice "audio/voice/E2/D5/VB/ValerieE2D5REDO79.ogg"
            vb "Why not?"
            pf "I know you're not drunk."
            show valerie sad b1 at cc
            voice "audio/voice/E2/D5/VB/ValerieE2D5REDO80.ogg"
            vb "What?"
            pf "And there's definitely a guy in the room."
            show question:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            show valerie sur b1 at cc
            voice "audio/voice/E2/D5/VB/ValerieE2D5REDO81.ogg"
            vb "What?!"
            "Genuine shock shows on her face."
            show panic:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            show valerie sad b1 at cc
            voice "audio/voice/E2/D5/VB/ValerieE2D5REDO82.ogg"
            vb "Nooo, of course not! What makes you think that?"
            pf "Well, I watched you do this same thing to another guy in the kitchen."
            show valerie thi b1 at cc
            voice "audio/voice/E2/D5/VB/ValerieE2D5REDO83.ogg"
            vb "Oh, you noticed?"
            pf "Yup."
            show valerie mis b1 at cc
            "A smirk returns to her face and she sits up straight."
            voice "audio/voice/E2/D5/VB/ValerieE2D5REDO84.ogg"
            vb "Huh. Guess you're smarter than you look."
            "I'm not sure if I should be flattered or insulted."
    
    play ambient "audio/ambience/Pilot Lounge.ogg" fadein 7
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 7
    pf "Why are you doing this?"
    show valerie cur b1 at cc
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO85.ogg"
    vb "Doing what?"
    pf "You know what I mean."
    show valerie smi b1 at cc
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO86.ogg"
    vb "I'm just having a little fun. It is a party after all."
    pf "But you're toying with these guys' emotions. Aren't you worried someone's going to get hurt?"
    show valerie hap b1 at cc
    "Valerie laughs."
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO87.ogg"
    vb "Oh please, like they're any better."
    pf "Huh?"
    show valerie mis b1 at cc
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO88.ogg"
    vb "A drunk girl and an empty room…"
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO89.ogg"
    vb "The fact that they jumped on that opportunity means there was only one thing on their mind. Then who would have gotten hurt?"
    "She does have a point. A good guy wouldn't take advantage of someone who wasn't thinking clearly."
    show valerie hap b1 at cc
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO90.ogg"
    vb "I'm just turning their own game against them."
    
    menu:
        "It's still wrong.":
            pf "I can see your point, but leading them on in order to turn it back on them doesn't make it right."
            show valerie neu b1 at cc
            pf "Especially since {i}you're{/i} the one approaching them and suggesting the idea."
            show valerie thi b1 at cc with dissolve
            $renpy.pause(1.0)
            show bulb:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            show valerie mis b1 at cc with dissolve
            "She bites on her lower lip in thought, then wears her signature smirk."
            voice "audio/voice/E2/D5/VB/ValerieE2D5REDO91.ogg"
            vb "Fine, I'll stop. But only because I've thought of something even more fun."
    
        "You're a regular vigilante.":
            pf "I suppose they aren't that innocent, huh?"
            show valerie smi b1 at cc
            voice "audio/voice/E2/D5/VB/ValerieE2D5REDO92.ogg"
            vb "Exactly, and someone has to show them the error or their ways."
            pf "And that just happens to be you…"
            show valerie thi b1 at cc
            voice "audio/voice/E2/D5/VB/ValerieE2D5REDO93.ogg"
            vb "Weelll…"
            show bulb:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            "She draws out the word, then smirks."
            show valerie mis b1 at cc
            ##MISSINGLINE##
            voice "audio/voice/E2/missing/valerie/3.ogg"
            vb "Nah, not tonight. I've got something even better in mind."
    
        "Your system is flawed.":
            pf "That doesn't make sense."
            show valerie cur b1 at cc
            voice "audio/voice/E2/D5/VB/ValerieE2D5REDO94.ogg"
            vb "What do you mean?"
            pf "You're purposely setting up this scenario and then only blaming one side."
            show valerie ske b1 at cc
            voice "audio/voice/E2/D5/VB/ValerieE2D5REDO95.ogg"
            vb "So? They'd be willing to do something to a drunk girl who isn't thinking straight."
            pf "They also might be drunk and not thinking straight."
            show valerie neu b1 at cc
            "Valerie seems thoughtful, but her eyes are still locked on me. I think she's surprised by my words. Then she shrugs."
            voice "audio/voice/E2/D5/VB/ValerieE2D5REDO96.ogg"
            vb "Well, whatever, I'm done with that anyway. I've thought of something even better."
            pf "Hm?"
    
    
    "She grabs my hand and leads me towards the rave downstairs."
    show note:
        xoffset 720
        yoffset 125
        xzoom .75
        yzoom .75
    show valerie hap b1 at cc
    voice "audio/voice/E2/D5/VB/ValerieE2D5REDO97.ogg"
    vb "C'mon, let's dance!"
    hide valerie with dissolve
    scene black with fade
    stop music fadeout 5
    "Although at first I try to protest, she is persistent, and we end up having a great night of dancing and chatting."
    jump E2D5VB_End
    
    label E2D5VB_End:
        $ E2D5VB_Completed = 1
        stop ambient fadeout 3
        "It's late by the time I get home, and everyone is already asleep. I tiptoe into my room and collapse onto my bed. Exhausted, I fall asleep as soon as my head hits the pillow."
        jump E2D6S1

    
