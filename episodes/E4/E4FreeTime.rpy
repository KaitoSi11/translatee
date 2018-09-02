# E4 free time choices
label E4FreeTime:
    
    menu:
        "Kaori" if freeTime == "evening" and E4KIS1_Completed == 0:
            $ timeSpent = "kaori"
            $ kaoriSocialLink += 1
            jump E4KIS1
        "Kaori" if freeTime == "evening" and E4KIS1_Completed == 1 and E4KIS2_Completed == 0:
            $ timeSpent = "kaori"
            $ kaoriSocialLink += 1
            jump E4KIS2
            
        "Mayu" if freeTime == "afternoon" and E4MAS1_Completed == 0:
            $ timeSpent = "mayu"
            $ mayuSocialLink += 1
            jump E4MAS1
        "Mayu" if freeTime == "evening" and E4MAS1_Completed == 1  and E4MAS2_Completed == 0 and timeSpent != "mayu":
            $ timeSpent = "mayu"
            $ mayuSocialLink += 1
            jump E4MAS2
            
        "Shou" if freeTime == "afternoon" and E4SSS1_Completed == 0 and E4SSS1_NOTDAY1 == 1:
            $ timeSpent = "shou"
            $ shouSocialLink += 1
            jump E4SSS1
        "Shou" if freeTime == "afternoon" and E4SSS1_Completed == 1 and E4SSS2_Completed == 0:
            $ timeSpent = "shou"
            $ shouSocialLink += 1
            jump E4SSS2
            
        "Valerie" if freeTime == "evening" and E4VBS1_Completed == 0:
            $ timeSpent = "valerie"
            $ valerieSocialLink += 1
            jump E4VBS1
        "Valerie" if freeTime == "afternoon" and E4VBS1_Completed == 1 and E4VBS2_Completed == 0 and valrelatonship == 0:
            $ timeSpent = "valerie"
            $ mayuSocialLink += 1
            jump E4VBS2 ### Platonic Route
        "Valerie" if freeTime == "afternoon" and E4VBS1_Completed == 1 and E4VBS3_Completed == 0 and valrelatonship == 1:
            $ timeSpent = "valerie"
            $ mayuSocialLink += 1
            jump E4VBS3 ### Relationship Route
            
        "Yuuna" if freeTime == "afternoon" and E4YMS1_Completed == 0:
            $ timeSpent = "yuuna"
            $ yuunaSocialLink += 1
            jump E4YMS1
        "Yuuna" if freeTime == "evening" and E4YMS1_Completed == 1 and E4YMS2_Completed == 0 and timeSpent != "yuuna":
            $ timeSpent = "yuuna"
            $ yuunaSocialLink += 1
            jump E4YMS2
            
