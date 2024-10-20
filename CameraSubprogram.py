#Subprogram
def Switchcamera(thecurrentcam):
    global vice
    #switch the camera up to the next one.
    currentcam = thecurrentcam
    #check its not at camera 10
    if currentcam != 10:
        #add to it
        return thecurrentcam + 1
    else:
        return 0
