import threading
import time
import sys
import tty
from metronome.metronome import Metronome
import select
import termios

"""
Metronome, sounds taken with permission from https://pixabay.com/sound-effects/search/metronome/
"""


def main():
    """
    Gets arguments from sys.argv.
    Creates a metronome and object.
    Starts the metronome (main thread) and a separate thread that runs the change_bpm method.
    runs the validate_input method. 
    Params:
        None
    Returns:
        None
    """

    stop_event = threading.Event() # got help from chatgpt for the improved thread-killing logic. 
    
    if not len(sys.argv) == 3:
        sys.exit("Please enter number of beats, and bpm, ex: 4 120")

    number_of_beats, bpm = validate_input(sys.argv[1], sys.argv[2])
    metronome = Metronome(number_of_beats, bpm)
    # print(metronome._bpm)

    try:
        # Pass the stop_event to both threads
        threading.Thread(target=change_bpm, args=(metronome, stop_event), daemon=True).start()
        metronome.run_metronome(stop_event)
    except KeyboardInterrupt:
        print("\nExiting gracefully...")
        stop_event.set()
        time.sleep(0.5)  # Give the thread time to stop
        sys.exit()


def validate_input(number_of_beats, bpm) -> tuple[int, int]:
    """
    validates the input from main(), set the variables _number_of_beats and _bpm

    params:
        number_of_beats: str
        bpm: str
    returns:
        None

    """
    if not number_of_beats.isdigit():
        raise ValueError("Should be an int, try again")

    if not bpm.isdigit():
        raise ValueError("Should be an int, try again")
    bpm = int(bpm)
    if not (20 <= bpm <= 320):
        raise ValueError(f"Tempo should be between 20 and 320 {bpm}")

    return int(number_of_beats), int(bpm)


def change_bpm(metronome: Metronome, stop_event : threading.Event):
    """
    Registers keypresse, calls on the increment/decrement methods based on keypress

    Params:
        metronome: Metronome
    Returns:
        None
    """

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setcbreak(fd)

        print(
            """
Metronome Controls:
    increment by 1   - press i
    increment by 10  - press o
    decrement by 1   - press d
    decrement by 10  - press f
    quit             - press Ctrl+C
"""
        )

        while not stop_event.is_set():
            if sys.stdin in select.select([sys.stdin], [], [], 0.5)[0]:
                key_press = sys.stdin.read(1)
                n = 0

                match key_press:
                    case "i":
                        n = 1
                    case "o":
                        n = 10
                    case "d":
                        n = -1
                    case "f":
                        n = -10
                    case "h":
                        # optional help trigger
                        print(
                            """
    i  - increment by 1
    o  - increment by 10
    d  - decrement by 1
    f  - decrement by 10
    h  - show help
    Ctrl+C - quit
                            """
                        )

                if n > 0:
                    increment(metronome, n)
                elif n < 0:
                    decrement(metronome, n)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)




def increment(metronome: Metronome, n: int):
    """
    Increments the bpm by n, ensures that the bpm cannot be incremented beyond 320

    Params:
        metronome: Metronome, 
        n: int
    Returns:
        None
    """

    new_bpm = min(320, metronome.get_bpm() + n)
    metronome.set_bpm(new_bpm)
    print(f"New bpm = {new_bpm}")

def decrement(metronome: Metronome, n: int):
    """
    Decrements the bpm by n, ensures that the bpm cannot be decremented to less than 20
    Params:
        metronome: Metronome, 
        n:int
    Returns:
        None
    """

    new_bpm = max(20, metronome.get_bpm() + n)
    metronome.set_bpm(new_bpm)
    print(f"New bpm = {new_bpm}")

# TODO find a more elegant way to kill the program?
# TODO break up this script into several scripts? 

if __name__ == "__main__":
    main()
