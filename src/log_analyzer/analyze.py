import json
import logging
from pathlib import Path
from collections import Counter
from typing import Dict, Any

from log_analyzer.parser.syslog import parse_line

logger = logging.getLogger(__name__)


def run(config: Dict[str, Any]) -> None:
    """
    Run the log analyzer with the given configuration.
    """
    input_paths = config.get("input", {}).get("paths", [])
    if not input_paths:
        logger.warning("No input paths specified in config")
        return

    total_lines = 0
    parsed_lines = 0

    level_counts = Counter()
    program_counter = Counter()

    for path_str in input_paths:
        path = Path(path_str)
        if not path.exists():
            logger.warning("Input path does not exist: %s", path)
            continue

        logger.info("Processing file: %s", path)

        with path.open("r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                total_lines += 1
                line = line.strip()
                if not line:
                    continue

                result = parse_line(line)
                if result is None:
                    logger.debug("Unparsed line: %s", line)
                    continue

                parsed_lines += 1
                level_counts[result["level"]] += 1
                program_counter[result["program"]] += 1

    report = {
        "total_lines": total_lines,
        "parsed_lines": parsed_lines,
        "by_level": dict(level_counts),
        "top_programs": program_counter.most_common(10),
    }

    output_dir = Path("out")
    output_dir.mkdir(exist_ok=True)
    report_path = output_dir / "report.json"

    with report_path.open("w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    logger.info("Analysis complete. Report written to %s", report_path)
