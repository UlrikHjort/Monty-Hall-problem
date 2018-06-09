########################################################################
#                                                                           
#                                                                    
#                      Monty Hall Problem Simulated
#                             MH_Problem.py                                      
#                                                                           
#                                MAIN                                      
#                                                                           
#                 Copyright (C) 1998 Ulrik Hoerlyk Hjort                   
#                                                                           
#  Monty Hall Problem Simulated is free software;  you can  redistribute it                          
#  and/or modify it under terms of the  GNU General Public License          
#  as published  by the Free Software  Foundation;  either version 2,       
#  or (at your option) any later version.                                   
#  Monty Hall Problem Simulated is distributed in the hope that it will be                           
#  useful, but WITHOUT ANY WARRANTY;  without even the  implied warranty    
#  of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                  
#  See the GNU General Public License for  more details.                    
#  You should have  received  a copy of the GNU General                     
#  Public License  distributed with Yolk.  If not, write  to  the  Free     
#  Software Foundation,  51  Franklin  Street,  Fifth  Floor, Boston,       
#  MA 02110 - 1301, USA.                                                    
########################################################################        

import numpy as np
import itertools
import random
import sys


##############################################################################
#
# 
#
##############################################################################

class MontyHall:
    ##########################################################################
    #
    #
    #
    ##########################################################################
    def __init__(self, num_of_doors, iterations):
        self.num_of_doors = num_of_doors
        self.iterations = iterations
        self.pick_wins = 0
        self.pick_loss = 0
        self.switch_wins = 0
        self.switch_loss = 0
        self.win_door = random.randrange(self.num_of_doors)
        self.game()



    ##########################################################################
    #
    #
    #
    ##########################################################################
    def new(self):
        self.win_door = random.randrange(self.num_of_doors)



    ##########################################################################
    #
    #
    #
    ##########################################################################
    def choose(self):
        return random.randrange(self.num_of_doors)

    ##########################################################################
    #
    #
    #
    ##########################################################################
    def pick(self):
        self.new()
        door = self.choose()
        if self.win_door == door:
                self.pick_wins += 1
        else:
                self.pick_loss += 1        


    ##########################################################################
    #
    #
    #
    ##########################################################################
    def switch(self):
        self.new()
        door = self.choose()
        # if choosen door is the winner we have lost since we switch:
        # if not winner door will be the one we switch to
        if self.win_door == door:
            self.switch_loss +=1
        else:
            self.switch_wins +=1            
            


    ##########################################################################
    #
    #
    #
    ##########################################################################
    def game(self):
        print "Doors: " + str(self.num_of_doors) + "  #Iterations: " + str(self.iterations)
        while(self.iterations > 0):
            self.pick()
            self.switch()
            self.iterations -= 1
        self.results()

    ##########################################################################
    #
    #
    #
    ##########################################################################
    def results(self):
        print "PICK: " + str(100.0 *self.pick_wins / (self.pick_wins + self.pick_loss)) + "% wins"
        print "SWITCH: " + str(100.0 *self.switch_wins / (self.switch_wins + self.switch_loss)) + "% wins"            
        

if len(sys.argv) != 3:
    print "usage: python " + sys.argv[0] + " <#doors> <#iterations>"
    sys.exit(1)
else:
    m = MontyHall(int(sys.argv[1]),int(sys.argv[2]))
