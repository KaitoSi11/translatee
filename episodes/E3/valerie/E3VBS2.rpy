#
label E3VBS2:


$ valOut = renpy.random.choice(['Gym'])
$ valHairF = renpy.random.choice(['pony'])
$ valHairB = renpy.random.choice(['pony'])

stop music fadeout 3
stop ambient fadeout 3
$renpy.pause(1.0)
scene black with fade

if (MCStory == 1):
    "I've been acing Physical Education these past couple of weeks, but I still feel like I need a challenge. I better hit the gym and get some extra training in."

else:
    "I've been slacking a little on my training and I can feel myself falling slightly behind in Physical Education. I need to be in peak condition for our match this week, so it's time to hit the gym!"

"When I arrive at the rec center, I head straight to the lockers to change. Afterwards, I walk towards the main gym but decide to go around the back entrance. It's closer to the weight section so I don't have to weave through the cardio equipment."


scene bg campus gym day with fade
"As I follow the new route, I walk past the rec center's group classrooms. There are no classes scheduled at this time, so I'm surprised to see a familiar lone figure pummeling a free-standing punching bag."

show valerie ann at cc with dissolve
pf "Valerie?"
play music "audio/music/Stress (GAME VERSION).ogg" fadein 5
"She pauses, and her hair whips across her face as she turns towards the sound of my voice."
show valerie neu
voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL65.ogg"
vb "Oh, it's you."
pf "Glad to see you too…"
"Instead of biting back with her usual witty retort, Valerie refocuses on the punching bag and throws another jab."
show valerie ann
"I've never seen her like this before… {w}With her fierce scowl and that murderous look in her eyes, she kind of reminds me of Kaori…"
pf "Geez, what did that thing ever do to you?"
show valerie ang
voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL66.ogg"
vb "It's what it {i}didn't{/i} do!"
show valerie ann
"She strikes the bag with a powerful roundhouse. The bag wobbles from the force."
pf "Whoa…"
"There's no way this tiny girl can pack that much power without many years of training under her belt."
pf "Remind me not to get on your bad side…"

"Just then, a soft melody fills the room. Valerie glances at her gym bag, which was tossed to the side of the room, and her frown returns. Instead of answering the phone call, she resumes her fighting stance in front of the punching bag and aims a hard punch."
pf "Uh, aren't you going to get that?"
voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL67.ogg"
vb "Why? So she can disappoint me all over again?"
"She finishes her question with a yell and another punch. Her hair sticks to her face and neck and her skin glistens with a layer of sweat. The call seems to have riled her up even more and she's getting sloppy with her movements."
pf "Valerie, are you okay?"
"{i}Punch.{/i}"
voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL68.ogg"
vb "What does it look like?"
"{i}Kick.{/i}"
pf "It looks like you should tell me what's bothering you."
"She prepares for another kick, when I stop her."
pf "Valerie..."
show storm:
    xoffset 720
    yoffset 125
    xzoom .75
    yzoom .75
"She grits her teeth, but after a moment, she lets her hands drop to her sides."
show valerie neu
voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL69.ogg"
vb "... It's my mom."
pf "What about her?"
show valerie ann
voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL70.ogg"
vb "She's breaking her promises… {i}again{/i}!"
"She accentuates that last word with an angry punch."
voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL71.ogg"
vb "This weekend was supposed to be {i}our{/i} weekend. She promised she'd fly out and come visit me for the first time since I started here at ACE, but of course that's not going to happen anymore."
"I'm taken aback by the bitterness in her voice."
pf "Why not?"
voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL72.ogg"
vb "Because apparently her {i}new{/i} boyfriend is more important than her own daughter!"
"She vents her frustrations with a formidable sidekick, wobbling the punching bag once more."
pf "I'm sure that's not--"
voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL73.ogg"
vb "It's true. She called me earlier today to tell me she can't make it because \"mon chéri Matthieu\" surprised her with a romantic getaway for the weekend."
pf "Didn't she tell him about her plans with you?"
show valerie neu
voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL74.ogg"
vb "Yes? I don't know. All I understood was that he had already made all the arrangements and bookings and it was all so romantic that she couldn't say no."
show valerie ann
stop music fadeout 10
voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL75.ogg"
vb "And the best part is when she told me \"Ma belle, why are you getting so worked up? I can see you at any time\"."
pf "Anytime… in Japan…"
voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL76.ogg"
vb "Yup."
"I'm dumbfounded. No wonder she's so angry!"

$ E3VBS2_LoopBackStop = 0

label E3VBS2_MenuLoopBack:
menu:
    "That's wrong of her...":
        pf "I'm sorry that this happened to you. She shouldn't have done that."
        show valerie sad
        "Valerie sighs."
        voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL77.ogg"
        vb "It's my own fault. I should have known that would happen."
        pf "Nobody would expect that, especially from their own mother. You deserve so much better."
        show valerie cur
        "Valerie stares at me with a strange look on my face, as if she can't believe I just said that."
        show valerie hap
        play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 5
        "Then she bursts out laughing."
        pf "Uhh, was it something I said…?"
        show valerie smi
        voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL78.ogg"
        vb "That line sounds like it came straight out of a soap opera."

    "The silver lining is we can hang out!":
        play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 5
        pf "Lucky for you, my weekend just opened up."
        show valerie cur
        "Valerie gives me a strange look."
        voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL79.ogg"
        vb "What does that mean?"
        pf "That depends. On a scale of 1-10, how emotionally vulnerable are you?"
        show valerie smi
        "She pauses, then chuckles."
        voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL80.ogg"
        vb "Just enough…"
        pf "I like where this is going."
        show valerie hap
        voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL81.ogg"
        vb "...for us to cuddle and talk about our feelings!"
        pf "Actually, I forgot. There was a thing I have to do this weekend."
        show valerie mis
        "Valerie bursts out laughing."

    "She's missing out.":
        pf "It's her loss."
        show valerie cur
        "Valerie looks curiously at me."
        pf "She's missing out on the chance to see her daughter, who is not only in one of the top university programs for Cenorobotics, but also a kickass engineer."
        show valerie smi
        play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 5
        "A broad grin spreads across Valerie's face."
        voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL82.ogg"
        vb "I had no idea that's what you thought of me."
        pf "...You were just fishing for compliments, weren't you?"
        show valerie hap
        "She laughs."

    "AT LEAST YOU HAVE A MOM!" if (E3VBS2_LoopBackStop == 0):
        $ E3VBS2_LoopBackStop = 1
        "Wait, is this really how I want to respond?"

        menu:
            "YES!":
                "Am I sure? Even though this is a really awful thing to say?"

                menu:
                    "YES YES YES!":
                        stop music fadeout 1
                        pf "At least you have a mom who can cancel plans on you!"
                        show valerie sur with dissolve
                        "Valerie stares at me and grows pale. For once, she's speechless. We stare at each other for a painfully long time."
                        $renpy.pause(1.5)
                        scene black with fade
                        $renpy.pause(1.0)
                        scene bg campus gym day
                        show valerie ann at cc
                        with fade
                        "I snap back to reality. {w}Yeah, there's no chance that would ever go well."
                        jump E3VBS2_MenuLoopBack

                    "NO!":
                        "Yeah, better not."
                        jump E3VBS2_MenuLoopBack
                
            "NO!":
                "I didn't think so. Let's try that again."
                jump E3VBS2_MenuLoopBack

show valerie neu with dissolve
"Valerie seems to be in better spirits at least. {w}Once she catches her breath, she sighs in resignation."
voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL83.ogg"
vb "This is just how she is and I hate that after all these years I still believe that she'll be different… That this time she really will follow through with her promises."
show valerie sad
voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL84.ogg"
vb "I mean, I had planned a whole day of fun things for us to do when she got here, and I'm disappointed that won't be happening now."
pf "It'll still happen. I'll do it with you."
show valerie sur
show exclamation:
    xoffset 720
    yoffset 125
    xzoom .75
    yzoom .75
"She blinks, clearly surprised."
show valerie cur
voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL85.ogg"
vb "But you don't even know what I have planned."
pf "It doesn't matter. If I'm hanging out with you, I know I'll have a good time."
"She stares at me again with that strange look of disbelief. Then slowly her face melts into a bright smile. She flings her arms around my neck and hugs me tight."
show valerie hap
show heart:
    xoffset 720
    yoffset 125
    xzoom .75
    yzoom .75
voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL86.ogg"
vb "Thank you!"

menu:
    "She's hugging me!":
        "She beams at me as she pulls away."
        "Her faint perfume of wildflowers lingers on my body even after she lets go. I can still feel the heat of her skin spreading up my neck and to my face… Or maybe that's the heat of my blush…"
        pf "N-No problem!"
        show valerie mis
        show note:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        "Valerie giggles."
        voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL87.ogg"
        vb "Are you blushing?"
        pf "No!"
        "The burn in my face is undeniable."
        pf "Well, maybe."
        pf "Okay, yes…"
        show valerie smi
        "She continues to look at me with amusement. {w}I need to change the subject! Scanning the room, my gaze falls on her forgotten punching bag."
        pf "Why don't you give that punching bag a rest and practice with me?"
        "She smirks."
        show valerie mis
        voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL88.ogg"
        vb "No… well, maybe… okay, yes."
        pf "Very funny."

    "This would be better if she weren't so sweaty.":
        "She beams at me as she pulls away."
        pf "I don't know if you realise this, but you are pretty sweaty."
        show valerie sur with dissolve
        $renpy.pause(.75)
        show valerie ang with dissolve
        "In one smooth moment, Valerie flips me over her hip and throws me on my back. It happened so quickly, I still can't make out how I went from standing to falling."
        pf "Ow…"
        show valerie ann
        voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL89.ogg"
        vb "How dare you say something like that to a lady."
        pf "A lady can't usually do that."
        show valerie mis with dissolve
        "She laughs and offers me a hand to help me up."
        pf "Well, I was going to offer to practice with you, but I'm not sure I want to get beat up again."
        show valerie smi
        voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL90.ogg"
        vb "How about I show you a few moves?"
        voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL91.ogg"
        vb "I promise I'll be gentle."
        pf "No more throwing?"
        show note:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL92.ogg"
        vb "Only when you deserve it."
        pf "Fair enough."

    "...":
        "I freeze in place."
        show question:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        show valerie cur
        voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL93.ogg"
        vb "Are you okay?"
        pf "Yeah, why?"
        show valerie ner
        voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL94.ogg"
        vb "It's like hugging a pole…"
        show valerie neu
        voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL95.ogg"
        vb "Usually people will, you know, hug back or something."
        pf "Oh, sorry."
        "I lift one arm and wrap it around Valerie's back. Then I pat her a couple of times before letting go."
        "She raises an eyebrow as she pulls away."
        show valerie thi
        show drop:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL96.ogg"
        vb "I'm not going to lie. That was pretty bad."
        pf "Okay."
        "We stand in silence, and I feel obligated to say something."
        pf "So, how about you give that punching bag a rest and practice with me instead?"

if (MCStory == 1):
    show valerie mis
    "Valerie grins and is about to punch my arm when I block her."
    voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL97.ogg"
    vb "That's a good start."

else:
    show valerie mis
    "Valerie grins and playfully punches my arm in response."
    pf "Hey!"
    "She chuckles."
    
show valerie hap
voice "audio/voice/E3/Free/VB/S2/valerie/E3ValArcL98.ogg"
vb "Step one is to teach you how to block."  

scene black with fade

"I find some extra pads lying around and join Valerie in her practice session. We spend the rest of the evening together until we both have to leave the room for a scheduled group class."

stop music fadeout 3
stop ambient fadeout 3
$renpy.pause(2.5)

$ E3VBS2_Completed = 1