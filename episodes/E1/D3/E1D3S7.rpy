label E1D3S7:
    
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 1 fadeout 1
    "I make my way to the reference shelves and start reviewing titles."
    "What should I read?"
    
    menu: 
        "Something about cores.":
            "I grab {i}Understanding GEAR Cores{/i} and take it to one of the desks." 
            "{i}GEARs are powered by a stored energy in the form of a \"core\", which manages all of the arsenal and mechanics of the robot. This includes: thruster output, shields, weapons, and other functions of the GEAR.{/i}"
            "{i}Cores vary from engineer to engineer but are generally created following a procedure approved by in-use experience. They continue to change and develop as the industry grows.{/i}" 
            "{i}Each Core has limited stored energy. Because of this, pilots are trained to be efficient. They learn to exercise restraint in order to avoid being left stranded in the middle of a battlefield due to energy depletion.{/i}" 
            "{i}The core also self-regulates to ensure it doesn't overheat. Careful management of energy core is a key skill that pilots learn early in their careers.{/i}"
    
        "History. Time to nerd out!":
            "I grab {i}History of GEAR{/i} and take it to one of the desks." 
            "{i}GEARs were initially developed for military use, but overtime their function has evolved beyond the battlefield and into commercial use. It is now common to see GEAR used in construction, mining, ports, and other labor intensive industries.{/i}" 
            "{i}The popularity of GEARs have expanded into recreational use by those of the public who can afford the purchase and maintenance of GEARs. This popularity has spawned new forms of entertainment. The most popular form being \"War Games\", which is played in stadiums and designated recreational facilities. In these \"War Games\", small squads of GEARs will compete and battle rival squads using non-lethal armaments.{/i}"
            "{i}The prevalent use and popularity of GEARs has also created a new area of study called \"Cenorobotics\".{/i}"
            "... That was all stuff I already knew…"
    
        "Military, because I'm a badass.":
            "I can't decide between {i}Military GEAR{/i} and {i}The Evolution of GEAR Weaponry{/i}."
    
            menu: 
                "Let's learn about weapons.": 
                    "I grab {i}The Evolution of GEAR Weaponry{/i} and take it to one of the desks." 
                    "{i}Civilian weapons have limiters to regulate the weaponry output and ensure the damages caused are non-lethal.{/i}"
                    "{i}All weaponry and defense systems of a GEAR are powered by the core. A more efficient core can produce a more powerful shield and a deadlier shot.{/i}" 
                    "{i}The superior mobility and intense firepower built into these mechanized suits have made them the ideal system for modern day use, replacing all previous conventional armored vehicles.{/i}" 
                    "{i}Pilots learn to manage their weapons by making the appropriate use of their energy core. The trick is for pilots to maximize energy for weapon and shield usage while maintaining their overheating status.{/i}" 
                    "Cool. Sounds like it's all about skill and core management." 
    
                "I'd rather get a general background.":
                    "I grab {i}Military GEAR{/i} and take it to one of the desks." 
                    "{i}Military GEAR are mechanized suits with superior mobility and firepower. They have replaced all conventional armored ground vehicles.{/i}"
                    "{i}A GEAR is controlled by its core, which manages all of the arsenal and mechanics of the robot. This includes: the thruster output, shields, weapons, and other functions of the GEAR, so core upkeep is essential when using Military GEAR.{/i}"
                    "{i}Due to the prevalence of GEAR in society and the risk they pose to the public, police departments now have dedicated custom GEAR to apprehend misused or rogue civilian GEAR models.{/i}"
                    "It's a good thing not everyone can access military GEAR." 
    
        "Power Study!":
            "I grab the closest book to me and sit at a table. Flipping it open, I start reading…" 
    
            
    #fade to black
    stop music fadeout 3
    scene black with fade
    $renpy.pause(2.5)
    "By the time I'm done studying, it's time for me to head home." 
    stop ambient fadeout 3
    
    jump E1D3S8