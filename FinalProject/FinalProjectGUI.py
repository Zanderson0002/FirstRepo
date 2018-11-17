from tkinter import *

class eCardGUI:
    def __init__(self):
        window = Tk()  # Create window
        window.title("E-Card Generator") # Window title

        # Set canvas
        self.canvas = Canvas(window, width = 592, height = 420)
        self.canvas.pack()

        # Images must be initialized in 'init' to be called in functions
        self.testPhoto = PhotoImage(file = 'Test.gif')

        # Buttons in frame
        frame = Frame(window)
        frame.pack()
        btChristmas = Button(frame, text = "Christmas", command = self.christmasCard)
        btThanksgiving = Button(frame, text = "Thanksgiving", command = self.thanksgivingCard)
        btHalloween = Button(frame, text = "Halloween", command = self.halloweenCard)
        btEaster = Button(frame, text = "Easter", command = self.easterCard)
        btNewYears = Button(frame, text = "New Years", command = self.newYearsCard)
        btStPatricksDay = Button(frame, text = "St Patrick's Day", command = self.stPatricksDay)
        btValentinesDay = Button(frame, text = "Valentine's Day", command = self.valentinesDay)
        btExport = Button(frame, text = "Export", command = self.export)

        # Button locations
        btNewYears.grid(row = 1, column = 1)
        btValentinesDay.grid(row = 1, column = 2)
        btEaster.grid(row = 1, column = 3)
        btStPatricksDay.grid(row = 1, column = 4)
        btHalloween.grid(row = 1, column = 5)
        btThanksgiving.grid(row = 1, column = 6)
        btChristmas.grid(row = 1, column = 7)
        btExport.grid(row = 2, column = 7)

        window.mainloop()

    def christmasCard(self):
        print("Christmas card button was pressed")
        self.canvas.delete("all") # Emptys canvas before calling PhotoImage
        # Calls photo and adds to canvas at 0,0 (top left) anchored at top left corner of PhotoImage
        self.canvas.create_image(0, 0, image = self.testPhoto, anchor = NW)

    def thanksgivingCard(self):
        print("Thanksgiving card button was pressed")
        self.canvas.delete("all")

    def halloweenCard(self):
        print("Halloween card button was pressed")
        self.canvas.delete("all")

    def easterCard(self):
        print("Easter card button was pressed")
        self.canvas.delete("all")

    def newYearsCard(self):
        print("New Years card button was pressed")
        self.canvas.delete("all")

    def stPatricksDay(self):
        print("St Patrick's Day card button was pressed")
        self.canvas.delete("all")

    def valentinesDay(self):
        print("Valentine Day card button was pressed")
        self.canvas.delete("all")

    def export(self):
        print("Export button was pressed")
        # No delete canvas so canvas can be captured for export to PDF or other file type

eCardGUI()
