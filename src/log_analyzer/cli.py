import argparse


def parse_cli_args():
    parser = argparse.ArgumentParser(
        description="Log Analyzer tool"
        )
        
    parser.add_argument(
        "--config",
        required=True,
        help="Path to the configuration file"
        )

    return parser.parse_args()        
