from pathlib import Path
from fofiPathsAndNames_iro import *
from terminalFormatting_iro import *

def rename_cli(
        fofiParentPath:str, initialName:str, finalName:str,
        #parameters for naming7_...
        naming7_duplicateFofiPrefix:str=" (", naming7_duplicateFofiStartingIndex:int=2, naming7_duplicateFofiSuffix:str=")", 
        naming7_illegalFofiPrefix:str="", naming7_illegalFofiSuffix:str="_",
        naming7_isLongPathEnabled:bool=False
    ) -> tuple[Path|None, int]:
    try:
    except Exception as e:
        xPrint(f"{fofiParentPath}\\{initialName} failed due to exception: {e}", BOLD + RED)

def move_cli():

def copy_cli():
