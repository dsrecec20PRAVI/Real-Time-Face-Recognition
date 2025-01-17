import argparse
from src.train import train
from src.evaluate import evaluate

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["train", "evaluate"], help="Run training or evaluation")
    args = parser.parse_args()

    if args.mode == "train":
        train()
    elif args.mode == "evaluate":
        evaluate()
