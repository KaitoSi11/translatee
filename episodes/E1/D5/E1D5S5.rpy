label E1D5S5:


"I wonder what Shou's doing."
play sound "audio/sfx/Technology/Phone Dial.ogg"
"I grab my phone and dial his number."
play sound "audio/sfx/Technology/Phone Answer.ogg"
"He picks up after a few rings."
voice "audio/voice/E1/D5/S5/Shou/1.ogg"
ss "Broseph, what can I do for you?"
pf "Hey man, want to chill or something?"
voice "audio/voice/E1/D5/S5/Shou/2.ogg"
ss "Yeah! I'm at the cafe near campus. Why don't you drop by?"
pf "Sounds good. I'll head out now."
voice "audio/voice/E1/D5/S5/Shou/3.ogg"
ss "Cool, see you soon!"
"I say a quick goodbye before hopping on my bike."

stop music fadeout 3.0
stop ambient fadeout 3.0
scene black with fade
$renpy.pause(.5)   

label E1D5S5_ConvergenceFromMayuCall:

play sound "audio/sfx/Vehicles/Bike Ignition.ogg" fadeout 4
$renpy.pause(4.0)

$ shoOut = "sCasual"
$ mayOut = "sCasual"

play ambient "audio/ambience/Desert Maid Cafe.ogg" fadein 2
play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5.0
scene bg campus cafe day with fade

$renpy.pause(.25)

if (E1D5S1_EventShou == 1):

    show shou smi at l2
    show mayu neu at r2
    with dissolve
    "I enter the cafe and see Shou waving at me from the back corner of the room."
    "As I make my way over I'm surprised to see Mayu staring silently at me."
    show mayu smi with dissolve
    "She smiles politely when she notices my gaze."
    show shou hap
    voice "audio/voice/E1/D5/S5/Shou/4.ogg"
    ss "Good to see you, man."
    pf "Hey Shou, Mayu. I didn't know you'd both be here."
    show shou cur
    "Shou blinks in surprise."
    voice "audio/voice/E1/D5/S5/Shou/5.ogg"
    ss "That's not a problem is it? Mayu was actually the one who wanted to come here."
    "Wait--Mayu invited him...?"
    pf "Of course not, but if you two already made plans I can always hang out with you later."
    show shou hap
    voice "audio/voice/E1/D5/S5/Shou/6.ogg"
    ss "Don't be ridiculous! I invited you so you should stay. Mayu doesn't mind."
    "I glance at her and she shakes her head."
    voice "audio/voice/E1/D5/S5/Mayu/1.ogg"
    ma "No, please, join us."
    voice "audio/voice/E1/D5/S5/Shou/7.ogg"
    ss "Have a seat."

    menu:
        "I don't want to interrupt them.":
            $ E1D5S1_EventShou = 0
            $ E1D5S1_EventAlone = 1
            pf "Actually, you two look like you're in the middle of something so I'll hang out with you later."
            show mayu cur
            show shou neu
            voice "audio/voice/E1/D5/S5/Shou/8.ogg"
            ss "You don't have to go."
            show mayu sad
            voice "audio/voice/E1/D5/S5/Mayu/2.ogg"
            ma "Please don't leave on my account."
            pf "No, no, it's not you. I have some stuff I need to get done anyway. You two have fun okay? I'll see you later!"
            show mayu cur
            "Shou looks like he wants to protest, but I wave and leave before he can."
            hide mayu
            hide shou
            with dissolve
            "I heard a new GEAR simulator came out at an arcade nearby, I might as well go check it out."
            "I return to my bike and head out."
            jump E1D5S2_ArcadeConvergence

        "Sit down.":
            pf "Thanks."
            "I sit down beside Shou."

elif (E1D5S1_EventMayu == 1):

    show shou smi at l2
    show mayu neu at r2
    with dissolve
    "Shou waves me over to the back of the cafe where he and Mayu are sitting."
    show mayu smi with dissolve
    "Mayu smiles when she notices me."
    voice "audio/voice/E1/D5/S5/Mayu/3.ogg"
    ma "Hi."
    pf "Hey Mayu, Shou."
    show shou hap
    voice "audio/voice/E1/D5/S5/Shou/4.ogg"
    ss "Good to see you, man!"
    voice "audio/voice/E1/D5/S5/Shou/7.ogg"
    ss "Have a seat."
    pf "Thanks."
    "I sit down beside Mayu."

show shou smi
show mayu smi
"Shou slides me a menu. I quickly scan it, and when the waitress comes over I ask for a green tea latte. The waitress leaves as soon as I order."
pf "What about you guys?"
voice "audio/voice/E1/D5/S5/Shou/9.ogg"
ss "It's okay, we already ordered."
pf "Oh..."
voice "audio/voice/E1/D5/S5/Shou/10.ogg"
ss "So, what rank do you think we earned?"
pf "Huh?"
show shou mis
voice "audio/voice/E1/D5/S5/Shou/12.ogg"
ss "From the qualifiers."

menu:
    "Probably somewhere mid-range.":
        pf "Hm, I think we'll fall somewhere mid-range."
        voice "audio/voice/E1/D5/S5/Shou/13.ogg"
        ss "Yeah? Why's that?"
        pf "Well, I know I certainly could have done better if I had my weapons, but we still did well despite that. I think that'll average things out."
        show shou hap
        voice "audio/voice/E1/D5/S5/Shou/14.ogg"
        ss "I'm with you there!"

    "Top ten for sure!":
        pf "Oh, we'll definitely be up top!"
        show shou cur
        voice "audio/voice/E1/D5/S5/Shou/15.ogg"
        ss "You think so?"
        pf "Yeah! Did you see those AI's? By the time we were done with them they were as good as scrap metal."
        show shou hap
        "Shou just laughs."

    "Somewhere on the lower end of the spectrum.":
        pf "I'm not sure... We could have done better."
        show shou thi
        show mayu cur
        voice "audio/voice/E1/D5/S5/Shou/16.ogg"
        ss "I thought we did well."
        pf "Yeah, but there were a lot of factors against us and I don't think we were at our peak."
        show shou neu
        show mayu neu
        voice "audio/voice/E1/D5/S5/Shou/17.ogg"
        ss "Hmm."
voice "audio/voice/E1/D5/S5/Shou/18.ogg"
ss "Well, I think we're going to get a good ranking! What do you think, Mayu?"
show mayu cur
voice "audio/voice/E1/D5/S5/Mayu/4.ogg"
ma "We'll probably be somewhere in the 20's range."
show shou hap
voice "audio/voice/E1/D5/S5/Shou/19.ogg"
ss "That's pretty good!"
show mayu smi
"The waitress sets down my latte. I breathe in the fragrant tea and take a sip. It tastes even better than it smells--the perfect mixture of tea and milk."
show shou smi
voice "audio/voice/E1/D5/S5/Shou/20.ogg"
ss "How is it?"
pf "Amazing."
show shou mis
"Shou grins."
voice "audio/voice/E1/D5/S5/Shou/21.ogg"
ss "Now you know our worst kept secret. This is the best cafe on campus."
pf "Worst kept secret?"
show note:
    xoffset 1040
    yoffset 135
    xzoom .75
    yzoom .75
show mayu hap
voice "audio/voice/E1/D5/S5/Mayu/5.ogg"
ma "Because everyone else knows this place is good too."
show mayu smi
show shou smi
voice "audio/voice/E1/D5/S5/Shou/22.ogg"
ss "Yeah!"
pf "Ohh."
"They both wait patiently while I sip my drink."
pf "Didn't you guys order too?"
"Mayu nods."
pf "So where are your drinks?"
voice "audio/voice/E1/D5/S5/Shou/23.ogg"
ss "We finished them."
pf "You mean you guys had ordered and finished your drinks before I even arrived?"
voice "audio/voice/E1/D5/S5/Shou/24.ogg"
ss "Yeah."
pf "Oh."
"Another silence falls. Suddenly my tea seems very interesting."
"After a few minutes, Mayu stands."
voice "audio/voice/E1/D5/S5/Mayu/6.ogg"
ma "I'm sorry but I just remembered I need to go. I promised my father I'd meet him later today."
show exclamation:
    xoffset 365
    yoffset 20
    xzoom .75
    yzoom .75
show shou cur
"Shou seems surprised."
voice "audio/voice/E1/D5/S5/Shou/25.ogg"
ss "Really? I thought earlier you said you were free all day."
show mayu ner with dissolve
stop music fadeout 5
voice "audio/voice/E1/D5/S5/Mayu/7.ogg"
ma "I'm sorry, I had forgotten about this. I'll catch up with you later."
show mayu smi with dissolve
$renpy.pause(.5)
hide mayu
with dissolve
$renpy.pause(.5)
hide shou with dissolve
"We exchange goodbyes and she leaves."
show shou neu at cc with dissolve
play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 10
"I continue to sip at my drink while Shou watches her walk away, his face a mirror of curiosity and skepticism. Once she is completely out of earshot, I turn back towards Shou."
pf "Mayu left in kind of a hurry…"
voice "audio/voice/E1/D5/S5/Shou/26.ogg"
ss "Yeah…"
pf "Is that normal?"
show shou thi
voice "audio/voice/E1/D5/S5/Shou/27.ogg"
ss "No."
"I wonder if she's disappointed I dropped in and interrupted them."
pf "Do you think she left because of me?"
show shou cur
"He glances at me in surprise."
voice "audio/voice/E1/D5/S5/Shou/28.ogg"
ss "Why would you think that?"
pf "Well, I don't know. She left pretty soon after I arrived… Is there anything going on between you two?"
show shou neu
voice "audio/voice/E1/D5/S5/Shou/29.ogg"
ss "Nothing. We're just friends."
pf "Does she know that?"
show question:
    xoffset 720
    yoffset 20
    xzoom .75
    yzoom .75
voice "audio/voice/E1/D5/S5/Shou/30.ogg"
ss "Huh?"
pf "I kind of get the feeling that she might be into you…"
show shou cur
$renpy.pause(.75)
show shou hap with dissolve
$renpy.pause(.5)
"Shou pauses, then bursts out laughing."
show shou smi
voice "audio/voice/E1/D5/S5/Shou/31.ogg"
ss "That's silly! Mayu and I have known each other for years. I'm pretty sure she sees me as her older brother."

if (E1D5S1_EventMayu == 1):
    pf "So… you wouldn't mind if I maybe ask her out sometime?"
    show shou mis
    "Shou flashes me a wide grin."
    voice "audio/voice/E1/D5/S5/Shou/32.ogg"
    ss "For real? You two would be great together! Mayu's an awesome girl."
    pf "Yeah, I can tell."

    menu:
        "Talk to Shou about something else.":
            $ E1D5S5_MechConversation = 1
            jump E1D5S7_MechConvergence

        "Since Mayu's already left I have no reason to stay.":
            "I down the last bit of my drink."
            pf "It was good to see you again, Shou, but I need to be heading out too. I've got to do something with Nikki."
            show shou smi
            "He looks a bit surprised but nods."
            voice "audio/voice/E1/D5/S5/Shou/38.ogg"
            ss "No problem. We can hang out another time."
            pf "Yeah."
            
            stop music fadeout 3.0
            stop ambient fadeout 3.0
            scene black with fade
            $renpy.pause(2.0)   
            
            "We both get up and pay for our orders, then leave the cafe and head our separate ways."
            "I spend some time at the mall checking out GEAR equipment. Once it gets late, I head home."
            jump E1D5S7
            
elif (E1D5S1_EventShou == 1):
    menu:
        "Continue this conversation.":
            pf "How long have you two known each other anyway?"
            show shou smi
            voice "audio/voice/E1/D5/S5/Shou/39.ogg"
            ss "Since forever--we grew up together."
            pf "Oh wow."
            ss "Yeah."
            pf "You two have really different personalities. I never would have guessed that you guys were such old friends."
            "Shou laughs again."
            show shou hap
            voice "audio/voice/E1/D5/S5/Shou/40.ogg"
            ss "Yeah, I get that a lot. I think we compliment each other."
            show shou smi
            voice "audio/voice/E1/D5/S5/Shou/40_1.ogg"
            ss "We understand each other because we watched each other become the person we are today."
            pf "And you don't think that kind of bond creates feelings?"
            voice "audio/voice/E1/D5/S5/Shou/41.ogg"
            ss "Nah, not that kind of feelings."
            pf "Hm… What about this cafe date then?"
            show shou cur
            voice "audio/voice/E1/D5/S5/Shou/42.ogg"
            ss "It wasn't a date. We do this all the time."
            pf "Do what?"
            show shou thi
            voice "audio/voice/E1/D5/S5/Shou/43.ogg"
            ss "Come here for coffee, maybe lunch… Sometimes we'll go see a movie afterwards or go to the mall or just hang out. It'd be no different than if you or I did that."

            menu:
                "That is the definition of a date.":
                    pf "Everything you just described sounds like a typical date."
                    show shou ske
                    voice "audio/voice/E1/D5/S5/Shou/44.ogg"
                    ss "What? No."
                    pf "If you wanted to ask someone out on a date, what activity would you ask them to do with you?"
                    show shou thi
                    voice "audio/voice/E1/D5/S5/Shou/45.ogg"
                    ss "I'd ask if they wanted to see a movie, or maybe go to dinner, or get coffee… That's everything I just listed, isn't it?"
                    show shou thi
                    pf "Yup."

                "No homo.":
                    pf "If I didn't know any better, I'd think you wanted to do all of that with me at once."
                    show shou hap
                    voice "audio/voice/E1/D5/S5/Shou/46.ogg"
                    ss "Would that be so bad?"
                    pf "Sorry man, you're just not my type."
                    show shocked:
                        xoffset 720
                        yoffset 20
                        xzoom .75
                        yzoom .75
                    show shou sur
                    voice "audio/voice/E1/D5/S5/Shou/47.ogg"
                    ss "What? No! That is not what I meant! I just meant I'd be cool to hang out as friends."
                    pf "Like how you and Mayu hang out as friends?"
                    show shou cur
                    ss "Yeah."
                    pf "But do all those date things?"
                    show shou sur
                    voice "audio/voice/E1/D5/S5/Shou/48.ogg"
                    ss "Yeah--Wait, no!"
                    show shou thi
                    "Shou leans back into his chair looking thoughtful."

                "It'd be very different.":
                    pf "If we did that together we'd be going on a date."
                    show shou cur
                    voice "audio/voice/E1/D5/S5/Shou/49.ogg"
                    ss "What? Guys can't do things together as friends?"
                    pf "No, we can--just maybe not all of it at once."
                    show shou thi
                    voice "audio/voice/E1/D5/S5/Shou/50.ogg"
                    ss "... I guess that would be a little weird."
                    pf "Yeah."

            show shou neu
            voice "audio/voice/E1/D5/S5/Shou/51.ogg"
            ss "The point is--it's different with Mayu."
            pf "Sure."
            voice "audio/voice/E1/D5/S5/Shou/52.ogg"
            ss "And she knows that we're just friends."
            pf "Uh-huh, and the fact that she left early today has nothing to do with me being here crashing your date."
            show shou cur
            voice "audio/voice/E1/D5/S5/Shou/53.ogg"
            ss "No, of course not. She had something with her dad."
            pf "Right."
            show shou smi
            "He's a lost cause."

        "Talk about something else.":
            $ E1D5S5_MechConversation = 1
            "I'm unconvinced, but I don't want to push it."
            jump E1D5S7_MechConvergence

            
            
label E1D5S7_MechConvergence:
if (E1D5S5_MechConversation == 1):
    pf "So how's your GEAR doing after the qualifiers? Obviously mine has seen better days."
    show shou mis
    voice "audio/voice/E1/D5/S5/Shou/33.ogg"
    ss "She's hanging in there."
    pf "Okay, I've got to ask--why do you call your GEAR a \"she\"?"
    show shou smi
    voice "audio/voice/E1/D5/S5/Shou/34.ogg"
    ss "Well, you know how people call their cars and boats a \"she\"? Well, Emerald is my boat."
    pf "Okay, but then how come she hasn't got a female frame?"
    voice "audio/voice/E1/D5/S5/Shou/35.ogg"
    ss "Because that's me."
    pf "What?"
    show shou cur
    voice "audio/voice/E1/D5/S5/Shou/36.ogg"
    ss "You know--the GEAR embodies the pilot."
    pf "Yeah, I know that. But if the essence of your GEAR is a female… and the GEAR embodies the pilot… then you--"
    show shou mis
    voice "audio/voice/E1/D5/S5/Shou/37.ogg"
    ss "I can see where you're going with this and I'm going to stop you right there because that's not it. As a vessel, I refer to her as female, but the aesthetics and frame and whatnot are a reflection of me."
    pf "Oh… right."
    show shou hap
    "I nod, but I'm still not sure if I completely understand."

show shou smi
"As the conversation lulls to a close, I take another sip from what I'm surprised to find is an empty cup."
voice "audio/voice/E1/D5/S5/Shou/54.ogg"
ss "You done with that?"
pf "Apparently, yeah."
voice "audio/voice/E1/D5/S5/Shou/55.ogg"
ss "Want another one?"
pf "No, I'm good thanks."

menu:
    "Go home.":
        pf "Well, it was good to see you again but I should be heading out."
        "He nods."
        show shou hap
        voice "audio/voice/E1/D5/S5/Shou/56.ogg"
        ss "Yea, we can hang out again another time."
        show shou smi
        pf "Yeah."
        
        stop music fadeout 3.0
        stop ambient fadeout 3.0
        scene black with fade
        $renpy.pause(2.0)           

        "We both get up and pay for our orders, then leave the cafe and head our separate ways."
        "I spend some time at the mall checking out GEAR equipment. Once it gets late, I head home. "
        jump E1D5S7

    "Let's go to the arcade.":
        pf "Are you doing anything after this?"
        show shou cur
        voice "audio/voice/E1/D5/S5/Shou/57.ogg"
        ss "Not that I know of."
        pf "I'm thinking of heading to the arcade to practice. We could play a few rounds?"
        show shou hap
        voice "audio/voice/E1/D5/S5/Shou/58.ogg"
        ss "Sounds good to me!"
        pf "I only know of the one by my house. Is there a closer one?"
        show shou smi
        voice "audio/voice/E1/D5/S5/Shou/59.ogg"
        ss "Yeah, there's a good one nearby. I'll take you there."
        pf "Cool."
        
        stop music fadeout 3.0
        stop ambient fadeout 3.0
        scene black with fade
        $renpy.pause(2.0)   
        
        "We both pay for our orders, then Shou leads me to the arcade. We play simulated GEAR matches until it gets late. Then we say our goodbyes and head home."
        jump E1D5S7

