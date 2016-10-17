set terminal png size 1024,768
set output "target.png"

set yrange[-0.3:3.1]
set xrange[0:19]

set ytics ("CONCEPTO" 0, "LETRA/FORMA" 1, "COLOR" 2, "RUIDO" 3)

set xtics ("movistar" 17, "chevrolet" 2, "mcdonalds1" 9, "america" 13, "cocacola2" 4, "farmacity" 14, "honda" 5, "claro" 16, "disco" 11, "addidas" 7, "havana" 10, "facebook" 8, "vw" 3, "unicenter" 18, "android" 15, "audi" 12, "cocacola" 1, "superman" 6) rotate by -45

plot "target.data" using 1:2:(0.8+150*$3):3 with points pt 7 ps var lt palette t ''
