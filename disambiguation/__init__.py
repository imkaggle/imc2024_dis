import logging
import sys
from .calculate_geodesic_consistency_scores import calculate_geodesic_consistency_scores_fn
from .calculate_missing_correspondences_scores import calculate_missing_correspondences_scores_fn

def set_logger(log_fname):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(log_fname)
    ch = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('[%(asctime)s %(levelname)s] %(message)s',
                                  '%m/%d/%Y %H:%M:%S')
    logging.captureWarnings(True)
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.handlers = []
    logger.addHandler(fh)
    logger.addHandler(ch)
