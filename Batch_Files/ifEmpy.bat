@ECHO OFF
dir /A /B "C:\Users\Burudani\Documents\TestingFolder" | findstr /R ".">NUL && GOTO Label1

:Label1
   ECHO Folder is not empty
   goto endLabel

:endLabel
    PAUSE