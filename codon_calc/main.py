from optparse import OptionParser

from codon_calc.sequence_processor import SequenceProcessor


def main():
    usage = "usage: %prog [-i] csvfile [-o] outputfilename"
    parser = OptionParser(usage)
    parser.add_option("-i", "--inputfilename", dest = "inputfilename" ,
                  help = "read sequence from csv input FILE", metavar = "FILE")
    parser.add_option("-o", "--outputfile", dest = "outputfilename",
                  help="write sequence to pdf output file")

    (options,args)= parser.parse_args()


    seqio = SequenceProcessor(options.inputfilename, options.outputfilename)
    seqio.process_sequence()
    seqio.codon.populate_codon_dictionary()
    seqio.codon.print_codon_dictionary()


if __name__ == "__main__":
    main()
