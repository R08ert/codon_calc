from optparse import OptionParser
from parse_file import SequenceReader

def main():
    usage = "usage: %prog [-i] csvfile [-o] outputfilename"
    parser = OptionParser(usage)
    parser.add_option("-i", "--inputfilename", dest = "inputfilename" ,
                  help = "read sequence from csv input FILE", metavar = "FILE")
    parser.add_option("-o", "--outputfile", dest = "outputfilename",
                  help="write sequence to pdf output file")

    (options,args)= parser.parse_args()


    seqio = SequenceReader(options.inputfilename, options.outputfilename)
    seqio.read_file()
    seqio.codon.make_codons()


if __name__ == "__main__":
    main()
