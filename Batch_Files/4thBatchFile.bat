::========================================================================
:: This Batch Script allows  selective outcome, based on chosen conditions
::
::========================================================================

@echo off
set /p UserSelection="Choose between Choices 1,2, or 3: "
ECHO %UserSelection%
IF %UserSelection%==1 GOTO Label1
IF %UserSelection%==2 GOTO Label2

:Label1
   Echo the input was  1


:Label2
   Echo the input was  2
   goto endLabel

:Label3
   Echo the input was  3

:endLabel
    PAUSE

