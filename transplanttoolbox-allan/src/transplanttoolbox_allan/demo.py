from __future__ import division, print_function, absolute_import
import argparse
import sys
import logging
from pkgutil import get_data

#data = get_data('transplanttoolbox_allan', 'UNOS_conversion_table_with_rules.csv')


import os
import re
import requests   
import operator
import glob
#import transplanttoolbox_allan.hla 
#from transplanttoolbox_allan.hla import allele_truncate, locus_string_geno_list, expand_ac, single_locus_allele_codes_genotype

#from transplanttoolbox_allan import __version__

__author__ = "Gragert Lab"
__copyright__ = "Gragert Lab"
__license__ = "gpl3"

#_logger = logging.getLogger(__name__)

allele_to_ag_dict = {}
population_allele_frequencies = {}
allele_frequencies = {}


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(BASE_DIR)
#STATIC_DIR = os.path.join(BASE_DIR,"transplanttoolbox_allan")
### Dictionary with alleles and equivalent antigens

#UNOS_conversion_table_filename = "./src/transplanttoolbox_allan/UNOS_conversion_table_with_rules.csv"
UNOS_conversion_table_filename = os.path.join(BASE_DIR,"transplanttoolbox_allan/UNOS_conversion_table_with_rules.csv")
UNOS_conversion_table_file = open(UNOS_conversion_table_filename, 'r')
#for row in UNOS_conversion_table_file:
	#print(row)




race_list = ["AAFA", "AFA", "CAU", "HIS", "NAM", "AFB", "AINDI", "API",
			 "AISC", "ALANAM", "AMIND", "CARB", "CARHIS", "CARIBI", 
			"EURCAU", "FILII", "HAWI", "JAPI", "KORI", "MENAFC", "MSWHIS", "NCHI", "SCAHIS", "SCAMB", "SCSEAI", "VIET"] 



for pop in race_list:
	file = BASE_DIR + "/transplanttoolbox_allan/freqs_6loc/" + pop + ".ARS.freqs"
	#print(file)
	freq_file = open(file, 'r')
	for line in freq_file:
		if line.startswith("Haplo"):
			continue
		else:
			line_split = line.split(",")
			allele_list = line_split[0]
			count = line_split[1]
			haplotype_frequency = line_split[2]
			allele_split = allele_list.split("~")

			for allele in allele_split:
				allele = allele.rstrip("g")
				key = pop + "%" + allele
				if key in population_allele_frequencies:
					population_allele_frequencies[key] += float(haplotype_frequency)
				else:
					population_allele_frequencies[key] = float(haplotype_frequency)


