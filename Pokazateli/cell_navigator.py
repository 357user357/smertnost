
basis_cells = [ "A", "B", "C",      "D", "E", "F",      \
                "G", "H", "I",      "J", "K", "L",      \
                "M", "N", "O",      "P", "Q", "R",      \
                "S", "T", "U",      "V", "W", "X",      \
                "Y", "Z" ]

#print(basis_cells)

array_columns_basis = {}
array_columns_basis_letters_to_index = {}

array_columns = {}



for cell_number_for_letter in range(0,26):
    #if len( str(cell_number_for_letter) ) == 1:
    #    cell_number_for_letter = "0" + str(cell_number_for_letter)
    #array_columns = [basis_cells[cell_number_for_letter]]
    
    array_columns_basis[cell_number_for_letter] = basis_cells[cell_number_for_letter]

    array_columns_basis_letters_to_index[ basis_cells[cell_number_for_letter] ] = cell_number_for_letter + 1

#print(array_columns_basis_letters_to_index)


array_columns = array_columns_basis

array_columns_letters_to_index = array_columns_basis_letters_to_index


#print(array_columns)

initial_padding_number_for_columns = 25

increment_for_columns = 1

for cell_number_for_letter in range(0,26):
    #if len( str(cell_number_for_letter) ) == 1:
    #    cell_number_for_letter = "0" + str(cell_number_for_letter)
    #array_columns = [basis_cells[cell_number_for_letter]]    
    #array_columns[cell_number_for_letter + 27] = basis_cells[cell_number_for_letter]
    #for first_index_columns in range(0,26):
    #    array_columns[first_index_columns] = 
    #print(array_columns[0][0])
    #for ii in range(0,26):
    #    print(array_columns[ii])
    #print(basis_cells[cell_number_for_letter])
    ##################print("cell_number_for_letter = " + str(cell_number_for_letter) )

    for cell_second_number_for_letter in range(0,26):
        
        #print("cell_second_number_for_letter = " + str(cell_second_number_for_letter) )

        array_columns[initial_padding_number_for_columns + increment_for_columns ] = \
            basis_cells[cell_number_for_letter] + basis_cells[cell_second_number_for_letter]

        array_columns_letters_to_index[  basis_cells[cell_number_for_letter] + basis_cells[cell_second_number_for_letter]  ] = \
            initial_padding_number_for_columns + increment_for_columns + 1

        increment_for_columns += 1


    

#print(array_columns_letters_to_index)
#quit()

