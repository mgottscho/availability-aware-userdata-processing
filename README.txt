============== SPLIT ===============
run: $ sh split.sh <path_to_file>
purpose: splits a user's data into its general categories

============== REMOVE_REDUNDANCIES ===============
run: $ python remove_redundancies.py <path_to_file>
purpose: remove redundant values from a file

============== CLEAN_DATA ===============
run: $ python clean_data.py <path_to_file> <descriptor>
purpose: prepares data in CSV for subsequent analysis, splits files by descriptor.
		A descriptor is a word such as "voltage" (don't write the quotes) that
		corresponds to the final semantic description of the data in a file. We
		assume these are unique for a given file. 

