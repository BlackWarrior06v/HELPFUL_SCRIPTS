# Read the file contents
with open('binary_Angular.par', 'r') as file:
    lines = file.readlines()

# Define the numerical values to add
rho = ["1.5d0","2.0d0"]
MBH = ["2.0d0","6.0d0"]
y_0 = ["5.0d0","10.0d0"]
vx0 = ["0.05d0","0.1d0","0.15d0","0.2d0"]

rhonames = ["15","20"]
MBHnames = ["2","6"]
y_0names = ["5","10"]
vx0names = ["05","1","15","2"]

for i in range (len(rho)):
    for j in range(len(MBH)):
        for k in range(len(y_0)):
            for l in range(len(vx0)):
                # Define the parameters of ur simulations
                new_lines = [f"rhoc2={rho[i]}\n",
                             f"MBH2={MBH[j]}\n",
                             f"yBH={y_0[k]}\n",
                             f"vxBH={vx0[l]}\n"]
                
                # Insert new lines before the last line
                lines_new_files = lines[:-1] + new_lines + lines[-1:]

                # Write the modified content to a new file
                with open(f'binary_rho{rhonames[i]}_MBH{MBHnames[j]}_y{y_0names[k]}_v{vx0names[l]}.par', 'w') as file:
                    file.writelines(lines_new_files)                    
