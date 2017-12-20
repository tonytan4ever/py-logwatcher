from optparse import OptionParser


def main():
    # command-line parsing
    cmdline = OptionParser(usage="usage: %prog [options] logfile",
        description="Print log file lines that have not been read.")
    cmdline.add_option("--offset-file", "-o", action="store",
        help="File to which offset data is written (default: <logfile>.offset).")
    cmdline.add_option("--paranoid", "-p", action="store_true",
        help="Update the offset file every time we read a line (as opposed to"
             " only when we reach the end of the file).")
    cmdline.add_option("--every-n", "-n", action="store",
        help="Update the offset file every n'th time we read a line (as opposed to"
             " only when we reach the end of the file).")
    cmdline.add_option("--no-copytruncate", action="store_true",
        help="Don't support copytruncate-style log rotation. Instead, if the log file"
             " shrinks, print a warning.")
    cmdline.add_option("--version", action="store_true",
        help="Print version and exit.")

    options, args = cmdline.parse_args()