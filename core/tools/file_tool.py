import os
from datetime import datetime
from pathlib import Path

from selene import factory


def capture_screenshot(prefix):
    dr = factory.get_shared_driver()
    home = str(Path.home())
    directory = home + '/Documents/py_scr/'

    if not os.path.isdir(directory):  # check is dir exist
        os.mkdir(directory)

    time_str = datetime.today().strftime('%Y-%m-%d %H_%M_%S')
    file_name = prefix + '_' + time_str + '.png'

    dr.save_screenshot(directory + file_name)
    print('--> Screenshot captured : ' + directory + file_name)