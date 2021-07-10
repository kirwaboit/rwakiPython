@ECHO OFF
   •
   •
CHOICE /C:123 /N Choose 1, 2 or 3
IF ERRORLEVEL 3 GOTO Label3
IF ERRORLEVEL 2 GOTO Label2
IF ERRORLEVEL 1 GOTO Label1
   •
   •
:Label1
ECHO You chose 1
GOTO End

:Label2
ECHO You chose 2
GOTO End

:Label3
ECHO You chose 3
GOTO End
   •
   •
:End

PAUSE