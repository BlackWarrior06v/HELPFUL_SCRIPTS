set pm3d map
set size ratio -1

set style line 1 lc rgb 'red' pt 7 ps 1
set style line 2 lc rgb 'blue' pt 7 ps 1

set xrange[-40:40]
set yrange[-40:40]

do for [k=1:99] {
    set term jpeg
    set output sprintf("Orbiting_BH_IMG/ImageColor_%d.jpg", k)
    splot 'Orbiting_BH/rho.xy.asc' i k notitle with pm3d, 'Orbiting_BH/black_hole_1_xyz.t.asc' i k u 1:2:(0) notitle w p ls 2,'Orbiting_BH/black_hole_2_xyz.t.asc' i k u 1:2:(0) notitle w p ls 1
    set output
}
