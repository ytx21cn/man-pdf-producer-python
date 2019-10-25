import os, sys, subprocess as sp

def main():

    generatedDir = './pdf'
    os.makedirs(generatedDir, exist_ok=True)

    argv = sys.argv
    if not (len(argv) >= 2):
        print('Usage: python3 man_pdf_producer.py <list_of_man_pages>')
        exit(-1)

    with open(argv[1]) as infile:

        commentLineStart = '#'

        for line in infile:
            line = line.strip()
            # ignore empty lines
            if (not line) or line.isspace():
                continue
            # also, ignore comment lines
            elif line[:len(commentLineStart)] == commentLineStart:
                continue

            # each line is a man command minus the "man" at the beginning
            line = line.split(' ')

            # for this part, see:
            # https://docs.python.org/3/library/subprocess.html#replacing-shell-pipeline
            generateMan = sp.Popen(['man', '-t'] + line, stdout=sp.PIPE)
            generatedFileName = '%s.pdf' % (','.join(line))
            generatePdf = sp.Popen(['ps2pdf', '-', '%s/%s' % (generatedDir, generatedFileName)], stdin=generateMan.stdout)
            generateMan.stdout.close()
            generatePdf.communicate()
            pass

if __name__ == '__main__':
    main()
