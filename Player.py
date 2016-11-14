from abc import ABCMeta, abstractmethod


class Player:
    __metaclass__ = ABCMeta

    @abstractmethod
    def make_move(self):
        pass

    def set_player_won(self):
        pass

    def set_player_lost(self):
        pass
