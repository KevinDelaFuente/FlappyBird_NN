DISPLAY_W = 960
DISPLAY_H = 540
FPS = 30

DATA_FONT_SIZE = 18
DATA_FONT_COLOR =  (40,40,40)

BG_FILENAME = 'BG.png'
PIPE_FILENAME = 'Pipe.png'
BIRD_FILENAME = 'Robin.png'

PIPE_SPEED = 70/1000
PIPE_DONE = 1
PIPE_MOVING = 0
PIPE_UPPER = 1
PIPE_LOWER = 0
PIPE_MIN = 80
PIPE_MAX = 500
FIRST_PIPE = 450
VERTICAL_GAP  = 150
HORIZONTAL_GAP = 180

BIRD_START_SPEED = -.32
BIRD_START_X = 200
BIRD_START_Y = 200
BIRD_ALIVE = 1
BIRD_DEAD = 0
GRAVITY = .001

#Generations
GENERATION_SIZE = 60

NNET_INPUTS = 2
NNET_HIDDEN = 5
NNET_OUTPUTS = 1

JUMP_CHANCE = 0.5

MAX_Y_DIFF = DISPLAY_H - PIPE_MIN - VERTICAL_GAP/2
MIN_Y_DIFF = VERTICAL_GAP/2 - PIPE_MAX
Y_SHIFT = abs(MIN_Y_DIFF)
NORMALIZER = abs(MIN_Y_DIFF) + MAX_Y_DIFF

MUTATION_WEIGHT_MODIFY_CHANCE = 0.2
MUTATION_ARRAY_MIX_PERC = 0.5