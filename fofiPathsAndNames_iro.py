from pathlib import Path
from terminalFormatting_iro import *

# Internal Constants
_ILLEGAL_CHARACTERS_PRINTABLES_ONLY_NNO_ALTERNATIVES = {
    "?" : "？",
    "<" : "＜",
    ">" : "＞",
    "*" : "＊",
    '"' : "”",
    ":" : "：",
    "|" : "｜",
    "/" : "／",
    "\\" : "＼",
}
_ILLEGAL_CHARACTERS_NON_PRINTABLES_ONLY = {
    "\x00", "\x01", "\x02", "\x03", "\x04", "\x05", "\x06", "\x07",
    "\x08", "\x09", "\x0a", "\x0b", "\x0c", "\x0d", "\x0e", "\x0f",
    "\x10", "\x11", "\x12", "\x13", "\x14", "\x15", "\x16", "\x17",
    "\x18", "\x19", "\x1a", "\x1b", "\x1c", "\x1d", "\x1e", "\x1f",
}
_ILLEGAL_NAMES = {
    "CON", "PRN", "AUX", "NUL",

    "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9",
    "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9",

    "COM¹", "COM²", "COM³",
    "LPT¹", "LPT²", "LPT³",

    "CONIN$", "CONOUT$", "CLOCK$",
}
_convertIllegalCharacters = str.maketrans(_ILLEGAL_CHARACTERS_PRINTABLES_ONLY_NNO_ALTERNATIVES) # DEPENDENCIES: _ILLEGAL_CHARACTERS_PRINTABLES_ONLY_NNO_ALTERNATIVES
_deleteIllegalCharacters = str.maketrans({c: None for c in _ILLEGAL_CHARACTERS_NON_PRINTABLES_ONLY}) # DEPENDENCIES: _ILLEGAL_CHARACTERS_NON_PRINTABLES_ONLY

# External Functions
def convertToValidAndUniqueFofiName_returnsPath_cli(
        fofiParentPath:Path, fofiName:str, 
        duplicateFofiPrefix:str=" (", duplicateFofiStartingIndex:int=2, duplicateFofiSuffix:str=")", 
        illegalFofiPrefix:str="", illegalFofiSuffix:str="_",
        isLongPathEnabled:bool=False
    ) -> Path|None:
    """
    DEPENDENCIES:
        from pathlib import Path

        terminalFormatting_iro:
            BOLD
            RED
            GREEN
            xPrint()
            xInput()
        __file__:
            _ILLEGAL_CHARACTERS_PRINTABLES_ONLY_NNO_ALTERNATIVES
            _ILLEGAL_CHARACTERS_NON_PRINTABLES_ONLY
            _ILLEGAL_NAMES
            _convertIllegalCharacters
            _deleteIllegalCharacters
    WARNINGS:
        Since custom x = str(illegalFofiPrefix+illegalFofiSuffix) is not being checked for any potential issues that it might have,
            so ensure that you do not set its value to something dumb that might raise errors.
            Examples include, but are not limited to, setting x="" or putting illegal characters like "?" in x.
    RETURNS:
        None if "fofiParentPath doesn't exist" else Path.
    **FUNCTIONS**:
        1. Checks if fofiParentPath is a folder.
        2. Converts fofiName into a valid and unique fofiName.
    MORE:
        Sometimes, in other (parent) functions, this function is referred as "naming7_..." for simplicity.
    """
    #checks if parent folder exists
    if not fofiParentPath.is_dir():
        return None
    #converts illegal characters. removes non-printable characters, trailing periods, and leading/trailing spaces.
    fofiName = fofiName.translate(_convertIllegalCharacters).translate(_deleteIllegalCharacters)
    fofiName = fofiName.lstrip(" ").rstrip(" .")
    #counters empty fofiName
    if not fofiName:
        fofiName = "_"
    #creates Path object
    fofiPath = fofiParentPath / fofiName
    #counters illegal fofiName
    suffixes = "".join(fofiPath.suffixes)
    stem = fofiPath.name[:-len(suffixes)] if suffixes else fofiPath.name
    if stem.upper() in _ILLEGAL_NAMES:
        fofiPath = fofiPath.with_name(f"{illegalFofiPrefix}{stem}{illegalFofiSuffix}{suffixes}")
    #counters duplicate fofiName
    stem = fofiPath.name[:-len(suffixes)] if suffixes else fofiPath.name
    while fofiPath.exists():
        fofiPath = fofiPath.with_name(f"{stem}{duplicateFofiPrefix}{duplicateFofiStartingIndex}{duplicateFofiSuffix}{suffixes}")
        duplicateFofiStartingIndex+=1
    #counters long fofiPath and fofiName
    if (len(fofiPath.name) > 255) or (not isLongPathEnabled and len(str(fofiPath)) > 259):
        xPrint(f"The final fofiName is too long: {fofiPath.name}", BOLD + RED)
        x = xInput("Enter new fofiName (with extensions): ", BOLD + RED, BOLD + GREEN)
        return convertToValidAndUniqueFofiName_returnsPath_cli(
            fofiParentPath, x, 
            duplicateFofiPrefix, duplicateFofiStartingIndex, duplicateFofiSuffix, 
            illegalFofiPrefix, illegalFofiSuffix,
            isLongPathEnabled
        )
    #returns
    return fofiPath
