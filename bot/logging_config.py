import logging
import os


def setup_logger():
    log_folder = "logs"

    # create logs folder if it doesn't exist
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    log_file = os.path.join(log_folder, "bot.log")

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

    # optional: also print logs in console (useful while testing)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    formatter = logging.Formatter("%(levelname)s: %(message)s")
    console.setFormatter(formatter)

    logging.getLogger().addHandler(console)
