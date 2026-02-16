#CONSTANTS
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"

#FUNCTIONS
def xPrint(text:str="", properties:str="", end:str="\n") -> None:
    print(properties + text + "\033[0m", end=end)

def xInput(text:str="", inputProperties:str="", outputProperties:str="") -> str:
    i = input(inputProperties + text + "\033[0m" + outputProperties)
    print("\033[0m", end="")
    return i
