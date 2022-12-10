#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

Accumulator := 1
Cycle := 1
Signals := 0

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
MsgBox % Signals
return

Next_Cycle:
if (Mod(Cycle + 20, 40) = 0 and Cycle < 240)
{
	MsgBox % (Accumulator * Cycle)
	Signals += (Accumulator * Cycle)
}
Cycle += 1
return

r::
return