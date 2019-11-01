from sys import argv
from os.path import exists

script, from_file, to_file = argv

print (f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how ?
in_file = open(from_file).read()

print (f"""The input file is {len(in_file)} bytes long
Does the output file exist ? {} 
Ready, hit RETURN to continue, CTRL-C to abort.
""") # len(in_file) mencari panjang data dalam file , exists(to_file) mencari keberadaan file

input ()

out_file = open(to_file, 'w').write(in_file) # menulis atau mengcopy ke file yang dimasukkan

print("Alright, all done.")
