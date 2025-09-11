import pyautogui as PAG
import time


class EclipseAutomationLogics():
    def __init__(self):
        self.Hello = "Hello There :)"
        self.Message = "Sit Back, Relax, and Let Me Do This Repetitve Task For You :)"
        print(self.Hello)
        return None

    # Moves Mouse To And Double Clicks To Open The Entity Relations Widget Within The ERP System
    def EntityRelationsLogic(self, ShipToListSelectionXCord=590, ShipToListSelectionYCord=143):
        PAG.moveTo(ShipToListSelectionXCord, ShipToListSelectionYCord, duration=2)
        PAG.doubleClick()

    # Moves Mouse To And Single Left Clicks To Open The Entity Ship-To List SubMenu Inside Of The Entity Relations Widget
    def ShipToListSelectionLogic(self, StartPointXCord=260, StartPointYCord=155):
        PAG.moveTo(StartPointXCord, StartPointYCord, duration=1)
        PAG.click(button="left")


    # The Automation Logic To Update The Specificied Credit Check Boxes For The Customer Entity
    def CreditControlUpdateLogic(self, StartingEntityXCord = 243, StartingEntityYCord = 195,
                                 CreditControlsButXCord=345, CreditControlsButYCord=330,
                                 WhenCredit1ButXCord = 40, WhenCredit1ButYCord = 572,
                                 WhenCredit2ButXCord = 40 ,WhenCredit2ButYCord = 888,
                                 ExitButXCord = 940, ExitButYCord = 285,
                                 SaveChangesYesButXCord = 420, SaveChangesYesButYCord = 655, 
                                 CustomerExitButXCord = 860, CustomerExitButYCord = 258,
                                 YesButXCord = 370, YesButYCord = 610,
                                 ):
        
        PAG.moveTo(StartingEntityXCord, StartingEntityYCord, duration=1)
        PAG.doubleClick()

        PAG.moveTo(CreditControlsButXCord, CreditControlsButYCord, duration=2)
        PAG.click(button="left")

        PAG.moveTo(WhenCredit1ButXCord, WhenCredit1ButYCord, duration=1)
        PAG.click(button="left")

        PAG.moveTo(WhenCredit2ButXCord, WhenCredit2ButYCord, duration=1)
        PAG.click(button="left")

        PAG.moveTo(ExitButXCord, ExitButYCord, duration=1)
        PAG.click()

        PAG.moveTo(SaveChangesYesButXCord, SaveChangesYesButYCord, duration=1)
        PAG.click()

        PAG.moveTo(CustomerExitButXCord, CustomerExitButYCord, duration=1)
        PAG.click()

        PAG.moveTo(YesButXCord, YesButYCord, duration=1)
        PAG.click()


if __name__ == "__main__":
    # Launches a GUI for Mouse Info
    # PAG.mouseInfo()

    MainInstance = EclipseAutomationLogics()

    MainInstance.EntityRelationsLogic()
    time.sleep(5)

    # Change this int value based on the GUI`s vertical (y-axis) position on the computer
    StartingEntityYCord = 195

    # Update 38 Customer Records Per Program`s Execution
    x = 0
    while x <= 37
        MainInstance.ShipToListSelectionLogic()
        MainInstance.CreditControlUpdateLogic(StartingEntityYCord=StartingEntityYCord)
        StartingEntityYCord+=20
        x+=1
