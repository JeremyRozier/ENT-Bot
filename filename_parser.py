"""Module which contains functions which parse filenames
"""
from mimetypes import guess_type
import unicodedata
import os
import re
from constants import RegexPatterns

def get_valid_filename(filename):
    """
    Return the given string converted to a string that can be used for a clean
    filename. Remove leading and trailing spaces; convert other spaces to
    underscores; and remove anything that is not an alphanumeric, dash,
    underscore, or dot.
    """
    if "." in filename:
        tuple_before_after = os.path.splitext(filename)
        if guess_type(tuple_before_after[1]) is not None:
            filename = tuple_before_after[0]

    valid_filename = str(filename).strip().replace(" ", "_")
    valid_filename = RegexPatterns.FILENAME_FORBIDDEN_CHARS.sub("", valid_filename)
    valid_filename = unicodedata.normalize("NFKD", valid_filename)
    valid_filename = "".join(
        [c for c in valid_filename if not unicodedata.combining(c)]
    )
    return valid_filename


def get_nb_origin_same_filename(folder_path, filename):
    """
    Returns for a given filename the number of files
    already saved which match with this pattern
    rf{filename}(_d+)?, or 0 if there aren't any conflicts.
    """
    list_files = [
        os.path.splitext(f)[0]
        for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
    ]
    list_same_file = [f for f in list_files if f == filename]
    if len(list_same_file) == 0:
        return 0

    pattern = rf"{filename}(_\d+)?"
    list_similar = [f for f in list_files if re.match(pattern, f)]
    return len(list_similar)
