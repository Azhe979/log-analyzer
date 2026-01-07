from log_analyzer import cli


def main():
    args=cli.parse_cli_args()
    print("Starting log-analyzer")
    print(f"Config file contents: {args.config}")


if __name__ == "__main__":
    main()