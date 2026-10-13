import pyautogui as PAG

class Logics():
    def __init__(self):
        self.Hello = "Hello There :)"
        self.Message = "Sit Back, Relax, and Let Me Do This Repetitve Task For You :)"
        print(self.Hello)
        return None


    
    def NewZipCodeEntryLogic(self, LoopAmount, NewButtonX, NewButtonY, CellAx, CellAy, NewZipEntryX, NewZipEntryY,
                             CellCx, CellCy, NewStateEntryX, NewStateEntryY, JurrisX, JurrisY, CellBx,
                             CellBy, NewCityEntryX, NewCityEntryY, GeneralHeadX, GeneralHeady):

        # LoopAmount = Total Amount of Zip Codes That Need To Be Added To The Solar Eclipse System
        for iter in range (0, LoopAmount):

            # Opening up a New Zip Code Entry Menu
            PAG.moveTo(NewButtonX, NewButtonY, duration=1)
            PAG.click(button="left", clicks=2, interval=0.25)

            # Moving Mouse To ZIP CODES Excel File and Selecting the Zip Code Cell
            PAG.moveTo(CellAx, CellAy, duration=1)
            PAG.click(button="left", clicks=2, interval=0.5)
            PAG.press("f2", interval=0.25)
            PAG.hotkey("ctrl", "a", "c")

            # Move Mouse To NEW Zip Entry Menu, Pasting the ZipCode that has been copied, Clicking OK
            PAG.moveTo(NewZipEntryX, NewZipEntryY, duration=1)
            PAG.click(button="left", clicks=2, interval=0.5)
            PAG.hotkey("ctrl", "v")
            PAG.press("enter", presses=2, interval=0.5)

            # Entring UNITED STATES As the Country For The NEW Zip Code and Clicking OK
            PAG.typewrite("UNITED", 0.01, False, True)
            PAG.press("enter", presses=1, interval=0.5)
            PAG.press("down", presses=3, interval=0.5)
            PAG.press("enter", presses=2, interval=0.5)

            # Moving Mouse To ZIP CODES Excel File and Selecting the State Cell
            PAG.moveTo(CellCx, CellCy, duration=1)
            PAG.click(button="left", clicks=2, interval=0.5)
            PAG.hotkey("ctrl", "c")

            # Move Mouse To NEW Zip Entry Menu and Pasting the State Value that has been copied
            PAG.moveTo(NewStateEntryX, NewStateEntryY, duration=1)
            PAG.click(button="left", clicks=2, interval=0.5)
            PAG.hotkey("ctrl", "v")
            PAG.press("tab", interval=0.01)

            # Entering the Out Of State (OOS) Default Tax Juris Code and then Selecting Juris Overr Header
            PAG.typewrite("OOS", 0.01, False, True)
            PAG.moveTo(JurrisX, JurrisY, duration=0.5)
            PAG.click(button="left", clicks=1, interval=0.5)

            # Moving Mouse To ZIP CODES Excel File and Selecting the State Cell
            PAG.moveTo(CellBx, CellBy, duration=1)
            PAG.click(button="left", clicks=2, interval=0.5)
            PAG.press("f2", interval=0.25)
            PAG.hotkey("ctrl", "a", "c")

            # Move Mouse To NEW Zip Entry Menu and Pasting the City Value that has been copied
            PAG.moveTo(NewCityEntryX, NewCityEntryY, duration=1)
            PAG.click(button="left", clicks=1)
            PAG.hotkey("ctrl", "v")
            PAG.moveTo(601, 350, duration=0.25) 
            PAG.click(button="left", clicks=2, interval=0.01)
            PAG.moveTo(NewCityEntryX, NewCityEntryY, duration=0.25)
            PAG.click(button="left", clicks=2, interval=0.01)
            PAG.press("tab", presses=3, interval=0.1)

            #MAKING Sure Zip Code Maintenenace Widget Is On GENERAL Header
            PAG.moveTo(GeneralHeadX, GeneralHeady, duration=0.5)
            PAG.click(button="left", clicks=2, interval=0.25)

            # Click on the NEW Button again and lastly select the Yes optipn
            PAG.moveTo(NewButtonX, NewButtonY, duration=0.75)
            PAG.click(button="left", clicks=1, interval=0.5)
            PAG.press("enter")

            CellAy , CellBy , CellCy = CellAy + 15 , CellBy + 15 , CellCy + 15



class EclipseAutomations(Logics):
    def __init__(self):
        self.Hello = "Hello There :)"
        print(self.Hello)
        return None

    def AddingNewZipCodes(self, NewButtonX=0, NewButtonY=0):

        # Excel Horizontal Cells A-C Coordinates For Row 1
        XCellA , YCellA = 175, 275
        XCellB , YCellB = 275, 275
        XCellC , YCellC = 335, 275

        # For Each Row Down, Add 275 by 15 (YCellA/C += 15 for each iteration)

        # Permanent Eclipse Zip Code Maintenance Usage Coordinates
        GenHeadX , GenHeadY = 540 , 270
        NewButtX , NewButtY = 745 , 233 # XY Cords for the New Button
        NewZipX , NewZipY = 865 , 342 # XY Cords for the New Zip Code Entry
        # OKButtX , OKButtY = 768 , 382 # XY Cords for the OK Button After Enting USA As the Country Choice
        StateEntryX , StateEntryY = 728 , 325 # XY Cords for the NEW State Entry (Copy Paste From Excel)
        # TaxJurEntryX , TaxJurEntryY = 728 , 350 # XY Cords for the Tax Jurrisdition (OOS)
        JurisdOverrHeaderX , JurisdOverrHeaderY = 621 , 270 # XY Cords for the Jurrisdiciton Override Header Button
        JurisCityEntryX , JurisCityEntryY = 567 , 328 # XY Cords for the Jurrisdiciton Override City Entry (Copy Paste From Excel)
        # CurrZipCodeEntryX , CurrZipCodeEntryY = 650 , 233

        # Total Amount Of Zip Codes That Need To Be Added To The System
        Loop_Amount = 20

        self.NewZipCodeEntryLogic(Loop_Amount, NewButtX, NewButtY, XCellA, YCellA, NewZipX, NewZipY, XCellC, 
                                 YCellC, StateEntryX, StateEntryY, JurisdOverrHeaderX, JurisdOverrHeaderY, 
                                 XCellB, YCellB, JurisCityEntryX, JurisCityEntryY, GenHeadX, GenHeadY)
        return None

if __name__ == "__main__":""
    # Launches a GUI for Mouse Info

# PAG.mouseInfo()

# MAKE SURE THE GENERAL TAB IS OPENED BEFORE RUNNING THIS PROGRAM
MainInst = EclipseAutomations()
MainInst.AddingNewZipCodes()
