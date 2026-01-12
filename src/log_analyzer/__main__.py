import logging
from log_analyzer import cli
from log_analyzer.config import load_config
from log_analyzer.analyze import run
from log_analyzer.logger import setup_logging

def main():
    args=cli.parse_cli_args()
    config=load_config(args.config)
    log_level=config.get("log",{}).get("level","INFO")
    setup_logging(log_level)
    logger = logging.getLogger(__name__)
    logger.info(f"Starting log-analyzer with config: {config}")
    run(config)



if __name__ == "__main__":
    main()