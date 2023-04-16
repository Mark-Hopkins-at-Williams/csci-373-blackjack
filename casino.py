from pgl import GWindow, GLabel, GRect
from qlearning import QLearningAgent
from blackjack import BlackjackEnvironment
from games import initialize_game

GWINDOW_WIDTH = 1000               # Width of the graphics window
GWINDOW_HEIGHT = 500              # Height of the graphics window
LETTER_BASE = 10                  # Distance from bottom to the letters
LETTER_FONT = "bold 24px 'Monaco','Monospaced'"
MESSAGE_FONT = "30px 'Helvetica Neue','Arial','Sans-Serif'"

gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
env = BlackjackEnvironment(initialize_game())
agent = QLearningAgent(env)

def createWindow():
    
    def createCardTotalLabels():
        alphabet = ['02','03','04','05','06','07','08','09','10',
                    '11','12','13','14','15','16','17','18','19',
                    '20','21']
        alphabetLabels = [GLabel(letter) for letter in alphabet]
        for label in alphabetLabels:
            label.setFont(LETTER_FONT)    
        return alphabetLabels


    def createUpCardLabels():
        alphabet = ['01','02','03','04','05','06','07','08','09','10']
        alphabetLabels = [GLabel(letter) for letter in alphabet]
        for label in alphabetLabels:
            label.setFont(LETTER_FONT)           
        return alphabetLabels
    
     
    def makeDisplay(alphabetLabels, upCardLabels):
        decisionIndicators = dict()
        letterWidth = alphabetLabels[0].getWidth()
        letterHeight = alphabetLabels[0].getHeight()
        XMARGIN = 50
        offset = (GWINDOW_WIDTH - XMARGIN -
                  (len(alphabetLabels) * letterWidth)) / (len(alphabetLabels) + 1)
        for (i, label) in enumerate(alphabetLabels):
            x = XMARGIN + (offset + letterWidth) * i + offset
            gw.add(label, x, GWINDOW_HEIGHT - LETTER_BASE)
            
        YMARGIN = 100        
        upCardOffset = (GWINDOW_HEIGHT - YMARGIN - 
                  (len(upCardLabels) * letterHeight)) / (len(upCardLabels) + 1)
        for (i, label) in enumerate(upCardLabels):
            y = YMARGIN + (upCardOffset + letterHeight) * i + upCardOffset
            gw.add(label, LETTER_BASE, y)

        for (i, upCardLabel) in enumerate(upCardLabels):
            y = YMARGIN + (upCardOffset + letterHeight) * i + upCardOffset - letterHeight
         
            for (j, totalLabel) in enumerate(alphabetLabels):
                x = XMARGIN + (offset + letterWidth) * j + offset
        
                decisionIndicator = GRect(x, y, letterHeight, letterWidth)
                decisionIndicator.setFillColor("black")
                decisionIndicator.setFilled(True)
                gw.add(decisionIndicator)
                decisionIndicators[(str(int(totalLabel.getLabel())), 
                                    str(int(upCardLabel.getLabel())))] = decisionIndicator
        return decisionIndicators
            
    cardTotalLabels  = createCardTotalLabels()
    upCardLabels = createUpCardLabels()
    return makeDisplay(cardTotalLabels, upCardLabels)

def runSimulation():

    decisionIndicators = createWindow()
    progressLabel = GLabel("GAMES PLAYED: 0")
    progressLabel.setFont(MESSAGE_FONT)
    gw.add(progressLabel, 20, 50)
    
    def adjustIndicators():
        progressLabel.setLabel('GAMES PLAYED: {}'.format(agent.get_rollouts_so_far()))
        for state in decisionIndicators:
            hitValue = agent.get_qvalue(state, 'hit')
            standValue = agent.get_qvalue(state, 'stand')
            hitDifferential = hitValue - standValue
            if hitDifferential > 1:
                color = "#00FF00"
            elif hitDifferential > 0.5:
                color = "#00CC00"
            elif hitDifferential > 0.2:
                color = "#008800"
            elif hitDifferential > 0.1:
                color = "#006600"
            elif hitDifferential > 0.05:
                color = "#004400"
            elif hitDifferential > -0.05:
                color = "#000000"
            elif hitDifferential > 0.1:
                color = "#440000"
            elif hitDifferential > -0.2:
                color = "#660000"
            elif hitDifferential > -0.5:
                color = "#880000"
            elif hitDifferential > -1:
                color = "#CC0000"
            else:
                color = "#FF0000"
            indicator = decisionIndicators[state]
            indicator.setFillColor(color)
            indicator.setFilled(True)
    
    def perform_k_rollouts():
        for _ in range(500):
            agent.perform_rollout()

    timer1 = gw.createTimer(perform_k_rollouts, 100)
    timer1.setRepeats(True)
    timer1.start()
    timer2 = gw.createTimer(adjustIndicators, 1500)
    timer2.setRepeats(True)
    timer2.start()

if __name__ == '__main__':
    runSimulation()
