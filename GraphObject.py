import math

# Zero min or max

class Graph:
    def __init__(self, value=None, x=960, y=540, scale = 1, xmin=-10, xmax=10, ymin=-10, ymax=10, axisColor = "white", pointsColor = "red", start=0, duration=5):
        self.equation = value

        self.xPos = x
        self.yPos = y

        self.scale = scale

        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

        self.axisColor = axisColor
        self.pointsColor = pointsColor

        self.start = start
        self.duration = duration
        
        self.statement = ""
    
    def toText(self):
        negetive_x_offset = (self.xmin / (-self.xmin + abs(self.xmax))) * 100
        positive_x_offset = (self.xmax / (-self.xmin + abs(self.xmax))) * 100

        if (negetive_x_offset + positive_x_offset > 100):
            positive_x_offset = 100
            negetive_x_offset = 0
            self.statement += f"drawbox=:x={self.xPos}:y={self.yPos}:w={abs(positive_x_offset * self.scale)}:h={3}:color={self.axisColor}:enable='between(t,{int(self.start)},{self.duration})',"
        elif (negetive_x_offset <= 0 and positive_x_offset <= 0):
            negetive_x_offset = 100
            positive_x_offset = 0
            self.statement += f"drawbox=:x={self.xPos - abs(negetive_x_offset) * self.scale}:y={self.yPos}:w={abs(negetive_x_offset * self.scale)}:h={3}:color={self.axisColor}:enable='between(t,{int(self.start)},{self.duration})',"
        else:
            self.statement += f"drawbox=:x={self.xPos - abs(negetive_x_offset) * self.scale}:y={self.yPos}:w={abs(negetive_x_offset * self.scale)}:h={3}:color={self.axisColor}:enable='between(t,{int(self.start)},{self.duration})',"
            self.statement += f"drawbox=:x={self.xPos}:y={self.yPos}:w={abs(positive_x_offset * self.scale)}:h={3}:color={self.axisColor}:enable='between(t,{int(self.start)},{self.duration})',"
        
        negetive_y_offset = (self.ymin / (-self.ymin + abs(self.ymax))) * 100
        positive_y_offset = (self.ymax / (-self.ymin + abs(self.ymax))) * 100

        if (negetive_y_offset + positive_y_offset > 100):
            positive_y_offset = 100
            negetive_y_offset = 0
            self.statement += f"drawbox=:x={self.xPos}:y={self.yPos - abs(positive_y_offset) * self.scale}:w={3}:h={abs(positive_y_offset * self.scale)}:color={self.axisColor}:enable='between(t,{int(self.start)},{self.duration})',"
        elif (negetive_y_offset <= 0 and positive_y_offset <= 0):
            negetive_y_offset = 100
            positive_y_offset = 0
            self.statement += f"drawbox=:x={self.xPos}:y={self.yPos}:w={3}:h={abs(negetive_y_offset * self.scale)}:color={self.axisColor}:enable='between(t,{int(self.start)},{self.duration})',"
        else:
            self.statement += f"drawbox=:x={self.xPos}:y={self.yPos - abs(positive_y_offset) * self.scale}:w={3}:h={abs(positive_y_offset * self.scale)}:color={self.axisColor}:enable='between(t,{int(self.start)},{self.duration})',"
            self.statement += f"drawbox=:x={self.xPos}:y={self.yPos}:w={3}:h={abs(negetive_y_offset * self.scale)}:color={self.axisColor}:enable='between(t,{int(self.start)},{self.duration})',"


        xRange = abs(self.xmax - self.xmin)
        xInterval = xRange / (100 * self.scale)
        index = self.xmin
        xpos = 0
        while (index < self.xmax):
            expression = self.equation.replace("x", f"({index})")
            yvalue = eval(expression)

            if (yvalue > self.ymax):
                index += xInterval
                xpos += 1
                continue
            if (yvalue < self.ymin):
                index += xInterval
                xpos += 1
                continue

            self.statement += f"drawbox=:x={self.xPos - abs(negetive_x_offset) * self.scale + xpos}:y={self.yPos - self.scale * yvalue * 5}:w={3}:h={3}:color={self.pointsColor}:enable='between(t,{int(self.start)},{self.duration})',"

            index += xInterval
            xpos += 1
            
        return self.statement

    def type(self):
        return "graph"
   