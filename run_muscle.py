import os
from datetime import datetime

def muscle(protein_cluster):
    aligned_out = protein_cluster+'.afa'
    os.system('muscle -in {0} -out {1} -quiet'.format(protein_cluster,aligned_out))


