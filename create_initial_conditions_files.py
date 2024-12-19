basepar = 'binary_Angular.par'

# Supposing every par filename ends with .par
base = basepar[:-4] 
print(base)

# Read the file contents
with open(basepar, 'r') as file:
    lines = file.readlines()
# Remove empty lynes
lines = [line for line in lines if line.strip()] 

# Define the numerical values to add
numerical_values = [["1.5d0","2.0d0"],                   #rho
                    ["2.0d0","6.0d0"],                  #MBH
                    ["5.0d0","10.0d0"],                 #y
                    ["0.05d0","0.1d0","0.15d0","0.2d0"]]#v

# Define the labels of the final par filename
labels_value = [["15","20"],  #rho
          ["2","6"],          #MBH
          ["5","10"],         #y
          ["05","1","15","2"]]#v

labels = ["rhoc2","MBH2","yBH","vxBH"]

for i, label_value in enumerate(labels_value):
    for value in label_value:
        value = labels[i]+value
print(labels_value)

for i in range (len(numerical_values[0])):
    for j in range(len(numerical_values[1])):
        for k in range(len(numerical_values[2])):
            for l in range(len(numerical_values[3])):
                # Define the parameters of ur simulations
                new_lines = [f"{labels[0]}={numerical_values[0][i]}\n",
                             f"{labels[1]}={numerical_values[1][j]}\n",
                             f"{labels[2]}={numerical_values[2][k]}\n",
                             f"{labels[3]}={numerical_values[3][l]}\n"]
                
                # Insert new lines before the last line
                lines_new_files = lines[:-2] + new_lines + lines[-2:]

                # Write the modified content to a new file
                with open(f'{base}{labels_value[0][i]}_MBH{labels_value[1][j]}_y{labels_value[2][k]}_v{labels_value[3][l]}.par', 'w') as file:
                    file.writelines(lines_new_files)                    
