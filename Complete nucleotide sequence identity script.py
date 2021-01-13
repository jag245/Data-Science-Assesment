#Script to assess total nucleotide identity between two sets of genomic sequence data (comparing genomic  data sets from Barley yellow dwarf virus isolates.)

import pandas as pd

k460_file_handle = open('Barley_Yelllow_Dwarf_Virus_Ker_III_K460_sequence.txt', 'r')

k439_file_handle = open('Barley_Yellow_Dwarf_Virus_Ker_II_K439_sequence.txt', 'r')

k439_sequence_string = (k439_file_handle.read())

k460_sequence_string = (k460_file_handle.read())

k439_file_handle.close()

k460_file_handle.close()

k439_sequence_list = list(k439_sequence_string)

k460_sequence_list = list(k460_sequence_string)

nucleotide_identity=[]

nucleotide_position_index=[]

while (len(k460_sequence_list))  == (len(k439_sequence_list)):
    for index, nucleotide_k439 in enumerate(k439_sequence_list):
        if k460_sequence_list[index] == k439_sequence_list[index]:
            nucleotide_identity.append("100%")
            nucleotide_position_index.append(index)
        elif (k439_sequence_list[index] == '-') or (k460_sequence_list[index] == '-'):
            nucleotide_identity.append("Gap")
            nucleotide_position_index.append(index)
        elif k439_sequence_list[index] != k460_sequence_list[index]:
            nucleotide_identity.append("0%, " + k439_sequence_list[index] + ":" + k460_sequence_list[index])
            nucleotide_position_index.append(index)
    print(nucleotide_identity)
    print(nucleotide_position_index)
    break   
    
data_dictionary = {'Index':nucleotide_position_index,'Pairwise nucleotide identity':nucleotide_identity}

df = pd.DataFrame(data_dictionary)

df.to_excel(excel_writer="Comparative Genomics Sequence Identity.xls", sheet_name="Sequence Identity", index=False)

nucleotide_identity.clear()
nucleotide_position_index.clear()