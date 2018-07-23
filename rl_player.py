import pickle
from player import Player


class RLPlayer(Player):
    def __init__(
            self, name: str, alpha: float, gamma: float, epsilon: float):
        """Args:
         - name (str): the name of the player for display purpose.
         - alpha (float): the learning rate of the update scheme.
         - gamma (float): the discount factor in (0, 1]
         - epsilon (float): the value of the epsilon greedy strategy
        """
        super().__init__(name)
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

        # True if the agent is in a training phase, False otherwise
        self.training = True

        # storing the estimates of Q(s, a)
        self.q = dict()

        # The internal current state of the board.
        self.state = None

    def getColumn(self, board):
        self.state = self.getState(board)
        self.action = self.sample(board)
        return self.action

    def getState(self, board):
        """Returns a representation of the state of the board

        Args:
         - board: a Board object (see board.py)
        """
        # TODO(student): implement it !
        pass

    def observe(self, board, winner):
        """This method should update the estimates of Q(s, a) according to the
        Q-learning algorithm.

        Not that the state of the board
        Args:
         - board: a Board object
         - winner: a player object or None if no-one has won
        """
        # TODO(student): implement it!
        pass

    def sample(self, board):
        """This method should sample an action based on the policy extracted
        from the current estimate of Q(s, a) following a epsilon greedy
        strategy."""
        # TODO(olivier): implement it!
        pass

    def save(self, basename):
        filename = "{0}_{1}_a{2:.2f}_g{3:.2f}_e{4:.2f}.pickle".format(
            basename, self.name, self.alpha, self.gamma, self.epsilon)
        with open(filename, 'wb') as fp:
            pickle.dump(self, fp)
        return filename
