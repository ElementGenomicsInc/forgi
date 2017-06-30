#!/usr/bin/python

from __future__ import print_function
import sys
import os.path as op
import forgi.threedee.model.coarse_grain as ftmc

from optparse import OptionParser

def main():
    usage = """
    ./pdb_to_ss_fasta.py pdb_file

    Take a pdb file, extract the secondary structure and print it out
    as a fasta file like this:

        >id
        sequence
        secondary structure

    Where the id will be the part of the filename without the extension.
    """
    num_args= 1
    parser = OptionParser(usage=usage)

    #parser.add_option('-o', '--options', dest='some_option', default='yo', help="Place holder for a real option", type='str')
    #parser.add_option('-u', '--useless', dest='uselesss', default=False, action='store_true', help='Another useless option')
    parser.add_option('-c', '--chain', dest='chain', default=None, help="Extract the secondary structure of a particular chain in the PDB file")
    parser.add_option('-p', '--pseudoknots', dest='pseudoknots', default=False, action='store_true', help='Include pseudoknots?')

    (options, args) = parser.parse_args()

    if len(args) < num_args:
        parser.print_help()
        sys.exit(1)

    #pdb_id = op.basename(op.splitext(args[0])[0])
    cg = ftmc.from_pdb(args[0], chain_id=options.chain, remove_pseudoknots = not options.pseudoknots)

    print(cg.to_fasta_string())

if __name__ == '__main__':
    main()

