# Scientfic Calculator

Welcome to my scientific-calculator Repo! This little project is meant for me as a coding-playground with a real usecase. This is an application coded in Python; a scientific calculator. I plan on making one application that supports a **calculator** and a **graphical calculator**, both of which will accept input through buttons and keyboard. The current state is that I have a backend for the calculator, and the frontend for it too (in TKinter). In other words: lots of work to do still.

The only thing you need to do in order to get this application to run, is running `runapp.py` in the project root.

## Project Structure

src/
├── backend/
│   ├── calculator/
│   ├── parser/
│   └── pathmanager/
└── frontend/
    └── app/
        ├── calculator/
        └── plotter/

## TODOs

First and foremost, I need to add a lot of documentation, everywhere.

The actual calculator itself is working in its first, and simplest version. The 'basic' calculator buttons work, as do the simple functions. The more complex mathematical functions, that also need some adjustments in the order of inputs, still need to be worked out (currently these buttons are highlighted in light purple). The skeleton is ready though, so the extension here should be very doable.

The entire graphcial - calculator still needs to be setup. This will be similar to the one by desmos (desmos.com/calculator), where there are multiple fields available for one expression each ($y=1$, $x=1$, but also $f(x): y = x$) as well as the Cartesian axes on which these functions or expressions are plotted. These should allow for interactive use: i.e. zooming in and out, hovering over curves, etc.