# Import color classes
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
import sys
# __file__ will show the script name
print(bcolors.OKBLUE + bcolors.WARNING + 'running ' + __file__  + bcolors.ENDC)

print()
print (bcolors.WARNING + 'running basics/output/simple_message.py' + bcolors.ENDC)
from basics.output.simple_message import start
start()

print()
from basics.output.multiline_message import start
print (bcolors.WARNING + 'running basics/output/multiline_message.py' + bcolors.ENDC)
start()

print()
from basics.output.escape_characters import run
print (bcolors.WARNING + 'running basics/output/escape_characters.py' + bcolors.ENDC)
run()

print()
from basics.output.show_beep import run
print (bcolors.WARNING + 'running basics/output/show_beep.py' + bcolors.ENDC)
run()

print()
from basics.output.ascii_art import run
print (bcolors.WARNING + 'running basics/output/ascii_art.py' + bcolors.ENDC)
run()

print()
from basics.input.user_input import run
print (bcolors.WARNING + 'running basica/input/user_input.py' + bcolors.ENDC)
print('What is your name?')
run(sys.argv[1])

print()
from basics.input.ascii_robot import run
print (bcolors.WARNING + 'running basics/input/ascii_robot.py' + bcolors.ENDC)
print('What character should I use for my eye? e.g 0')
run(sys.argv[2])

print()
from basics.input.user_age import run
print (bcolors.WARNING + 'running basics/input/user_age.py' + bcolors.ENDC)
print('How old are you?')
run(sys.argv[3])

print()
from basics.input.data_types import run
print (bcolors.WARNING + 'running basics/input/data_types.py' + bcolors.ENDC)
print('What is your name human? ')
print('How old are you (in years)? ')
print('How tall are you (in meters)? ')
print('How much do you weigh (in kilograms)? ')
run(sys.argv[4], sys.argv[5], int(sys.argv[6]), int(sys.argv[7]))

print()
from basics.input.string_operators import run
print (bcolors.WARNING + 'running basics/input/string_operators.py' + bcolors.ENDC)
print('Please enter the number of lives. ' + sys.argv[8])
print('Please enter the energy level. ' + sys.argv[9] )
print('Please enter the shield level. ' + sys.argv[10])
run(int(sys.argv[8]), int(sys.argv[9]), int(sys.argv[10]))

print()
from basics.input.review import run
print (bcolors.WARNING + 'running basics/input/review.py' + bcolors.ENDC)
print(f'What is your name human? {sys.argv[9]} ')
print(f'What is your age human? {sys.argv[10]} ')
print(f'How tall are you human? in metres {sys.argv[11]}')
print(f'How much do you weigh human? {sys.argv[12]} ')
print(f'Please enter the number of lives. {sys.argv[13]} ')
print(f'Please enter the shield level. {sys.argv[14]} ')
run(sys.argv[9], sys.argv[10], sys.argv[11], sys.argv[12], sys.argv[13], sys.argv[14])