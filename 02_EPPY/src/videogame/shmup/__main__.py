import sys
from shmup.game import Game

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    game = Game()
    game.run()

if __name__ == '__main__':
    sys.exit(main())