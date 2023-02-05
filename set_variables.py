import os

GITHUB_ACTIONS = os.getenv('GITHUB_ACTIONS')

def set_variables():
    if os.getenv('KAGGLE_USERNAME') is None:
        os.environ['KAGGLE_USERNAME'] = "DUMMY_USERNAME"
        os.environ['KAGGLE_KEY'] = "DUMMY_KEY"
        os.putenv('KAGGLE_USERNAME', "DUMMY_USERNAME")


def main():
    set_variables()

if __name__ == "__main__":
    main()