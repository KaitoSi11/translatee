#
label E3D1S3:
    
    stop music fadeout 3
    stop ambient fadeout 3
    
    $renpy.pause(1)
    play ambient "audio/ambience/Night Crickets.ogg" fadein 3
    scene bg homekaito main night with fade
    
    "It's quiet in the house when I arrive home. I guess no one's here. It's no surprise that Uncle Kaito's still at work, but I would have expected Nikki to be home by now. {w}She's been spending more and more time at her cooking club. It must be going really well!"
    
    play sound "audio/sfx/Human/Going Upstairs (wood).ogg" fadein 1
    scene black with fade
    $renpy.pause(.75)
    scene bg homekaito myroom night with fade
    
    "I should take advantage of the quiet and study. {w}As I head upstairs, a blonde head peeks around the corner."
    
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 5
    show nikki cur at cc with dissolve
    voice "audio/voice/E3/D1/S3/nikki/Nikki_1_001.ogg"
    sf "Is that you, big bro?"
    "I pause at the top of the stairs."
    pf "Hey, I didn't know you were home."
    show nikki mis at cc
    "Nikki grins mischievously."
    voice "audio/voice/E3/D1/S3/nikki/Nikki_1_002.ogg"
    sf "Is it because for once I wasn't slaving away in the kitchen waiting for you to come back?"
    
    menu:
        "A little bit, but it's not a bad thing.":
            pf "Since you cook so often, I basically associate food with you now."
            show nikki ske at cc
            "Her eyebrow is raised in either confusion or thought."
            voice "audio/voice/E3/D1/S3/nikki/Nikki_1_003.ogg"
            sf "Hm, not sure if that's a compliment or not…"
            pf "Sorry, I meant I only associate {i}yummy{/i} food with you."
            show drop:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            "Nikki wears that same look for a moment longer, than shrugs."
            show nikki thi at cc
            voice "audio/voice/E3/D1/S3/nikki/Nikki_1_004.ogg"
            sf "Thanks, I think?"
    
        "A good woman should know her place.":
            pf "I mean, that's kind of where a woman belongs."
            show shocked:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            show nikki sur at cc
            "Nikki's eyes grow wide before she narrows them in a glare."
            show nikki ann at cc
            voice "audio/voice/E3/D1/S3/nikki/Nikki_1_005.ogg"
            sf "You're joking, right?"
    
            menu:
                "Yes.":
                    "I burst out laughing."
                    pf "Your face!... So shocked!"
                    show nikki dis at cc
                    "She pouts."
                    voice "audio/voice/E3/D1/S3/nikki/Nikki_1_006.ogg"
                    sf "Not funny!"
                    pf "It was a little funny."
                    show storm:
                        xoffset 720
                        yoffset 160
                        xzoom .75
                        yzoom .75
                    "She just gives me a look."
    
                "No.":
                    pf "Get back in the kitchen and make me a sandwich."
                    show nikki ang at cc
                    voice "audio/voice/E3/D1/S3/nikki/Nikki_1_007.ogg"
                    sf "Don't you dare be serious about that comment!"
                    "I've never seen Nikki's face so red before."
                    show vein:
                        xoffset 720
                        yoffset 160
                        xzoom .75
                        yzoom .75
                    voice "audio/voice/E3/D1/S3/nikki/Nikki_1_008.ogg"
                    sf "If I do go back in the kitchen and make a sandwich I will only make one for me!"
                    show nikki ann at cc
                    pf "What about Uncle--"
                    voice "audio/voice/E3/D1/S3/nikki/Nikki_1_009.ogg"
                    sf "Okay, yes, and Uncle Kaito. But not you!"
                    pf "Will you make me--"
                    voice "audio/voice/E3/D1/S3/nikki/Nikki_1_010.ogg"
                    sf "No!"
                    pf "You didn't let me finish--"
                    show nikki ang at cc
                    voice "audio/voice/E3/D1/S3/nikki/Nikki_1_010.ogg"
                    sf "No!"
                    show nikki ann at cc
                    "Nikki has her arms crossed and glares hard at me. {w}Uh oh, she's really upset… I don't want to survive on my cooking alone!"
                    pf "I'm sorry! It was a joke."
                    voice "audio/voice/E3/D1/S3/nikki/Nikki_1_011.ogg"
                    sf "It wasn't funny."
                    pf "I'm sorry. {w}Please cook for me again!"
                    show nikki dis at cc
                    voice "audio/voice/E3/D1/S3/nikki/Nikki_1_012.ogg"
                    sf "I think forcing you to eat your own cooking is fitting punishment."
                    pf "I might die of starvation."
                    show nikki thi at cc
                    "Nikki's trying to stay angry, but sighs instead."
                    show storm:
                        xoffset 720
                        yoffset 160
                        xzoom .75
                        yzoom .75
                    voice "audio/voice/E3/D1/S3/nikki/Nikki_1_013.ogg"
                    sf "Fine… But only because I still need you alive!"
                    "\"Needs\" me? That can't be good..."
                    if MCStory == 3:
                        "I bet she's about to ask me for a favour."
    
    
        "No, it was way too quiet.":
            pf "No, nothing like that. There's just no way the house can be this quiet if you're home."
            show nikki sur at cc
            voice "audio/voice/E3/D1/S3/nikki/Nikki_1_014.ogg"
            sf "Hey!"
            pf "What?"
            show nikki wor at cc
            voice "audio/voice/E3/D1/S3/nikki/Nikki_1_015.ogg"
            sf "I'm always quiet!"
            pf "Is this what you'd call quiet?"
            show nikki dis at cc
            voice "audio/voice/E3/D1/S3/nikki/Nikki_1_016.ogg"
            sf "It was quiet before you got home, which means {i}you're{/i} the one who brings the noise!"
            pf "Uh…"
            show nikki neu at cc
            "Nikki grins."
    
        "You're like the waifu I didn't ask for.":
            pf "Uh, I didn't realise you'd suddenly turned into my wife."
            show nikki cur at cc
            "Nikki stares at me."
            show nikki ske at cc
            voice "audio/voice/E3/D1/S3/nikki/Nikki_1_017.ogg"
            sf "Uhh d-did you just call me your wife?"
            pf "No! Your comment sounded like something a wife would say--"
            show drop:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E3/D1/S3/nikki/Nikki_1_019.ogg"
            sf "Um, don't make this weird, bro."
            pf "{i}You{/i} made it weird!"
            show nikki dis at cc
            "She just shakes her head."
            show storm:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E3/D1/S3/nikki/Nikki_1_020.ogg"
            sf "Stop, just stop."
            
    show nikki smi at cc
    voice "audio/voice/E3/D1/S3/nikki/Nikki_1_021.ogg"
    sf "Anyway, before you so rudely distracted me, I had a question for you."
    pf "What is it?"
    show nikki hap at cc
    voice "audio/voice/E3/D1/S3/nikki/Nikki_1_022.ogg"
    sf "Can you give me a ride to the beach tomorrow?"
    "I blink at her."
    pf "How did you know I was going to the beach?"
    show nikki neu at cc
    voice "audio/voice/E3/D1/S3/nikki/Nikki_1_023.ogg"
    sf "Because tomorrow is Umiko's festival."
    pf "How do you know about that?"
    show nikki ske at cc
    "Nikki stares at me as if I have two heads."
    voice "audio/voice/E3/D1/S3/nikki/Nikki_1_024.ogg"
    sf "Because I live in Isokaze…"
    show question:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E3/D1/S3/nikki/Nikki_1_025.ogg"
    sf "Did you know about this?"
    
    if E2VBS4_Completed == 1:
        pf "Of course. I learned all about Umiko's story."
        show nikki hap at cc
        voice "audio/voice/E3/D1/S3/nikki/Nikki_1_026.ogg"
        sf "She was so badass! My friends and I are going to stop by her temple to pay our respects."
        pf "I didn't know there was a temple dedicated to her."
        show nikki neu at cc
        voice "audio/voice/E3/D1/S3/nikki/Nikki_1_027.ogg"
        sf "It's by the coast so a little out of the way from the city."
        pf "That seems fitting."
        show shiny:
            xoffset 720
            yoffset 160
            xzoom .75
            yzoom .75
        show nikki hap at cc
        voice "audio/voice/E3/D1/S3/nikki/Nikki_1_028.ogg"
        sf "I'm really excited about it! What are you excited about?"
    
        menu:
            "The food.":
                pf "Festivals mean awesome noms, right?"
                show nikki thi at cc
                voice "audio/voice/E3/D1/S3/nikki/Nikki_1_029.ogg"
                sf "Well, most do, but I doubt that'll be the case in this one."
                pf "There won't be food?"
                show nikki ner at cc
                voice "audio/voice/E3/D1/S3/nikki/Nikki_1_030.ogg"
                sf "No, there won't."
                show nikki cur at cc
                voice "audio/voice/E3/D1/S3/nikki/Nikki_1_031.ogg"
                sf "Besides…"
                play sound "audio/sfx/Human/Poke Noise.ogg"
                "She pokes my stomach."
                show nikki mis at cc
                voice "audio/voice/E3/D1/S3/nikki/Nikki_1_032.ogg"
                sf "Are you sure you want to be stuffing your face when you've got this beach bod?"
                pf "H-Hey!"
                show note:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                show nikki smi at cc
                "I push her hand away but she just laughs."
    
            "The girls.":
                "I can already imagine the girls in their cute bikinis… as they bounce across the sand… and splash around in the water…"
                show nikki ske at cc
                "Nikki wrinkles her nose."
                voice "audio/voice/E3/D1/S3/nikki/Nikki_1_033.ogg"
                sf "Ugh, actually I don't want to know."
                pf "But I didn't say anything!"
                show drop:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                show nikki dis at cc
                voice "audio/voice/E3/D1/S3/nikki/Nikki_1_034.ogg"
                sf "That stupid grin on your face gave it away."
    
            "The waves.":
                pf "I can't wait to jump in the water and go swimming!"
                show nikki mis at cc
                "Nikki grins."
                voice "audio/voice/E3/D1/S3/nikki/Nikki_1_035.ogg"
                sf "I'm surprised that's what you'd choose considering your horrible defeat the last time we went swimming..."
                "I knew exactly what she was talking about. Nikki and I were arguing who was the faster swimmer so Mom and Dad had us race. Mom stood at the starting point while Dad was the finish line."
                pf "We were just kids."
                show nikki cur at cc
                voice "audio/voice/E3/D1/S3/nikki/Nikki_1_036.ogg"
                sf "So?"
                pf "So I let you win!"
                show nikki mis at cc
                "Nikki snickers."
                show note:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E3/D1/S3/nikki/Nikki_1_037.ogg"
                sf "Uh-huh, sure. Whatever helps you sleep at night."
    
    else:
        pf "Not exactly. Shou didn't specify why we were going when he invited me."
        show nikki dis at cc
        voice "audio/voice/E3/D1/S3/nikki/Nikki_1_038.ogg"
        sf "And you didn't bother to ask?"
        pf "Do I really need a reason to go to the beach?"
        show nikki thi at cc
        voice "audio/voice/E3/D1/S3/nikki/Nikki_1_039.ogg"
        sf "Fair point."
        show nikki neu at cc
        voice "audio/voice/E3/D1/S3/nikki/Nikki_1_040.ogg"
        sf "Well, if you want to know, tomorrow is a festival to honor Umiko, the protector of Isokaze."
        voice "audio/voice/E3/D1/S3/nikki/Nikki_1_041.ogg"
        sf "A long time ago the dragon king threatened to drown the island if Umiko didn't marry him, so when she agreed to live with him in his underwater castle, she stole his magical pearl and now uses it to control the waves."
        pf "Huh, that's pretty cool. How did you learn about this?"
        show nikki smi at cc
        voice "audio/voice/E3/D1/S3/nikki/Nikki_1_042.ogg"
        sf "You know I've always loved mythologies."
        pf "That's true."
        
    show nikki hap at cc
    voice "audio/voice/E3/D1/S3/nikki/Nikki_1_043.ogg"
    sf "Soooo, can you take me or not?"
    pf "Sure. I'll be leaving at 10:45."
    show nikki ner at cc
    "Her face falls."
    voice "audio/voice/E3/D1/S3/nikki/Nikki_1_044.ogg"
    sf "Oh."
    pf "Why \"oh\"?"
    show nikki sad at cc
    voice "audio/voice/E3/D1/S3/nikki/Nikki_1_046.ogg"
    sf "Well my friends aren't going to be there until later."
    pf "So hitch a ride with them."
    show nikki ner at cc
    voice "audio/voice/E3/D1/S3/nikki/Nikki_1_047.ogg"
    sf "Ehhh… I don't feel comfortable asking them."
    pf "Fine, then you can come with me."
    show crying:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    show nikki sad at cc
    voice "audio/voice/E3/D1/S3/nikki/Nikki_1_048.ogg"
    sf "But you're going so early…"
    pf "Then take the bus."
    show nikki smi at cc
    "She smiles sweetly."
    voice "audio/voice/E3/D1/S3/nikki/Nikki_1_049.ogg"
    sf "When I said \"early\" I actually meant \"that's perfect\"."
    pf "That's what I thought."
    
    show nikki neu at cc
    "Nikki cranes her neck to peek down the stairs behind me."
    voice "audio/voice/E3/D1/S3/nikki/Nikki_1_050.ogg"
    sf "You hungry yet?"
    pf "A bit, yeah."
    show nikki smi at cc
    voice "audio/voice/E3/D1/S3/nikki/Nikki_1_051.ogg"
    sf "Me too. Come on, let's go downstairs and see what we have."
    hide nikki with dissolve
    "She moves past me and flies down the stairs. I follow her slowly."
    
    #black screen
    stop music fadeout 5
    scene black with fade
    "Nikki and I whip up a quick dinner, then I spend the rest of the night looking up more information about the festival before going to bed. I flip around in bed, too excited to settle down, before finally drifting off to sleep."
    stop ambient fadeout 5
    $renpy.pause(1)
    
    jump E3D2S1

