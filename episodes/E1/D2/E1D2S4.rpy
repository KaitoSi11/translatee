label E1D2S4:
    
    
    menu:
        "Head to the hangar.":
            "My GEAR should have arrived by now. If I leave now, I should have enough time to handle registration." 
    
            pf "Where's the hangar again…?"
    
            "Checking my map,  it seems the hangar is on the other side of the school. I squint towards a cluster of buildings I think to be in right direction. Even at my fastest sprint, I don't think I'd be able to make it to and from the hangar without missing the first few minutes of class, especially since the registration process will probably take a while." 
    
            "I wonder if there's a shortcut…"
    
            "I consult my map again, which doesn't provide much help. It only illuminates the major routes around campus. If there are smaller paths I'll have to find them myself."
            show mayu thi at cc with dissolve
            "As if on cue, a petite girl wearing teal stripes walks by me. {w}A pilot! {w}She'd definitely know the closest route to the hangar."
    
            label E1D2S4_mayuloopback:
                menu:
                    "Call out." if (E1D2S4_mayushouldertap == 0):
                        $ E1D2S4_mayushouldertap = 1
                        pf "Hey!"
                        "I seem to catch the attention of everyone {i}but{/i} the girl. That's an achievement in itself, I guess. She walks on, unfazed."
                        jump E1D2S4_mayuloopback
                        
    
    
                    "Tap her shoulder":
                        if  (E1D2S4_mayushouldertap == 1):
                            "This is getting me nowhere. {w}Breaking into a jog, I quickly catch up with her."
    
                        else:
                            "I break into a jog to catch up with her."
    
                        play sound "audio/sfx/Human/Poke Noise.ogg"
                        "When I'm close enough, I gently tap her shoulder."
                        show mayu sur at cc
                        "She jumps."
                        show exclamation:
                            xoffset 720
                            yoffset 135
                            xzoom .75
                            yzoom .75
                        show mayu sur b1 at cc with dissolve
                        voice "audio/voice/E1/D2/S4/Mayu/1.ogg"
                        ma "Ahh!"
    
                        menu:
                            "Eeeep!":
                                $ E1D2S4_eeep = 1
                                pf "Ah!"
                                show mayu cur b1 at cc
                                "I cover my head defensively. {w}When nothing happens, I peek out from behind my arm and see the girl staring curiously at me. She immediately drops her gaze to the ground when our eyes meet."
                                show mayu ner b1 at cc
                                show panic:
                                    xoffset 720
                                    yoffset 135
                                    xzoom .75
                                    yzoom .75
                                voice "audio/voice/E1/D2/S4/Mayu/2.ogg"
                                ma "S-Sorry... I didn't mean to surprise you..."
                                pf "Oh, no, you didn't surprise me. That was just--something I always… {w}Um, I surprised you though. Sorry."
                                show mayu smi b1 at cc
                                voice "audio/voice/E1/D2/S4/Mayu/3.ogg"
                                ma "It's okay."
                                show mayu ner b1 at cc with dissolve
                                "Her eyes move to meet mine for a second before she glances down again."
                                voice "audio/voice/E1/D2/S4/Mayu/4.ogg"
                                ma "Umm..."
                                pf "Oh! Yes, I had a question."
                                pf "You know the hangar? Sorry, that's a stupid question. Of course you do. You're wearing a pilot's uniform."
                                show mayu smi b1 at cc
                                "She smiles faintly."
                                pf "Are there any shortcuts to get to the hangar? As far as I can tell, the only way to get there is if I take this long route. I'm kind of a in rush and was hoping there was a faster way to get there."
    
                            "And the Oscar for overreacting goes to...":
                                $ E1D2S4_overreact = 1
                                pf "Whoa! Relax, woman."
                                show mayu ner b1 at cc
                                show panic:
                                    xoffset 720
                                    yoffset 135
                                    xzoom .75
                                    yzoom .75
                                voice "audio/voice/E1/D2/S4/Mayu/5.ogg"
                                ma "Sorry..."
                                "She shuffles her feet awkwardly and stares at the ground."
                                pf "Hey, don't worry about it. I'm no stranger to making a woman scream."
                                "I wink at her."
                                show mayu cur b1 at cc
                                "She glances up at me with bewildered eyes, and seems to have trouble understanding."
                                voice "audio/voice/E1/D2/S4/Mayu/6.ogg"
                                ma "Oh..."
                                show mayu ner b1 at cc
                                pf "Anyway, I'm just wondering if you could help me with directions to the hangar."
                                "She pauses."
                                show mayu smi b1 at cc
                                voice "audio/voice/E1/D2/S4/Mayu/7.ogg"
                                ma "Um, I can try."
                                pf "Thanks. Do you know what the fastest route is to the hangar?"
    
    
                            "Just ask if there is a shortcut to the hangar.":
                                $ E1D2S4_quickshortcut = 1
                                pf "How can I get to the hangar?"
                                show mayu cur b1 at cc
                                voice "audio/voice/E1/D2/S4/Mayu/8.ogg"
                                ma "The hangar?"
                                "She blinks at me a few times before her gaze flicks to my teal stripes."
                                show bulb:
                                    xoffset 720
                                    yoffset 135
                                    xzoom .75
                                    yzoom .75
                                show mayu smi b1 at cc
                                voice "audio/voice/E1/D2/S4/Mayu/9.ogg"
                                ma "Oh, you're a pilot too."
                                pf "Yeah. I'm new around here so was wondering if there's a shortcut." 
    
                        "I point out the route on my map, and she nods in understanding."
                        show mayu smi at cc
                        voice "audio/voice/E1/D2/S4/Mayu/10.ogg"
                        ma "O-Oh... you can actually cut through here..."
                        "She points to the Pilot's Lounge."
                        voice "audio/voice/E1/D2/S4/Mayu/11.ogg"
                        ma "There's a path from the lower floor that connects directly to the hangar." 
    
                        if (E1D2S4_eeep == 1):
                            pf "Ah, thanks! You've been a big help!"
                            show mayu cur at cc
                            "I beam at her. She blinks twice before looking back down."
                            show mayu ner b1 at cc
                            voice "audio/voice/E1/D2/S4/Mayu/12.ogg"
                            ma "Oh... It's nothing..."
                            voice "audio/voice/E1/D2/S4/Mayu/13.ogg"
                            ma "I-I have to get going or I'll be late."
                            pf "Right, sorry to keep you."
    
                        elif (E1D2S4_overreact == 1):
                            pf "Got it, thank you."
                            show mayu cur at cc
                            "She looks at me for a second before looking back down."
                            show mayu ner b1 at cc
                            voice "audio/voice/E1/D2/S4/Mayu/14.ogg"
                            ma "... I-I have to get going..."
                            pf "Alright. Thanks again, have a good day."
    
                        elif (E1D2S4_quickshortcut == 1):
                            pf "Thanks."
                            show mayu cur at cc
                            "She looks at me for a second before looking back down."
                            show mayu ner b1 at cc
                            voice "audio/voice/E1/D2/S4/Mayu/15.ogg"
                            ma "I have to get going..."
                            pf "Okay. Have a good one."
    
                        $ E1D2S4_MayuGaveDirections = 1
                        hide mayu with dissolve
                        "She bows slightly before heading off. {w}That was strangely formal. I study the path she showed me on the map."
                        pf "Pilot's Lounge? Got it."
                        stop ambient fadeout 3
                        scene bg campus lounge day with fade
                        play ambient "audio/ambience/Pilot Lounge.ogg" fadein 1
                        "Following the map, I find the building and gape at the sheer size of the lounge. Groups of students gather around the bar, sipping drinks and watching past competitions on the big-screen TVs. I wander around the room, checking out the recreational games, and the comfortable chairs."
                        show guard extra at cc with dissolve
                        "In the far corner of the room, I see a guard reading a portable holobook in front of a door. This must lead to the hangar."
                        play sound [ "audio/sfx/Technology/ID Tap.ogg", "audio/sfx/Technology/ID Tap Fail.ogg" ]
                        "As I approach, the guard motions for me to tap my student ID against the card reader. It beeps and turns red."
    
                        "He frowns. With a heavy sigh, he puts down the reader and holds out his hand."
                        voice "audio/voice/E1/D2/S4/Guard/1.ogg"
                        "Reception" "ID, please."
                        ##NEW SOUND NEEDED##play sound "audio/sfx/Technology/Passcode Entry.ogg"
                        "I hand it over, and he types into his computer, his fingers flying across the keys." 
                        voice "audio/voice/E1/D2/S4/Guard/2.ogg"
                        "Reception" "Ah, it says your GEAR is still being cleared."
                        "He looks expectantly at me."
                        pf "Oh… What does that mean? I can't get in?"
                        voice "audio/voice/E1/D2/S4/Guard/3.ogg"
                        "Reception" "It means you'll get an email when it's available and then you will able to register it. Once we get your registration, you'll have access to the hangar." 
                        pf "Alright, thanks."
                        "He grunts in acknowledgement and hands back my card."
                        hide guard extra
                        "Well, that was a bust, but at least I now know how to get here."
                        "As I head back towards the Pilot's Lounge, I check the time. Hm, about half an hour. I may as well head to class."
                        
                        scene black with fade
                        jump E1D2S8
    
        "I should take care of my parking permit.":
            $ E1D2S4_GoingToGetPassNoYuuna = 1
            "Studying the map on my phone, I steadily make my way towards the administrative building. Luckily this campus is pretty easy to navigate because these buildings all look the same."
            scene bg campus building day with fade
            stop ambient fadeout 3
            "Eventually, I pause before the administrative building. I confidently push open the doors and am greeted with a series of hallways. Of course, more navigating. How very bureaucratic of them."
            scene black with fade
            "After a few minutes of wrong turns and doubling back, I arrive at a door labeled \"Campus Administration\"."
            scene bg campus office day with fade
            play ambient "audio/ambience/Campus Office.ogg" fadein 1
            "What would have been a spacious office is instead crowded with irritated students. Only one person mans the desk and he does not look like someone who is particularly accommodating."
            
            jump E1D2S5
