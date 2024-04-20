class Television:
    """
    A class that contains methods to create a Television object
    MIN_VOLUME (int) - Class variable that sets the minimum volume at 0.
    MAX_VOLUME (int) - Class variable that sets the maximum volume at 2.
    MIN_CHANNEL (int) - Class variable that sets the minimum channel number at 0.
    MAX_CHANNEL (int) - Class Variable that sets the maximum channel number at 3.
    """

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initialize the Television object.
        Variables:
        __status (bool): Indicates whether the television is powered on (True) or off (False).
        __muted (bool): Indicates whether the television is muted (True) or not muted (False).
        __volume (int): The current volume level of the television.
        __channel (int): The current channel number of the television.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Power on/off the television by using a boolean.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Mute/unmute the television by using a boolean.
        """
        if self.__status:
            if not self.__muted:
                self.__muted = True
                self.prev_volume = self.__volume
                self.__volume = 0
            else:
                self.__muted = False
                self.__volume = self.prev_volume

    def channel_up(self) -> None:
        """
        Switch to the next channel. If it hits the last channel (3), the Channel
        is automatically set at the first channel (0).
        """
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Switch to the previous channel. If it hits the first channel (0), the Channel
        is automatically set at the last channel (3).
        """
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increase the volume. If it hits maximum volume (2), it does not change.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.prev_volume
            self.__volume += 1
            if self.__volume > Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME

    def volume_down(self) -> None:
        """
        Decrease the volume. If it's the lowest volume (0), it does not change.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.prev_volume
            self.__volume -= 1
            if self.__volume < Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME

    def __str__(self) -> str:
        """
        Return a string representation of the Television object.
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
