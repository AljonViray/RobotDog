# Step 1: Make movement sequences using Maestro Control Center
    # These will be stored inside the Maestro itself, 
    #   but it will specifically look for the PC of the person who made the sequences
    # Therefore we need to make copies of them on the PC itself and place them in the Maestro if needed

# Step 2: Install Maestro library (basically one script called maestro.py) on Pi to call these sequences
    # Install following library into Raspberry Pi (https://github.com/FRC4564/Maestro)
    # Alexandra said that it worked before but only for one motor, may have been a power issue so worth a try.

# [NOT NEEDED] Step 3: Install PS4 Controller Library on Pi to control the raspberry pi's actions
    # Found here: https://github.com/ArturSpirin/pyPS4Controller
    # Can supposedly recognize all buttons and joystick movement, translate into values/bools
    # Bobby says it was buggy, might have to try this instead: https://github.com/FRC4564/BasicPiBot
    # Or this with XBOX CONTROLLER: https://github.com/FRC4564/BasicPiBot

# [NEW] Step 3: Make code for simple text commands for movement
    # Running this script from my laptop via SSH on the Pi will be simple.



# LIST OF MAESTRO MOTOR MOVEMENT SEQUENCES:
# 0 = Sit
# 1 = Stand / Idle
# 2 = Walk Forward
# 3 = Walk Backward
# 4 = Turn Left
# 5 = Turn Right
# 6 = Crouch before Jumping
# 7 = Jump



# Note: This script would be in the Pi itself
# python-given imports
import sys
import time #For pausing the script
# third party imports
import maestro #For controlling Maestro



# Ensures the code underneath this if-statement only runs when run directly, rather than if it is imported
if __name__ == "__main__":
    # m = maestro.Controller('COM4') # for Aljon's PC, the value here should be the string 'COM4'
    # r = voice control

    # Mode text = 0 vs Mode text = 1
    mode = 0

    while True:
        command = input("> ").split()


        # Switch Mode
        if (len(command) == 1 and command[0] == "walk" and command[1] == "forward"):
            


        # Walk Forward
        elif (len(command) == 2 and command[0] == "walk" and command[1] == "forward"):
            # m.runScriptSub(0) # run idle/reset sequence
            # while (m.isMoving): continue
            
            # maestro sequences can be infinite when called

            print("Walking... press Enter to walk another step, type 'stop' to stop walking.")
            # m.runScriptSub(1) # run walking sequence
            # while (m.isMoving): time.sleep(0.5)
            x = input()


        # Walk Backward
        elif (len(command) == 2 and command[0] == "walk" and command[1] == "backward"):
            # m.runScriptSub(0) # run idle/reset sequence
            # while (m.isMoving): continue
            
            print("Walking... press Enter to walk another step, type 'stop' to stop walking.")
            done = False
            time_waiting = 0

            while not done:
                time_waiting += 1
                print(f"Steps taken = {time_waiting}")
                x = input()

                # m.runScriptSub(1) # run walking sequence
                # while (m.isMoving): time.sleep(0.5)

                if x == "stop": 
                    done = True


        # Jump
        elif (len(command) == 1 and command[0] == "jump"):
            # m.runScriptSub(0) # run idle/reset sequence
            # while (m.isMoving): time.sleep(0.5)
            
            print("Preparing to jump...")
            # m.runScriptSub(6) # run crouching sequence
            # while (m.isMoving): time.sleep(0.5)
            print("Ready to jump!")
            # m.runScriptSub(7) # run jumping sequence
            # while (m.isMoving): time.sleep(0.5)
            print("JUMP!!!")

        
        # Quit
        elif (len(command) == 1 and command[0] == "quit"):
            print("Shutting down Robot Dog...")
            # m.runScriptSub(0) # run idle/reset sequence?
            # m.stopScript() #stops the current Maestro sequence
            break



    # m.stopScript() #stops the current Maestro sequence
    # m.close() #cleanly close USB serial port













# def connect():
#     # any code you want to run during initial connection with the controller
#     print("connected")
#     pass

# def disconnect():
#     # any code you want to run during loss of connection with the controller or keyboard interrupt
#     #m.close()
#     print("dc")
#     pass
    
# class MyController(Controller):

#     def __init__(self, **kwargs):
#         Controller.__init__(self, **kwargs)

#     def on_x_press(self):
#         print("Hello world")

#     def on_x_release(self):
#         print("Goodbye world")
    
#     def on_L3_up(self, value):
#         # Input any code that you want to run when left joystick (L3) is pushed up
#         # value will indicate the degree of how far the joystick is pushed
#         #m.runScriptSub(0)    #Run the Maestro script subroutine 0, which would be Walk Forward??
#         print("L3 pushed up:", value)

#     def on_L3_release(self):
#         # Input any code that you want to run when left joystick (L3) is back to its resting state
#         print("L3 at rest!")
#         #m.stopScript() # stop the current Maestro script. Only one can run at a time.

#     def on_L3_down(self):
#         #m.runScriptSub(1)
#         pass

# controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# controller.listen(on_connect=connect, on_disconnect=disconnect)
# # you can start listening before controller is paired, as long as you pair it within the timeout window
# controller.listen(timeout=60)