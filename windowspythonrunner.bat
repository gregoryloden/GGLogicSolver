@echo off
:main
set /p program=Enter a program or "quit": 
for /f "tokens=1,2,3,4,5,6,7,8,9,10,11 delims= " %%a in ("%program%") do set theprogram=%%a&set arg1=%%b&set arg2=%%c&set arg3=%%d&set arg4=%%e&set arg5=%%f&set arg6=%%g&set arg7=%%h&set arg8=%%i&set arg9=%%j&set arg10=%%k
if %theprogram%==quit (goto quit) else (goto java)
:java
python %theprogram%.py %arg1% %arg2% %arg3% %arg4% %arg5% %arg6% %arg7% %arg8% %arg9% %arg10%
goto main
:quit