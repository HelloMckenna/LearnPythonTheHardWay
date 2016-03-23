
CEA_SNSWC = "L"




def name_to_number(NUM_SNSWC):
    if (CEA_SNSWC == "H"):
        return 3
    elif (CEA_SNSWC == "M"):
        return 2
    elif (CEA_SNSWC == "L"):
        return 1
    elif (CEA_SNSWC == "VLN"):
        return 0
    else:
        return "<Null>"

name_to_number(NUM_SNSWC)



def Reclass (NUM_SNSWC):
	if (CEA_SNSWC == "H"):
		return 3
	elif CEA_SNSWC == "M":
		return 2
	elif (CEA_SNSWC == "L"):
		return 1
	elif (CEA_SNSWC == VLN):
		return 0
