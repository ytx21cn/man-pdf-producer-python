import os
from sys import argv
import subprocess as sp
from os.path import abspath

from print_in_colors import FgColor, BgColor, get_colored_str


def main():

    generated_dir = './pdf'
    os.makedirs(generated_dir, exist_ok=True)

    if not (len(argv) >= 2):
        print('Usage: python3 %s <list_of_man_pages>' % __file__)
        exit(-1)

    with open(argv[1]) as infile:

        comment_line_start = '#'

        for line in infile:
            line = line.strip()
            # ignore empty lines
            if (not line) or line.isspace():
                continue
            # also, ignore comment lines (i.e. start with '#')
            elif line[:len(comment_line_start)] == comment_line_start:
                continue

            # handle each man page entry
            # each line is a single man page entry
            generated_file_path = abspath('%s/%s.pdf' % (generated_dir, line))

            # skip the pdf file if already existent
            if os.path.exists(generated_file_path):
                completion_mark = get_colored_str('[!]', fg_color=FgColor.BLACK, bg_color=BgColor.BROWN)
                print('%s "%s" exists, skipping' % (completion_mark, generated_file_path))
                continue

            # otherwise, generate the pdf
            # for this part, see:
            # https://docs.python.org/3/library/subprocess.html#replacing-shell-pipeline
            generate_man_cmd = sp.Popen(['man', '-t', line], stdout=sp.PIPE)
            generate_pdf_cmd = sp.Popen(['ps2pdf', '-', generated_file_path], stdin=generate_man_cmd.stdout)
            generate_man_cmd.stdout.close()
            generate_pdf_cmd.communicate()

            completion_mark = get_colored_str('[#]', fg_color=FgColor.BLACK, bg_color=BgColor.GREEN)
            print('%s "%s" generated' % (completion_mark, generated_file_path))


if __name__ == '__main__':
    main()
