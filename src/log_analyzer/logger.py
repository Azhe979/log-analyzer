import logging


def setup_logging(level: str = "INFO") -> None:
    """
    Setup global logging configuration.

    This function should be called once at application startup.
    """
    root_logger = logging.getLogger()

    # 防止重复初始化（非常重要）
    if root_logger.handlers:
        return

    numeric_level = getattr(logging, level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {level}")

    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
    )
