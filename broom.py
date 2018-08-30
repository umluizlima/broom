"""Functions for cleaning and organizing folders."""

import os
import shutil


def repeat_checking(src, dst, filename):
    if os.path.lexists(os.path.join(dst, filename)):
        n = 1
        root, ext = os.path.splitext(filename)
        while os.path.lexists(os.path.join(dst, f'{root}({n}){ext}')):
            n += 1
        new_filename = f'{root}({n}){ext}'
        os.rename(
            os.path.join(src, filename),
            os.path.join(src, new_filename)
        )
        return new_filename
    else:
        return filename


def run():
    user = os.path.expanduser('~')
    src = os.path.join(user, 'Desktop')
    dst = os.path.join(user, 'Downloads', 'Rug')

    try:
        os.makedirs(dst)
    except OSError:
        pass

    for filename in os.listdir(src):
        filename = repeat_checking(src, dst, filename)
        shutil.move(
            os.path.join(src, filename),
            os.path.join(dst, filename)
        )


if __name__ == "__main__":
    run()
