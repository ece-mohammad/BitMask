# RegMask
A small tool that makes generating bit masks easy.

Intro:
------

It's not like what it sounds. It doesn't *actually* edit registers in your device's memory.

This tool shows you 34-buttons. 32 of them represent a 32-bit register, each button maps to a bit.
And the decimal, hexadecimal value that's held in those 32-bits. The other two are a *Clear* and *Exit* button.

You can toggle any bit, simply by clicking on the corresponding button, the value will be updated almost instantly.
You can also clear all the bits, by clicking the *Clear* button.

This tool is made for newbie programmers (like myself) who struggle with register values when debugging.


TODO:
------
- Allow user to input a decimal/hexadecimal value and see the set bits in the register.
