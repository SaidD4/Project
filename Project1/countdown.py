import time
import sys
import ansi_color 


def countdown_generator(seconds):
    """
    Generator function that yields the countdown time from seconds to zero.
    
    :param seconds: The number of seconds to count down from.
    """
    while seconds >= 0:
        yield seconds
        time.sleep(1)
        seconds -= 1

def countdown_timer(seconds):
    """
    Displays a countdown timer with ANSI colors.
    
    :param seconds: The number of seconds to count down from.
    """
    for remaining in countdown_generator(seconds):
        if remaining > 10:
            color = ansi_color.CYAN
        elif remaining > 5:
            color = ansi_color.GREEN
        elif remaining > 2:
            color = ansi_color.YELLOW
        else:
            color = ansi_color.RED
        
        sys.stdout.write(f"{color}Time left: {remaining} seconds{ansi_color.RESET}\r")
        sys.stdout.flush()
    
    print(f"{ansi_color.MAGENTA}Time's up!{ansi_color.RESET}")

def main():
    """
    Main function to run the countdown timer.
    """
    try:
        seconds = int(input("Enter the countdown time in seconds: "))
        countdown_timer(seconds)
    except ValueError:
        print(f"{ansi_color.RED}Invalid input! Please enter a valid integer.{ansi_color.RESET}")

if __name__ == "__main__":
    main()
