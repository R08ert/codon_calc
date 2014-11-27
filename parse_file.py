__author__ = 'Laura'
import csv
import re
from SequenceProcessor import Codon

class SequenceReader:
    def __init__(self, inputfilename = None, outputfilename=None):
        self.inputfile = inputfilename
        self.outputfile = outputfilename
        self.codon = None

    def read_file(self):
        with open(self.inputfile, 'rb') as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.readline(),[',',';','\t'])
            csvfile.seek(0)
            sequencereader = csv.reader(csvfile, dialect)
            for sequence in sequencereader:
                self.validate_input(sequence)
                self.codon = Codon(sequence[0])
                # print sequence

    def validate_input(self, sequence):
        if len(sequence[0]) % 3 is  not 0:
            print "Error in sequence " + str(sequence)
            print "Length is: " + str(len(sequence[0]))
        if not re.match("^[AaGgCcTtUu]*$", sequence[0]):
            print "invalid value in sequence " + str(sequence[0])

