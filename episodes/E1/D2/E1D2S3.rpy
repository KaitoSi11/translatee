label E1D2S3:
    
    $renpy.pause(1)
    
    "After parting with Nikki, I make my way to the garage. I can't believe I even considered the bus a possibility when my baby is waiting here for me!"
    
    play sound "audio/sfx/Technology/Garage Door Open.ogg" fadein 1.0
    scene white with fade
    
    "My heart pounds in anticipation as the garage door crawls open and bathes my pride and joy in a halo of soft light. The way the sun sparkles off the polished metal nearly brings tears to my eyes."
    
    "I tenderly caress the bike's smooth curves. We've been apart for so long, but now, we're finally reunited. {w}I'll never leave you again, I promise."
    
    pf "{i}Hup!{/i}"
    
    
    "Vaulting from the back of the bike, I drop into its seat with a soft thud. {w}Still as comfy as ever."
    
    "My hands settle on the handles. As I go through the nuances of preparation, I get the feeling I'm forgetting something important... {w}Something that will protect my brain from becoming pavement pizza."
    $ E1D2S3_mcwithhelmet = 0
    menu:
        "Safety first!":
            $ E1D2S3_mcwithhelmet = 1
            "Only a fool wouldn't wear a helmet."
            scene black with fade
            play sound "audio/sfx/Technology/Helmet HUD Power On.ogg"
            "As it slips over my head, my vision momentarily darkens. Then the HUD illuminates my visor with digital scrolling text and numbers, sharing more information and applications than I need."  
            
            "I remember reading about original helmets, which did nothing more than protect your head. I can't even imagine using such primitive technology. Now, even the most standard helmet includes a GPS, as well as speed monitors and music players." 
    
        "Helmets are a good accessory.":
            $ E1D2S3_mcwithhelmet = 1
            "The ladies will already know I'm a badass based on my bike alone, but a helmet covering my face adds a flavour of mystery, which chicks dig. They'll want to know: \"whose that sexy guy on that sexy bike?\" And when I take off my helmet and flash them my winning smile, the only thing I'll need to worry about is catching them as they swoon."
            scene black with fade
            play sound "audio/sfx/Technology/Helmet HUD Power On.ogg"
            "As the helmet slips over my head, my vision momentarily darkens. Then the HUD illuminates my visor with digital scrolling text and numbers, sharing more information and applications than I need."  
    
            "I remember reading about original helmets, which did nothing more than protect your head. I can't even imagine using such primitive technology. Now, even the most standard helmet includes a GPS, as well as speed monitors and music players."
    
        "Psh, helmets are for wimps.":
            "Yeah. Right. Like I'll be caught wearing one of those lame things."
    
    scene bg isokaze neighborhood day with fade
    #SFX: Bike starting up
    play sound "audio/sfx/Vehicles/Bike Ignition.ogg" fadeout 3
    "I turn the key in the ignition. The roar of the motor sends a shiver down my spine. {w}Perfect."
    play sound "audio/sfx/Vehicles/Bike Revving.ogg"
    "I rev the bike several times, enjoying the sound, before driving into the street."
    play sound "audio/sfx/Vehicles/Bike driving off.ogg" fadein 3
    $renpy.pause(1)
    play music "audio/music/Open Road (GAME VERSION).ogg" fadein 1
    #Road BG
    scene bg travel openroad day with fade
    stop ambient fadeout 5
    $renpy.pause(1)
    "This is the life. {w}Nothing beats the thrill of the open road."
    
    if (E1D2S3_mcwithhelmet == 0):
        play ambient "audio/ambience/Open Road No Helmet.ogg"
        $renpy.pause(1)
        $ persistent.gpix[1][0] = 1
        scene cg mc firstride nohelmet at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
        "... The number of bugs I choke on ruins the effect just a tad, but this is the life I chose. {w}No regrets!"
        $renpy.pause(1)
    
    elif (E1D2S3_mcwithhelmet == 1):
        play ambient "audio/ambience/Open Road Helmet.ogg" fadein 1
        $renpy.pause(1)
        $ persistent.gpix[2][0] = 1
        scene cg mc firstride helmet at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
        "I take full advantage of my helmet's capabilities. {w}With a glance, I can see how fast my vehicle is going and how fast the vehicles surrounding me are going. {w}There's even a feature that will alert me if I'm in danger of being hit."
    
        "The speakers are embedded on the inside of my helmet, right next to my ears, providing optimal acoustics for music. {w}Some might argue that is a safety issue, but I have the sense to keep the volume low."
        $renpy.pause(1)
    
    "Traffic is in my favour and I make good progress."
    
    scene bg campus intersection day with fade
    
    "The stoplight ahead of me is green. Perfect. Hopefully it stays that way long enough for me to pass."
    
    play sound "audio/sfx/Vehicles/Bike Accelerate.ogg"
    
    "Stay green. Stay green. Staygreenstaygreenstaygreenstay--"
    
    "No! Yellow."
    
    "I'm actually not {i}that{/i} far away. It'd be a close call, but I'm pretty sure I could still make it. I tighten my grip on the handles and then--"
    
    $ qtebase = 3
    $ qtetotal = qteath + qtebase
    $ t_var = qtetotal
    show screen timer_scr(place="E1D2S3_dontgunit")
    
    menu:
        "Hit the brakes. It was a stupid idea.":
            label E1D2S3_dontgunit:
                $ renpy.hide_screen ("timer_scr")
                "Actually, it's not as close as I thought. Not worth risking it."
                play sound "audio/sfx/Vehicles/Bike Screech.ogg"
                "I squeeze the brakes and coast to a gradual stop at the now red light."
                "Several ACE Academy students cross the street, chatting animatedly as they saunter past me. I drum my fingers, mildly impatient. Before long, the students have all crossed and the light reverts to green."
                jump E1D2S7
    
        "GUN IT!":
            $ renpy.hide_screen ("timer_scr")
            "I can make it!"
    
    play sound "audio/sfx/Vehicles/Bike Accelerate.ogg"
    "I slam on the gas, which roars with renewed strength."
    
    "I'm almost home free! Just a little bit more and--"
    
    $ E1D2S3_EncounteredKaori = 1
    voice "audio/voice/E1/D2/S3/Kaori/1.ogg"
    ki "{b}Kyaa~!{/b}"
    
    scene white with fade
    stop ambient fadeout 3
    stop music fadeout 3
    
    pf "{b}Whoa!{/b}"
    
    play sound "audio/sfx/Vehicles/Bike Screech.ogg"
    
    "I see a flash of red hair out of the corner of my eye. Swerving to the side, I narrowly avoid a student. That was a close one!"
    voice "audio/voice/E1/D2/S3/Kaori/2.ogg"
    ki "{i}Oof!{/i}"
    play sound "audio/sfx/Impacts/Kaori Falling Over.ogg"

    $ persistent.gpix[21][0] = 1 
    $ persistent.gpix[22][0] = 1
    $ persistent.gpix[23][0] = 1
    $ persistent.gpix[24][0] = 1
    scene cg kaori intersection fall1 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    play ambient "audio/ambience/Campus Road.ogg" fadein 1
    "She topples backwards onto the ground as her belongings scatter across a good portion of the crossing."
    scene cg kaori intersection fall2 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    "She blinks up at me in a daze."
    scene cg kaori intersection fall3 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    "But that is quickly replaced with the scariest looking face I've ever seen. {w}Uh-oh."
    
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 1
    
    menu:
        "This is my fault. I should help her.":
    
            if (E1D2S3_mcwithhelmet == 0):
                pf "Are you okay? Here, take my hand."
    
            elif (E1D2S3_mcwithhelmet == 1):
                $ E1D2S3_mctakeshelmetoff = 1
                pf "Are you okay--"
    
                "The heat of her glare could melt my helmet. {w}Oh, right. The helmet. I probably sound like a muffled alien with this thing on."
    
                "Let's try that again."
    
                "I take off my helmet."
    
                pf "Are you okay? Here, let me help."
    
            jump E1D2S6
    
        "Watch it!":
            "This crazy {i}pedestrian{/i} just jumped out of nowhere in front of my bike! Does she have a death wish?" 
    
            if (E1D2S3_mcwithhelmet == 1):
                $ E1D2S3_mctakeshelmetoff = 1
                "I pull off my helmet." 
    
            pf "Didn't anyone tell you to look both ways before crossing the street?"
            
            scene cg kaori intersection fall4 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    
            "She stares up at me in shock. No wait--{w}that's anger. Yup. Definitely anger."
            voice "audio/voice/E1/D2/S3/Kaori/3.ogg"
            ki "Are you kidding me?! The light was red, you idiot!"
    
            menu:
                "My bad. Are you ok?":
                        "Okay, I guess it's maybe possible that light might have already turned red before I'd gotten to the intersection. I might have been a little harsh just now."
    
                        pf "Sorry, my bad. Here, are you alright?"
                        jump E1D2S6
                                
                "I think someone is a little colourblind.":
                    "I roll my eyes. Some people think that the world revolves around them and that they can do no wrong."
    
                    pf "Are you colour blind? The light was green."
                    
                    scene cg kaori intersection fall3 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    
                    "She stares incredulously at me."
    
                    "I'm not about to apologise for something that clearly wasn't my fault!"
                    
                    scene cg kaori intersection fall4 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
                    voice "audio/voice/E1/D2/S3/Kaori/4.ogg"
                    ki "Are you..."
                    
                    scene bg campus intersection day with fade
    
                    "She pauses as she hoists herself off the ground. After dusting her skirt, she stomps towards me and glares."
                    
                    show kaori ang b1 at cc with dissolve
                    show vein:
                        xoffset 720
                        yoffset 110
                        xzoom .75
                        yzoom .75
                    voice "audio/voice/E1/D2/S3/Kaori/5.ogg"
                    ki "Are you really this stupid?! The light was red. RED. R-E-D. Do you know what that means? It means you STOP! How do you even have a license?!"
    
                    "She seems certain that the light was red. Is it possible that she's right? {w}… {w}Haha! Me, wrong? Sometimes I crack myself up."
    
                    #honk honk
                    play sound "audio/sfx/Vehicles/A couple of honks.ogg"
                    "I'm about to crush her with a witty retort when a car horn interrupts me."
                    "Oh, right. I'm still on the road … and there is a scary number of cars behind me.  {w}And the lights have turned green again--see, I know what green looks like!" 
                    pf "Look, I'd {i}love{/i} to stay and talk, but--"
    
                    #honk honk honk
                    play sound "audio/sfx/Vehicles/More harsher honks.ogg"
    
                    "An angry orchestra of honks interrupt me again."
    
                    pf "Okay, okay! I'm going!"
    
                    if (E1D2S3_mcwithhelmet == 0):
                        "I offer the girl a look of sympathy, and quickly drive off."
    
                    if (E1D2S3_mcwithhelmet == 1):
                        "I offer the girl a look of sympathy, before putting my helmet on and driving off."
                
                    show kaori ann at cc
                    "Even though this was all her fault, I can't help but feel a little sorry for her. With the number of cars on the road, she's going to have a hell of a time picking up all of her things."
                    
                    $ E1D2S3_MetKaoriWasRudeNoHelmet = 1
    
                    "Oh well. What are the odds of us meeting again anyway?"
                    stop music fadeout 3
                    scene black with fade
                    jump E1D2S7
                        
                        
                "Seeya.":
                    $ E1D2S3_MetKaoriWasRudeNoHelmet = 1
                    jump E1D2S3_seeya
    
        "Nope. I'm out of here.":
            label E1D2S3_seeya:
                $ E1D2S3_MetKaoriWasRudeNoHelmet = 1
                "Yeah, no. It's probably best I get the hell out of here before things turn as sour as her face."
                scene cg kaori intersection fall4 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0)
                play sound "audio/sfx/Vehicles/Bike driving off.ogg"
                "As soon as the light turns green, I speed out of there, making sure to give her a wide berth." 
                "I doubt I'll run into her again anyway."
                if (E1D2S3_mcwithhelmet == 1) and (E1D2S3_mctakeshelmetoff == 0):
                    $ E1D2S3_MetKaoriWasRudeNoHelmet = 0
                    $ E1D2S3_MetKaoriWasRudeYesHelmet = 1
                    "Not that it would matter, considering she couldn't see my face. Thank god for helmets."
                stop music fadeout 3
                scene black with fade
                jump E1D2S7
    
    
    scene black with fade
    jump E1D2S4
