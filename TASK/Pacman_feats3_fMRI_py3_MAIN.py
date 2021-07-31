#!/usr/bin/ python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Fri 12 May 14:15:55 2017
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle, uniform
import os  # handy system and path functions
import sys # to get file system encoding
from pyglet.window import key # to detect key state, whether key is held down, to move slider on key hold
import pyglet
import pandas as pd
from scipy import stats
from scipy.stats import norm
from random import uniform, random, randint
from psychopy.hardware.emulator import launchScan
import csv
import glob




# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'PacMan_3feat_fMRI_MAIN.py'
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['startblock'] = 1

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

    
MB=0.0
PO=0
file_list = glob.glob("/Users/asuka-ya/Desktop/Program/Pacman_fMRI/data/%s_PacMan_3feat_fMRI_MAIN.py*.csv" %(expInfo['participant']))
if len(file_list) > 0:
    #thisExp0 = csv.DictReader(u'data/%s_PacMan_3feat_fMRI_MAIN.py*.csv'%(expInfo['participant']))
    #thisExp0 = data.importConditions(u'data/1_PacMan_3feat_fMRI_MAIN.py_2018_Aug_23_1350.csv')
    #addOtherData(u'data/%s_PacMan_3feat_fMRI_MAIN.py*.csv'%(expInfo['participant']),fileCollisionMethod=filename)
    #thisExp.update(thisExp0)
    #file_list = glob.glob("/Users/asuka-ya/Desktop/Program/Pacman_fMRI/data/%s_PacMan_3feat_fMRI_MAIN.py*.csv" %(expInfo['participant']))
    data_frames = [pd.read_csv(file) for file in file_list]
    thisExp0 = pd.concat(data_frames)
    MB0=thisExp0['MoneyBlock']
    MB = sum([row if str(row) != 'nan' else 0 for k, row in enumerate(MB0)])
    PO0=thisExp0['PointsTrial']
    PO = sum([row if str(row) != 'nan' else 0 for k, row in enumerate(PO0)])
    BL0=thisExp0['block']
    expInfo['startblock'] = int(BL0[len(BL0)-1])
    #thisExp0.to_csv(filename, mode='a', header=False)
    #thisExp0.nextEntry()
    
#expInfo['phase2_loop.thisTrialN']=(expInfo['startblock']-1)*80
    
# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)

#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
endSmart = False  # flag for 'escape' or other condition => quit the exp

# settings for launchScan:
MR_settings = { 
    'TR': 1.000,     # duration (sec) per whole-brain volume
    'volumes': 300,  # number of whole-brain 3D volumes per scanning run
    'sync': 't', 	 # character to use as the sync timing event; assumed to come at start of a volume
    'skip': 0,      # number of volumes lacking a sync pulse at start of scan (for T1 stabilization)
    'sound': True    # in test mode: play a tone as a reminder of scanner noise
    }
infoDlg = gui.DlgFromDict(MR_settings, title='fMRI parameters', order=['TR','volumes'])
if not infoDlg.OK: core.quit()

# Start Code - component code to be run before the window creation

#### MAKE STIMULI ####
theta_left = np.linspace(0,2*3.14,80) 

x = np.cos(theta_left)
y = np.sin(theta_left)

# build the list of points 
ext_left = list() 
ext_left.append((0,0)) # add 0 point
# loop over x,y, add each point to list 
for itheta in range(len(theta_left)): 
    ext_left.append((x[itheta],y[itheta])) 

#--

theta_right = np.linspace(2.75*3.14,1.25*3.14,80) 

x = np.cos(theta_right)
y = np.sin(theta_right)

# build the list of points 
ext_right = list() 
ext_right.append((0,0)) # add 0 point
# loop over x,y, add each point to list 
for itheta in range(len(theta_right)): 
    ext_right.append((x[itheta],y[itheta])) 

# build eyeball interior points 
theta_left=np.linspace(0,2*3.14,30) 
x = 0.1*np.cos(theta_left)+0.2 
y = 0.1*np.sin(theta_left)+0.7

inter_left = list() 
for itheta in range(len(theta_left)): 
    inter_left.append((x[itheta],y[itheta])) 
inter_left.append((x[0],y[0]))

#----------------------------------
# build stripes

#draw mouth 

theta_left = np.linspace(-0.25*3.14,0.25*3.14,40) 

x =1.2* np.cos(theta_left)
y =1.2* np.sin(theta_left)

# build the list of points 
ext_mouth = list() 
ext_mouth.append((0,0)) # add 0 point
# loop over x,y, add each point to list 
for itheta in range(len(theta_left)): 
    ext_mouth.append((x[itheta],y[itheta])) 



# stripes vertices
theta_left=np.linspace(0,2*3.14,30) 
x = np.cos(theta_left) 
y = np.sin(theta_left)

x1_stripes_vert = np.linspace(min(x),max(x),30) 
alph1 =  np.arccos(x1_stripes_vert)
y1_up_stripes_vert =np.sin(alph1)
y1_dwn_stripes_vert = -np.sin(alph1)

jj = 0

stripes_vert = list() 
while jj+2 <= len(x1_stripes_vert): 
    stripes_vert.append((x1_stripes_vert[jj],y1_up_stripes_vert[jj])) 
    stripes_vert.append((x1_stripes_vert[jj+1],y1_up_stripes_vert[jj+1])) 
    stripes_vert.append((x1_stripes_vert[jj+1],y1_dwn_stripes_vert[jj+1])) 
    stripes_vert.append((x1_stripes_vert[jj],y1_dwn_stripes_vert[jj])) 
    jj = jj + 2


theta_right=np.linspace(0,2*3.14,30) 
x = 0.1*np.cos(theta_right)-0.2 
y = 0.1*np.sin(theta_right)+0.7


inter_right = list() 
for itheta in range(len(theta_right)): 
    inter_right.append((x[itheta],y[itheta])) 
inter_right.append((x[0],y[0]))

keyState = key.KeyStateHandler()



# Setup the Window
win = visual.Window(size=(1440, 900), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=u'black', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
win.winHandle.push_handlers(keyState)

# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#Instalize components for Routine Introduction
IntroductionClock =core.Clock()

IntroductionText =visual.TextStim(win,text='Welcome to this experiment. \n\n\nPress space to find out what the task involves!',
    units='cm', color='white', pos=(0,2.0),  height=1, wrapWidth=30)

# Initialize components for ITI
ITIClock =core.Clock()

# Instructions
Instructions1Clock =core.Clock()

#Instructions2Text =visual.TextStim(win,text=u"In this task you will be shown various members of the PAC-MAN family.\nThey can be distinguished by some# particular features:\n\n 1. Color\n 2. Orientation of their stripes\n3. Direction of their mouths\n\nEvery PAC-MAN prefers eating a particular type of fruit/vegetable. \nYou will be asked to indicate which fruit one type of PAC-MAN will prefer.",
#    units='cm', color='white', pos=(0,2.0),  height=1, wrapWidth=30)

#Instructions2Text1 =visual.TextStim(win,text=u"The option you choose (selected using keys left \u2190 and right \u2192 ) will be highlighted by a square. \n\n If the square surrounding your chosen option is GREEN, you were correct and you receive 1 point. If the square is RED, you were incorrect and you receive no points. If you don't select any alternative within 4 seconds the trial will be MISSED. \n\nYou will be presented with blocks in which 2 of the features are relevant to discover the iation between PACMAN and FRUIT. If you have correct answers in a row the block will be finished. The number of required correct answers to terminate the block may be between 8-12 trials  \n\n\nPress the space bar to start a practice block.",
#    units='cm', color='white', pos=(0,2.0),  height=1, wrapWidth=30)

Instructions3Text =visual.TextStim(win,text=u"Ready to start the experiment.",
    units='cm', color='white', pos=(0,2.0),  height=1, wrapWidth=30)
    
InstructionsCompar =visual.TextStim(win,text=u"Does             prefer? \n\n              or",units='cm', color='white', pos=(0,0),  height=3, wrapWidth=30, alignHoriz='center',alignVert='center')

#ghost_instructions = visual.ImageStim(win, image='pac_ghosts2.png', pos=(0.6, -0.6))

#QuestionCategory =visual.TextStim(win,text=u"Is this fruit preferred by the following PAC-MAN? ",units='cm', color='white', pos=(0,8.0),  height=1, wrapWidth=30, alignHoriz='center',alignVert='center')

#These images won't be used
#ghost_display1 = visual.ImageStim(win, image='orange.png', pos=(0, 0))
#ghost_display2 = visual.ImageStim(win, image='grapes.png', pos=(0, 0))
#ghost_display3 = visual.ImageStim(win, image='tomato.png', pos=(0, 0))
#ghost_display4 = visual.ImageStim(win, image='pear.png', pos=(0, 0))
#ghost_display5 = visual.ImageStim(win, image='cherry.png', pos=(0, 0))
#ghost_display6 = visual.ImageStim(win, image='banana.png', pos=(0, 0))
#ghost_display7 = visual.ImageStim(win, image='kiwi.png', pos=(0, 0))
#ghost_display8 = visual.ImageStim(win, image='avocado.png', pos=(0, 0))
#ghost_display9 = visual.ImageStim(win, image='watermelon.png', pos=(0, 0))
#ghost_display10 = visual.ImageStim(win, image='pine.png', pos=(0, 0))
#ghost_display11 = visual.ImageStim(win, image='strawberry.png', pos=(0, 0))
#ghost_display12 = visual.ImageStim(win, image='apple_g.png', pos=(0, 0))
#ghost_display13 = visual.ImageStim(win, image='lemon.png', pos=(0, 0))
#ghost_display14 = visual.ImageStim(win, image='peach.png', pos=(0, 0))


ShapeLeft1 = visual.ShapeStim(win, vertices=ext_left, fillColor=[1,-1,-1], lineWidth=0, size=100, pos=(0,0), units='pix')
ShapeLeft2 = visual.ShapeStim(win, vertices=inter_left, fillColor='black', lineWidth=0, size=100, pos=(0,0), units='pix')

#time_question = 1

# Starting Time point (respect to the   for pacman appearance and options (fruits) appearance on screen).
init_wait=10.0
final_wait=6.0
time_pacman=1.0
time_options=3.0
time_miss=6.0 
time_trial=8.0
time_uncert=0.00115

#Money parameter
A=150


#----------------

#Generate shape Stim for Stripes
#test if we can put a for cicle here to automatize
arrow=[]
jj = 0
i=0

ShapeMouth1 = visual.ShapeStim(win, vertices=ext_mouth, fillColor='black', lineWidth=0, size=100, pos=(0,0), units='pix')
while jj + 3 <= len(stripes_vert): 
    arrowVert = [stripes_vert[jj],stripes_vert[jj+1],stripes_vert[jj+2],stripes_vert[jj+3]]
    arrow_t = visual.ShapeStim(win, vertices=arrowVert, fillColor=[-0.5,-1,-1], size=100, lineColor=[-0.5,-1,-1],units='pix',lineColorSpace='rgb',fillColorSpace='rgb')
    arrow.append(arrow_t)
    jj = jj+4
    i=1


#---------------------------------
#Options IMAGE 1 or IMAGE 2
names_list_pract = ['carrot.png','hotPepper.png']
names_list = ['orange.png','grapes.png','tomato.png','pear.png','cherry.png','banana.png','kiwi.png','avocado.png','watermelon.png','pine.png','strawberry.png','apple_g.png','lemon.png','peach.png','coconut.png','brocoli.png','eggplant.png','maize.png',
              'grapes.png','tomato.png','pear.png','avocado.png','watermelon.png','pine.png','strawberry.png','cherry.png','banana.png','kiwi.png','apple_g.png','lemon.png','peach.png','coconut.png','brocoli.png','eggplant.png','maize.png','orange.png',
              'tomato.png','pear.png','cherry.png','banana.png','kiwi.png','strawberry.png','apple_g.png','lemon.png','peach.png','coconut.png','avocado.png','watermelon.png','pine.png','brocoli.png','eggplant.png','maize.png','orange.png','grapes.png'
              'apple_g.png','lemon.png','peach.png','coconut.png','avocado.png','watermelon.png','pine.png','brocoli.png','eggplant.png','maize.png','orange.png','tomato.png','pear.png','cherry.png','banana.png','kiwi.png','strawberry.png','grapes.png',
              'lemon.png','peach.png','avocado.png','watermelon.png','pine.png','brocoli.png','maize.png','orange.png','pear.png','cherry.png','banana.png','kiwi.png','strawberry.png','grapes.png']

#opt_left = visual.ImageStim(win, image='orange.png', pos=(-0.46, -0.5), size = (0.2,0.3),units='norm')
#opt_right = visual.ImageStim(win, image='grapes.png', pos=(0.46, -0.5), size = (0.2,0.3),units='norm')
opt_left = visual.ImageStim(win, image='orange.png', pos=[-300, -200], size = (256*0.7,240*0.7),units='pix')
opt_right = visual.ImageStim(win, image='grapes.png', pos=[300, -200], size = (256*0.7,240*0.7),units='pix')
#---------------------------------

FixationCross =visual.TextStim(win,text="+",
    units='pix', color='white', pos=(0, 0), height=50, wrapWidth=80)
    

OutcomeMissText = visual.TextStim(win=win, ori=0, name='guess_txt', text=u'Too Slow!', font=u'Arial', pos=[0, 0], height=0.5, wrapWidth=None, color=u'white', colorSpace=u'rgb', opacity=1, depth=0.0)

OutcomeBoxLeft = visual.Rect(win=win,
    name='OutcomeBoxLeft', units='pix',
    width=[200, 200][0], height=[200, 200][1],
    ori=0, pos=[-300, -200],
    lineWidth=5, lineColor=u'yellow',
    lineColorSpace=u'rgb',
    fillColor=None, fillColorSpace=u'rgb',
    opacity=1, depth=-4.0, interpolate=True)
    
OutcomeBoxRight = visual.Rect(win=win,
    name='OutcomeBoxRight', units='pix',
    width=[200, 200][0], height=[200, 200][1],
    ori=0, pos=[300, -200],
    lineWidth=5, lineColor=u'yellow',
    lineColorSpace=u'rgb',
    fillColor=None, fillColorSpace=u'rgb',
    opacity=1, depth=-4.0, interpolate=True)

QuestionClock=core.Clock()
ChoiceClock=core.Clock()
FeedbackClock=core.Clock()

OutcomeBoxLeftCorrect = visual.Rect(win=win,
    name='OutcomeBoxLeft', units='pix',
    width=[200, 200][0], height=[200, 200][1],
    ori=0, pos=[-300, -200],
    lineWidth=5, lineColor=[-1,1,-1],
    lineColorSpace=u'rgb',
    fillColor=None, fillColorSpace=u'rgb',
    opacity=1, depth=-4.0, interpolate=True)
    
OutcomeBoxRightCorrect = visual.Rect(win=win,
    name='OutcomeBoxRight', units='pix',
    width=[200, 200][0], height=[200, 200][1],
    ori=0, pos=[300, -200],
    lineWidth=5, lineColor=[-1,1,-1],
    lineColorSpace=u'rgb',
    fillColor=None, fillColorSpace=u'rgb',
    opacity=1, depth=-4.0, interpolate=True)

OutcomeBoxLeftError = visual.Rect(win=win,
    name='OutcomeBoxLeft', units='pix',
    width=[200, 200][0], height=[200, 200][1],
    ori=0, pos=[-300, -200],
    lineWidth=5, lineColor=[1,-1,-1],
    lineColorSpace=u'rgb',
    fillColor=None, fillColorSpace=u'rgb',
    opacity=1, depth=-4.0, interpolate=True)
    
OutcomeBoxRightError = visual.Rect(win=win,
    name='OutcomeBoxRight', units='pix',
    width=[200, 200][0], height=[200, 200][1],
    ori=0, pos=[300, -200],
    lineWidth=5, lineColor=[1,-1,-1],
    lineColorSpace=u'rgb',
    fillColor=None, fillColorSpace=u'rgb',
    opacity=1, depth=-4.0, interpolate=True)
    
# Initialize components for Confidence trials
ConfidenceClock = core.Clock()
Confidence1 = visual.RatingScale(win=win, name='Confidence', marker=u'triangle', markerColor=u'orange', leftKeys='b', rightKeys='y', size=0.6,
    pos=[0.0, -0.8], low=0, high=1, precision=100, labels=[u'Wrong', u'Correct'], scale=u'',
    markerStart = u'0.5', tickHeight=u'0', showAccept=False, acceptKeys=[u'down'])

GuessingText = visual.TextStim(win=win, ori=0, name='guess_txt', text=u'Guessing', font=u'Arial', pos=[0, -0.835], height=0.045, wrapWidth=None, color=u'white', colorSpace=u'rgb', opacity=1, depth=0.0)


# Instalize components for "Rest"
RestClock = core.Clock()
RestText = visual.TextStim(win=win, ori=0, name='rest_prompt_txt', text=u'Great! \nYou have earned \u00A30 so far! Now take a rest and press spacebar when you are ready to begin the next block.', font=u'Arial', pos=[0, 0], height=0.08, wrapWidth=None, color=u'white', colorSpace=u'rgb', opacity=1, depth=0.0)

# Initialize components for "Break"
BreakClock = core.Clock()
BreakText = visual.TextStim(win=win, ori=0, name='break_txt', text=u'Great! \nYou have earned \u00A30 so far! You are halfway through this task. \n\nPlease contact the experimenter.', font=u'Arial', pos=[0, 0], height=0.08, wrapWidth=None, color=u'white', colorSpace=u'rgb', opacity=1, depth=0.0)
    
# Initialize components for "Thank You"
ThankYouClock = core.Clock()
ThankYouText = visual.TextStim(win=win, ori=0, name='rest_prompt_txt', text=u'You have now completed this experiment. \nYou have earned 0 points! Thank you for your participation. Please inform the experimenter that you have finished.', font=u'Arial', pos=[0, 0], height=0.08, wrapWidth=None, color=u'white', colorSpace=u'rgb', opacity=1, depth=-6.0)
ThankYouBox = visual.Rect(win=win,
    name='ThankYouBox', units='pix',
    width=[1000, 1000][0], height=[800, 800][1],
    pos=[0, 0],
    lineWidth=5, lineColor=[1,-1,-1],
    lineColorSpace=u'rgb',
    fillColor=[-1,-1,-1], fillColorSpace=u'rgb',
    opacity=0.9, depth=-5.0, interpolate=True)


# for fMRI
# summary of run timing, for each key press:
output = u'vol    onset key\n'
for i in range(-1 * MR_settings['skip'], 0):
    output += u'%d prescan skip (no sync)\n' % i

counter = visual.TextStim(win, height=.05, pos=(0,0), color=win.rgb+0.5)
output += u"  0    0.000 sync  [Start of scanning run, vol 0]\n"



##############################################
########## START EXPERIMENT (MAIN) ###########
##############################################


### Main Experiment

#------Prepare to start Routine "Instructions"-------
t = 0
Instructions1Clock.reset()  # clock

frameN = -1
# update component parameters for each repeat
Instructions1Response = event.BuilderKeyResponse()  # create an object of type KeyResponse
Instructions1Response.status = NOT_STARTED
# keep track of which components have finished
Instructions1Components = []
Instructions1Components.append(Instructions3Text)
Instructions1Components.append(Instructions1Response)
for thisComponent in Instructions1Components:
	if hasattr(thisComponent, 'status'):
		thisComponent.status = NOT_STARTED


#-------Start Routine "Instructions"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
	# get current time
	t = Instructions1Clock.getTime()
	frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
	# update/draw components on each frame

	# *Instructions3Text* updates
	if t >= 0.0 and Instructions3Text.status == NOT_STARTED:
		# keep track of start time/frame for later
		Instructions3Text.tStart = t  # underestimates by a little under one frame
		Instructions3Text.frameNStart = frameN  # exact frame index
		Instructions3Text.setAutoDraw(True)

	# *Instructions1Response* updates
	if t >= 0 and Instructions1Response.status == NOT_STARTED:
		# keep track of start time/frame for later
		Instructions1Response.tStart = t  # underestimates by a little under one frame
		Instructions1Response.frameNStart = frameN  # exact frame index
		Instructions1Response.status = STARTED
		# keyboard checking is just starting
		Instructions1Response.clock.reset()  # now t=0
		event.clearEvents(eventType='keyboard')
	if Instructions1Response.status == STARTED:
		theseKeys = event.getKeys(keyList=['space'])

		# check for quit:
		if "escape" in theseKeys:
			endExpNow = True
		if len(theseKeys) > 0:  # at least one key was pressed
			Instructions1Response.keys = theseKeys[-1]  # just the last key pressed
			Instructions1Response.rt = Instructions1Response.clock.getTime()
			# a response ends the routine
			continueRoutine = False

	# check if all components have finished
	if not continueRoutine:  # a component has requested a forced-end of Routine
		routineTimer.reset()  # if we abort early the non-slip timer needs reset
		break
	continueRoutine = False  # will revert to True if at least one component still running
	for thisComponent in Instructions1Components:
		if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
			continueRoutine = True
			break  # at least one component has not yet finished

	# check for quit (the Esc key)
	if endExpNow or event.getKeys(keyList=["escape"]):
		core.quit()

	# refresh the screen
	if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
		win.flip()
	else:  # this Routine was not non-slip safe so reset non-slip timer
		routineTimer.reset()

#-------Ending Routine "Instructions"-------
for thisComponent in Instructions1Components:
	if hasattr(thisComponent, "setAutoDraw"):
		thisComponent.setAutoDraw(False)
# check responses
if Instructions1Response.keys in ['', [], None]:  # No response was made
   Instructions1Response.keys=None

tri = pd.read_csv('trials_3feats_shift_frut_fMRI_3.csv')
idx = tri.loc[tri[u'block'] >= int(expInfo['startblock'])].index.values


# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method=u'sequential', extraInfo=expInfo, originPath=None,
	trialList=data.importConditions(u'trials_3feats_shift_frut_fMRI_%s.csv' % expInfo['participant'],selection=idx),
	seed=None, name='phase2_loop')
thisExp.addLoop(trials)
thisTrial = trials.trialList[0]

#thisExp['phase2_loop.thisTrialN']=(expInfo['startblock']-1)*80

if thisTrial != None:
	for paramName in thisTrial.keys():
		#exec(paramName + '= thisTrial.' + paramName)
		exec(paramName + '= thisTrial["{paramName}"]'.format(paramName=paramName))

# Set up trial counter
Trial = 0
points = PO
points_trial = 0
points_trial_vect = []


points_strike =0
ntrial=0
ntrial_block=0
ntrial_block_vect=[]

strike_max=[7,9,11]
achievedStrike=0

prev_block=block

# note: globalClock has been reset to 0.0 by launchScan()
vol = launchScan(win, MR_settings, globalClock=globalClock)
blockstart = globalClock.getTime()
# initial waiting time to avoid T1 saturation effects
#core.wait(init_wait)
ISI.start(init_wait)
ISI.complete()

for thisTrial in trials:
	trialstart = globalClock.getTime()
	currentLoop = trials
	if thisTrial != None:
		for paramName in thisTrial.keys():
			#exec(paramName + '= thisTrial.' + paramName)
			exec(paramName + '= thisTrial["{paramName}"]'.format(paramName=paramName))

	strike_max_use=strike_max[randint(0, 2)]

   # print ('str_max', str(strike_max_use))
   # print ('achStr', str(achievedStrike))
   # print ('StrCpunt', str(points_strike))
   # print ('Puerta', str(points_strike>strike_max_use | achievedStrike == 1))


	# In case we are in a correct strike we jump to the next block
	if points_strike>strike_max_use or achievedStrike == 1:
		if achievedStrike==0:
			achievedStrike=1
		if  prev_block==block:
			prev_block=block
			continue
		else:
			thisExp.addData('StrikeMax', points_strike)
			thisExp.addData('PointsTrial', points_trial)
			thisExp.addData('PointsAcc', points)
			thisExp.addData('MoneyBlock', A*(points_trial/ntrial_block) - (ntrial_block - 12)*1.5 )


			points_strike = 0
			achievedStrike = 0

	
	#------------BreakBlock Routine 
	if prev_block != block :    
		
		# final wait of 6 sec
		ISI.start(final_wait)
		ISI.complete()
		blockend = globalClock.getTime() - blockstart
		print(blockend)
		thisExp.addData('Block length', blockend)  
		thisExp.nextEntry()
		#------Prepare to start Routine "Rest"-------
		t = 0
		RestClock.reset()
		frameN = -1
		
		RestText.setText(text=u'You earned {0}Yen in this block ({1} points out of {2} trials).\nYou have earned {3} points so far! In the next block, the preferred fruits and relevant features will change.' .format(int(A*(points_trial/ntrial_block) - (ntrial_block - 12)*1.5), int(points_trial),int(ntrial_block),int(points)))


		ntrial_block_vect.append(ntrial_block)
		points_trial_vect.append(points_trial)
		#restart point count in this trial
		points_trial = 0
		ntrial_block = 0
		points_strike = 0


		# update component parameters for each repeat
		RestResponse = event.BuilderKeyResponse()
		RestResponse.status = NOT_STARTED
		# keep track of which components have finished
		RestComponents = []
		RestComponents.append(RestText)
		RestComponents.append(RestResponse)
		for thisComponent in RestComponents:
			if hasattr(thisComponent, 'status'):
				thisComponent.status = NOT_STARTED

		#-------Start Routine "Rest"-------
		continueRoutine = True
		while continueRoutine:
			t = RestClock.getTime()
			frameN = frameN + 1

			# *RestText* updates
			if t >= 0.0 and RestText.status == NOT_STARTED:
				RestText.tStart = t
				RestText.frameNStart = frameN
				RestText.setAutoDraw(True)

			# *RestResponse* updates # 30 seconds of rest
			if t >= 5.0 and RestResponse.status == NOT_STARTED: 
				RestResponse.tStart = t
				RestResponse.frameNStart = frameN
				RestResponse.status = STARTED
				RestResponse.clock.reset()
				event.clearEvents(eventType='keyboard')
			if RestResponse.status == STARTED:
				theseKeys = event.getKeys(keyList=['space'])
	
				# check for quit:
				if 'escape' in theseKeys:
					endExpNow = True
				if 'q' in theseKeys:
					endSmart = True
				if len(theseKeys) > 0:
					RestResponse.keys = theseKeys[-1]
					RestResponse.rt = RestResponse.clock.getTime()
					continueRoutine = False
		

			# check if all components have finished
			if not continueRoutine:
				routineTimer.reset()
				break
			continueRoutine = False
			for thisComponent in RestComponents:
				if hasattr(thisComponent, 'status') and thisComponent.status != FINISHED:
					continueRoutine = True
					break

			# check for quit (the Esc key)
			if endExpNow or event.getKeys(keyList=['escape']):
				core.quit()

			if endSmart or event.getKeys(keyList=['q']):
				endSmart = True
				break

			# refresh the screen
			if continueRoutine:
				win.flip()
			else:
				routineTimer.reset()
				
		if endSmart: 
			break
			
		#-------Ending Routine "Rest"-------
		for thisComponent in RestComponents:
			if hasattr(thisComponent, 'setAutoDraw'):
				thisComponent.setAutoDraw(False)
		# check responses
		if RestResponse.keys in ['', [], None]:
			RestResponse.keys = None
		# store data for MainStaircase (ExperimentHandler)
		if RestResponse.keys != None:
			thisExp.addData('RestTime', RestResponse.rt)  
			thisExp.nextEntry()


		# note: globalClock has been reset to 0.0 by launchScan()
		vol = launchScan(win, MR_settings, globalClock=globalClock)
		blockstart = globalClock.getTime()
		# initial waiting time to avoid T1 saturation effects
		#core.wait(init_wait)
		ISI.start(init_wait)
		ISI.complete()
		trialstart = globalClock.getTime()
				
	prev_block=block        

	if endSmart: 
		break
		
			
			
			
	#------Prepare to start Routine "Choice"-------
	t = 0
	ChoiceClock.reset()
	frameN = -1

   # SET THE PROPERTIES TO BE CHANGED EVERY TRIAL
	#ori1=ntrial%2 # Stripes orientation.For the tests.
	#ori_mouth1=ntrial%2 # Stripes orientation.For the tests.

	ShapeLeft1.setFillColor([-1+2*color1,1-2*color1, -1])
	#1. set Color
	#ShapeRight1.setFillColor([-1,color2,1])

	#2. set Size
	ShapeLeft1.setSize(size1*100+100)
	ShapeMouth1.setSize(size1*100+100)

	#4. set Mouth orientation
	ShapeMouth1.setOri(dir_mouth1*180)

	#Set stripes properties
	#3. set stripes orientation
	j = 0
	while j+1 <= len(arrow): 
		arrow[j].setSize(size1*100+100)
		arrow[j].setOri(ori1*90)
		#we have to leave the stripes in a darker color than the fill of the circle
		arrow[j].setFillColor([(-1+2*color1)*(1-1.5*color1),(1-2*color1)*(-0.5+1.5*color1), -1])
		arrow[j].setLineColor([(-1+2*color1)*(1-1.5*color1),(1-2*color1)*(-0.5+1.5*color1), -1])
		j = j+1

	# SET ORDER OF THE OPTION ORDER FOR THIS TRIAL 
	opt_left.setImage (names_list[DisplayClass1-1])
	opt_right.setImage (names_list[DisplayClass2-1])



	Trial += 1

	#ShapeLeft1.setSize(size1)
	#ShapeLeft2.setSize(size1)


	event.clearEvents(eventType='keyboard')
	KeyRespCal = event.BuilderKeyResponse()
	KeyRespCal.status = NOT_STARTED

	# keep track of which components have finished
	ChoiceComponents = []
	ChoiceComponents.append(FixationCross)
	ChoiceComponents.append(ShapeLeft1)
	ChoiceComponents.append(ShapeLeft2)
	ChoiceComponents.append(OutcomeBoxLeft)
	ChoiceComponents.append(OutcomeBoxRight)
	ChoiceComponents.append(opt_left)
	ChoiceComponents.append(opt_right)
	ChoiceComponents.append(ShapeMouth1)
	ChoiceComponents.append(arrow)

	for thisComponent in ChoiceComponents:
		if hasattr(thisComponent, 'status'):
			thisComponent.status = NOT_STARTED


	 #-------Start Routine "Choice"-------
	continueRoutine = True
	while continueRoutine:
		t = ChoiceClock.getTime()
		frameN = frameN + 1

		# *FixationCross* updates
		if t >= 0.0 and FixationCross.status == NOT_STARTED:
			crossstart = globalClock.getTime() - trialstart
			FixationCross.tStart = t
			FixationCross.frameNStart = frameN
			FixationCross.setAutoDraw(True)
			
		if t >= time_pacman and FixationCross.status == STARTED:
			pacmanstart = globalClock.getTime() - trialstart
			FixationCross.setAutoDraw(False)

		# *ShapeLeft2* updates
		if t >= time_pacman and ShapeLeft2.status == NOT_STARTED:
			ShapeLeft1.tStart = t
			ShapeLeft1.frameNStart = frameN
			ShapeLeft1.setAutoDraw(True)
			ShapeLeft2.tStart = t
			ShapeLeft2.frameNStart = frameN
			j = 0
			while j+1 <= len(arrow): 
				arrow[j].setAutoDraw(True)
				j = j+1	
		   # ShapeLeft2.setAutoDraw(True)
			ShapeMouth1.setAutoDraw(True)
			

		 # *options* updates
		if t >= time_options and opt_left.status == NOT_STARTED:
			optionstart = globalClock.getTime() - trialstart
			opt_left.setAutoDraw(True)
			opt_right.setAutoDraw(True)
   
		# *KeyRespCal* updates
		if t >= time_options and KeyRespCal.status == NOT_STARTED:
			event.clearEvents(eventType='keyboard')
			KeyRespCal.tStart = t
			KeyRespCal.frameNStart = frameN
			KeyRespCal.status = STARTED
			KeyRespCal.clock.reset()
			
		if KeyRespCal.status == STARTED:
			theseKeys = event.getKeys(keyList=['b', 'y'])

			# check for quit or missed trial:
			if 'escape' in theseKeys:
				endExpNow = True
			if 'q' in theseKeys:
				endSmart = True
			if len(theseKeys) > 0:
				KeyRespCal.keys = theseKeys[-1]
				KeyRespCal.rt = KeyRespCal.clock.getTime()
				continueRoutine = False
			if t>=time_miss:
				KeyRespCal.keys ='missed'
				KeyRespCal.rt = KeyRespCal.clock.getTime()
				continueRoutine = False

		# check if all components have finished
		if not continueRoutine:
			routineTimer.reset()
			break
		continueRoutine = False
		for thisComponent in ChoiceComponents:
			if hasattr(thisComponent, 'status') and thisComponent.status != FINISHED:
				continueRoutine = True
				break

		 # check for quit (the Esc key)
		if endExpNow or event.getKeys(keyList=['escape']):
			core.quit()
		if endSmart or event.getKeys(keyList=['q']):
			endSmart = True
			break

		# refresh the screen
		if continueRoutine:
			win.flip()
		else:
			routineTimer.reset()
	if endSmart: 
		break

	 #-------Ending Routine "Phase 2 Choice"-------
	for thisComponent in ChoiceComponents:
		if hasattr(thisComponent, 'setAutoDraw'):
			thisComponent.setAutoDraw(False)
			j = 0
			while j+1 <= len(arrow): 
				arrow[j].setAutoDraw(False)
				j = j+1
	
	# check responses
	if KeyRespCal.keys in ['', [], None]:
		KeyRespCal.keys = None

	# was no response the correct answer?!
	if KeyRespCal.keys == correct: 
		KeyRespCal.corr = 1  # correct non-response
		points += 1
		points_trial += 1
		points_strike +=1
	else: 
		KeyRespCal.corr = 0  # failed to respond (incorrectly)
		points_strike = 0

	# Store data for experiment:
	thisExp.addData('Correct', KeyRespCal.corr)
	thisExp.addData('Response', KeyRespCal.keys)
	if KeyRespCal.keys != None:
		thisExp.addData('RT', KeyRespCal.rt)

	# if conf_report==1:
# 		#------Prepare to start Routine "Confidence"-------
# 		t = 0
# 		ConfidenceClock.reset()
# 		frameN = -1
# 		Confidence1.reset()
# 
# 		 # keep track of which components have finished
# 		ConfComponents = []
# 		ConfComponents = []
# 		ConfComponents.append(FixationCross)
# 		ConfComponents.append(ShapeLeft1)
# 		ConfComponents.append(ShapeLeft2)
# #        ConfComponents.append(ShapeRight1)
# #        ConfComponents.append(ShapeRight2)
# 		ConfComponents.append(OutcomeBoxLeft)
# 		ConfComponents.append(OutcomeBoxRight)
# 		ConfComponents.append(Confidence1)
# 		ConfComponents.append(opt_left)
# 		ConfComponents.append(opt_right)
# 		ConfComponents.append(ShapeMouth1)
# 		ConfComponents.append(arrow)
# 		ConfComponents.append(GuessingText)
# 
# 		for thisComponent in ConfComponents:
# 			if hasattr(thisComponent, 'status'):
# 				thisComponent.status = NOT_STARTED
# 
# 	#-------Start Routine "Confidence"-------
# 		# continueRoutine = True
# 		while continueRoutine:
# 			t = ConfidenceClock.getTime()
# 			frameN = frameN + 1
# 
# 			# *FixationCross* updates
# 			if t >= 0.0 and FixationCross.status == NOT_STARTED:
# 				opt_left.setAutoDraw(True)
# 				opt_right.setAutoDraw(True)
# #                FixationCross.tStart = t
# #                FixationCross.frameNStart = frameN
# #                FixationCross.setAutoDraw(True)
# #    
# 			# *ShapeLeft1* updates
# 			if t >=0.0 and ShapeLeft1.status == NOT_STARTED:
# 				ShapeLeft1.tStart = t
# 				ShapeLeft1.frameNStart = frameN
# 				ShapeLeft1.setAutoDraw(True)
# 
# 			# *ShapeLeft2* updates
# 			if t >= 0.0 and ShapeLeft2.status == NOT_STARTED:
# 				ShapeLeft2.tStart = t
# 				ShapeLeft2.frameNStart = frameN
# 				j = 0
# 				while j+1 <= len(arrow): 
# 					arrow[j].setAutoDraw(True)
# 					j = j+1
# 		
# 				#ShapeLeft2.setAutoDraw(True)
# 				ShapeMouth1.setAutoDraw(True)
# 
# #            # *ShapeRight1* updates
# #            if t >= 0.0 and ShapeRight1.status == NOT_STARTED:
# #                ShapeRight1.tStart = t
# #                ShapeRight1.frameNStart = frameN
# #                ShapeRight1.setAutoDraw(True)
# #    
# #            # *ShapeRight2* updates
# #            if t >= 0.0 and ShapeRight2.status == NOT_STARTED:
# #                ShapeRight2.tStart = t
# #                ShapeRight2.frameNStart = frameN
# #                ShapeRight2.setAutoDraw(True)
# 
# 			# *OutcomeBoxLeft* updates
# 			if KeyRespCal.keys == 'b':
# 				if t >= 0.0 and OutcomeBoxLeft.status == NOT_STARTED:
# 					OutcomeBoxLeft.tStart = t
# 					OutcomeBoxLeft.frameNStart = frameN
# 					OutcomeBoxLeft.setAutoDraw(True)
# 	
# 			# *OutcomeBoxRight* updates
# 			if KeyRespCal.keys == 'y':
# 				if t >= 0.0 and OutcomeBoxRight.status == NOT_STARTED:
# 					OutcomeBoxRight.tStart = t
# 					OutcomeBoxRight.frameNStart = frameN
# 					OutcomeBoxRight.setAutoDraw(True)
# 
# 			# *MainRating* updates
# 			if t > 1.0:
# 				continueRoutine = Confidence1.noResponse
# 				while Confidence1.noResponse:
# 					Confidence1.draw()
# 					GuessingText.setAutoDraw(True)
# 					win.flip()
# 					hist = set(np.array(Confidence1.getHistory())[:, 0])
# 					if len(hist) < 2:
# 						Confidence1.noResponse = True
# 						Confidence1.status = 0
# 					if keyState[key.LEFT] == True and Confidence1.markerPlacedAt > 0.01:
# 						Confidence1.markerPlacedAt = Confidence1.markerPlacedAt - 0.02
# 						Confidence1.draw()
# 					elif keyState[key.LEFT] == True and Confidence1.markerPlacedAt == 0.01:
# 						Confidence1.markerPlacedAt = Confidence1.markerPlacedAt - 0.01
# 						Confidence1.draw()
# 					elif keyState[key.RIGHT] == True and Confidence1.markerPlacedAt < 0.99:
# 						Confidence1.markerPlacedAt = Confidence1.markerPlacedAt + 0.02
# 						Confidence1.draw()
# 					elif keyState[key.RIGHT] == True and Confidence1.markerPlacedAt == 0.99:
# 						Confidence1.markerPlacedAt = Confidence1.markerPlacedAt + 0.01
# 						Confidence1.draw()
# 				Confidence1.response = Confidence1.getRating()
# 				Confidence1.rt = Confidence1.getRT()
# 	
# 			 # check for quit (the Esc key)
# 			if endExpNow or event.getKeys(keyList=['escape']):
# 				core.quit()
# 			if endSmart or event.getKeys(keyList=['q']):
# 				endSmart = True
# 				break
# 	
# 			# refresh the screen
# 			if continueRoutine:
# 				win.flip()
# 			else:
# 				routineTimer.reset()
# 
# 		 #-------Ending Routine "Confidence"-------
# 		for thisComponent in ConfComponents:
# 			if hasattr(thisComponent, 'setAutoDraw'):
# 				thisComponent.setAutoDraw(False)
# 			j = 0
# 			while j+1 <= len(arrow): 
# 				arrow[j].setAutoDraw(False)
# 				j = j+1
# 
# 		# store data for trials (TrialHandler)
# 		thisExp.addData('Conf', Confidence1.getRating())
# 		thisExp.addData('Conf_rt', Confidence1.getRT())
	if endSmart: 
		break



#------Prepare to start Routine "Phase 2 Feedback"-------
	#fbtime = globalClock.getTime() - trialstart
	#routineTimer.add(1.0+time_miss-fbtime)
	routineTimer.add(1.0)
	#print fbtime
	
	t = 0
	FeedbackClock.reset()
	frameN = -1

	 # keep track of which components have finished
	FeedbackComponents = []
	FeedbackComponents.append(FixationCross)
	FeedbackComponents.append(ShapeLeft1)
	FeedbackComponents.append(ShapeLeft2)
#    FeedbackComponents.append(ShapeRight1)
#    FeedbackComponents.append(ShapeRight2)
	FeedbackComponents.append(OutcomeBoxLeftCorrect)
	FeedbackComponents.append(OutcomeBoxRightCorrect)
	FeedbackComponents.append(OutcomeBoxLeftError)
	FeedbackComponents.append(OutcomeBoxRightError)
	FeedbackComponents.append(OutcomeMissText)
	FeedbackComponents.append(opt_left)
	FeedbackComponents.append(opt_right)
	FeedbackComponents.append(ShapeMouth1)
	FeedbackComponents.append(arrow)
	for thisComponent in FeedbackComponents:
		if hasattr(thisComponent, 'status'):
			thisComponent.status = NOT_STARTED

#-------Start Routine "Phase 2 Feedback"-------
	continueRoutine = True
	while continueRoutine and routineTimer.getTime() > 0:
		t = FeedbackClock.getTime()
		frameN = frameN + 1
		
	   	# in case it misses show the message
		if KeyRespCal.keys == 'missed' :
			if t >= 0.0 and OutcomeMissText.status == NOT_STARTED:
				OutcomeMissText.tStart = t
				OutcomeMissText.frameNStart = frameN
				OutcomeMissText.setAutoDraw(True)
				win.flip()
		else:

			# *ShapeLeft1* updates
			if t >= 0.0 and ShapeLeft1.status == NOT_STARTED:
				opt_left.setAutoDraw(True)
				opt_right.setAutoDraw(True)
				ShapeLeft1.tStart = t
				ShapeLeft1.frameNStart = frameN
				ShapeLeft1.setAutoDraw(True)

			#if ShapeLeft1.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
			if ShapeLeft1.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
				ShapeLeft1.setAutoDraw(False)
				opt_left.setAutoDraw(False)
				opt_right.setAutoDraw(False)
	
			# *ShapeLeft2* updates & includes stripes and mouth modifications   
			if t >= 0.0 and ShapeLeft2.status == NOT_STARTED:
				ShapeLeft2.tStart = t
				ShapeLeft2.frameNStart = frameN
				j = 0
				while j+1 <= len(arrow): 
					arrow[j].setAutoDraw(True)
					j = j+1
				#ShapeLeft2.setAutoDraw(True)
				ShapeMouth1.setAutoDraw(True)
				
			#if ShapeLeft2.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
			if ShapeLeft2.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
				ShapeLeft1.setAutoDraw(False)    
				j = 0
				while j+1 <= len(arrow): 
					arrow[j].setAutoDraw(False)
					j = j+1
				#ShapeLeft2.setAutoDraw(True)
				ShapeMouth1.setAutoDraw(False)
	
	#        # *FixationCross* updates
	#        if t >= 0.0 and FixationCross.status == NOT_STARTED:
	#            FixationCross.tStart = t
	#            FixationCross.frameNStart = frameN
	#            FixationCross.setAutoDraw(True)
	#        if FixationCross.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
	#            FixationCross.setAutoDraw(False)
	
			# *OutcomeBoxLeftCorrect* updates
			if KeyRespCal.keys == 'b' and value1>value2:
				if t >= 0.0 and OutcomeBoxLeftCorrect.status == NOT_STARTED:
					OutcomeBoxLeftCorrect.tStart = t
					OutcomeBoxLeftCorrect.frameNStart = frameN
					OutcomeBoxLeftCorrect.setAutoDraw(True)
			#if OutcomeBoxLeftCorrect.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
			if OutcomeBoxLeftCorrect.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
				OutcomeBoxLeftCorrect.setAutoDraw(False)
	
			# *OutcomeBoxRightCorrect* updates
			if KeyRespCal.keys == 'y' and value2>value1:
				if t >= 0.0 and OutcomeBoxRightCorrect.status == NOT_STARTED:
					OutcomeBoxRightCorrect.tStart = t
					OutcomeBoxRightCorrect.frameNStart = frameN
					OutcomeBoxRightCorrect.setAutoDraw(True)
			#if OutcomeBoxRightCorrect.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
			if OutcomeBoxRightCorrect.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
				OutcomeBoxRightCorrect.setAutoDraw(False)
	
			# *OutcomeBoxLeftError* updates
			if KeyRespCal.keys == 'b' and value2>value1:
				if t >= 0.0 and OutcomeBoxLeftError.status == NOT_STARTED:
					OutcomeBoxLeftError.tStart = t
					OutcomeBoxLeftError.frameNStart = frameN
					OutcomeBoxLeftError.setAutoDraw(True)
			#if OutcomeBoxLeftError.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
			if OutcomeBoxLeftError.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
				OutcomeBoxLeftError.setAutoDraw(False)
	
			# *OutcomeBoxRightError* updates
			if KeyRespCal.keys == 'y' and value1>value2:
				if t >= 0.0 and OutcomeBoxRightError.status == NOT_STARTED:
					OutcomeBoxRightError.tStart = t
					OutcomeBoxRightError.frameNStart = frameN
					OutcomeBoxRightError.setAutoDraw(True)
			#if OutcomeBoxRightError.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
			if OutcomeBoxRightError.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
				OutcomeBoxRightError.setAutoDraw(False)

		#Finish miss
		#if OutcomeMissText.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
		if OutcomeMissText.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
			OutcomeMissText.setAutoDraw(False)

		# check if all components have finished
		if not continueRoutine:
			break
		continueRoutine = False
		for thisComponent in FeedbackComponents:
			if hasattr(thisComponent, 'status') and thisComponent.status != FINISHED:
				continueRoutine = True
				break

		 # check for quit (the Esc key)
		if endExpNow or event.getKeys(keyList=['escape']):
			core.quit()
		if endSmart or event.getKeys(keyList=['q']):
			endSmart = True
			break

		# refresh the screen
		if continueRoutine:
			win.flip()

	#Go to the Thank you if we use endSmart
	if endSmart: 
		break

#-------Ending Routine "Phase 2 Feedback"-------
	for thisComponent in FeedbackComponents:
		if hasattr(thisComponent, 'setAutoDraw'):
			thisComponent.setAutoDraw(False)
			j = 0
			while j+1 <= len(arrow): 
				arrow[j].setAutoDraw(False)
				j = j+1
				
				
				
#-------Start Routine "ITI"-------
	# flip to have black blank screen
	win.flip()
	ITItime = time_trial - (globalClock.getTime() - trialstart) - time_uncert
	# wait ITI time (variable time depending on response/no respones to have trial length == 9 sec
	#core.wait(ITItime)
	ISI.start(ITItime)
	ISI.complete()

	# final data saving
	time = globalClock.getTime()
	thisExp.addData('Fixation', crossstart)
	thisExp.addData('Pacman', pacmanstart)
	thisExp.addData('Options', optionstart)
	thisExp.addData('ITI', ITItime)
	thisExp.addData('time', time)

	print(time-trialstart)

	thisExp.nextEntry()
	ntrial=ntrial+1
	ntrial_block=ntrial_block+1
	if endSmart: 
		break


#//////////////MAIN EXP END/////////////////////////////////////



#------Prepare to start Routine "Thank You"-------
t = 0
ThankYouClock.reset()  # clock 
frameN = -1

#Add the last block info to the vector (only if it has Corrects strike)
if points_strike>8:
    ntrial_block_vect.append(ntrial_block)
    points_trial_vect.append(points_trial)

#Money 

hello=range(len(ntrial_block_vect))
money = 0
#A=1.1

#print money
#print points_trial_vect
#print ntrial_block_vect
#print hello


for x in hello:
    money=money + A*(points_trial_vect[x]/ntrial_block_vect[x]) - (ntrial_block_vect[x] - 12)*1.5 
    print(money)
    
money=money+MB

ThankYouText.setText(text=u'You have now completed this experiment. \nYou have earned {0} points in total which is {1} JPY. Thank you for your participation.'.format(points,money))

# update component parameters for each repeat
ThankYouResponse = event.BuilderKeyResponse()  # create an object of type KeyResponse
ThankYouResponse.status = NOT_STARTED
# keep track of which components have finished
ThankYouComponents = []
ThankYouComponents.append(ThankYouText)
ThankYouComponents.append(ThankYouBox)
ThankYouComponents.append(ThankYouResponse)
for thisComponent in ThankYouComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "ThankYou"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = ThankYouClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
        # *ThankYouText* updates
    if t >= 0.0 and ThankYouText.status == NOT_STARTED:
        # keep track of start time/frame for later
        ThankYouText.tStart = t  # underestimates by a little under one frame
        ThankYouText.frameNStart = frameN  # exact frame index
        ThankYouText.setAutoDraw(True)
    
    
    if t >= 0.0 and ThankYouBox.status == NOT_STARTED:
        ThankYouBox.tStart = t  # underestimates by a little under one frame
        ThankYouBox.frameNStart = frameN  # exact frame index
        ThankYouBox.setAutoDraw(True)
    


        
    # *ThankYouResponse* updates
    if t >= 0 and ThankYouResponse.status == NOT_STARTED:
        # keep track of start time/frame for later
        ThankYouResponse.tStart = t  # underestimates by a little under one frame
        ThankYouResponse.frameNStart = frameN  # exact frame index
        ThankYouResponse.status = STARTED
        # keyboard checking is just starting
        ThankYouResponse.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if ThankYouResponse.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            ThankYouResponse.keys = theseKeys[-1]  # just the last key pressed
            ThankYouResponse.rt = ThankYouResponse.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThankYouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "Thank You"-------
for thisComponent in ThankYouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if ThankYouResponse.keys in ['', [], None]:  # No response was made
   ThankYouResponse.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('ThankYouResponse.keys',ThankYouResponse.keys)
if ThankYouResponse.keys != None:  # we had a response
    thisExp.addData('ThankYouResponse.rt', ThankYouResponse.rt)
thisExp.nextEntry()
win.close()

print("total points:" + str(points))
print("money:" + str(money))

core.quit()

win.close()
core.quit()

if gw == 1:
    data_frames1 = pd.read_csv(filename+'.csv')
    data_frames1.to_csv(fileList[0], mode='a', header=False, index=False)