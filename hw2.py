"""This module include function process_data,which writes statistics to a file."""


import json
import os

MAIL = 'email'
REGISTER = 'registered'


def make_path(path: list):
    """Make path to output file.

    Args:
        path: list with name of directory and output filename

    Returns:
        None or self without the first element.
    """
    if len(path) == 1:
        with open(f'{path[0]}', 'w') as new_file:
            new_file.close()
        return None
    if not os.path.isdir(path[0]):
        os.mkdir(path[0])
    os.chdir(path[0])
    return make_path(path[1:])


def file_found(in_path: str, out_path: str) -> None:
    """Check if the arguments are files.

    Args:
        in_path: path to json file with data on site clients
        out_path: path to json output file

    Raises:
        FileNotFoundError: If in_path is not file
    """
    if not os.path.isfile(in_path):
        raise FileNotFoundError('Is not a file path')
    if not os.path.isfile(out_path):
        out_path = out_path.replace(os.getcwd(), '')
        make_path(out_path.split('/')[1:])


def dict_path(count_dct: dict[str, dict]) -> dict[str, dict]:
    """Take a set and two lists and returns a dictionary with statistics.

    Args:
        count_dct:dict with counts

    Returns:
        A dictionary with statistics.
    """
    res_dict = {MAIL: {}, REGISTER: {}}
    regist_len = len(count_dct[REGISTER]) if count_dct[REGISTER] else 1
    email_len = len(count_dct[MAIL]) if count_dct[MAIL] else 1

    for register, mail_host in zip(count_dct[REGISTER], count_dct[MAIL]):
        res_dict[REGISTER][register] = round((
            count_dct[REGISTER][register]/regist_len
        )*100, 2,
        )
        res_dict[MAIL][mail_host] = round((count_dct[MAIL][mail_host]/email_len)*100, 2)
    return res_dict


def process_data(input_filepath: str, output_filepath: str) -> None:
    """Take json file and returns emailing and registration statiatic.

    Args:
        input_filepath: path to json file with data on site clients
        output_filepath: path to json output file

    Returns:
        None or error message.

    """
    file_found(input_filepath, output_filepath)
    with open(input_filepath, 'r') as input_file:
        res_dict = {MAIL: {}, REGISTER: {}}
        try:
            data_files = json.load(input_file)
        except json.decoder.JSONDecodeError:
            return 'Input file is empty'

        for user in data_files.values():
            for key in user.keys():
                if key == REGISTER:
                    res_dict[REGISTER][user[key]] = res_dict.get(user[key], 0)+1
                elif key == MAIL:
                    mail_host = user[key][user[key].find('@')+1:]
                    res_dict[MAIL][mail_host] = res_dict.get(mail_host, 0)+1
        res_dict = dict_path(res_dict)
    with open(output_filepath, 'w') as output_file:
        json.dump(res_dict, output_file)
