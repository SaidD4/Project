import time
import sys
import colorization


class CountdownBase:
    """
    Base class for countdown functionality.
    """
    def __init__(self, seconds):
        self._seconds = seconds
    
    @property
    def seconds(self):
        """Getter for seconds."""
        return self._seconds
    
    @seconds.setter
    def seconds(self, value):
        """Setter for seconds."""
        if value < 0:
            raise ValueError("Seconds cannot be negative.")
        self._seconds = value
    
    @staticmethod
    def time_delay(seconds):
        """Static method to introduce a delay."""
        time.sleep(seconds)

class CountdownTimer(CountdownBase):
    """
    Countdown timer class that includes ANSI color formatting and uses a generator.
    """
    def __init__(self, seconds):
        super().__init__(seconds)
    
    def countdown_generator(self):
        """
        Generator function that yields the countdown time from seconds to zero.
        """
        while self.seconds >= 0:
            yield self.seconds
            self.time_delay(1)
            self.seconds -= 1
    
    def start_countdown(self):
        """
        Starts the countdown timer and displays the output with ANSI colors.
        """
        for remaining in self.countdown_generator():
            if remaining > 5:
                color = colorization.GREEN
            elif remaining > 2:
                color = colorization.YELLOW
            else:
                color = colorization.RED
            
            sys.stdout.write(f"{color}Time left: {remaining} seconds{colorization.RESET}\r")
            sys.stdout.flush()
        
        print(f"{colorization.RED}Time's up!{colorization.RESET}")

if __name__ == "__main__":
    timer = CountdownTimer(10)  # Change the value to set a different countdown time
    timer.start_countdown()