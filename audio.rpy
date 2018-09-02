###################################################################### ~ Music

############################################################# Everyday (Upbeat)

#play music "audio/music/Bright New Day (GAME VERSION).ogg"
#play music "audio/music/Day Out (GAME VERSION).ogg"
#play music "audio/music/Hanging Out (GAME VERSION).ogg"
#play music "audio/music/Isnt This Nice (GAME VERSION).ogg"
#play music "audio/music/After a Long Day (GAME VERSION).ogg"
#play music "audio/music/Timeless.ogg"

############################################################# Everyday (Neutral / tension)

#play music "audio/music/Isokaze (GAME VERSION).ogg"
#play music "audio/music/Idle Conversation (GAME VERSION).ogg"
#play music "audio/music/Stress (GAME VERSION).ogg"
#play music "audio/music/Inventory (GAME VERSION).ogg"

############################################################# Romantic / Event

#play music "audio/music/Evening Out (GAME VERSION).ogg"
#play music "audio/music/Open Road (GAME VERSION).ogg"
#play music "audio/music/Tender Moments (GAME VERSION).ogg"
#play music "audio/music/Tender Moments [Piano Ver] (GAME VERSION).ogg"
#play music "audio/music/Yuuna Misaki (GAME VERSION).ogg"
#play music "audio/music/You and I (GAME VERSION).ogg"

############################################################# Action

#play music "audio/music/Fight Song 1 (GAME VERSION).ogg"
#play music "audio/music/Fight Song 2 (GAME VERSION).ogg"
#play music "audio/music/Raycrash (GAME VERSION).ogg"
#play music "audio/music/Raycrash.ogg"
#play music "audio/music/Rivals (GAME VERSION).ogg"
#play music "audio/music/Victory! (GAME VERSION).ogg"

############################################################# Bad News Bears

#play music "audio/music/Light Tension (GAME VERSION).ogg"
#play music "audio/music/A Bad Feeling (GAME VERSION).ogg"
#play music "audio/music/Next Time (GAME VERSION).ogg"

############################################################# Sad/Quieter

#play music "audio/music/Slow Day (GAME VERSION).ogg"
#play music "audio/music/Kaori Itami (GAME VERSION).ogg"

############################################################# Comedy

#play music "audio/music/Baka! (GAME VERSION).ogg"
#play music "audio/music/Sneaking About (GAME VERSION).ogg"

############################################################# Misc

#play music "audio/music/Bring It On! (Vocal).ogg"
#play music "audio/music/Bring It On! [INSTRUMENTAL].ogg"
#play music "audio/music/Let's Get It Done! (GAME VERSION).ogg"
#play music "audio/music/Mayu Akemi (GAME VERSION).ogg"







###################################################################### ~ Ambience

#play ambient "audio/ambience/Ace Academy Library.ogg"
#play ambient "audio/ambience/Arcade.ogg"
#play ambient "audio/ambience/Bullet Train.ogg"
#play ambient "audio/ambience/Bus Stop.ogg"
#play ambient "audio/ambience/Bus.ogg"
#play ambient "audio/ambience/Campus Office.ogg"
#play ambient "audio/ambience/Campus Road.ogg"
#play ambient "audio/ambience/Campus.ogg"
#play ambient "audio/ambience/Desert Maid Cafe.ogg"
#play ambient "audio/ambience/Electronics Store.ogg"
#play ambient "audio/ambience/GEAR Cockpit.ogg"
#play ambient "audio/ambience/Hangar.ogg"
#play ambient "audio/ambience/Kitchen Cooking.ogg"
#play ambient "audio/ambience/Mall.ogg"
#play ambient "audio/ambience/Morning.ogg"
#play ambient "audio/ambience/Night Crickets.ogg"
#play ambient "audio/ambience/Open Road Helmet.ogg"
#play ambient "audio/ambience/Open Road No Helmet.ogg"
#play ambient "audio/ambience/Parking Lot.ogg"
#play ambient "audio/ambience/Pilot Lounge.ogg"
#play ambient "audio/ambience/Train Station.ogg"
#play ambient "audio/ambience/Shoreline.ogg"
#play ambient "audio/ambience/Rooftop.ogg"
#play ambient "audio/ambience/beach day.ogg"
#play ambient "audio/ambience/beach evening.ogg"



###################################################################### ~ SFX


#Manually do as script requires


###################################################################### ~ VO


#Manually do as script requires


###################################################################### ~ Audio Channels

init python:
    renpy.music.register_channel("ambient", "ambient",  loop=True)
    renpy.music.register_channel("ambient2", "ambient",  loop=True)
init python:
    renpy.music.register_channel("sound2", "sfx",  loop=False)
    renpy.music.register_channel("sound3", "sfx",  loop=False)



#init:
$ bloSound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Block.ogg', 'audio/sfx/GEAR Combat/Block.ogg' ])
$ dodSound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Dodge.ogg', 'audio/sfx/GEAR Combat/Dodge.ogg' ])
$ fistSound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Power Fist Attack 1.ogg', 'audio/sfx/GEAR Combat/Power Fist Attack 2.ogg' ])
$ hitSound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Hit.ogg', 'audio/sfx/GEAR Combat/Hit.ogg' ])
$ rifSound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Rifle.ogg', 'audio/sfx/GEAR Combat/Rifle.ogg' ])
$ smgSound = renpy.random.choice([ 'audio/sfx/GEAR Combat/SMG.ogg', 'audio/sfx/GEAR Combat/SMG.ogg' ])
$ sniSound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Sniper.ogg', 'audio/sfx/GEAR Combat/Sniper.ogg' ])
$ sw1Sound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Sword Single.ogg', 'audio/sfx/GEAR Combat/Sword Single.ogg' ])
$ sw2Sound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Sword Double.ogg', 'audio/sfx/GEAR Combat/Sword Double.ogg' ])

$ retSound = bloSound
$ attSound = hitSound

$ meleeSound = hitSound
$ rangeSound = hitSound
