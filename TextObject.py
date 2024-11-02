class Text:

    COLOR_DICT = {
        "r": "red", "o": "orange", "y": "yellow", 
        "g": "green", "b": "blue", "p": "purple", 
        "n": "black", "s": "gray", "w": "white"}
    
    def __init__(self, value=None, x=960, y=540, font="ConsolaMono-Bold.ttf", size = 24, color = "white", start=0, end=1, duration=5, spacing = 30, length=25):
        self.value = [letter for letter in value]
        self.xPos, self.yPos = x, y
        self.font, self.size = font, size
        self.color = color
        self.spacing = size * 0.6
        self.length = float('inf') if length <= 0 else length
        self.start, self.animation_end, self.duration = start, end, duration
        self.statement = ""

    def debug_location(self):
        self.statement += f"drawbox=:x={self.xPos}:y={self.yPos}:w={5}:h=5:color=RED,"
    
    def change_color(self, code="w"):
        self.color = self.COLOR_DICT.get(code)

    def add_color(self, color="random", code="z"):
        self.COLOR_DICT[code] = color
        self.change_color(code=code)

    def raised_character(self, letter="2", x_offset=0, y_offset=0, time_offset=0):
        self.statement += f"drawtext=text='{letter}':fontfile='{self.font}':x={self.xPos + x_offset}:y={self.yPos + y_offset}-({self.size}/2):fontsize={self.size}/2:fontcolor={self.color}:enable='between(t,{int(self.start) + time_offset},{self.duration})':y_align=baseline,"

    def animate(self, style="scroll"):
        if style == "scroll":
            return self.scroll()
        if style == "fade":
            print("Kemper needs to make the fade command.")
            return self.fade()
    
    def scroll(self):
        wrap = 0

        interval = (float(self.animation_end) - float(self.start)) / float(len(self.value))     # The time between each letter
            
        total_time_offset = 0                       # The current time delay of each letter
        total_x_offset = -(self.spacing * len(self.value))/4           # The current X positon of each letter
        total_y_offset = 0                          # The current line of each letter

        enteredCommand = False                      # The commands to determine what is done
        raisedCommand = False

        for letter in self.value:
            if (wrap >= self.length) and (letter == " "):       # Tests if its a new word and greater than the wrap length
                total_y_offset += self.size * 1.5                   # Creates a new line
                total_x_offset = -(self.spacing * len(self.value))/4 + self.spacing                                  # Resets the X of the character back to 0
                wrap = 0
                continue

            if enteredCommand == True:
                if letter in self.COLOR_DICT:
                    self.change_color(code=letter)
                    enteredCommand = False
                    continue
                if letter == "^":
                    raisedCommand = True
                    enteredCommand = False
                    continue
            if raisedCommand == True:                       # If the letter is raised, add to the statement the raised character
                self.raised_character(letter=letter, x_offset=total_x_offset, y_offset=total_y_offset, time_offset=total_time_offset)
                total_x_offset += self.spacing/2
                raisedCommand = False
            elif letter == "&":                               # If the letter is the "&" sign
                enteredCommand = True                           # Enter the command protocol
                continue
            else:                                           # Otherwise, adds to the statement
                self.statement += f"drawtext=text='{letter}':fontfile='{self.font}':x={self.xPos + total_x_offset}:y={self.yPos + total_y_offset}:fontsize={self.size}:fontcolor={self.color}:enable='between(t,{int(self.start) + total_time_offset},{self.duration})':y_align=baseline"
                self.statement += ","
                total_x_offset += self.spacing                      # Moves to the next X
                wrap += 1                                        # Adds to the wrap counter
            total_time_offset += interval
        return self.statement

    def fade(self):
        return ""
    
    def type(self):
        return "text"