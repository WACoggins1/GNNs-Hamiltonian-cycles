import configparser
import os.path

DEFAULT_DATASET_SIZES = [25, 50, 100, 150, 200]
DEFAULT_EXAMPLES_PER_SIZE_IN_DATASET = 5000

CONFIG_FILE_PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "config.cfg"))
config = configparser.ConfigParser()
config.read(CONFIG_FILE_PATH)
MODEL_WEIGHTS_FOLDER = config["MODELS"]["MODEL_WEIGHTS_FOLDER"]
CONCORDE_SCRIPT_PATH = config["CONCORDE"]["CONCORDE_SCRIPT_PATH"]
CONCORDE_WORK_DIR = config["CONCORDE"]["CONCORDE_WORK_DIR"]
CONCORDE_INPUT_FILE = config["CONCORDE"]["CONCORDE_INPUT_FILE"]
WEIGHTS_BACKUP_PATH = config["DATABASE"]["WEIGHTS_BACKUP_PATH"]
EVALUATION_DATABASE_LOCK_PATH = config["DATABASE"]["EVALUATION_DATABASE_LOCK_PATH"]

HAMILTONIAN_PROBABILITY = 0.8
MAX_NR_BATCHES_TO_USE_FOR_EVALUATION = 5000
EVALUATION_DATA_FOLDERS = ["DATA"]
