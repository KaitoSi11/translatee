# E3 free time choices
label E3FreeTime:
    
    menu:
        "Kaori" if freeTime == "afternoon" and day == 1:
            $ timeSpent = "kaori"
            $ kaoriSocialLink += 1
            jump E3KIS1
        "Kaori" if freeTime == "evening" and day == 3:
            $ timeSpent = "kaori"
            $ kaoriSocialLink += 1
            jump E3KIS2
            
        "Mayu" if freeTime == "afternoon" and E3MAS1_Completed == 0:
            $ timeSpent = "mayu"
            $ mayuSocialLink += 1
            jump E3MAS1
        "Mayu" if freeTime == "afternoon" and E3MAS1_Completed == 1  and E3MAS2_Completed == 0 and timeSpent != "mayu":
            $ timeSpent = "mayu"
            $ mayuSocialLink += 1
            jump E3MAS2
            
        "Shou" if freeTime == "evening" and E3SSS1_Completed == 0:
            $ timeSpent = "shou"
            $ shouSocialLink += 1
            jump E3SSS1
        "Shou" if freeTime == "afternoon" and E3SSS1_Completed == 1 and E3SSS2_Completed == 0 and timeSpent != "shou":
            $ timeSpent = "shou"
            $ shouSocialLink += 1
            jump E3SSS2
            
        "Valerie" if freeTime == "evening" and E3VBS1_Completed == 0:
            $ timeSpent = "valerie"
            $ valerieSocialLink += 1
            jump E3VBS1
        "Valerie" if freeTime == "evening" and E3VBS1_Completed == 1 and E3VBS2_Completed == 0:
            $ timeSpent = "valerie"
            $ mayuSocialLink += 1
            jump E3VBS2
            
        "Yuuna" if freeTime == "afternoon" and E3YMS1_Completed == 0:
            $ timeSpent = "yuuna"
            $ yuunaSocialLink += 1
            jump E3YMS1
        "Yuuna" if freeTime == "evening" and E3YMS1_Completed == 1 and E3YMS2_Completed == 0 and timeSpent != "yuuna":
            $ timeSpent = "yuuna"
            $ yuunaSocialLink += 1
            jump E3YMS2
            
