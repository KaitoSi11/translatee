init python:

    something = "none"
    testWarning = 0
    
###################################################################### ~ Playthrough Variables (Characters)

    E1C1E1_C = 0
    E1C1_WON = 0

    E3C1E1_C = 0
    E3C1_WON = 0 
    
    
    TATBATTLECOUNTER = 0
    
    
    E1D4S3_FakeFightWin = 0
    E1D4S4_LOOPINGMENU1 = 0
    E1D4S4_LOOPINGMENU2 = 0
    E1D4S4_LOOPINGMENU3 = 0
 
    
    yuuromance = 100
    yuufriend = 100
    yuunaSocialLink = 0
    yuurelatonship = 0
    
    valromance = 100
    valfriend = 100
    valerieSocialLink = 0
    valrelatonship = 0
    
    kaoromance = 100
    kaofriend = 100
    kaoriSocialLink = 0
    comradeKaori = 1
    kaorelatonship = 0
    
    mayfriend = 100
    mayuSocialLink = 0
    comradeMayu = 1
    mayrelatonship = 0
    
    shofriend = 100
    shouSocialLink = 0
    comradeShou = 1
    
    highSocialLink = "None"
    
    #label SocialLink_Check_ARCHIVED:
        #if yuunaSocialLink >= kaoriSocialLink and yuunaSocialLink >= valerieSocialLink and yuunaSocialLink >= mayuSocialLink and yuunaSocialLink >= shouSocialLink:
            #highSocialLink = "Yuuna"
        
        #elif kaoriSocialLink >= yuunaSocialLink and kaoriSocialLink >= valerieSocialLink and kaoriSocialLink >= mayuSocialLink and kaoriSocialLink >= shouSocialLink:
            #highSocialLink = "Kaori"
        
        #elif valerieSocialLink >= yuunaSocialLink and valerieSocialLink >= kaoriSocialLink and valerieSocialLink >= mayuSocialLink and valerieSocialLink >= shouSocialLink:
            #highSocialLink = "Valerie"
        
        #elif mayuSocialLink >= yuunaSocialLink and mayuSocialLink >= valerieSocialLink and mayuSocialLink >= kaoriSocialLink and mayuSocialLink >= shouSocialLink:
            #highSocialLink = "Mayu"
        
        #elif shouSocialLink >= yuunaSocialLink and shouSocialLink >= valerieSocialLink and shouSocialLink >= mayuSocialLink and shouSocialLink >= kaoriSocialLink:
            #highSocialLink = "Shou"
        
        #return

###################################################################### ~ Episode 1

    MCStory = 0
    
    E1D1S1_nikkimad = 0
    
    E1D1S3_mcdoesntlikesushi = 0
    
    E1D2S1_timetogetup = 0
    E1D2S1_okaytimetogo = 0
    E1D2S1_almostup = 0
    
    E1D2S1_firstdaybus = 0
    E1D2S1_firstdaybike = 0
    
    E1D2S2_talkwithyuunayes = 0
    E1D2S2_yuunaloopback = 0
    E1D2S2_YuunaComesWithYouPass = 0
    
    E1D2S3_mcwithhelmet = 0
    E1D2S3_mctakeshelmetoff = 0
    
    E1D2S3_EncounteredKaori = 0
    
    E1D2S3_MetKaoriWasRudeNoHelmet = 0
    E1D2S3_MetKaoriWasRudeYesHelmet = 0
    E1D2S3_MetKaoriWasNice = 0
    
    E1D2S4_mayushouldertap = 0
    E1D2S4_eeep = 0
    E1D2S4_overreact = 0
    E1D2S4_quickshortcut = 0
    E1D2S4_MayuGaveDirections = 0
    E1D2S4_GoingToGetPassNoYuuna = 0
    
    E1D2S5_offer50directly = 0
    E1D2S5_gotbikepass = 0
    E1D2S5_bribedforpass = 0
    E1D2S5_flirtforpass = 0
    E1D2S5_GotYuunasNumber = 0
    
    E1D2S7_BullyFight = 0
    E1D2S7_BullyFightWin = 0
    E1D2S7_ParkedFar = 0
    E1D2S7_CleanMove = 0
    
    E1D2S9_AgreeJoinShouTeam = 0
    
    E1S2D10_AskedOtherTeams = 0
    E1D2S10_EnoughRejection = 0
    
    E1D2S11_ComingCleanAboutRunningOverKaori = 0
    E1D2S11_JoinedTheTeam = 0
    
    E1D3S1_BikeImpounded = 0
    E1D3S1_BikeDrove = 0
    E1D3S1_BusRide = 0
    
    E1D3S4_PlayedAnotherWithShou = 0
    E1D3S4_WentToThePilotsLounge = 0
    E1D3S6_WentLibraryStudied = 0
    E1D3S6_WentLibraryYuuna = 0
    
    E1D3S5_AkiraNoticedMe = 0
    
    E1D4S1_Pioneer = 0
    
    E1D4S3_Stare = 0
    
    E1D4S4_FollowMatchPlan = 0
    
    E1D4S6_FiftyShadesLoopback = 0
    E1D4S6_Ceonardo = 0 # new for ep4
    E1D4S6_CeonardoLoopback = 0
    
   
    E1D5S1_EventAlone = 0

    E1D5S1_EventYuuna = 0

    E1D5S1_EventKaori = 0

    E1D5S1_EventShou = 0

    E1D5S1_EventMayu = 0

    E1D5S2_SoloWon = 0
        
    E1D5S2_ArcadeMatchWon = 0    
    
    E1D5S3_YuunaLoopbackOption1 = 0
    E1D5S3_YuunaLoopbackOption2 = 0
    E1D5S3_YuunaLoopbackOption3 = 0
    E1D5S3_YuunaLoopbackOption4 = 0
    E1D5S3_YuunaLoopbackOption5 = 0
    E1D5S3_YuunaLoopbackCounter = 0
    
    E1D5S3_StayWithYuunaLoop = 0
    
    E1D5S3_HelpedYuuna = 0
    
    E1D5S6_MayuNoThanksLoop = 0
    
    E1D5S5_MechConversation = 0
    
###################################################################### ~ Episode 2

    freeTime = "afternoon"
    day = 1
    timeSpent = "none"
    E2FreeTime_CalledNikki = 0
    
    E2KIS1_Food = 0
    E2KIS1_Completed = 0
    E2KIS2_Response = "Relax"
    E2KIS2_Completed = 0
    E2KIS3_Ranger = "Justice"
    E2KIS3_Completed = 0
    E2KIS4_Sushi = "Whatever"
    E2KIS4_Completed = 0
    
    E2MAS1_Completed = 0
    E2MAS2_Completed = 0
    E2MAS3_Completed = 0
    E2MAS4_Completed = 0
    
    E2SSS1_Coop = 0
    E2SSS1_Completed = 0
    E2SSS2_Completed = 0
    E2SSS3_Cars = 0
    E2SSS3_Completed = 0
    E2SSS4_Completed = 0
    
    E2VBS1_Completed = 0
    E2VBS2_Refuse = 0
    E2VBS2_Completed = 0
    E2VBS3_Completed = 0
    E2VBS4_Abstinence = 0
    E2VBS4_Achievement = 0
    E2VBS4_Benevolence = 0
    E2VBS4_Fortitude = 0
    E2VBS4_Answers = 0
    E2VBS4_Completed = 0
    
    E2YMS1_Completed = 0
    E2YMS2_Completed = 0
    E2YMS3_Completed = 0
    E2YMS4_Completed = 0
    
    E2D4S3_RanAfter = 0
    E2D4S3_EngineerGet = 0
    
    E2D5S1_Nikki = 0
    E2D5S1_Praise = 0
    
    E2D5S2_Spirit = 0
    
    E2D5S3_Distraction = "MC"
    
    E2D5S4_Drink = "Water"
    E2D5S4_Gladiator = 0
    E2D5S4_Style = 0
    E2D5S4_Victory = 0
    
    E2D5KI_Completed = 0
    E2D5KI_KaoriHit = 0
    
    E2D5MA_MayuScene = 0
    E2D5MA_Completed = 0
    
    E2D5SS_Completed = 0
    
    E2D5VB_Completed = 0
    
    E2D6S1_ChoseAlone = 0
    E2D6S1_ChoseKaori = 0
    E2D6S1_ChoseMayu = 0
    E2D6S1_ChoseShou = 0
    E2D6S1_ChoseValerie = 0
    E2D6S1_ChoseYuuna = 0
    
    E2D6S2_How = 0
    E2D6S2_Thrones = 0
    
###################################################################### ~ Episode 3

    #label SocialLink_Check:
        #if E2YMS4_Completed == 1:
            #highSocialLink = "Yuuna"
        
        #elif E2KIS4_Completed == 1:
            #highSocialLink = "Kaori"
        
        #elif E2VBS4_Completed == 1:
            #highSocialLink = "Valerie"
        
        #elif E2MAS4_Completed == 1:
            #highSocialLink = "Mayu"
        
        #elif E2SSS4_Completed == 1:
            #highSocialLink = "Shou"
                
    E3KIS1_Completed = 0
    E3KIS1_maamcall = 0
    E3KIS2_Completed = 0
    E3KIS3_Completed = 0
    E3KIS3_LoopbackChoiceVariable = 0
    
    E3YMS1_Correct = 0
    E3YMS1_Completed = 0
    E3YMS2_Completed = 0
    E3YMS3_Completed = 0
    E3YMS3_Choice1 = 0
    
    E3MAS1_Completed = 0
    E3MAS2_Paid = 0
    E3MAS2_Completed = 0
    E3MAS3_Order = "None"
    E3MAS3_Genre = "None"
    E3MAS3_RomCom = 0
    E3MAS3_RomanticMock = 0
    E3MAS3_MockCompleted = 0
    E3MAS3_RealCompleted = 0
    
    E3VBS1_Completed = 0
    E3VBS2_Completed = 0
    E3VBS2_LoopBackStop = 0
    E3VBS3_Completed = 0
    E3VBS3_Nekogirl = 0
    E3VBS3_GetNailed = 0
    
    E3SSS1_Completed = 0
    E3SSS1_SUCCESSFULLYATHLETIC = 0
    E3SSS2_Completed = 0
    
    E3SSS3_FoodChoice = 0
    E3SSS3_Completed = 0
    
    E3D2S2_Balance = 0
    E3D2S5_Voyeur = 0
    
    E3D2S4_SwimFast = 0
    
    E3D3S1_Lie = 0
    
    E3D4S1_Brawl = 0
    
    E3D4S2_Duelist = 1
    E3D4S2_Takedown = 0
    E3D4S2_Interfered = 0
    E3D4S2_Waited = 0
    
    E3D4S3_Thoughts = "None"
    
    E3D4S4_ChaseKaori = 0
    E3D4S4_Loopback = 0
    E3D4S4_Consoled = 0
    
    E3D4KI_Embraced = 0
    
    E3D5S1_YuunaAsked = 0
    E3D5S4_Reaction = 0
    
    E3D6S1_ChoseYuuna = 0
    E3D6S1_ChoseShou = 0
    E3D6S1_ChoseValerie = 0
    E3D6S1_ChoseMayu = 0
    E3D6S1_ChoseAlone = 0
    E3D6S1_ChoseKaori = 0
    
    E3D6S2_FakeTears = 0
    
    E3D7S2_ValVolunteer = 0
    
###################################################################### ~ Episode 3.5

    #E3_5S?_ToldNikki = 0 << Needed for E4D1S4
    
    E3_5S4_Costume = "None"
    
    E3_5YM_Cleavage = 0
    E3_5YM_Retry = 0
    
###################################################################### ~ Episode 4

    E4D1S3_Target = "None"
    E4D1S3_Suggestion = "None"
    
    E4D2S2_Minds = 0
    
    E4D2S3_Innocent = 0
    
    E4D4S2_QTELossCount = 0
    E4D4S2_WonDuel = 0
    
    E4D5S1_Question1 = 0
    E4D5S1_Question2 = 0
    
    E4D5YM_Sleep = 0
    
    E4D6SS_Completed = 0
    
    E4D7S1_Bus = 0
    
    E4D7S2_CoreDestroyed = 0
    
    
    E4YMS2_Indoors = 0
    E4YMS2_Slobber = 0
    
    E4YMS3_hiking = 0
    E4YMS3_swimming = 0
    E4YMS3_scavenge = 0
    E4YMS3_love = 0
    E4YMS3_oral = 0
    E4YMS1_Completed = 0
    E4YMS2_Completed = 0
    
    E4KIS1_TalkedKaori = 0
    E4KIS1_nothing = 0
    E4KIS3_BoughtGift = 0
    E4KIS3_SleepTogether = 0
    E4KIS3_LoveYou = 0
    E4KIS3_Shareoffer = 0
    E4KIS1_Completed = 0
    E4KIS2_Completed = 0
    
    E4MAS1_Fanfiction = "None"
    E4MAS1_Completed = 0
    E4MAS2_Completed = 0
    E4MAS3_Completed = 0
    
    E4SFS1_Fun = 0
    
    E4SSS1_Completed = 0
    E4SSS1_NOTDAY1 = 0
    E4SSS2_Completed = 0
    
    E4VBS1_DanceMachine = 0
    E4VBS3_Kissie = 0
    E4VBS3_Nofancoaster = 0
    E4VBS4_LoopCounter = 0
    E4VBS4_choice1 = 0
    E4VBS4_choice2 = 0
    E4VBS4_choice3 = 0
    E4VBS4_Loving = 0
    E4VBS1_Completed = 0
    E4VBS2_Completed = 0
    E4VBS3_Completed = 0
    
###################################################################### ~ QTE Variables
    
    qteintel = 0
    qteath = 0
    qtetrack = 0
    qtebase = 0
    qtetotal = 0
    qtestrat = qteintel + qtebase
    qtereaction = qteath + qtetrack + qtebase
    t_var = qtetotal