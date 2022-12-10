#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
#SingleInstance
#Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

Accumulator := 1
Cycle := 1
Line := ""
Output := FileOpen("output.txt", "w")

Main:
Loop, Read, test_data.txt
{
	Parts := StrSplit(A_LoopReadLine, A_Space)
	if (Parts[1] = "noop")
	{
		Gosub, Next_Cycle
	}
	else if (Parts[1] = "addx")
	{
		Gosub, Next_Cycle
		Gosub, Next_Cycle
		Accumulator += Parts[2]
	}
}
Output.write(Line)
Output.close()
return

Next_Cycle:
if (Mod(Cycle - 1, 40) = 0 and Cycle > 39)
{
	Line = % Line "`n"
	Output.write(Line)
	Line = % ""
}
Position := Mod(Cycle - 1, 40)
if (Position >= Accumulator - 1 and Position <= Accumulator + 1)
{
	Line = % Line "#"
}
else
{
	Line = % Line "."
}
Cycle += 1
return

r::
return