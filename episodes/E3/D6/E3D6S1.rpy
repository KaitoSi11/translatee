#
label E3D6S1:

$ kaoHairF = "default"
$ kaoHairB = kaoHairF
$ kaoOut = "sUniform"

$ mayHairF = "default"
$ mayHairB = mayHairF
$ mayOut = "sUniform"

$ nikHairF = "default"
$ nikHairB = nikHairF
$ nikOut = "sUniform"

$ shoHairF = "default"
$ shoHairB = shoHairF
$ shoOut = "sUniform"

$ valHairF = "default"
$ valHairB = valHairF
$ valOut = "sUniform"

$ yuuHairF = "default"
$ yuuHairB = yuuHairF
$ yuuOut = "sUniform"

$ meiHairB = "default"
$ meiOut = "sUniform"
$ meiHairF = "default"

$ day = 6
$ timeSpent = "none"
$renpy.pause(2.5)
play ambient "audio/ambience/Morning.ogg" fadein 1
$renpy.pause(2.5)
scene bg homekaito myroom day with fade
play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3

"I wake up naturally for once and enjoy my chance to sleep in. Is this what it feels like to be rested? Why doesn't this happen everyday?"
"With a wide yawn, I pull my arms over my head to stretch, then throw back my comforter and hop out of bed."

play sound "audio/sfx/Technology/ID Tap Success.ogg"
$renpy.pause(0.5)
"My tablet flashes with a notification. {w}I have an email. Curious, I open up the email and read it."

"..."

"It's from Dasshu. They're hosting a promotional photoshoot and networking event tomorrow right before Ex Zee's big concert. All sponsored Dasshu teams and individuals will be there, and after the shoot we are welcome to stay for for the concert."
"Wait--Dasshu sponsors Ex Zee?!"
"I guess I shouldn't be surprised. Dasshu might be breaking into the world of mecha, but they're a huge name in the sports and entertainment industry. {w}Still, Ex Zee is a supremely popular pop star. His shows get sold out within minutes!"

"There's no way I'm passing up such an opportunity!"
"I quickly type out a response confirming my attendance. I'm positive everyone else on the team will go as well, if only for the chance to meet Ex Zee."

if (E3KIS2_Completed == 1):
    "Grabbing my clothes for the day, I get changed."
    play sound "audio/sfx/Technology/Phone Vibration Once.ogg"
    play sound2 "audio/sfx/Technology/Phone Alarm.ogg"
    $renpy.pause(1)
    stop sound
    stop sound2
    "As soon as I grab my phone, it rings but cuts out immediately after the first ring."
    "?!"
    "That's weird."
    "I glance at my \"missed calls\". {w}It was Kaori… I bet she's going to ask me about Dasshu's event."
    "I call her back but she doesn't pick up. {w}Hm..."
    "I shoot her a text: {i}What's up?{/i}. Then I go downstairs into the kitchen."
    
    stop ambient fadeout 2.0
    scene black with fade
    scene bg homekaito main day with fade
    
    "Nobody's home again? It's like I live alone."
    "Opening the fridge, I spot a covered plate left for me. I unwrap the foil to find oyakodon.{w} Not a traditional breakfast, but delicious nonetheless! Nikki must have been practicing her recipes."
    "As I dig in, I glance at my phone. {w}Still no response from Kaori."
    "I'm starting to get a little concerned. She wouldn't call if she didn't have a good reason… So why isn't she responding?"

    if (MCStory == 3):
        "This isn't like her at all. I think something is bothering her."

    if (kaofriend > 0):
        "My heart drops as my mind wanders to the worst possible scenarios."
        "She must be hurt and tried to call for help. Is she unconscious? There's no other reason she'd be acting this way."
        "As the theories race in my mind, I take a deep breath to clear my head."
        "I'm overreacting. It's probably nothing."
        "...But what if it's something…"

    else:
        "I bet her phone battery died or something equally stupid."

    "Still, she'd most likely be at her dorm right now, and campus is not far away. I could double check to make sure everything's okay."

    menu:
        "Make sure Kaori is okay.":
            $ E3D6S1_ChoseKaori = 1
            "I need to do a few things on campus so I'll just stop by while I'm there. No big deal, right?"
            jump E3KIS3

        "She can call me back." if E3D4KI_Embraced == 0:
            "I'm sure she just got busy. She knows how to reach me if she needs me."
            jump E3D6S1_CONVERGE

else:
    "Grabbing my clothes for the day, I get changed, then go downstairs into the kitchen."
    
    stop ambient fadeout 2.0
    scene black with fade
    scene bg homekaito main day with fade
    
    "Nobody's home again? It's like I live alone."
    "Opening the fridge, I spot a covered plate left for me. I unwrap the foil to find oyakodon.{w} Not a traditional breakfast, but delicious nonetheless! Nikki must have been practicing her recipes."
    "I dig in with gusto."
    jump E3D6S1_CONVERGE

    label E3D6S1_CONVERGE:
    "After eating, I notice a note from Nikki."
    "{i}By the time you read this Uncle Kaito and I will be at his cafe slaving away. Just kidding, he won't be slaving but hopefully I will. Volunteer work experience ftw!!{/i}"
    "{i}PS. I spat in your food.{/i}"
    "{i}Just kidding! No I didn't.{/i}"
    "{i}Or did I?{/i}"
    "{i}Maybe if you were awake you'd know!{/i}"

    "..."

    "Wow, she actually wrote that. Sometimes, I wonder about her. {w}At least she's looking to gain some experience in the food and beverage industry. Working at the cafe will give her a lot of insight into what goes into running a restaurant."
    "I guess that means I should decide what I want to do today."

    menu:
        "I wonder what Yuuna is up to today." if E3YMS2_Completed == 1:
            $ E3D6S1_ChoseYuuna = 1
            jump E3YMS3
        
        "I have commitments to hang out with Shou and his brother." if E3SSS2_Completed == 1:
            $ E3D6S1_ChoseShou = 1
            jump E3SSS3
        
        "Let's see what Valerie has planned!" if E3VBS2_Completed == 1:
            $ E3D6S1_ChoseValerie = 1
            jump E3VBS3
        
        "Is Mayu free to hang out?" if E3MAS2_Completed == 1:
            $ E3D6S1_ChoseMayu = 1
            jump E3MAS3
        
        "Just sleep in and skip my day.": #if E3KIS2_Completed == 0 and E3MAS2_Completed == 0 and E3VBS2_Completed == 0 and E3SSS2_Completed == 0 and E3YMS2_Completed == 0:
            label E3D6S1_Loner:
                "I want to do nothing productive with my time and just sleep in!"
                "But first, I must gorge myself on some delicious take-out food."
                scene black with fade
                "I call a nearby restaurant and place an order obscenely large for a single person to eat.{w} Pickup will be ready in 15 minutes!"
                stop music fadeout 3
                $renpy.pause(1.5)
                $ E3D6S1_ChoseAlone = 1
                jump E3D6S2_ChoseAlone