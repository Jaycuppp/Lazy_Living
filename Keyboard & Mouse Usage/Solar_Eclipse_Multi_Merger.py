import pyautogui as PAG

class EclipseAutomationLogics():
    def __init__(self):
        self.Hello = "Hello There :)"
        self.Message = "Sit Back, Relax, and Let Me Do This Repetative Multi Product Merging Task For You :)"
        print(self.Hello)
    
    
    def MergePurgeProductSelectionLogic(self, EnterKey='', KeepProductXCord=0, KeepProductYCord=0, MergeProductXCord=0, MergeProductYCord=0):
        PAG.moveTo(KeepProductXCord, KeepProductYCord, duration=1.5)
        PAG.click(button="left")
        PAG.typewrite(EnterKey, 0.01, False, True)
        PAG.keyDown("enter", None, False)
        PAG.moveTo(40, 185, duration=1)
        PAG.keyDown("enter", None, False)
        PAG.typewrite(EnterKey, 0.01, False, True)
        PAG.keyDown("enter", None, False)
        PAG.moveTo(MergeProductXCord, MergeProductYCord, duration=1.5)
        PAG.click(button="left")

        # Auto Checks the Boxes To Do A Complete Product Merger
        for Iter in range (0, 5):
            PAG.keyDown("space", None, False)
            PAG.keyDown("enter", None, False)
            Iter += 1



class EclipseAutomations(EclipseAutomationLogics):
    def __init__(self):
        self.Hello = "Hello There :)"
        print(self.Hello)
        return None

    def MergePurgeMultiFullScreen(self):

        KeepProduct = {"1st": (75, 130),
                    "2nd": (75, 155),
                    "3rd": (75, 180),
                    "4th": (75, 205),
                    "5th": (75, 230),
                    "6th": (75, 255),
                    "7th": (75, 280)}
        
        MergeProduct = {"1st": (420, 200),
                    "2nd": (420, 240),
                    "3rd": (420, 280),
                    "4th": (420, 320),
                    "5th": (420, 360),
                    "6th": (420, 400),
                    "7th": (420, 440)}
        
        JunkEnterKey = '/junk'
        MouseClickDelay = 1.5 #Seconds

        # Moves Mouse To And Clicks On Top Of The Merge GUI Widget To Ensure The Mouse and Keyboard are In Scope Of The Merge GUI
        PAG.moveTo(700, 0, MouseClickDelay)
        PAG.click(button="left")

        self.MergePurgeProductSelectionLogic(JunkEnterKey, KeepProductXCord=KeepProduct["1st"][0], KeepProductYCord=KeepProduct["1st"][1], MergeProductXCord=MergeProduct["1st"][0], MergeProductYCord=MergeProduct["1st"][1])
        self.MergePurgeProductSelectionLogic(JunkEnterKey, KeepProductXCord=KeepProduct["2nd"][0], KeepProductYCord=KeepProduct["2nd"][1], MergeProductXCord=MergeProduct["2nd"][0], MergeProductYCord=MergeProduct["2nd"][1])
        self.MergePurgeProductSelectionLogic(JunkEnterKey, KeepProductXCord=KeepProduct["3rd"][0], KeepProductYCord=KeepProduct["3rd"][1], MergeProductXCord=MergeProduct["3rd"][0], MergeProductYCord=MergeProduct["3rd"][1])
        self.MergePurgeProductSelectionLogic(JunkEnterKey, KeepProductXCord=KeepProduct["4th"][0], KeepProductYCord=KeepProduct["4th"][1], MergeProductXCord=MergeProduct["4th"][0], MergeProductYCord=MergeProduct["4th"][1])
        self.MergePurgeProductSelectionLogic(JunkEnterKey, KeepProductXCord=KeepProduct["5th"][0], KeepProductYCord=KeepProduct["5th"][1], MergeProductXCord=MergeProduct["5th"][0], MergeProductYCord=MergeProduct["5th"][1])
        self.MergePurgeProductSelectionLogic(JunkEnterKey, KeepProductXCord=KeepProduct["6th"][0], KeepProductYCord=KeepProduct["6th"][1], MergeProductXCord=MergeProduct["6th"][0], MergeProductYCord=MergeProduct["6th"][1])
        self.MergePurgeProductSelectionLogic(JunkEnterKey, KeepProductXCord=KeepProduct["7th"][0], KeepProductYCord=KeepProduct["7th"][1], MergeProductXCord=MergeProduct["7th"][0], MergeProductYCord=MergeProduct["7th"][1])


        # Move Mouse To & Click On The Hold Function ShortCut
        PAG.moveTo(10, 57, MouseClickDelay)
        PAG.click(button="left")


        # Move Mouse To & Click On The Yes Button To Execute The Multi-Product Merge
        PAG.moveTo(925, 550, MouseClickDelay)
        PAG.click(button="left")

        return None

if __name__ == "__main__":
    # Launches a GUI for Mouse Info

    # PAG.mouseInfo()
    MainInstance = EclipseAutomations()

    MainInstance.MergePurgeMultiFullScreen()