#This code takes the BEC energy and add the kinetic energy of the BH
#and the potential energy if n .gt. 1

import numpy as np

dirs = ["15_2_10_05/",
"15_2_10_1/",
"15_2_10_15/",
"15_2_10_2/",
"15_2_5_05/",
"15_2_5_1/",
"15_2_5_15/",
"15_2_5_2/",
"15_6_10_05/",
"15_6_10_1/",
"15_6_10_15/",
"15_6_10_2/",
"15_6_5_05/",
"15_6_5_1/",
"15_6_5_15/",
"20_2_5_15/",
"20_2_5_2/",
"20_6_5_1/",
"20_6_5_2/"]
base_dir = "/media/curi99/TOSHIBA EXT/binary_core_BH/"
for dir in dirs:

    print(dir)

    tv1 = np.loadtxt(base_dir+dir+"black_hole_1_vxyz.t.asc")
    tv2 = np.loadtxt(base_dir+dir+"black_hole_2_vxyz.t.asc")

    tr1 = np.loadtxt(base_dir+dir+"black_hole_1_xyz.t.asc")
    tr2 = np.loadtxt(base_dir+dir+"black_hole_2_xyz.t.asc")

    E = np.loadtxt(base_dir+dir+"E.t.asc")

    t = E[:,0]
    EBEC = E[:,1]

    v1x = tv1[:,1]
    v2x = tv2[:,1]
    v1y = tv1[:,2]
    v2y = tv2[:,2]
    v1z = tv1[:,3]
    v2z = tv2[:,3]

    x1 = tr1[:,1]
    x2 = tr2[:,1]
    y1 = tr1[:,2]
    y2 = tr2[:,2]
    z1 = tr1[:,3]
    z2 = tr2[:,3]
    m1 = 1.0
    m2 = float(dir[3:4])
    print("m2=",m2)
    M  = m1 + m2
    K = []
    W = []
    algo = True
    tCol = 0.0
    for i in range(len(v1x)):
        if(i < len(v2x)):
            v1 = np.sqrt(v1x[i]**2 + v1y[i]**2 + v1z[i]**2)
            v2 = np.sqrt(v2x[i]**2 + v2y[i]**2 + v2z[i]**2)
            k0 = 0.5 * m1 * v1**2 + 0.5 * m2 * v2**2
        else:
            if algo:
                algo = False
                print(t[i])
                tCol = t[i]
            v1 = np.sqrt(v1x[i]**2 + v1y[i]**2 + v1z[i]**2)
            k0 = 0.5 * M * v1**2
        K.append(k0)

    for i in range(len(x1)):
        if(i < len(v2x)):
            dx = x1[i]-x2[i]
            dy = y1[i]-y2[i]
            dz = z1[i]-z2[i]
            r = np.sqrt(dx**2+dy**2+dz**2)
            w0 = -m1*m2/(4.0*np.pi*r)
        else:
            w0 = 0
        W.append(w0)

    #KineticBH
    with open(base_dir+dir+'KineticBH.txt', 'w') as f:
        for i in range (len(K)):
            f.write(str(t[i])+" "+str(K[i]) + '\n')

    #PotentialBH
    with open(base_dir+dir+'WBH.txt', 'w') as f:
        for i in range (len(W)):
            f.write(str(t[i])+" "+str(W[i]) + '\n')

    #EBEC + EBHs
    with open(base_dir+dir+'E_TOTAL.txt', 'w') as f:
        for i in range (len(W)):
            f.write(str(t[i])+" "+str(W[i]+K[i]+EBEC[i]) + '\n')

    #EBEC + EBHs
    with open(base_dir+dir+'tCol.txt', 'w') as f:
        f.write(str(tCol) + '\n')
