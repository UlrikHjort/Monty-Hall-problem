.The Monty Hall problem is a probability puzzle, loosely based on the American television game show 
"Let's Make a Deal" named after its original host, Monty Hall.

In the game show you are given the choice of three doors: Behind one door is a car; behind the others, goats. 
You pick a door and the host, who knows what's behind the doors, opens another door which has a goat. 
You then get the choice to open the door you first selected or to switch to  the still closed door. 
The longterm winning strategy is always to swich doors. Intuitively this can be hard to grep with 3 doors but scaling up to say 
 100 doors makes it more intuitive. 

This little simulator simulate the problem from 1 up to "many" doors and print out the percentage winning rate for staying on the 
 first choice (PICK) and swithcing doors (SWITCH).

Usage is as follow: python montyHall.py <#doors> <#iterations> , where doors is number of doors and iterations number of game iterations.

Sample outputs:

$ python montyHall.py 3 10000
Doors: 3  #Iterations: 10000
PICK: 32.84% wins
SWITCH: 66.95% wins


$ python montyHall.py 100 10000
Doors: 100  #Iterations: 10000
PICK: 0.93% wins
SWITCH: 98.99% wins
