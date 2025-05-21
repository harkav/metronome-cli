# Metronome app, final project for cs50p
#### Video demo: https://youtu.be/QHMxAvOUjOo
#### Description: A metronome cli app for linux, I don't think it works on Windows. 


## Purpose: 
To create a cli app that functions as a metronome, furthermore, to teach myself the basics 
of threading in Python. 
A metronome is a tool that musicians use to follow a beat while they are playing.  
I need threads in this assignment because I need to run two separate processes since I want 
to be able to adjust the bpm while the metronome is running. 

## Usage: 
create a directory with the files listed under files. 
[optional] create a venv, run source ./bin/activate in the parent directory
install the requirements using pip install -r requirements.txt 

Run python -m metronome.project.py [number of beats per bar] [beats per minute ], for example python project.py 3 120 in a directory containing 
the files listed under files. 
Make sure that the two wav-files, monitor.py, project.py and test_project.py (for testing) are all in the same directory. 


## Files 
- project.py - the main program 
- metronome-85688.mp3 and metronome-85688(1).mp3 - the two sound files that the metronome uses
- requirements.txt - the requirements file 
- README.md - the readme file. 
- metronome.py - a custom class 
- test_project.py - the tests. 


## Citations: 
Most of the code is based on topics that we've gone through in the lectures. I've also read about threading in
the offical python docs: https://docs.python.org/3/library/threading.html 
I read about how to register key presses on a substack thread. 
https://stackoverflow.com/questions/34497323/what-is-the-easiest-way-to-detect-key-presses-in-python-3-on-a-linux-machine
The logic for registering key presses in my code is an adoptation of the first answer in that thread by user Turn. 
The sound files are taken from https://pixabay.com/, with permission. They've been uploaded by user freesound_community


Usage of CS50.ai 
I've used CS50.ai to discuss the problem, but I've not used any code provided by CS50 directly. We discussed the different possibilities of threading in python. CS50.ai suggested using the asyncio library, but I thought it looked a bit too complicated 
for my usecase, so I went with threading instead. 
In my first working implementation, I had another class that acted like a wrapper for the metronome-class, which contained the methods of project.py. That implementation made it hard for me to fulfill the requirement of having 3 methods in addition to the main method that was at the same level as the main method. I asked cs50.ai if it would be possible to fulfill the requirement by breaking the wrapper class up into several methods instead, to which cs50.ai replied yes.

Update after submission and approval by cs50: 
I ran the whole program through ChatGPT and got some feedback. More things remains to be done, but I've fixed some minor things based on the 
help by chatgpt. 



## Limitations: 
I think that my way of registering key presses is OS-dependent. I'm using Linux Mint, and I'm assuming that the program will only
run on UNIX based operating systems, so I am not expecting the program to run on Windows computers. The bpm of the metronome cannot go below 20 or above 320. The program takes two arguments beats per bar and beats per minute, for instance 3, 120 would give you a 3 beats per bar, at 120 beats per minute. 

## Possible expansions: 
A gui could be fun, perhaps in the form of a web app. It could also be fun to make the app run on Windows.
I should also write more and better tests, but I'm not sure how to test some of the key methods in a more programatic way than just running the program and to see that it runs more or less as expected. 

## Bird's eye view of the program
    
I've used an OOP approach to the problem because I think that this apporach made the code easier to read and maintain than a 
purely procedural approach would be. 

class: 

Metronome - gets and validates the args from sys.argv via the main() method. Contains methods for setting and getting the bpm. 

methods: 

main(), checks for correct number of sys.args, creates a metronome and a thread that runs the change_bpm method. runs validate_input() 

validate_input() validates and returns the input from sys.argv, tested in test_project.py 
increment() increments the bpm of the metronome, tested in test_project.py 
decrement() decrements the bpm of the metronome  tested in test_project.py 



Encapsulation: 
    I've used a underscore to indicate variables and methods that the user shouldn't call on directly, rather than the property method that was used in class. 



## Requirements: 

Most of the libraries are built in python libraries, and I've written the program with python 3.10.12. 
I've also used pygame version 2.6.1 to play sounds as well as pytest 8.3.3 for running the tests. 


### Final thoughts 

    I've learned a lot from this project. I still don't quite understand why I don't seem to need any locks. Isn't bpm a shared resource between two threads, and shouldn't there be some danger of race conditions? I should probably practice writing documentation a bit, 
    but I think this is relatively clear, and that the language is possible to understand, despite my typos and lack of style. 
    I also think that my tests aren't really testing some of the most important parts of the program, but I'm not sure how to test them with pytest. I have tried to run the program and stress-test it a bit, and it hasn't crashed yet. There is a little possible bug in the increment and decrement functions; if bpm is 312 and you try to increment with 10, it will just remain at 312. It would perhaps be better if it had incremented it up to 320, which is the upper limit. Same goes for the decrement function. Update, bug is supposed to be fixed now. 


### Post-submission updates: 

    Ran the code through chatgpt and got some help for fixing a few minor and not so minor things. Most importantly, the program exits more gracefully now. The menu doesn't print to the terminal every 0.5 seconds. 