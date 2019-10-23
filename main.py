import argparse 
import os

parser = argparse.ArgumentParser()
parser.add_argument(
                    '--exp_name',
                    '-e',
                    type=str,
                    default='NYT10',
                    help='experiments/NYT10'
)
parse.add_argument(
                    '--mode',
                    '-m',
                    type=str,
                    default='NYT11',
                    help='experiments/NYT11'
)

args = parser.parse_args()

class Runner(object):
    def __init__(self, exp_name: str):
        self.exp_name = exp_name
        self.model_dir = 'saved_models'

        self.hyper = Hyper()


if __name__ = "__main__":
    config = Runner(exp_name=args.exp_name)
    Runner.run(mode=args.mode)