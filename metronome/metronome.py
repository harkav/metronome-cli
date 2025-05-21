"""Metronome module - provided the Metronome class"""

import pygame 
import time 
import sys 
from pathlib import Path 
import threading

class Metronome:
    
    """Custom class that acts like a metronome """

    def __init__(self, number_of_beats: int, bpm: int):
        """
       Initialize a metronome instance.

        Args:
            number_of_beats (int) : the number of beats per measure. 
            bpm (int): the number of beats per minute. 

        """

        self._number_of_beats =  number_of_beats  # instansiate number_of_beats
        self._bpm = bpm  # instansiate bpm
        self._file_one = "./metronome/assets/metronome-85688(1).mp3"
        self._file_other = "./metronome/assets/metronome-85688.mp3"
        self._validate_files(self._file_one, self._file_other)

    def _validate_files(self, file_one: str, file_two: str) -> None:
        """
        Validate that the program finds the sound files.

       
        Args:
            file_one (str): Path to the first sound file. 
            file_two (str): Path to the second sound file. 
            
        Raises: 
            SystemExit: If either or both of the files are missing.  
        """

        file_one_path = Path(file_one)
        if not file_one_path.is_file():
            raise ValueError(
                sys.exit(
                    f"Cannot file{file_one_path}, or {file_one_path} is not a file"
                )
            )
        file_two_path = Path(file_two)
        if not file_two_path.is_file():
            raise ValueError(
                sys.exit(
                    f"Cannot file{file_two_path}, or {file_two_path} is not a file"
                )
            )

    def get_bpm(self)-> int :
        """
        Return current BPM. 

       
        Returns:
            int : the current beats per minute
        """

        return self._bpm

    def set_bpm(self, bpm : int)-> None:
        """
        Set BPM.

        Args:
           bpm (int): new beats per minute. 
        
        """
        self._bpm = bpm

    def set_number_of_beats(self, number_of_beats: int) -> None:
        """
        Set the number of beats per measure. 

        Args:
            number_of_beats (int): New beat count. 

        """

        self._number_of_beats = number_of_beats

    def run_metronome(self, stop_event : threading.Event) -> None:
        """
        Run the metronome loop.

        Args:
            stop_event (threading.Event): Event used to stop the loop.
        Returns:
            None

        """
        sleep_time = float(60 / self._bpm)
        beat = 1
        pygame.init()

        while not stop_event.is_set():
            file = self._file_one if beat == 1 else self._file_other
            sound = pygame.mixer.Sound(file)
            sound.play()
            beat = 1 if beat == self._number_of_beats else beat + 1
            time.sleep(sleep_time)
            sleep_time = float(60 / self.get_bpm())  # update bpm
