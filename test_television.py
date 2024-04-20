import pytest
from television import Television


class TestTelevision:
    def setup_method(self):
        self.tv1 = Television()

    def teardown_method(self):
        del self.tv1

    def test_init(self):
        assert not self.tv1._Television__status
        assert not self.tv1._Television__muted
        assert self.tv1._Television__volume == Television.MIN_VOLUME
        assert self.tv1._Television__channel == Television.MIN_CHANNEL  

    def test_power(self):
        assert not self.tv1._Television__status
        self.tv1.power()
        assert self.tv1._Television__status
        self.tv1.power()
        assert not self.tv1._Television__status

    def test_mute(self):
        self.tv1.power() #tv on
        self.tv1.volume_up() # volume is 1
        self.tv1.mute() #muted
        assert self.tv1._Television__muted
        assert self.tv1._Television__volume == 0
        assert self.tv1._Television__status

        self.tv1.mute() #unmuted
        assert not self.tv1._Television__muted
        assert self.tv1._Television__volume == 1
        assert self.tv1._Television__status

        self.tv1.power() #tv off
        self.tv1.mute() #muted
        assert not self.tv1._Television__status
        assert self.tv1._Television__volume == 1

        self.tv1.mute() #unmuted tv still off
        assert not self.tv1._Television__muted
        assert self.tv1._Television__volume == 1
        assert not self.tv1._Television__status


    def test_channel_up(self):
        self.tv1.channel_up()
        assert not self.tv1._Television__status
        assert self.tv1._Television__channel == 0

        self.tv1.power()
        self.tv1.channel_up() #1
        assert self.tv1._Television__status
        assert self.tv1._Television__channel == 1

        self.tv1.channel_up() #2
        self.tv1.channel_up() #3
        self.tv1.channel_up() #0
        assert self.tv1._Television__status
        assert self.tv1._Television__channel == 0


    def test_channel_down(self):
        self.tv1.channel_down()
        assert self.tv1._Television__channel == 0
        assert not self.tv1._Television__status

        self.tv1.power()
        self.tv1.channel_down()
        assert self.tv1._Television__status
        assert self.tv1._Television__channel == 3

    def test_volume_up(self):
        self.tv1.volume_up()
        assert not self.tv1._Television__status
        assert self.tv1._Television__volume == 0

        self.tv1.power()
        self.tv1.volume_up()
        assert self.tv1._Television__status
        assert self.tv1._Television__volume == 1

        self.tv1.mute()
        self.tv1.volume_up()
        assert self.tv1._Television__status
        assert not self.tv1._Television__muted
        assert self.tv1._Television__volume == 2

        self.tv1.mute()
        self.tv1.volume_up()
        self.tv1.volume_up()
        assert self.tv1._Television__status
        assert not self.tv1._Television__muted
        assert self.tv1._Television__volume == 2


    def test_volume_down(self):
        self.tv1.volume_down()
        assert not self.tv1._Television__status
        assert self.tv1._Television__volume == 0

        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.volume_up()
        self.tv1.volume_down()
        self.tv1.volume_down()
        self.tv1.volume_down()
        assert self.tv1._Television__status
        assert self.tv1._Television__volume == 0

        self.tv1.mute()
        self.tv1.volume_up()
        self.tv1.volume_up()
        self.tv1.volume_down()
        assert self.tv1._Television__volume == 1
        assert self.tv1._Television__status
        assert not self.tv1._Television__muted

        self.tv1.volume_down()
        self.tv1.volume_down()
        self.tv1.volume_down()
        assert self.tv1._Television__volume == 0
        assert self.tv1._Television__status






if __name__ == "__main__":
    pytest.main()
