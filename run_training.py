import argparse
from game import Game
from player import RandomPlayer
from rl_player import RLPlayer


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--episodes', default=1000, type=int)
    parser.add_argument('--alpha', default=1.0, type=float)
    parser.add_argument('--gamma', default=1.0, type=float)
    parser.add_argument('--epsilon', default=0.1, type=float)
    parser.add_argument('--outputname', default='rl_agent', type=str)
    args = parser.parse_args()

    # TODO(student): Try different learning scenarios !
    player1 = RandomPlayer('random')
    player2 = RLPlayer(
        'RLagent', alpha=args.alpha, gamma=args.gamma, epsilon=args.epsilon)
    game = Game(player1, player2, verbose=False)
    game.train(args.episodes)

    # TODO(student): How to measure your learning agent performance ?

    if args.outputname:
        basename = "{0}_n{1}".format(args.outputname, args.episodes)
        filename = player2.save(basename)
        print('RL player saved in pickle file {0}'.format(filename))
