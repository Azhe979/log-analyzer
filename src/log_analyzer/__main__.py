from log_analyzer import cli
from log_analyzer.config import load_config


def main():
    args=cli.parse_cli_args()
    config=load_config(args.config)

    print("Starting log-analyzer")
    print(f"Loaded config: {config}")
    print(f"Config file contents: {args.config}")


if __name__ == "__main__":
    main()