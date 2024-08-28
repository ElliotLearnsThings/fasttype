import time
import msvcrt
from datetime import datetime

from translate import Text

state = {"RUNNING": True, "DEBUG": True, "FIRST": True, "START_TIME": None, "END_TIME": datetime.now(), "WAITTIME": 0.1, "PREV_LENG": 0}

class Input:

    def __init__(self) -> None:

        self.input: list[str] = []

    def monitor_terminal_input(self):
        print("Monitoring terminal input... (Press Ctrl+C to exit)")
        print(f"Waiting {state["WAITTIME"]} seconds between inputs...")

        try:
            while True:
                if msvcrt.kbhit():

                    if state["START_TIME"] is None:
                        state["START_TIME"] = datetime.now()

                    # Wait for WAITTIME seconds
                    time.sleep(state["WAITTIME"])
                    
                    # Read input character by character
                    input_data = ""
                    while msvcrt.kbhit():
                        char = msvcrt.getch()
                        input_data += char.decode('utf-8')
                    
                    # Process the input (for example, print it)
                    print("Input received after 0.2 seconds:", input_data.strip()) if state["DEBUG"] else None
                    self.input.append(curr_input := input_data.strip())

                    if curr_input == ".":
                        state["END_TIME"] = datetime.now()
                        self.process_input()

        except KeyboardInterrupt:
            print("Monitoring stopped.")

    def process_input(self):

        start_proc = datetime.now()

        input_str: str = str()

        for _str in self.input:
            input_str += _str+";"

        text = Text(input_str=input_str)

        end_proc = datetime.now()

        print(output)

        print(f"\nWROTE {(words := (len(output.split(" ")) - state["PREV_LENG"]))} words in {(secs := (state["END_TIME"]-state["START_TIME"]).total_seconds())} seconds")
        print(f"\nWPM: {words/(secs/60)}")
        print(f"\nPROCESSING TOOK {(end_proc-start_proc).seconds} seconds")
        state["PREV_LENG"] = len(output.split(" "))
        state["START_TIME"] = None

if __name__ == "__main__":
    input = Input()
    input.monitor_terminal_input()
