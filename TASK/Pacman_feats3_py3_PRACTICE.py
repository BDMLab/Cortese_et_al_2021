#!/usr/bin/env python2
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
from pyglet.window import key # to detect key state, whether key is held down, to move slider on key hold
import pyglet
import pandas as pd
from scipy import stats
from scipy.stats import norm
from random import uniform, random, randint


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'PacMan_3feat_fMRI_practice.py'
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

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
win = visual.Window(size=(1280, 800), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
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

Instructions2Text =visual.TextStim(win,text=u"PRACTICE BLOCK",
    units='cm', color='white', pos=(0,2.0),  height=1, wrapWidth=30)



ShapeLeft1 = visual.ShapeStim(win, vertices=ext_left, fillColor=[1,-1,-1], lineWidth=0, size=100, pos=(0,0), units='pix')
ShapeLeft2 = visual.ShapeStim(win, vertices=inter_left, fillColor='black', lineWidth=0, size=100, pos=(0,0), units='pix')

#time_question = 1

# Starting Time point (respect to the   for pacman appearance and options (fruits) appearance on screen).
time_pacman=2
time_options=4
time_miss=7 

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
Confidence1 = visual.RatingScale(win=win, name='Confidence', marker=u'triangle', markerColor=u'orange', leftKeys='left', rightKeys='right', size=0.6,
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




##############################################
### START EXPERIMENT (PRACTICE + MAIN) #######
##############################################
#------Prepare to start Routine "Instructions2"-------
t = 0
Instructions1Clock.reset()  # clock
frameN = -1
# update component parameters for each repeat
Instructions1Response = event.BuilderKeyResponse()  # create an object of type KeyResponse
Instructions1Response.status = NOT_STARTED
# keep track of which components have finished
Instructions1Components = []
Instructions1Components.append(Instructions2Text)
Instructions1Components.append(Instructions1Response)
#Instructions1Components.append(Instructions2Text1)
#Instructions1Components.append(ghost_instructions)
#Instructions1Components.append(opt_left)
#Instructions1Components.append(opt_right)


for thisComponent in Instructions1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instructions2"-------
continueRoutine = True
page_intro=0
while continueRoutine:
    # get current time
    t = Instructions1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *Instructions2Text* updates
    if t >= 0.0 and Instructions2Text.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instructions2Text.tStart = t  # underestimates by a little under one frame
        Instructions2Text.frameNStart = frameN  # exact frame index
        Instructions2Text.setAutoDraw(True)
    

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

#-------Ending Routine "Instructions2"-------
for thisComponent in Instructions1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Instructions1Response.keys in ['', [], None]:  # No response was made
   Instructions1Response.keys=None



# wait for 5 seconds before starting
win.flip()
core.wait(5.0)



### PRACTICE BLOCK ###
# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method=u'sequential', extraInfo=expInfo, originPath=None,
    trialList=data.importConditions (u'practice_3feat_MRI.csv'),
    seed=None, name='phase2_loop')
thisExp.addLoop(trials)
thisTrial = trials.trialList[0]

if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial["{paramName}"]'.format(paramName=paramName))

ntrial=0

for thisTrial in trials:
    currentLoop = trials
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial["{paramName}"]'.format(paramName=paramName))        
    
    

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
    
    opt_left.setImage (names_list_pract[DisplayClass1-1])
    opt_right.setImage (names_list_pract[DisplayClass2-1])
    
    #ShapeLeft2.setSize(size1)
    #ShapeRight1.setSize(size2)
    #ShapeRight2.setSize(size2)

    event.clearEvents(eventType='keyboard')
    KeyRespCal = event.BuilderKeyResponse()
    KeyRespCal.status = NOT_STARTED

    # keep track of which components have finished
    ChoiceComponents = []
    ChoiceComponents.append(FixationCross)
    ChoiceComponents.append(ShapeLeft1)
    ChoiceComponents.append(ShapeLeft2)
    #ChoiceComponents.append(ShapeRight1)
    #ChoiceComponents.append(ShapeRight2)
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
            FixationCross.tStart = t
            FixationCross.frameNStart = frameN
            FixationCross.setAutoDraw(True)
        if t >= time_pacman and FixationCross.status == STARTED:
            FixationCross.setAutoDraw(False)

        # *ShapeLeft2* updates & includes stripes and mouth modifications
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
            theseKeys = event.getKeys(keyList=['left', 'right'])

            # check for quit or missed trials:
            if 'escape' in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:
                KeyRespCal.keys = theseKeys[-1]
                KeyRespCal.rt = KeyRespCal.clock.getTime()
                continueRoutine = False
            # End selecion period after certain time    
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

        # refresh the screen
        if continueRoutine:
            win.flip()
        else:
            routineTimer.reset()

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
    else: KeyRespCal.corr = 0  # failed to respond (incorrectly)
    
    # Store data for experiment:
    thisExp.addData('Practice_Correct', KeyRespCal.corr)
    thisExp.addData('Practice_Response', KeyRespCal.keys)
    if KeyRespCal.keys != None:
        thisExp.addData('Practice_RT', KeyRespCal.rt)

    if conf_report==1:
        #------Prepare to start Routine "Confidence"-------
        t = 0
        ConfidenceClock.reset()
        frameN = -1
        Confidence1.reset()
    
         # keep track of which components have finished
        ConfComponents = []
        ConfComponents = []
        ConfComponents.append(FixationCross)
        ConfComponents.append(ShapeLeft1)
        ConfComponents.append(ShapeLeft2)
#        ConfComponents.append(ShapeRight1)
#        ConfComponents.append(ShapeRight2)
        ConfComponents.append(OutcomeBoxLeft)
        ConfComponents.append(OutcomeBoxRight)
        ConfComponents.append(Confidence1)
        ConfComponents.append(opt_left)
        ConfComponents.append(opt_right)
        ConfComponents.append(ShapeMouth1)
        ConfComponents.append(arrow)
        ConfComponents.append(GuessingText)
        
        for thisComponent in ConfComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
     
    #-------Start Routine "Confidence"-------
        continueRoutine = True
        while continueRoutine:
            t = ConfidenceClock.getTime()
            frameN = frameN + 1
            
#             *FixationCross* updates
            if t >= 0.0 and FixationCross.status == NOT_STARTED:
                opt_left.setAutoDraw(True)
                opt_right.setAutoDraw(True)
#                FixationCross.tStart = t
#                FixationCross.frameNStart = frameN
#                FixationCross.setAutoDraw(True)

            # *ShapeLeft1* updates
            if t >=0.0 and ShapeLeft1.status == NOT_STARTED:
                ShapeLeft1.tStart = t
                ShapeLeft1.frameNStart = frameN
                ShapeLeft1.setAutoDraw(True)

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

            # *OutcomeBoxLeft* updates
            if KeyRespCal.keys == 'left':
                if t >= 0.0 and OutcomeBoxLeft.status == NOT_STARTED:
                    OutcomeBoxLeft.tStart = t
                    OutcomeBoxLeft.frameNStart = frameN
                    OutcomeBoxLeft.setAutoDraw(True)
                
            # *OutcomeBoxRight* updates
            if KeyRespCal.keys == 'right':
                if t >= 0.0 and OutcomeBoxRight.status == NOT_STARTED:
                    OutcomeBoxRight.tStart = t
                    OutcomeBoxRight.frameNStart = frameN
                    OutcomeBoxRight.setAutoDraw(True)
    
            # *MainRating* updates
            if t > 1.0:
                continueRoutine = Confidence1.noResponse
                while Confidence1.noResponse:
                    Confidence1.draw()
                    GuessingText.setAutoDraw(True)
                    win.flip()
                    hist = set(np.array(Confidence1.getHistory())[:, 0])
                    if len(hist) < 2:
                        Confidence1.noResponse = True
                        Confidence1.status = 0
                    if keyState[key.LEFT] == True and Confidence1.markerPlacedAt > 0.01:
                        Confidence1.markerPlacedAt = Confidence1.markerPlacedAt - 0.02
                        Confidence1.draw()
                    elif keyState[key.LEFT] == True and Confidence1.markerPlacedAt == 0.01:
                        Confidence1.markerPlacedAt = Confidence1.markerPlacedAt - 0.01
                        Confidence1.draw()
                    elif keyState[key.RIGHT] == True and Confidence1.markerPlacedAt < 0.99:
                        Confidence1.markerPlacedAt = Confidence1.markerPlacedAt + 0.02
                        Confidence1.draw()
                    elif keyState[key.RIGHT] == True and Confidence1.markerPlacedAt == 0.99:
                        Confidence1.markerPlacedAt = Confidence1.markerPlacedAt + 0.01
                        Confidence1.draw()
                Confidence1.response = Confidence1.getRating()
                Confidence1.rt = Confidence1.getRT()
                
             # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=['escape']):
                core.quit()
                
            # refresh the screen
            if continueRoutine:
                win.flip()
            else:
                routineTimer.reset()
        
         #-------Ending Routine "Confidence"-------
        for thisComponent in ConfComponents:
            if hasattr(thisComponent, 'setAutoDraw'):
                thisComponent.setAutoDraw(False)
            j = 0
            while j+1 <= len(arrow): 
                arrow[j].setAutoDraw(False)
                j = j+1
    
        # store data for trials (TrialHandler)
        thisExp.addData('Practice_Conf', Confidence1.getRating())
        thisExp.addData('Practice_Conf_rt', Confidence1.getRT())
        

#------Prepare to start Routine "Phase 2 Feedback"-------
    t = 0
    FeedbackClock.reset()
    frameN = -1
    
    routineTimer.add(2.000000)

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
            if ShapeLeft1.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
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
            if ShapeLeft2.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
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
    #            
            # *OutcomeBoxLeftCorrect* updates
            if KeyRespCal.keys == 'left' and value1>value2:
                if t >= 0.0 and OutcomeBoxLeftCorrect.status == NOT_STARTED:
                    OutcomeBoxLeftCorrect.tStart = t
                    OutcomeBoxLeftCorrect.frameNStart = frameN
                    OutcomeBoxLeftCorrect.setAutoDraw(True)
            if OutcomeBoxLeftCorrect.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                OutcomeBoxLeftCorrect.setAutoDraw(False)
                
            # *OutcomeBoxRightCorrect* updates
            if KeyRespCal.keys == 'right' and value2>value1:
                if t >= 0.0 and OutcomeBoxRightCorrect.status == NOT_STARTED:
                    OutcomeBoxRightCorrect.tStart = t
                    OutcomeBoxRightCorrect.frameNStart = frameN
                    OutcomeBoxRightCorrect.setAutoDraw(True)
            if OutcomeBoxRightCorrect.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                OutcomeBoxRightCorrect.setAutoDraw(False)
                
            # *OutcomeBoxLeftError* updates
            if KeyRespCal.keys == 'left' and value2>value1:
                if t >= 0.0 and OutcomeBoxLeftError.status == NOT_STARTED:
                    OutcomeBoxLeftError.tStart = t
                    OutcomeBoxLeftError.frameNStart = frameN
                    OutcomeBoxLeftError.setAutoDraw(True)
            if OutcomeBoxLeftError.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                OutcomeBoxLeftError.setAutoDraw(False)
                
            # *OutcomeBoxRightError* updates
            if KeyRespCal.keys == 'right' and value1>value2:
                if t >= 0.0 and OutcomeBoxRightError.status == NOT_STARTED:
                    OutcomeBoxRightError.tStart = t
                    OutcomeBoxRightError.frameNStart = frameN
                    OutcomeBoxRightError.setAutoDraw(True)
            if OutcomeBoxRightError.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                OutcomeBoxRightError.setAutoDraw(False)
            
            #Finish miss
        if OutcomeMissText.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
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

        # refresh the screen
        if continueRoutine:
            win.flip()

     #-------Ending Routine "Phase 2 Feedback"-------
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, 'setAutoDraw'):
            thisComponent.setAutoDraw(False)
            j = 0
            while j+1 <= len(arrow): 
                arrow[j].setAutoDraw(False)
                j = j+1
            
    #increase counterx
    ntrial=ntrial+1
    print(ntrial)
    
    thisExp.nextEntry()

#/////////////////////// PRACTICE END \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


core.quit()

win.close()
core.quit()
