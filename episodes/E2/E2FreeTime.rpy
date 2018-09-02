# E2 free time choices
label E2FreeTime:
    
    menu:
        "See if Nikki needs a ride home." if E2FreeTime_CalledNikki == 0 and day == 1 and freeTime == "evening":
            jump E2D1Nikki
            
        "Kaori" if freeTime == "afternoon" and kaoriSocialLink == 0:
            $ timeSpent = "kaori"
            $ kaoriSocialLink += 1
            jump E2KIS1
        "Kaori" if freeTime == "evening" and kaoriSocialLink == 1 and timeSpent != "kaori":
            $ timeSpent = "kaori"
            $ kaoriSocialLink += 1
            jump E2KIS2
        "Kaori" if freeTime == "afternoon" and kaoriSocialLink == 2:
            $ timeSpent = "kaori"
            $ kaoriSocialLink += 1
            jump E2KIS3
                
        "Mayu" if freeTime == "afternoon" and mayuSocialLink == 0:
            $ timeSpent = "mayu"
            $ mayuSocialLink += 1
            jump E2MAS1
        "Mayu" if freeTime == "afternoon" and mayuSocialLink == 1:
            $ timeSpent = "mayu"
            $ mayuSocialLink += 1
            jump E2MAS2
        "Mayu" if freeTime == "afternoon" and mayuSocialLink == 2:
            $ timeSpent = "mayu"
            $ mayuSocialLink += 1
            jump E2MAS3
                
        "Shou" if freeTime == "evening" and shouSocialLink == 0 and timeSpent != "shou":
            $ timeSpent = "shou"
            $ shouSocialLink += 1
            jump E2SSS1
        "Shou" if freeTime == "afternoon" and shouSocialLink == 1:
            $ timeSpent = "shou"
            $ shouSocialLink += 1
            jump E2SSS2
        "Shou" if freeTime == "evening" and shouSocialLink == 2 and timeSpent != "shou":
            $ timeSpent = "shou"
            $ shouSocialLink += 1
            jump E2SSS3
                
        "Valerie" if freeTime == "afternoon" and valerieSocialLink == 0:
            $ timeSpent = "valerie"
            $ valerieSocialLink += 1
            jump E2VBS1
        "Valerie" if freeTime == "evening" and valerieSocialLink == 1 and timeSpent != "valerie":
            $ timeSpent = "valerie"
            $ valerieSocialLink += 1
            jump E2VBS2
        "Valerie" if freeTime == "afternoon" and valerieSocialLink == 2:
            $ timeSpent = "valerie"
            $ valerieSocialLink += 1
            jump E2VBS3
                
        "Yuuna" if freeTime == "evening" and yuunaSocialLink == 0 and timeSpent != "yuuna" and day != 3:
            $ timeSpent = "yuuna"
            $ yuunaSocialLink += 1
            jump E2YMS1
        "Yuuna" if freeTime == "afternoon" and yuunaSocialLink == 1 and day != 3:
            $ timeSpent = "yuuna"
            $ yuunaSocialLink += 1
            jump E2YMS2
        "Yuuna" if freeTime == "afternoon" and yuunaSocialLink == 2 and day != 3:
            $ timeSpent = "yuuna"
            $ yuunaSocialLink += 1
            jump E2YMS3
    
    
#menu:
    #"Hang out alone":
        #(JUMP to Alone Choice)
    #"See what Kaori is up to":
        #(JUMP to Kaori Choice)
    #"See what Mayu is up to":
        #(JUMP to Mayu Choice)
    #"See what Nikki is up to":
        #(JUMP to Nikki Choice)
    #"See what Shou is up to":
        #(JUMP to Shou Choice)
    #"See what Valerie is up to":
        #(JUMP to Valerie Choice)
