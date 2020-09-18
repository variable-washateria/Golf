

'''

ABOUT THE GAME: 

Golf is a simple card game played between two people. This program uses its most basic rules.  

The object is to get the lowest points possible by swapping with a discard pile. 

4 cards are dealt to each person. 

Per person- two of their cards are face up, two  of their cards are facedown. No one is allowed to see the facedown cards until the round is over. 

To the side of the players is the rest of the deck. On initial dealing, the top card from the deck is flipped into a pile which becomes the discard pile.

The player has three major options per turn. One of these options includes an additional second option. 

			i) Accept the card in the discard pile. Swap that card with one of their four cards. Pass the turn to the other player. 

			ii) Hit the deck to flip another card over in discard pile.  
						a) Accept new card in the discard pile. Swap that card with one of their four cards. Pass the turn to the other player. 
						b) Reject new card entirely. Pass the turn to the other player. Pass the turn to the other player. 

			iii) Reject card entirely. Pass the turn to the other player. 

There is also a fourth option that available whenever it is a player's turn. 

			iv) "Knock". This declares that the round is over. All cards must get flipped up. The scores must get tallied for that round. By making this decision,
			the player is betting that they are in the best time to stop the round. 

ABOUT THE PROGRAM:

Brief Synopsis: 
 This Tkinter applciation consists of three classes: Cards(), Round(), Game(), and one classless function, shuffle(). Cards() accepts .ppm files as arguments,
 proccesses them in the Tkinter fashion with customizable sizes. The function, shuffle(), supplies those .ppm files. It creates the images for the deck, the values for the 
 deck, shuffles the deck, and deals the deck. In addition, it sets up a number of things that are necessary to restart each round- like score. Finally, it sets up three buttons,
 but not their functions.  Round() contains the logic of the game. It supplies the toggle-functions for the User to choose, as well as the logic for the Robot to respond. 
 Finally, Game(), is there to be the root of the entire application. This makes it so there can be many rounds, so that the rounds can tally up for a final game score. 

My revelation: 
In the real world, when a card is on the table, there are three categorical types to register: the space it occupies, the physical constituents, and the 
value it represents.  To manage keeping these coherent, dictionaries were created so one could refer to the other. In this program, image files are 2D, so 
an additional ditionary was created to represent face down cards.  

One challenging riddle of this program was how to create a function that swapped cards based on position but without reference to position. 
In English, you can just say, "swap the corner card with the discard pile". In programming, you have to refer to the actual card object, but that object changes
as soon as the  swap is made. Basically I had to tell the computer to "swap this for that", then assert afterwards that "this = that", so when the 
the function "swap this for that" is reused, and the old "that" changed, it swapped "that" for a different "that".  

Some Notes About Syntax:

"User" and "human" are used interchangebly. 

The User's hand is referred with cardinal directions. The top left is NW. The top right is NE. The bottom left is SW. The bottom right is SE. 

The robot's hand is reffered to by position numbers. Position 1 is top left. Position 2 is top right. Position 3 is bottom left. Position 4 is bottom right. 

'''
from tkinter import *
from PIL import Image
from PIL import ImageTk
import random 

root = Tk()

lstofpics = []
lstofcardbacks =[]

class Cards():

	def __init__(self,file):
		self.file = file

	# Accepts .ppm image files as arguments, configures them, adds them to a list.
	# Basically, creates the deck, face up cards. 
	def steps(self,file):
		opened = Image.open(self.file)
		img = opened.resize((50,50), Image.ANTIALIAS)
		blah = ImageTk.PhotoImage(img)
		lstofpics.append(blah)
		return lstofpics

	# Same process as steps but does it len(a) times. 
	# Basically, creates the deck, face down cards- 52 times.  
	def steps2(self,file):
		for el in range(52):
			opened = Image.open(self.file)
			img = opened.resize((50,50), Image.ANTIALIAS)
			blah = ImageTk.PhotoImage(img)
			lstofcardbacks.append(blah)
		return lstofcardbacks

# I. CREATING THE DECK, 
#II. ASSIGNING VALUES TO CARD IMAGES (FACE UP AND FACE DOWN)
#III. SHUFFLING THE DECK
# (Classless function, but it works.)
def shuffle(self):
		
		# Each new round starts at 0 to 0. 
		self.humanscore = 0
		self.robotscore = 0

		# Each new round, the user begins the play. 
		self.usersturn = True
		self.havenothitthisturn = True

		# I. CREATING THE DECK 

		# An empty deck: 
		self.lstofpics = []		 
		self.lstofcardbacks =[]

		# Assigning card names to their image and to Cards() class.  

		kingclubs= Cards("KC.ppm")
		kingdiamond= Cards("KD.ppm")
		kingspade= Cards("KS.ppm")
		kingheart=  Cards("KH.ppm")

		aceclubs = Cards("AC.ppm") 
		acediamond= Cards("AD.ppm")
		acespade = Cards("AS.ppm") 
		aceheart = Cards("AH.ppm") 

		twoclubs = Cards("2C.ppm") 
		twodiamond = Cards("2D.ppm") 
		twospade = Cards("2S.ppm") 
		twoheart = Cards("2H.ppm") 

		threeclubs = Cards("3C.ppm") 
		threediamond = Cards ("3D.ppm") 
		threespade =Cards("3S.ppm")
		threeheart = Cards("3H.ppm") 

		fourclubs = Cards("4C.ppm")
		fourdiamond= Cards("4D.ppm")
		fourspade= Cards("4S.ppm")
		fourheart= Cards("4H.ppm")

		fiveclubs= Cards("5C.ppm")
		fivediamond= Cards("5D.ppm")
		fivespade= Cards("5S.ppm")
		fiveheart= Cards("5H.ppm")

		sixclubs= Cards("6C.ppm")
		sixdiamond= Cards("6D.ppm")
		sixspade= Cards("6S.ppm")
		sixheart= Cards("6H.ppm")

		sevenclubs= Cards("7C.ppm") 
		sevendiamond= Cards("7D.ppm")
		sevenspade= Cards("7S.ppm")
		sevenheart= Cards("7H.ppm")

		eightclubs = Cards("8C.ppm") 
		eightdiamond= Cards("8D.ppm")
		eightspade= Cards("8S.ppm")
		eightheart= Cards("8H.ppm")

		nineclubs= Cards("9C.ppm")
		ninediamond= Cards("9D.ppm")
		ninespade= Cards("9S.ppm")
		nineheart= Cards("9H.ppm")

		tenclubs= Cards("10C.ppm")
		tendiamond= Cards("10D.ppm")
		tenspade= Cards("10S.ppm")
		tenheart= Cards("10H.ppm")

		jackclubs= Cards("JC.ppm")
		jackdiamond= Cards("JD.ppm")
		jackspade= Cards("JS.ppm")
		jackheart= Cards("JH.ppm")

		queenclubs= Cards("QC.ppm")
		queendiamond= Cards("QD.ppm")
		queenspade= Cards("QS.ppm")
		queenheart= Cards("QH.ppm")

		blueback = Cards("blue_back.ppm")

		# Creates the face up deck by putting image data through configuration process. Maintains sequential order. (Kings = 0 in Golf.)

		self.lstofpics=kingclubs.steps("KC.ppm") 
		self.lstofpics=kingdiamond.steps("KD.ppm")
		self.lstofpics=kingspade.steps("KS.ppm")
		self.lstofpics=kingheart.steps("KH.ppm")

		self.lstofpics=aceclubs.steps("addams-family.pgm") 
		self.lstofpics=acediamond.steps("AD.ppm") 
		self.lstofpics=acespade.steps("AS.ppm") 
		self.lstofpics=aceheart.steps("AH.ppm") 

		self.lstofpics = twoclubs.steps("2C.ppm") 
		self.lstofpics = twodiamond.steps("2D.ppm") 
		self.lstofpics = twospade.steps("2S.ppm") 
		self.lstofpics = twoheart.steps("2H.ppm") 

		self.lstofpics=threeclubs.steps("voyager2.pgm") 
		self.lstofpics=threediamond.steps("3D.ppm") 
		self.lstofpics=threespade.steps("3S.ppm")  
		self.lstofpics=threeheart.steps("3H.ppm") 

		self.lstofpics=fourclubs.steps("4C.ppm") 
		self.lstofpics=fourdiamond.steps("4D.ppm")
		self.lstofpics=fourspade.steps("4S.ppm")
		self.lstofpics=fourheart.steps("4H.ppm")

		self.lstofpics=fiveclubs.steps("5C.ppm") 
		self.lstofpics=fivediamond.steps("5D.ppm")
		self.lstofpics=fivespade.steps("5S.ppm")
		self.lstofpics=fiveheart.steps("5H.ppm")

		self.lstofpics=sixclubs.steps("6C.ppm") 
		self.lstofpics=sixdiamond.steps("6D.ppm")
		self.lstofpics=sixspade.steps("6S.ppm")
		self.lstofpics=sixheart.steps("6H.ppm")

		self.lstofpics=sevenclubs.steps("7C.ppm") 
		self.lstofpics=sevendiamond.steps("7D.ppm") 
		self.lstofpics=sevenspade.steps("7S.ppm")
		self.lstofpics=sevenheart.steps("7H.ppm") 

		self.lstofpics=eightclubs.steps("8C.ppm") 
		self.lstofpics=eightdiamond.steps("8D.ppm") 
		self.lstofpics=eightspade.steps("8S.ppm") 
		self.lstofpics=eightheart.steps("8H.ppm") 

		self.lstofpics=nineclubs.steps("9C.ppm") 
		self.lstofpics=ninediamond.steps("9D.ppm") 
		self.lstofpics=ninespade.steps("9S.ppm") 
		self.lstofpics=nineheart.steps("9H.ppm") 

		self.lstofpics=tenclubs.steps("10C.ppm") 
		self.lstofpics=tendiamond.steps("10D.ppm") 
		self.lstofpics=tenspade.steps("10S.ppm") 
		self.lstofpics=tenheart.steps("10H.ppm") 

		self.lstofpics=jackclubs.steps("JC.ppm") 
		self.lstofpics=jackdiamond.steps("JD.ppm") 
		self.lstofpics=jackspade.steps("JS.ppm") 
		self.lstofpics=jackheart.steps("JH.ppm") 

		self.lstofpics=queenclubs.steps("QC.ppm") 
		self.lstofpics=queendiamond.steps("QD.ppm")
		self.lstofpics=queenspade.steps("QS.ppm")
		self.lstofpics=queenheart.steps("QH.ppm")

		# Creates the face down deck by putting image data through configuration process 52 times. Maintains same sequential order.
		self.lstofcardbacks = blueback.steps2("blue_back.ppm")
																	
		# II. ASSIGNING VALUES TO  CARD IMAGES (FACE UP AND FACE DOWN)
		# Each tuple and dictionary has a hash tag identifier (AAA, BBB, CCC, etc.) Their later instance of use is marked in a corresponding manner for ease of reference. 

		# Skeleton of values for listofpics. Value of card is it's number, not suite. (2 hearts = 2 clubs). Hence, 12 values:
		self.a = [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,] 

		# Dictionary,  {faceup pics : value}: 							
		self.dict_faceuppics_to_values = dict(zip(self.lstofpics,self.a))						## AAA

		# Dictionary, {facedown pics : face up pics} 
		self.dict_facedownpic_to_faceuppic = dict(zip(self.lstofcardbacks, self.lstofpics)) 	## BBB

		# Dictionary, {faceup pics : facedown pics}
		self.dict_faceuppic_to_facedownpic = dict(zip(self.lstofpics, self.lstofcardbacks))     ## CCC

		# III. SHUFFLING THE DECK- the faceup pics and their values, using (AAA). 
		
		self.shuffled_lstofvalues = []																	## DDD
		self.shuffled_lstofpics = []																	## EEE
		
		self.lstoftuples = list(zip(self.a, self.lstofpics))                                			
		self.shuffleddeck = random.sample(self.lstoftuples, k = len(self.lstoftuples))  		
		for self.tpl in self.shuffleddeck:
			self.shuffled_lstofvalues.append(self.tpl[0]) 												
			self.shuffled_lstofpics.append(self.tpl[1])

		# II DEALING THE DECK 
		# Dealing is a two step process: 
		# i) Popping the cards out of the deck. ii) Placing the cards down.   
		
		# i) Popping the cards out of the deck. 
		# (Remember that listofpics2 has been shuffled.) 
		# We're popping the first card out of the image "deck" each of these 9 iterations. Though only four cards will be shown faceup, we need to 
		# pop all 9 out to preserve the sequence. 
		# User's cards:
		self.dealtcard1 = self.shuffled_lstofpics.pop(0)										## (EEE)
		self.dealtcard2 = self.shuffled_lstofpics.pop(0)										## (EEE)
		self.dealtcard3 = self.shuffled_lstofpics.pop(0)										## (EEE)
		self.dealtcard4 = self.shuffled_lstofpics.pop(0)										## (EEE)
		# Robot's cards: 
		self.dealtcard5 = self.shuffled_lstofpics.pop(0)										## (EEE)
		self.dealtcard6 = self.shuffled_lstofpics.pop(0)										## (EEE)
		self.dealtcard7 = self.shuffled_lstofpics.pop(0)										## (EEE)
		self.dealtcard8 = self.shuffled_lstofpics.pop(0)										## (EEE)

		# This card will be the first card of the discard pile. 
		# Once game is in play, "lastcarddealt" will be triggered by "hitting" the deck functions. 
		self.lastcarddealt = self.shuffled_lstofpics.pop(0)
												## (EEE)
		# Each dealt card pic is to an object which will be placed appropriately in the User's hand. Later, other pics will be assigned to that object. 
		self.NWpositionpic_fromdeck = self.dealtcard1
		self.NEpositionpic_fromdeck = self.dealtcard2
		self.SWpositionpic_fromdeck = self.dealtcard3       											
		self.SEpositionpic_fromdeck = self.dealtcard4

		# Assigns values and faceup pics, of robot's dealt cards. 
		# We need to establish the faceup pic for all cards, for if/when the robot discards them. 
		self.position1value = self.dict_faceuppics_to_values[self.dealtcard5]  					# (AAA)
		self.position1pic = self.dealtcard5	
		self.position2value = self.dict_faceuppics_to_values[self.dealtcard6]					# (AAA)
		self.position2pic = self.dealtcard6
		self.position3value = self.dict_faceuppics_to_values[self.dealtcard7] 					# (AAA) 
		self.position3pic = self.dealtcard7
		self.position4value = self.dict_faceuppics_to_values[self.dealtcard8]					# (AAA)
		self.position4pic = self.dealtcard8

		# ii) Placing the cards down.   

		# User: 

		# Two cards facedown: 
		self.User_NW_button = Button(image= self.dict_faceuppic_to_facedownpic[self.dealtcard1], command= self.NW_card)		#(CCC)
		self.User_NW_button.grid(row = 8, column = 1)

		self.User_NE_button = Button(image= self.dict_faceuppic_to_facedownpic[self.dealtcard2], command = self.NE_card)		#(CCC)
		self.User_NE_button.grid(row = 8, column = 2)

		# Two cards faceup: 
		self.User_SW_button = Button(image= self.dealtcard3, command= self.SW_card)
		self.User_SW_button.grid(row = 9, column = 1) 

		self.User_SE_button = Button(image= self.dealtcard4, command = self.SE_card)
		self.User_SE_button.grid(row = 9, column = 2)

		# Robot:

		# Two cards faceup: 
		self.button5 = Button(image= self.dealtcard5, command= None)
		self.button5.grid(row = 1, column = 1)

		self.button6 = Button(image= self.dealtcard6, command = None)
		self.button6.grid(row = 1, column = 2)

		# Two cards facedown:
		# Even though all facedownpics look the same to user, they're not the same. We could theoretically asses their value through the dictionaries we created.   
		self.button7 = Button(image= self.dict_faceuppic_to_facedownpic[self.dealtcard7], command = None )				#(CCC)
		self.button7.grid(row = 2, column = 1)

		self.button8 = Button(image= self.dict_faceuppic_to_facedownpic[self.dealtcard8], command = None )				#(CCC)
		self.button8.grid(row = 2, column = 2)

		# First card of "discard pile", faceup: 
		self.button9 = Button(image= self.lastcarddealt, command = None )
		self.button9.grid(row = 3, column = 3)

		# "The deck." Image of facedowncard. 																
		self.blah = lstofcardbacks[51]																			# Is self.blah = lstofcardbacks[51] necessary?
		self.gb = Button(image= self.blah, command=self.deckforhumans,)  				
		self.gb.grid(row = 3, column = 4)

		# THREE BUTTONS USER CHOOSES FROM

		self.button10 = Button(text = "Knock!", command = self.knock)
		self.button10.grid(row = 8, column = 4)

		self.button11 = Button(text= "Reject Card", command = self.reject )
		self.button11.grid(row = 9, column = 4) 

		self.button12 = Button(text = "New Round", command = self.newround)
		self.button12.grid(row = 11, column = 4)

class Round():

	def __init__(self):

		# I SETTING UP 

		# Creates deck. Assigns Values. Shuffles deck
		self.shfl = shuffle(self)

		# Prevents user from hitting the deck twice in one turn. 
		self.havenothitthisturn = True

		# Prevents user from attemping "Next Round" when not turn or haven't knocked. 
		self.usersturn = True
		self.candeclarenewround = False

		# Keeps track of how many rounds have played. Prints string for scoreboard.  
		self.row = 11
		self.roww = 1

		# Keeps track of total score throughout game. 
		self.totalhumanscore = []
		self.totalrobotscore = []
		
		# Keeps track of whether the card user picks came from deck or robot 
		self.discardcamefromdeck = True   

		# User's cards initially all came from the deck. During play, they sometimes came from robot's hand.   
		self.NW_cardfromdeck = True 
		self.NE_cardfromdeck = True		
		self.SE_cardfromdeck = True
		self.SW_cardfromdeck = True 
		
		# In Knock function, used to tabulate user's score before summing them. 
		self.humanscorelist = []
		
		# This refers to user's deck.  Initial status is that every card being dealt came from deck. During game, other possibility is card came from robot. 
		self.NW_cardfromdeck = True
		self.NE_cardfromdeck = True
		self.SW_cardfromdeck = True 
		self.SE_cardfromdeck = True

		# Scoreboard for game: 
		self.w = Label(text="                        Robot Scores:")
		self.w.grid(row = 10, column = 10 )
		self.w = Label(text="                    1.           ")
		self.w.grid(row = 11, column = 10 )
		self.w = Label(text="                    2.           ")
		self.w.grid(row = 12, column = 10 )
		self.w = Label(text="                    3.           ")
		self.w.grid(row = 13, column = 10 )
		self.w = Label(text="                    4.           ")
		self.w.grid(row = 14, column = 10 ) 
		self.w = Label(text="                    5.           ")
		self.w.grid(row = 15, column = 10 )
		self.w = Label(text="                    6.           ")
		self.w.grid(row = 16, column = 10 )
		self.w = Label(text="                    7.           ")
		self.w.grid(row = 17, column = 10 )
		self.w = Label(text="                    8.           ")
		self.w.grid(row = 18, column = 10 )
		self.w = Label(text="                    9.           ")
		self.w.grid(row = 19, column = 10 )

		self.w = Label(text = "               Human Scores:")
		self.w.grid(row = 10, column = 8)
		self.w = Label(text = "                            1.			")
		self.w.grid(row = 11, column = 8)
		self.w = Label(text = "                            2.			")
		self.w.grid(row = 12, column = 8)
		self.w = Label(text = "                            3.			")
		self.w.grid(row = 13, column = 8)
		self.w = Label(text = "                           4. 			") 
		self.w.grid(row = 14, column = 8)
		self.w = Label(text = "                           5. 			")
		self.w.grid(row = 15, column = 8)
		self.w = Label(text = "                           6. 			")
		self.w.grid(row = 16, column = 8)
		self.w = Label(text = "                            7.			")
		self.w.grid(row = 17, column = 8)
		self.w = Label(text = "                            8.			")
		self.w.grid(row = 18, column = 8)
		self.w = Label(text = "                            9.			")
		self.w.grid(row = 19, column = 8)  

		# Scoreboard for round: 
		self.robotscorecard()
		self.humanscorecard()

	# AUTOMATICALLY INITIALIZIES/DISPLAYS SCOREBOARD FOR ROUND
	def robotscorecard(self):
		
		self.score = Label(text="Robot Score:  " + str(self.robotscore))
		self.score.grid(row=1, column=4, columnspan=2,)

	def humanscorecard(self):

		self.skore = Label(text="Your Score:  " +str(self.humanscore))
		self.skore.grid(row=4, column=4, columnspan=2,)

	def deckforhumans(self):

		if self.usersturn == True and self.havenothitthisturn == True: 
	
			# Pulls one card from the deck:  
			self.lastcarddealt = self.shuffled_lstofpics.pop(0)											## (EEE)
			
			# Lays it on the table: 																					
			self.button9 = Button(image= self.lastcarddealt, command = None )
			self.button9.grid(row = 3, column = 3)

			self.discardcamefromdeck = True
			self.havenothitthisturn = False 

		else: 
			print("Not your turn!")

	def deckforrobots(self):

		self.lastcarddealt = self.shuffled_lstofpics.pop(0)												## (EEE)
		 
		self.button9 = Button(image= self.lastcarddealt, command = None )
		self.button9.grid(row = 3, column = 3)

		self.discardcamefromdeck = True 

#	If the user wants to exhange their card with the discard pile, they will toggle one of these following four functions. 

#	(Other optinos are "reject" or "knock".) 

#	To the user's eye, each function is represented by one of the four cards in the user's hands. 

#	The function simply exchanges that user's card with the card in the discard pile. (Whether they choose NW_card or NE_card, etc...). 

#	These functions soley deal with the image of the card in the form of a button, not the value. 

#	The function also triggers robot() to move- passing two arguments. 


#	They all follow the same pattern.  It is the core logic of how this application works.
		


#	Once toggled, the function assesses the status of certain things to decide the proper manner of execution. It's a decision tree. 

#	First, it assures that usersturn == True, 

#		Second, it decides if elected card in the discard pile came from the deck or from the robot.
#			This decides whether the new image created on user's hand is from the deck or from the robot. 

#			Third, it decides if throwaway card came from the from the deck or robot.
#  				This decides whether the new image created on is discard pile came from the deck or from the robot.
#
#
#			Regardless of throwaycard, it makes a note about elected card's origins for the next move.
#
#		Finally - it clicks the buzzer to say it's robot's turn.    		

	def NW_card(self):
		print("first card pressed")

		if self.usersturn == True:
		
			if self.discardcamefromdeck == True:
				
				# CREATES NE CARD IN USER'S HAND
				# NW and NE are facedownpic
				self.User_NW_button = Button(image= self.dict_faceuppic_to_facedownpic[self.lastcarddealt], command= self.NW_card)		#(CCC)
				self.User_NW_button.grid(row = 8, column = 1)
				
				# CREATES CARD IN DISCARD PILE. Also, ends turn and and summons robot() to move. 
				# If User's throwaway card came from the deck, then the image will be the first dealt card. Earlier, shuffle() copied that as "NWpositionpic_fromdeck".  
				if self.NW_cardfromdeck == True:
					self.discardbutton = Button(image = self.NWpositionpic_fromdeck, command = None)
					self.discardbutton.grid(row=3, column=3)
					self.usersturn = False
					self.robot(self.NWpositionpic_fromdeck)

				# If User's throwaway card came from the robot, then the image will be the robot's previous discard. robot() function copies that as "NWpositionpic_frombot". 
				# It is impossible to call this without first hitting robot(). No errors will arise that NWpositionpic_frombot has not been defined earlier in passage. 
				if self.NW_cardfromdeck == False:
					self.discardbutton = Button(image = self.NWpositionpic_frombot, command = None)
					self.discardbutton.grid(row=3,column =3)
					self.usersturn = False
					self.robot(self.NWpositionpic_frombot)

				# MAKES NOTE OF TWO OBJECTS FOR FUTURE MOVES 
				# Because NW exchanged cards with discard from deck, NW_cardfromdeck == True 
				self.NW_cardfromdeck = True
				# "NWpositionpic_fromdeck" is no longer the first card dealt. Now, it is the lastcarddealt.
				print("1.", self.dict_faceuppics_to_values[self.NWpositionpic_fromdeck])      
				self.NWpositionpic_fromdeck = self.lastcarddealt
				print("2.", self.dict_faceuppics_to_values[self.NWpositionpic_fromdeck]) 
				
			elif self.discardcamefromdeck == False:

				# CREATES NW CARD 
				self.button = Button(image = self.dict_faceuppic_to_facedownpic[self.robotdiscard], command = self.NW_card)		#(CCC)
				self.button.grid(row = 8, column = 1) 


				# CREATES DISCARD
				if self.NW_cardfromdeck == True: 
					self.discardbutton = Button(image = self.NWpositionpic_fromdeck, command = None)
					self.discardbutton.grid(row=3, column=3)
					self.usersturn = False
					self.robot(self.NWpositionpic_fromdeck)
					
				if self.NW_cardfromdeck == False: 
					self.discardbutton = Button(image = self.NWpositionpic_frombot, command = None)
					self.discardbutton.grid(row=3,column =3)
					self.usersturn = False
					self.robot(self.NWpositionpic_frombot)

				# MAKES NOTES 
				# Because NW exchanged cards with discard from bot, NW_cardfromdeck == False
				self.NW_cardfromdeck = False
				# In robot() function, robotdiscard comes from position1 pic or position2 pic- depending on which it wants to discard.
				self.NWpositionpic_frombot = self.robotdiscard		
		else:
			print("Not your turn!")

	def NE_card(self):

		if self.usersturn == True:

			if self.discardcamefromdeck == True:  
				self.button = Button(image = self.dict_faceuppic_to_facedownpic[self.lastcarddealt], command= self.NE_card)  	#(CCC)
				self.button.grid(row = 8, column = 2) 

				if self.NE_cardfromdeck == True: 
					self.discardbutton = Button(image = self.NEpositionpic_fromdeck, command = None)
					self.discardbutton.grid(row=3, column=3)
					self.usersturn = False
					self.robot(self.NEpositionpic_fromdeck)

				if self.NE_cardfromdeck == False: 
					self.discardbutton = Button(image = self.NEpositionpic_frombot, command = None)
					self.discardbutton.grid(row=3,column =3)
					self.usersturn = False
					self.robot(self.NEpositionpic_frombot)

				self.NE_cardfromdeck = True 
				self.NEpositionpic_fromdeck = self.lastcarddealt

			elif self.discardcamefromdeck == False: 
				self.button = Button(image = self.dict_faceuppic_to_facedownpic[self.robotdiscard], command = self.NE_card)	#(CCC)
				self.button.grid(row = 8, column = 2) 
		

				if self.NE_cardfromdeck ==True: 
					self.discardbutton = Button(image = self.NEpositionpic_fromdeck, command = None)
					self.discardbutton.grid(row=3, column=3)
					self.usersturn = False
					self.robot(self.NEpositionpic_fromdeck)

				if self.NE_cardfromdeck == False:  
					self.discardbutton = Button(image = self.NEpositionpic_frombot, command = None)
					self.discardbutton.grid(row=3,column =3)
					self.usersturn = False
					self.robot(self.NEpositionpic_frombot)

				self.NE_cardfromdeck = False 
				self.NEpositionpic_frombot = self.robotdiscard
		else:
			print("Not your turn!")

	def SW_card(self):
		
		if self.usersturn == True:

			if self.discardcamefromdeck == True: 
				self.button = Button(image= self.lastcarddealt, command= self.SW_card)
				self.button.grid(row = 9, column = 1) 
				 
				if self.SW_cardfromdeck == True: 
					self.discardbutton = Button(image = self.SWpositionpic_fromdeck, command = None)
					self.discardbutton.grid(row=3, column=3)
					self.usersturn = False
					self.robot(self.SWpositionpic_fromdeck) 
					
				if self.SW_cardfromdeck == False: 
					self.discardbutton = Button(image = self.SWpositionpic_frombot, command = None)
					self.discardbutton.grid(row=3,column =3)
					self.usersturn = False
					self.robot(self.SWpositionpic_frombot)
					
				self.SW_cardfromdeck = True
				self.SWpositionpic_fromdeck = self.lastcarddealt  

			elif self.discardcamefromdeck == False: 
				self.button = Button(image = self.robotdiscard, command = self.SW_card)
				self.button.grid(row = 9, column = 1) 
				self.currentthirdcardcamefrompile = False  

				if self.SW_cardfromdeck == True: 
					self.discardbutton = Button(image = self.SWpositionpic_fromdeck, command = None)
					self.discardbutton.grid(row=3, column=3)
					self.usersturn = False
					self.robot(self.SWpositionpic_fromdeck) 
					
				if self.SW_cardfromdeck == False: 
					self.discardbutton = Button(image = self.SWpositionpic_frombot, command = None)
					self.discardbutton.grid(row=3,column =3)
					self.usersturn = False
					self.robot(self.SWpositionpic_frombot)
					
				self.SW_cardfromdeck = False 
				self.SWpositionpic_frombot = self.robotdiscard	
		else:
			print("Not your turn!")
			
	def SE_card(self):

		if self.usersturn == True:

			if self.discardcamefromdeck == True:  
				self.button = Button(image= self.lastcarddealt, command= self.SE_card)
				self.button.grid(row = 9, column = 2)
			
				if self.SE_cardfromdeck == True:  
					self.discardbutton = Button(image = self.SEpositionpic_fromdeck, command = None)
					self.discardbutton.grid(row=3, column=3)
					self.robot(self.SEpositionpic_fromdeck)
				if self.SE_cardfromdeck == False: 
					self.discardbutton = Button(image = self.SWpositionpic_frombot, command = None)
					self.discardbutton.grid(row=3,column =3)
					self.robot(self.SEpositionpic_frombot)

				self.SE_cardfromdeck = True
				self.SEpositionpic_fromdeck = self.lastcarddealt

			elif self.discardcamefromdeck == False: 
				self.button = Button(image = self.robotdiscard, command = self.SE_card)
				self.button.grid(row = 9, column = 2)
				
				if self.SE_cardfromdeck == True: 
					self.discardbutton = Button(image = self.SEpositionpic_fromdeck, command = None)
					self.discardbutton.grid(row=3, column=3)
					self.robot(self.SEpositionpic_fromdeck)  
				if self.SE_cardfromdeck == False: 
					self.discardbutton = Button(image = self.SWpositionpic_frombot, command = None)
					self.robot(self.SEpositionpic_frombot)

				self.SE_cardfromdeck = False
				self.SWpositionpic_frombot = self.robotdiscard
		else:
			print("Not your turn!")

	# THREE MORE BUTTONS: TWO MORE CHOICES & TO START A NEW ROUND

	# TWO MORE CHOICES 
	# User can reject the card so that it becomes robot's turn.  User can knock, which will force the round to end and points tallied. 


	def reject(self):
		if self.usersturn == True:
			self.robot(self.lastcarddealt)
			
			self.usersturn = False
		else:
			print("Not your turn!")

	def knock(self):
		if self.usersturn == True:
			print("knock knock!")

			self.humanscorelist = []

			# ROBOT SCORE:

			# Sum 'em all up  all in one line, easy breezy:  
			self.robotscore = self.position1value + self.position2value + self.position3value + self.position4value

			# Display image of two hidden cards (flip 'em'):

			self.button7 = Button(image= self.dict_facedownpic_to_faceuppic[self.dict_faceuppic_to_facedownpic[self.dealtcard7]], command = None ) #(CCC) #(BBB)
			self.button7.grid(row = 2, column = 1)

			self.button8 = Button(image= self.dict_facedownpic_to_faceuppic[self.dict_faceuppic_to_facedownpic[self.dealtcard8]], command = None ) #(CCC) #(BBB)
			self.button8.grid(row = 2, column = 2)

			# USER SCORE: 

			 
			if self.NW_cardfromdeck == True:
			# Display images (flip it)!
				self.User_NW_button = Button(image= self.dict_facedownpic_to_faceuppic[self.dict_faceuppic_to_facedownpic[self.NWpositionpic_fromdeck]], command= None)   #(CCC) #(BBB)
				self.User_NW_button.grid(row = 8, column = 1)
			# Determine and tally value!
				self.humanscorelist.append(self.dict_faceuppics_to_values[self.NWpositionpic_fromdeck])  # (AAA)
			elif self.NW_cardfromdeck == False:
			# Display images (flip it)! 
				self.User_NW_button = Button(image= self.dict_facedownpic_to_faceuppic[self.dict_faceuppic_to_facedownpic[self.NWpositionpic_frombot]], command= None)   #(CCC) #(BBB)
				self.User_NW_button.grid(row = 8, column = 1)
			# Determine and tally value!	
				self.humanscorelist.append(self.dict_faceuppics_to_values[self.NWpositionpic_frombot]) 	# (AAA)

			# Ditto
			if self.NE_cardfromdeck == True: 
				self.User_NE_button = Button(image= self.dict_facedownpic_to_faceuppic[self.dict_faceuppic_to_facedownpic[self.NEpositionpic_fromdeck]], command = None)  #(CCC) #(BBB)
				self.User_NE_button.grid(row = 8, column = 2)
				self.humanscorelist.append(self.dict_faceuppics_to_values[self.NEpositionpic_fromdeck])
			elif self.NE_cardfromdeck == False: 
				self.User_NE_button = Button(image= self.dict_facedownpic_to_faceuppic[self.dict_faceuppic_to_facedownpic[self.NEpositionpic_frombot]], command = None)  #(CCC) #(BBB)
				self.User_NE_button.grid(row = 8, column = 2)
				self.humanscorelist.append(self.dict_faceuppics_to_values[self.NEpositionpic_frombot])	# (AAA)

			# Determine and tally Card value! 
			if self.SE_cardfromdeck == True: 
				self.humanscorelist.append(self.dict_faceuppics_to_values[self.SWpositionpic_fromdeck])	# (AAA)
			if self.SE_cardfromdeck == False:
				self.humanscorelist.append(self.dict_faceuppics_to_values[self.SWpositionpic_frombot])	# (AAA)

			# Ditto
			if self.SW_cardfromdeck == True: 
				self.humanscorelist.append(self.dict_faceuppics_to_values[self.SEpositionpic_fromdeck])	# (AAA)
			if self.SW_cardfromdeck == False:
				self.humanscorelist.append(self.dict_faceuppics_to_values[self.SWpositionpic_frombot])	# (AAA)

			# Sum it up: 
			self.humanscore = sum(self.humanscorelist)
			# Display scores:
			self.robotscorecard()
			self.humanscorecard()

			self.candeclarenewround = True
			self.usersturn = False

		else:
			print("Not your turn!")

	# TO START A NEW ROUND:
	# Once done glorifying in their win or wallowing in their loss, user presses this to start next round and tally round to game scoreboard. 
	# This function will notify user when rounds are finished and will tally up total score at the end.     

	def newround(self):
		if self.candeclarenewround == False:
			print("You gotta knock, first.") 
		if self.candeclarenewround == True and self.row <=18:
			self.w = Label(text="               " + str(self.roww) + ".  "  + str(self.robotscore)) 
			self.w.grid(row = self.row, column = 10 )
			self.totalrobotscore.append(self.robotscore)
			self.w = Label(text=" " + str(self.roww) + ".  " + str(self.humanscore))  
			self.w.grid(row = self.row, column = 8 )
			self.totalhumanscore.append(self.humanscore)
			self.row += 1
			self.roww += 1
			self.nwrnd = shuffle(self)
			
		elif self.candeclarenewround == True and self.row >= 19:
			print("Game over!")

			self.w = Label(text="               " + str(self.roww) + ".  "  + str(self.robotscore)) 
			self.w.grid(row = self.row, column = 10 )
			self.totalrobotscore.append(self.robotscore)
			self.w = Label(text=" " + str(self.roww) + ".  " + str(self.humanscore))  
			self.w.grid(row = self.row, column = 8 )
			self.totalhumanscore.append(self.humanscore)

			self.button12 = Button(text = "Game Over!", command = self.newround, fg='red')
			self.button12.grid(row = 11, column = 4)

			self.w = Label(text= "Total Human Score: " + str(sum(self.totalhumanscore)))
			self.w.grid(row = 22,  column = 8 )
			self.w = Label(text= "Total Robot Score: " + str(sum(self.totalrobotscore))) 
			self.w.grid(row = 22, column = 10 )


			if sum(self.totalhumanscore) < sum(self.totalrobotscore):
				self.w = Label(text= "You win!")
				self.w.grid(row = 24,  column = 9 )
			if sum(self.totalhumanscore) > sum(self.totalrobotscore):
				self.w = Label(text= "Robot wins!")
				self.w.grid(row = 24,  column = 9 )
			if sum(self.totalhumanscore) == sum(self.totalrobotscore):
				self.w = Label(text= "Tie!")
				self.w.grid(row = 24,  column = 9 )

	# Logical thought process of robot opponent. All future strategy improvements on robot's strategy would be bundled here.

	# User passes "humandiscard" for robot to asses decision. It's an image, but dictionary can retrieve its value. 

	def robot(self, humandiscard):
		def robotmove():
			
			largestcard = max(self.position1value, self.position2value)
			if self.dict_faceuppics_to_values[humandiscard] < largestcard:											# (AAA)

				print("I choose to swap for your discard!")
				self.discardcamefromdeck = False

				if self.position1value > self.position2value: 
					# CREATE POSITION1 CARD IN ROBOT'S HAND:
					self.newbutton5 = Button(image= humandiscard, command= None)
					self.newbutton5.grid(row=1, column = 1)
					# CREATES CARD IN DISCARD PILE:  
					self.robotdiscard = self.position1pic
					self.discardbutton = Button(image = self.robotdiscard, command = None)
					self.discardbutton.grid(row = 3, column = 3)
					# MAKES NOTE FOR FUTURE MOVES:
					self.position1value = self.dict_faceuppics_to_values[humandiscard]								# (AAA)
					self.position1pic = humandiscard
					# Allows human to move:
					self.usersturn = True
					print("Your turn.") 
						
				elif self.position1value <= self.position2value:
					self.newbutton5 = Button(image= humandiscard, command= None)
					self.newbutton5.grid(row=1, column = 2)

					self.robotdiscard = self.position2pic
					self.discardbutton = Button(image = self.robotdiscard, command = None)
					self.discardbutton.grid(row = 3, column = 3)
					
					self.position2value = self.dict_faceuppics_to_values[humandiscard]									# (AAA)
					self.position2pic = humandiscard

					self.usersturn = True
					print("Your turn.") 
						
			else:
				print("I choose to hit the deck.")
				self.deckforrobots()
				if self.dict_faceuppics_to_values[self.lastcarddealt] < largestcard:									# (AAA)
					print("Now, I will swap cards.")
					
					def robotmove2():
						
						if self.position1value > self.position2value: 
							self.newbutton5 = Button(image= self.lastcarddealt, command= None)
							self.newbutton5.grid(row=1, column = 1)

							self.robotdiscard = self.position1pic
							self.position1value = self.dict_faceuppics_to_values[self.lastcarddealt]					# (AAA)
							self.position1pic = self.lastcarddealt			

							self.discardbutton = Button(image = self.robotdiscard, command = None)
							self.discardbutton.grid(row = 3, column = 3)

							self.discardcamefromdeck = False
							self.usersturn = True
							print("Your turn",self.usersturn)
						

						elif self.position1value <= self.position2value:
							self.newbutton5 = Button(image= self.lastcarddealt, command= None)
							self.newbutton5.grid(row=1, column = 2)

							self.robotdiscard = self.position2pic
							self.position2value = self.dict_faceuppics_to_values[self.lastcarddealt]						# (AAA)
							self.position2pic = self.lastcarddealt 

							self.discardbutton = Button(image = self.robotdiscard, command = None)
							self.discardbutton.grid(row = 3, column = 3)
							
							self.discardcamefromdeck = False 
							self.usersturn = True
							print("Your turn",self.usersturn)

					root.after(1500, robotmove2)

				else:
					print("I reject this card. Your turn.") 

			self.usersturn = True
			self.havenothitthisturn = True

		# Adds time delay of robot's move, to make more realistic.  
		root.after(1500, robotmove)

class Game(Frame):
    
	def __init__(self, fucktwitmaster =None):
		Frame.__init__(self, fucktwitmaster)
		
		self.pack()
		self.createWidgets()

		self.master.configure(background='black') 

	def startgame(self):

		self.my_gui = Round()
		
	def createWidgets(self):
		self.button5 = Button(text= "play", command= self.startgame)
		self.button5.grid(row = 1, column=1)
    
radish = Tk()
radish.geometry("400x200")
radish['bg']='green'

app = Game(fucktwitmaster = radish)
app.mainloop()
root.mainloop()


