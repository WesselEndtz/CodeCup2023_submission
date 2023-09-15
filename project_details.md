Introduction
This year we have chosen the puzzle sudoku as the CodeCup game for 2024. We follow the original rules for sudoku: you must end up with nine different digits (from 1 to 9) in all rows, columns and boxes. This two player game starts with an empty 9x9 grid, and you take turns placing one digit in a valid cell. The first player that believes the sudoku has a unique solution, claims the victory and wins the game.

Goal of the game
The challenge for this game is to claim that the sudoku — you both work with — has a unique solution, before your opponent does. If you overlooked that the sudoku has exactly one solution after your move, the chances are high that your opponent will claim uniqueness immediately in his next turn.

It turns out that not each obvious move can be played: the sudoku could have no solutions left after a move. If you make a move that makes the sudoku impossible to solve, you will lose immediately. The player claiming uniqueness successfully, wins. If you claim uniqueness but the sudoku has at least two distinct solutions, you will lose as well.

Making a move
The rows are numbered from A to I, the columns from a to i. For example, the move "Dg7" places a 7 on the cell Dg. If your program thinks a solution to the sudoku is unique after your move, you can add an exclamation mark to the move, like: "Hd7!". If you think your opponent left the sudoku behind with a unique solution, you can claim uniqueness directly with the move "!" instead. In both cases you win with 2-1.

Scoring
The scoring for this CodeCup game is a bit different than normal, because it is more challenging to find a valid move to play with this game. It’s possible that you run out of time while finding a move, because you are checking whether the sudoku still has a solution left. Otherwise, if you do not perform this check, you may provide an illegal move. In these two cases, we will be kind to your program. The following scorings are possible:

If your program exits during the game too early, or crashes, you lose with 0-2 instantly. The referee will not overtake your program this year.
If your program exceeds the time limit, you will lose with 1-2 instead.
If your move cannot be parsed, you place a digit on an occupied cell, or you place a digit in a row, column or box, that already contains this digit, you lose 0-2.
If your move causes the sudoku to be impossible to solve, you lose 1-2.
If you claim the sudoku is unique with a “!”, and this is indeed the case, you win 2-1. If it’s not the case, you lose 0-2 instead.
In the rare occasion both players do not claim victory, the final score is a draw: 1-1.
When your program is disqualified in a game (e.g. playing an illegal move), it will not be overtaken by the checker or referee, and that game finishes then immediately.

When you play an invalid move that is hard to check or you run out of time, we are kind to you and award you still a point. However, if the move was illegal but easy to check, we will not have mercy.

Input/output
A communication protocol has been designed for your program to communicate with the judging software.

The player that first reads "Start" from standard input must write his/her first move to standard output. If the player reads a move instead, he/she must write the second move to standard output. Do not forget to flush!

A player that reads "Quit" on standard input, must terminate his program.

Players can write information to standard error during execution, which can be read by you after the game is played. For more information, see the Technical rules.

	
Technical rules
This section explains how you should write your program. Since the competition is automatically controlled by scripts, it is important that your program works exactly according to these rules.

Sending your program
To enter the contest, you must write a program that is able to play Sudoku. You must submit the source code of your program on this website. The source code must consist of one single file. The maximum allowed size of the source file is 1 474 560 bytes. We will compile and run your program under Linux. Your program has to finish compiling in 5 minutes (this should be more than enough, typically compiling programs takes less than 2 seconds).

Input and output
Your program reads input from standard input (normally "the keyboard") and writes output to standard output (normally "the screen"). Your program is started once at the beginning of a game and keeps running until the end of the game.

You should strictly follow the dialogue described in the game rules. Each element of input or output is on a line by itself. You may assume that all input to your program is completely correct.

Note: when you write a move to standard output, make sure to flush the stream, so the referee is not waiting for the move. Below is explained how you can flush in some of the supported programming language.

For debugging, your program may write messages to standard error. Those mesages will become available to you, and only you, on the game result page. However there is a limit to the amount of characters that will be logged (approximately 10 000 characters), so you need to use it sparingly.

Programming languages
You may write your program in C/C++, Python, Java, Pascal, JavaScript, Haskell or OCaml. The table below shows which compiler and configuration we are using.

Language	Compiler	Version	Command
C	GNU GCC	11.3.0	gcc -Wall -pipe -O2 -march=native -g --std=c99 -lm
C++	GNU GCC	11.3.0	g++ -Wall -pipe -O2 -march=native -g --std=c++20 -lm
Python 2	 	2.7.18	python2
Python 3	 	3.10.6	python3
Java	OpenJDK	19.0.2	javac ; java -Xmx2000m -Xms2000m -XX:+UseSerialGC
Pascal	FreePascal	3.2.2	fpc -Sog -O2 -viwn -g -Cr-t-
JavaScript	V8	7.1.0	d8 --single-threaded
Haskell	GHC	8.8.4	ghc --make -O3
OCaml	 	4.13.1	ocamlopt -o
Go	 	1.18.1	go build
Rust	 	1.66.1	rustc -O --edition=2021 -C target-cpu=native
 

C and C++
Programs written in C or C++ are compiled with GCC, and linked with the standard math library.

You can use scanf to read from standard input, and printf to write to standard output. After you write a move to standard output, your program should call fflush(stdout); to make sure output is written immediately. Write debugging messages to standard error, using fprintf(stderr, "Debug info\n");

In C++ it is also possible to use cin, cout and cerr. Use cout.flush() to flush the output buffer.

Python
Programs written in Python are run with the Python interpreter.

You can use input() to read from standard input, and print to write to standard output. After you write a move to standard output, your program should either supply flush=True to print, or call sys.stdout.flush() to make sure output is written immediately. Write debugging messages to standard error, using print('Debug info', file=sys.stderr) for Python 3. In Python 2, you need to read input with sys.stdin.readline() instead, and write to standard error using print >>sys.stderr, 'Debug info'.

You can use all standard Python modules (e.g. sys, re, time) in your program, as well as numpy in Python 3. Your own code must be in a single file.

Note that Python programs are typically slower than programs in C, Pascal or Java.

Java
Programs written in Java are compiled and run with OpenJDK.

You can use the object System.in to read from standard input, and System.out to write to standard output. After you write a move to standard output, your program should call System.out.flush(); to make sure output is written immediately. Write debugging messages to standard error, using System.err.println("Debug info");

It is possible to make more than one class for your program, but you will have to put the source for all classes in a single .java file (the compiler will produce multiple .class files anyway). When you do this, you should not declare your classes public, or the compiler will complain about it.

When submitting your Java program on the website, don't forget to enter the exact name of the main class of your program (the class which contains the main method).

Pascal
Programs written in Pascal are compiled with FreePascal in TurboPascal mode.

FreePascal is a lot like Turbo Pascal, but it is more powerful. You can make an array of a few megabytes size without problems. Please note that the types Integer and Word can not contain numbers larger than 32767 and 65536 respectively. It is usually better to use the type LongInt.

You can use Read and ReadLn to read from standard input, and WriteLn to write to standard output. After you write a move to standard output, your program should make a call to Flush(Output); to make sure output is written immediately. Write debugging messages to standard error, using WriteLn(StdErr, 'Debug info');

Using units in your program is not recommended. They will not help you very much and may cause problems when your program runs in the competition system. It is not possible to use units you have written yourself, since your source code must consist of a single file. Especially the CRT unit will cause problems. Do not use the CRT unit.

JavaScript
Programs in JavaScript are run with the V8 JavaScript engine.

You can use readline to read from standard input, and write or print to write to standard output. Note that print works the same as write except that print appends a newline. Write debugging messages to standard error, using the printErr or console.error function.

 

Runtime environment
Computer 	Intel(R) Xeon(R) CPU E5-2620 0 @ 2.00GHz
Memory 	8 GB, your program can use 2 GB
Operating system 	Ubuntu 22.04.2 LTS
Time limit 	30 seconds per game
Compile time limit 	5 minutes (should be enough)
Your program is allowed to use at most 30 seconds per game. We measure only the time that your own program spends to select a move, not the time that your opponent spends to select a move. If your program exceeds the time limit, it loses the game and receives a penalty for irregular loss of a game.

There is no time limit per move, only the time limit per game. So your program could use 29 seconds for the first move, but then it would have to do the rest of the game in 1 second.

Remember that the CodeCup systems are 2.00GHz. If your computer at home is slower or faster, you will have to be careful. It is always a good thing to play a game at home exactly as it was played on the CodeCup system. You can see how much time had been used by your program.

To keep the contest fair, some things are not allowed:

Your program should not read or write any files.
It is not allowed to make network connections of any sort.
System dependent tricks like starting other programs or creating extra processes or threads are not allowed.
It is not possible to do calculations while it is your opponent's turn to make a move. In other words, your program can not "think in the opponent's time".