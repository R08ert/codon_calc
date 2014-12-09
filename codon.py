__author__ = 'Laura'
import itertools
from collections import OrderedDict


 # CodonsDict = {'TTT': 0, 'TTC': 0, 'TTA': 0, 'TTG': 0, 'CTT': 0,
 #   'CTC': 0, 'CTA': 0, 'CTG': 0, 'ATT': 0, 'ATC': 0,
 #   'ATA': 0, 'ATG': 0, 'GTT': 0, 'GTC': 0, 'GTA': 0,
 #   'GTG': 0, 'TAT': 0, 'TAC': 0, 'TAA': 0, 'TAG': 0,
 #   'CAT': 0, 'CAC': 0, 'CAA': 0, 'CAG': 0, 'AAT': 0,
 #   'AAC': 0, 'AAA': 0, 'AAG': 0, 'GAT': 0, 'GAC': 0,
 #   'GAA': 0, 'GAG': 0, 'TCT': 0, 'TCC': 0, 'TCA': 0,
 #   'TCG': 0, 'CCT': 0, 'CCC': 0, 'CCA': 0, 'CCG': 0,
 #   'ACT': 0, 'ACC': 0, 'ACA': 0, 'ACG': 0, 'GCT': 0,
 #   'GCC': 0, 'GCA': 0, 'GCG': 0, 'TGT': 0, 'TGC': 0,
 #   'TGA': 0, 'TGG': 0, 'CGT': 0, 'CGC': 0, 'CGA': 0,
 #   'CGG': 0, 'AGT': 0, 'AGC': 0, 'AGA': 0, 'AGG': 0,
 #   'GGT': 0, 'GGC': 0, 'GGA': 0, 'GGG': 0}


class Codon:
    def __init__(self, sequence = None ):
        # self.frequency_dict = OrderedDict(None)
        self.frequency_dict = {}
        self.sequence = sequence

    #creates a dictionary of codons from a sequence
    #if the codon exists, the frequency key is incremented
    def populate_codon_dictionary(self):
        seqiter = iter(self.sequence)
        while seqiter is not None:
            frequency = 1
            try:
                codon = str(seqiter.next())+str(seqiter.next())+str(seqiter.next())
                if codon in self.frequency_dict.keys():
                    updatefreq = self.frequency_dict[codon]
                    updatefreq = updatefreq + frequency
                    self.frequency_dict[codon] = updatefreq
                else:
                    self.frequency_dict[codon] = frequency

            except StopIteration:
                break;

    def identify_low_use_codon(self, threshold):
        threshold = 1
        low_use_codons = []
        for k, v in self.frequency_dict.iteritems():
            print k, v
            if v < threshold:
                low_use_codons.append(k)
        return low_use_codons

    def print_codon_dictionary(self):
        print "len: " + str(len(self.frequency_dict))
        for k, v in self.frequency_dict.iteritems():
            print "codon: " + str(k) + " frequency " + str(v)






#sequence length 3 bases to 100,000
#treat as a graph; each codon represents list of three elements or a tuple
# key of dictionary should be frequency of codon usage.

