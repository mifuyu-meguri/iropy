from pathlib import Path
import shutil

#iropy
from fofiPathsAndNames_iro import *
from terminalFormatting_iro import *

def rename_cli(
        fofiParentPath:Path, initialName:str, finalName:str,
        #parameters for naming7_...
        naming7_duplicateFofiPrefix:str=" (", naming7_duplicateFofiStartingIndex:int=2, naming7_duplicateFofiSuffix:str=")", 
        naming7_illegalFofiPrefix:str="", naming7_illegalFofiSuffix:str="_",
        naming7_isLongPathEnabled:bool=False
    ) -> tuple[int, Path|None]:
    """
    DEPENDENCIES:
        from pathlib import Path

        #iropy
        from fofiPathsAndNames_iro import *:
            convertToValidAndUniqueFofiName_returnsPath_cli()
                AND its dependencies.
        
        ! Already satisfied by other aforementioned dependencies:
            from terminalFormatting_iro import *:
                BOLD
                RED
                xPrint()
    RETURNS:
        (0, finalPath): Success.
        (1, None): Fofi doesn't exist.
        (2, None): An exception occured.
    """
    initialPath = fofiParentPath / initialName
    if not initialPath.exists():
        xPrint(f"{initialPath} doesn't exist.", RED + BOLD)
        return (1, None)
    finalPath = convertToValidAndUniqueFofiName_returnsPath_cli(
        fofiParentPath=fofiParentPath,
        fofiName=finalName,
        duplicateFofiPrefix=naming7_duplicateFofiPrefix,
        duplicateFofiStartingIndex=naming7_duplicateFofiStartingIndex,
        duplicateFofiSuffix=naming7_duplicateFofiSuffix,
        illegalFofiPrefix=naming7_illegalFofiPrefix,
        illegalFofiSuffix=naming7_illegalFofiSuffix,
        isLongPathEnabled=naming7_isLongPathEnabled,
    )
    try:
        initialPath.rename(finalPath)
        return (0, finalPath)
    except Exception as e:
        xPrint(f"{fofiParentPath}\\{initialName} failed due to exception: {e}", BOLD + RED)
        return (2, None)

def move_cli(
        initialFofiParentPath:Path, initialName:str, 
        finalFofiParentPath:Path, finalName:str,
        #parameters for naming7_...
        naming7_duplicateFofiPrefix:str=" (", naming7_duplicateFofiStartingIndex:int=2, naming7_duplicateFofiSuffix:str=")", 
        naming7_illegalFofiPrefix:str="", naming7_illegalFofiSuffix:str="_",
        naming7_isLongPathEnabled:bool=False
    ) -> tuple[int, Path|None]:
    """
    DEPENDENCIES:
        from pathlib import Path
        import shutil

        #iropy
        from fofiPathsAndNames_iro import *:
            convertToValidAndUniqueFofiName_returnsPath_cli()
                AND its dependencies.
        
        ! Already satisfied by other aforementioned dependencies:
            from terminalFormatting_iro import *:
                BOLD
                RED
                xPrint()
    RETURNS:
        (0, finalPath): Success.
        (1, None): Fofi doesn't exist.
        (2, None): An exception occured.
        (3, None): finalFofiParentPath doesn't exist.
    """
    initialPath = initialFofiParentPath / initialName
    if not initialPath.exists():
        xPrint(f"{initialPath} doesn't exist.", RED + BOLD)
        return (1, None)
    if not finalFofiParentPath.is_dir():
        return (3, None)
    finalPath = convertToValidAndUniqueFofiName_returnsPath_cli(
        fofiParentPath=finalFofiParentPath,
        fofiName=finalName,
        duplicateFofiPrefix=naming7_duplicateFofiPrefix,
        duplicateFofiStartingIndex=naming7_duplicateFofiStartingIndex,
        duplicateFofiSuffix=naming7_duplicateFofiSuffix,
        illegalFofiPrefix=naming7_illegalFofiPrefix,
        illegalFofiSuffix=naming7_illegalFofiSuffix,
        isLongPathEnabled=naming7_isLongPathEnabled,
    )
    try:
        shutil.move(str(initialPath), str(finalPath))
        return (0, finalPath)
    except Exception as e:
        xPrint(f"{initialFofiParentPath}\\{initialName} failed due to exception: {e}", BOLD + RED)
        return (2, None)

def copy_cli(
        initialFofiParentPath:Path, initialName:str, 
        finalFofiParentPath:Path, finalName:str,
        #parameters for naming7_...
        naming7_duplicateFofiPrefix:str=" (", naming7_duplicateFofiStartingIndex:int=2, naming7_duplicateFofiSuffix:str=")", 
        naming7_illegalFofiPrefix:str="", naming7_illegalFofiSuffix:str="_",
        naming7_isLongPathEnabled:bool=False
    ) -> tuple[int, Path|None]:
    """
    DEPENDENCIES:
        from pathlib import Path
        import shutil

        #iropy
        from fofiPathsAndNames_iro import *:
            convertToValidAndUniqueFofiName_returnsPath_cli()
                AND its dependencies.
        
        ! Already satisfied by other aforementioned dependencies:
            from terminalFormatting_iro import *:
                BOLD
                RED
                xPrint()
    RETURNS:
        (0, finalPath): Success.
        (1, None): Fofi doesn't exist.
        (2, None): An exception occured.
        (3, None): finalFofiParentPath doesn't exist.
        """
    initialPath = initialFofiParentPath / initialName
    if not initialPath.exists():
        xPrint(f"{initialPath} doesn't exist.", RED + BOLD)
        return (1, None)
    if not finalFofiParentPath.is_dir():
        return (3, None)
    isFile = True
    if initialPath.is_dir(): # check if file or folder
        isFile = False
    finalPath = convertToValidAndUniqueFofiName_returnsPath_cli(
        fofiParentPath=finalFofiParentPath,
        fofiName=finalName,
        duplicateFofiPrefix=naming7_duplicateFofiPrefix,
        duplicateFofiStartingIndex=naming7_duplicateFofiStartingIndex,
        duplicateFofiSuffix=naming7_duplicateFofiSuffix,
        illegalFofiPrefix=naming7_illegalFofiPrefix,
        illegalFofiSuffix=naming7_illegalFofiSuffix,
        isLongPathEnabled=naming7_isLongPathEnabled,
    )
    try:
        if isFile:
            shutil.copy2(str(initialPath), str(finalPath))
        else:
            shutil.copytree(
                str(initialPath),
                str(finalPath),
                symlinks=True,
            )
        return (0, finalPath)
    except Exception as e:
        xPrint(f"{initialFofiParentPath}\\{initialName} failed due to exception: {e}", BOLD + RED)
        return (2, None)
