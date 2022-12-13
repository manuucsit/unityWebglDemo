FOR /F "tokens=* USEBACKQ" %%F IN (`cd`) DO (
SET var=%%F
)
echo %var% > "C:\Users\Administrator\Documents\GitHub\unityWebglDemo\var.txt"