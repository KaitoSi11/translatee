#
label E3VBS1:

$ valOut = renpy.random.choice(['sUniform'])
$ valHairF = renpy.random.choice(['default'])
$ valHairB = renpy.random.choice(['default'])
    
"I wonder what Valerie is up to..."
play sound "audio/sfx/Technology/Phone Dial.ogg"
"I dial her number and wait for her to answer."

play sound "audio/sfx/Technology/Phone Answer.ogg"
$renpy.pause(2.0)
voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL1.ogg"
vb "Hello?"
pf "Hey, Valerie, you busy?"
voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL2.ogg"
vb "Yeah, I'm about to go meet a friend for some coffee."

if (MCStory == 3):
    "I have a feeling I know who it is..."
    pf "...You mean me?"
    voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL3.ogg"
    vb "Of course!"

else:
    pf "Oh, anyone I know?"
    voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL4.ogg"
    vb "It's you, silly."
    pf "Oh."
    
voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL5.ogg"
vb "I'll meet you at the cafe in front of the bookstore."
pf "Sounds like a plan. I'll see you in a bit."
voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL6.ogg"
vb "Au revoir!"

stop music fadeout 3.0
stop ambient fadeout 3.0
scene black with fade
"I make my way to the cafe."


play ambient "audio/ambience/Desert Maid Cafe.ogg" fadein 5
scene bg campus cafe day
show valerie neu at cc
with fade

play music "audio/music/Day Out (GAME VERSION).ogg" fadein 5
"Valerie is waiting for me in a booth by the time I arrive."

show valerie dis at cc with dissolve
voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL7.ogg"
vb "It's rude to keep a lady waiting."

menu:
    "I'm sorry!":
        pf "I'm sorry! I got here as fast as I could."
        show valerie smi
        voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL8.ogg"
        vb "Aw, alright, I'll forgive you then. But only because you were so eager to see me."
        show note:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        "She winks at me."

    "You? A lady? Ha!":
        pf "Then it's a good thing there are no ladies here. I certainly wouldn't want her to wait."
        show valerie sad
        "Valerie pouts."
        ### VOICE - currently multiple takes, make sure knocked down to 1 take
        voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL9.ogg"
        vb "What am I if not a lady?"
        pf "You're indescribable." 
        show valerie cur
        "She raises an eyebrow."
        voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL10.ogg"
        vb "Indescribable as in...?"
        pf "As in \"indescribable.\"."
        "After a moment, she shrugs."
        show valerie smi
        show drop:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL11.ogg"
        vb "I'll take it as a compliment."

    "Stare her down.":
        "I'm not even going to grace her with an answer."
        voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL12.ogg"
        vb "Well?"
        "I don't respond."
        "Valerie watches me, then smirks."
        show valerie smi
        voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL13.ogg"
        vb "You like what you see?"

        menu:
            "No.":
                pf "Eh, I've seen better."
                show valerie hap
                show note:
                    xoffset 720
                    yoffset 125
                    xzoom .75
                    yzoom .75
                "Valerie laughs."
                voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL14.ogg"
                vb "Sure, that's why you can't keep your eyes off of me."
                "I quickly look away."

            "Yes.":
                pf "I certainly wouldn't say no."
                show valerie hap
                show heart:
                    xoffset 720
                    yoffset 125
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL15.ogg"
                vb "Straight to the point, I see."

            "I don't know how to answer!" if (MCStory == 2):
                pf "Trick question! There is no right answer."
                show valerie hap
                show heart:
                    xoffset 720
                    yoffset 125
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL16.ogg"
                vb "Aw, you're smarter than you look."
                pf "Hey!"
                "Valerie laughs."

pf "Have you ordered yet?"
show valerie smi
voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL17.ogg"
vb "No, I was waiting for a certain someone to get their butt over here."
pf "So what I'm hearing is you want to see my butt."
show valerie mis
"Valerie smirks."
voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL18.ogg"
vb "Give me a twirl then."

menu:
    "Change the topic.":
        pf "Wow, this menu is certainly extensive, don't you think?"
        "Valerie masks her smile and pretends to pout."
        voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL19.ogg"
        vb "Aw, I don't get a private show?"
        "I don't dignify her with a response, but the heat rises to my face."

    "I put the \"maximus\" in \"gluteus maximus\".":
        show valerie cur
        "Without hesitation, I jump to my feet and give her a leisurely turn. Then throw in a small wiggle for good measure."
        "Valerie works hard to keep a straight face."
        show valerie mis
        show heart:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        ### VOICE - missing line?
        voice "audio/voice/MISSING/BATCH4/Valerie/ValE3Redos/E3ValerieArcS1Redo1.ogg"
        vb "That just made the wait worth it."
        pf "I knew it would."

    "I won't fall for your objectification.":
        pf "I don't have to because I'm more than just my body."
        show valerie mis
        "Valerie smirks."
        voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL20.ogg"
        vb "Sounds like someone skipped their squats at the gym and is embarrassed."
        pf "I won't fall for that either."
        "She pouts, but has trouble keeping a straight face."

"I flip open the menu and take a minute to read my options. Valerie and I both place our orders, then she pulls out a pencil and sketchbook."
pf "What are you doing?"
show valerie smi
voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL21.ogg"
vb "Not me… you."
pf "Huh?"
"She pushes the sketchbook towards me and grins playfully."
show valerie hap
voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL22.ogg"
vb "I want you to draw me like one of your French girls."

menu:
    "I can try…":
        pf "Okay…"
        "I pick up the pencil awkwardly. I don't even know where to start."
        pf "I'm not very good at drawing. I haven't really done this before."
        show valerie smi
        voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL23.ogg"
        vb "That's okay. I'll help you since it's your first time."

    "As you wish!":
        pf "If you insist, but you'll have to disrobe first as all of my French girls are painted in their purest form."
        show valerie mis
        "Valerie grins devilishly and slips one shoulder out of her jacket, then the other…"
        "My eyes widen as I drink in the scene. I can't believe that worked! Thank you, God!"
        "She slowly shimmies her arms out of the jacket."
        show valerie hap
        voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL24.ogg"
        vb "Okay, I've disrobed for you."
        "She laughs at my look of disappointment."

    "Eh…":
        pf "Art is not my thing."
        show valerie neu
        voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL25.ogg"
        vb "So?"
        pf "So I don't do it."
        "She pouts and blinks puppy dog eyes at me."
        voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL26.ogg"
        vb "Not even for me?"
        "I'm barely even phased. All those guilt trips from Nikki were good for one thing, I guess."
        pf "Nope."
        show valerie sad
        voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL27.ogg"
        vb "Aw, come on, I drew you. It's only fair that you draw me."
        show crying:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL28.ogg"
        vb "Pleeeaaase?"
        "I couple of cafe patrons are giving me dirty looks."
        pf "Fine, if it will make you stop."
        show valerie smi
        "She grins."

show valerie smi
"She leans onto the table, rests her chin in her hands, and flashes me a warm smile. Taking this as my cue to start drawing, I clumsily trace the pencil around the page."
"As hard as I try, my uncoordinated fingers cannot illustrate what my eyes see."
"..."
voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL29.ogg"
vb "Are you done yet?"
"Valerie speaks through her teeth, trying not to disturb her pose."
pf "No."
"I continue to sketch. {w}After a few minutes Valerie tries again."
show valerie cur
voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL30.ogg"
vb "How about now?"
pf "Still no."
"She waits another couple of minutes."
voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL31.ogg"
vb "... Now?"
pf "Calm down! It'll be done when it's done."
show valerie dis
"She sighs heavily."
show storm:
    xoffset 720
    yoffset 125
    xzoom .75
    yzoom .75
voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL32.ogg"
vb "The things I have to do for you…"
pf "In case you forgot, {i}you're{/i} the one who asked {i}me{/i} to draw you. You can't rush these things."
voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL33.ogg"
vb "Shouldn't you be concentrating? What are you doing talking to me."
pf "{i}You{/i} are the one talking to {i}me{/i}!"
voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL34.ogg"
vb "If you spent more time on your drawing and less time blaming me for things you'd be done by now."
"I glare at her."
show valerie smi
"She winks before returning to her pose."
"We fall silent as I work on the drawing. Valerie stares confidently at me, never looking away when I glance up at her. For some reason that makes me even more nervous."
"I push away my embarrassment and focus on her features. For all the times I've looked at her, I haven't really seen just how perfectly her features flow into each other."
"It's the first time I've noticed just how truly beautiful she is, and my face flushes from the thought."
"The next time I glance up at Valerie her smile looks more genuine. I know she saw me blush and that makes me blush even more."
"After a few more minutes, I drop my pencil."
pf "Okay, done."
"Valerie breaks from her pose."
show valerie cur
voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL35.ogg"
vb "Let me see!"
"Pushing forward the sketchbook, I wonder if she'll like that I drew her…"

menu:
    "...With tig ol' bitties!":
        show valerie sur with dissolve
        show exclamation:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        "She stares at the drawing and her eyes grow wide in wonder."
        "She doesn't react right away and I'm worried that she doesn't like it. Then, unexpectedly,  she looks down at herself and holds her hands over chest as if comparing them with something."
        pf "Uh…"
        show valerie cur
        "Suddenly, she grabs her breasts and begins to lift and push them together!"
        pf "Wha--Whoa! Hey! What are you doing?"
        show valerie thi
        voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL36.ogg"
        vb "I don't know what I was doing earlier, but if that's what I look like then I need to do that more often..."
        "My face burns as she continues to play with her chest. {w}Although I'm reluctant to make her stop, I don't need her attracting attention to herself and giving people the wrong idea."
        pf "I could give you a hint."
        show valerie cur
        voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL37.ogg"
        vb "Hm?"
        "She pauses and looks at me expectantly."
        pf "Why don't you lean over the table to get a better look at the drawing?"
        "Valerie blinks, then smirks and leans forward so I can see the top of her cleavage through her shirt."
        voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL38.ogg"
        vb "Like this?"
        pf "Perfect."
        "I'm sure she noticed I'm not looking at her face."
        show valerie hap b1 with dissolve
        voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL39.ogg"
        vb "Haha! You're a pervert!"
        "There's a smile on her face and she doesn't move from her position."

    "...As accurately as possible.":
        "She stares at the drawing and her eyes grow wide. She grabs the sketchbook off the table and studies it closely."
        pf "I hope it's okay…"
        show exclamation:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        show valerie sur
        voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL40.ogg"
        vb "This is more than okay! It's really good!"
        "I blink. I'd anticipated she'd use a lot of choice words, but \"good\" was not one of them."
        pf "Really?"
        show valerie cur
        voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL41.ogg"
        vb "Yeah! You really captured the eyes. They're so expressive."
        pf "Do they look like they're up to no good?"
        show valerie hap
        "She laughs."
        voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL42.ogg"
        vb "They look like they only do good. All the time."
        pf "Then I guess I've still got a long way to go."
        "She continues to look at the drawing."
        pf "You really think it's that good?"
        show valerie smi
        voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL43.ogg"
        vb "Mmhm. It's really pretty."
        pf "I had a good model. I just drew what I saw."
        "She hugs the sketchpad to her chest and beams."
        pf "Well, it's good to know that if this whole engineering thing doesn't work out you can always fall back on a modeling career."
        show valerie hap b1 with dissolve
        voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL44.ogg"
        vb "I'll keep that in mind."
        "Her cheeks are tinged pink. I think she's genuinely flattered."

    "...Like an ironing board.":
        stop music fadeout 5
        show valerie cur
        "She looks at my drawing, and her eyes grow wide."
        show valerie dis
        voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL45.ogg"
        vb "What is this?"
        "She points accusingly at the page."
        pf "A drawing…?"
        show storm:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL46.ogg"
        vb "Look closer."
        play music "audio/music/Baka! (GAME VERSION).ogg" fadein 3
        "Her finger points right to the chest."

        menu:
            "I don't get it...":
                pf "What do you mean?"
                voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL47.ogg"
                vb "You know exactly what I mean."
                pf "I just said that I don't--"
                "She looks hard at me. {w}Um, okay. I'll have to figure this out myself."
                "I focus again on the drawing and zoom in to where her finger points… that space below the neck but above the…"
                show valerie cur
                "I've got it!"
                pf "I forgot to draw in your necklace!"
                "Leaning over the table, I quickly add in a thin chain to hang below her throat. {w}Valerie stares at me in disbelief."
                show valerie dis
                voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL48.ogg"
                vb "Are you serious? That's what you think is missing?"
                pf "Uhh…"
                "She leans over the table."
                show vein:
                    xoffset 720
                    yoffset 125
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL49.ogg"
                vb "Don't you think there's something else missing?"
                pf "Um…?!"
                "She continues to lean forward, resting her chest on the table so it pushes her breasts up. My eyes are drawn to her chest and the heat rises in my cheeks."
                stop music fadeout 10
                pf "I--I think I got it."
                show valerie smi
                "Valerie follows my line of sight right before I look away."
                voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL50.ogg"
                vb "Are you sure?"
                "When I look back at her she's grinning, which causes me to blush further."
                pf "Yes!"
                "She falls back against her seat, still grinning."
                show valerie hap
                voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL51.ogg"
                vb "Better late than never, I guess."

            "This is an accurate representation.":
                pf "What is your complaint?"
                show vein:
                    xoffset 720
                    yoffset 125
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL52.ogg"
                vb "Don't you think there's a certain something missing?"
                pf "I only drew what I saw."
                show valerie sad
                "She pouts."
                voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL53.ogg"
                vb "So this is how you see me?"
                pf "Hm… Maybe I should take another look."
                show valerie cur
                "I very obviously stare at Valerie's breasts, and I'm enjoying the view when something flies at my face."
                pf "Hey!"
                show valerie hap
                "Valerie laughs and throws another sugar packet at me."
                stop music fadeout 10
                pf "Stop!"

                if (MCStory == 1):
                    "I catch the third one that flies at me."
                    voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL54.ogg"
                    vb "Nice catch!"
                    "With a devilish grin, I throw it back at her."

                else:
                    "As I protest, another one hits me in the face. {w}Oh yeah? Two can play at that game! I grab a sugar packet and toss it at her."

                show valerie cur
                "She ducks out of the way."
                voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL55.ogg"
                vb "Hey! That's not how you treat a lady."
                pf "Don't start something you can't finish."

            "Boobs.":
                pf "Those are your breasts."
                show valerie ann
                voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL56.ogg"
                vb "Really? Because I don't see any \"breasts\" there!"
                show valerie sur b2 with dissolve
                show shoBlush:
                    xoffset 720
                    yoffset 125
                    xzoom .75
                    yzoom .75
                "Her voice is louder than expected and attracts the attention of nearby patrons. She slowly slinks back into her chair as her cheeks turn red. {w}This is the first time I've seen her embarrassed!"
                show valerie neu b1 with dissolve
                "Picking up the pencil, I draw two circles over the chest in the drawing."
                stop music fadeout 10
                pf "Happy now?"
                show valerie dis with dissolve
                voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL57.ogg"
                vb "That looks dumb."
                show valerie smi
                "Despite her comment, there's a smile on her face."

"Valerie glances at the time and wrinkles her nose."
show valerie neu with dissolve
voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL58.ogg"
vb "Ugh, I've got class soon."
pf "...Don't sound so excited about it."
voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL59.ogg"
vb "It's not a fun one."
pf "Which one is it?"
voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL60.ogg"
vb "Introduction to Art History."
pf "Don't you like art?"
show valerie cur
voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL61.ogg"
vb "I do! And since I also like history, I thought this would be a good choice for one of my electives."
pf "So why the disappointment?"
show valerie thi
voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL62.ogg"
vb "Well, it turns out that although I like history and I like actually creating art, learning about other people creating art is not as fun."
pf "So was watching me create art for you today not fun either?"
show valerie smi
"She smirks."
voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL63.ogg"
vb "That doesn't count. I was part of the creative process."
pf "That's true."
"She glances again at the time and gathers her things."
voice "audio/voice/E3/Free/VB/S1/valerie/E3ValArcL64.ogg"
vb "Okay, I've got to head out."
"I nod."

scene black with fade

"After we pay for our drinks, we head our separate ways, but not before I catch Valerie fondly sneak another peek at my drawing."

stop music fadeout 3
stop ambient fadeout 3
$renpy.pause(2.5)

$ E3VBS1_Completed = 1