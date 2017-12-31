import operator


def evaluate(variable, operat, number):
    all_operators = {"==" : operator.eq, ">=" : operator.ge, "<=" : operator.le, ">" : operator.gt, "<" : operator.lt, "!=" : operator.ne}
    return all_operators[operat](variable ,number)

def find_max(alist, start_max=0):
    maximum = start_max
    minimum = alist[0]
    for entry in alist:
        if entry > maximum:
            maximum = entry
        if entry < minimum:
            minimum = entry
    #index = alist.index(maximum)
    return maximum, minimum


def and_or_trick(string):
    instructions = string.split("\n")
    decomposed = [inst.split() for inst in instructions]
    variables = {}
    all_over_max = 0
    for inst in decomposed:
        if not inst[0] in variables:
            variables[inst[0]] = 0
    for instruction in decomposed:
        if evaluate(variable=int(variables[instruction[4]]), operat=instruction[5], number=int(instruction[6])):
            if instruction[1] == "inc":
                variables[instruction[0]] += int(instruction[2])
            if instruction[1] == "dec":
                variables[instruction[0]] -= int(instruction[2])
            all_over_max = find_max(list(variables.values()),all_over_max)[0]
    return find_max(list(variables.values())), all_over_max        

test="""b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""

print(and_or_trick(test))

puzzle_input = """um inc -671 if lbf != 5
j inc 236 if umr > -6
fk inc -246 if j < 241
uy dec -404 if mmw <= 2
j inc 372 if gk >= -1
uy inc -380 if umr > -4
dy inc 257 if es > -9
es dec 769 if es < 4
t inc -429 if umr >= 0
hg dec 13 if dy < 267
is inc 66 if fk == -246
fk inc -30 if es > -775
ada inc 258 if umr > 3
eri inc -950 if lx > -4
umr dec -789 if x >= -4
um inc -783 if aao > -7
j inc -97 if ada != -1
es inc 406 if fk != -283
lx inc 43 if kg <= 7
f inc 464 if lx <= 44
kg inc 884 if t >= -435
mmw inc 836 if gk > -3
a dec 496 if um > -1447
eri dec -617 if uy == 24
j inc -858 if kg < 886
hg dec -854 if umr == 789
dy dec -246 if f >= 457
lbf inc 122 if a != 10
aao inc -408 if uy > 19
f dec 908 if uy != 18
t dec -775 if j >= -351
t inc -594 if yk <= 3
es inc 28 if gk == 0
es inc -306 if kg >= 894
mmw dec 154 if kg <= 885
dy inc 832 if aao <= -402
lx inc -426 if a >= -8
umr dec -792 if eri > -341
a inc -609 if gk <= -6
j dec -970 if lx > -393
uy dec -241 if yk > 0
yk inc 411 if is > 61
ada dec -253 if is == 66
is dec -486 if aao > -413
yk dec 561 if a == 0
dy inc 976 if um == -1454
dy inc 885 if eri < -331
hg inc -5 if gk <= -9
t dec 717 if f <= -443
mmw inc -293 if lx <= -379
t inc 77 if lx != -383
uy dec -89 if ada <= 258
fk inc -381 if fk < -272
eri dec 711 if mmw < 398
is dec -273 if gk != -3
umr dec 384 if aao != -414
is dec -36 if is != 825
ada dec 422 if es < -326
fk inc 207 if mmw < 389
uy dec -357 if lx == -383
es inc 829 if dy <= 3199
aao dec -173 if gk == 0
x dec 274 if is >= 824
t dec -400 if is <= 833
fk dec -677 if f == -444
x inc -494 if j == 623
t dec -406 if f < -443
gk dec 704 if gk == 0
x inc -637 if x < -758
x dec 194 if gk != -710
um inc 956 if fk > 26
ada inc -527 if aao > -239
j inc -774 if f <= -436
es inc -121 if ada > -689
hg dec -461 if gk < -698
t inc 780 if is < 828
yk inc -858 if es >= 504
dy inc 145 if j > -159
is inc 929 if f != -453
mmw inc 702 if fk > 17
lbf dec 123 if aao >= -240
hg dec -543 if a == 0
kg dec -610 if es > 488
hg inc -726 if hg < 1854
kg dec -410 if j <= -146
dy inc -469 if gk <= -712
a inc 252 if aao > -237
dy dec 168 if uy <= 478
gk inc -530 if a > 244
gk dec -254 if uy == 479
es inc -960 if j > -152
umr dec 561 if hg != 1126
uy inc 420 if j < -148
mmw inc 976 if j < -142
umr dec -852 if gk >= -1238
aao dec 559 if eri >= -1042
gk inc -745 if j <= -142
t dec 183 if hg < 1112
t inc 725 if yk == -150
lbf dec -142 if kg < 1912
mmw dec -908 if is <= 1758
um inc 329 if f == -447
x dec 543 if ada > -704
gk inc 226 if eri <= -1041
es dec -176 if mmw == 2975
ada inc -156 if eri >= -1053
ada inc -523 if t <= 1347
aao inc -717 if x < -2145
gk inc -236 if t >= 1354
lx dec -266 if lx != -389
hg dec -324 if dy >= 3169
f dec 96 if x != -2143
yk inc -270 if um != -1450
aao inc -916 if lbf == 141
es inc -943 if f == -540
a dec 974 if lbf > 131
dy dec -35 if yk == -413
kg inc 112 if eri >= -1053
mmw inc -30 if gk <= -1754
um dec -288 if mmw < 2978
es dec 774 if uy == 900
t dec -60 if x > -2145
j inc 1 if x > -2148
dy inc 222 if es >= -1232
is dec -221 if x != -2142
hg dec -626 if uy > 887
is dec -114 if t <= 1408
j inc -564 if umr == 1488
a inc -29 if f != -540
umr dec 373 if fk != 17
a dec -788 if fk >= 14
ada inc 316 if aao >= -1153
x dec 970 if lbf != 141
x dec -209 if aao >= -1159
uy dec 279 if lx != -117
f dec 517 if hg >= 2065
j dec 566 if a <= 75
x dec -346 if a <= 59
t inc 576 if lx > -118
um dec 785 if es >= -1229
a dec -949 if mmw > 2974
j inc 915 if x <= -1929
hg inc 177 if is < 1873
is inc -678 if f >= -1052
umr dec 254 if lx > -123
x dec 754 if um < -1160
aao dec 977 if uy <= 894
yk inc -157 if aao <= -2124
um inc 631 if is >= 1867
lx inc -99 if ada <= -1058
fk dec -834 if x < -2695
is dec 105 if x != -2680
a inc 462 if umr <= 864
mmw inc 394 if lbf > 150
gk inc -370 if lbf >= 146
is inc 722 if yk > -586
dy inc -882 if gk != -1753
t inc 983 if gk == -1763
fk dec 874 if fk > 14
hg dec -949 if lbf < 142
es dec -592 if uy == 891
dy dec 823 if gk >= -1762
mmw dec 137 if gk >= -1751
hg dec 704 if dy >= 2343
t dec -921 if j != -372
x dec 95 if is >= 2485
dy inc -117 if kg >= 2017
gk dec 551 if um <= -545
ada inc -161 if umr >= 856
mmw inc 633 if umr != 862
fk dec 38 if lbf >= 140
kg dec -954 if x >= -2787
um inc 325 if hg > 2481
um dec -72 if j > -375
umr dec 910 if gk <= -1756
fk dec -628 if j != -356
mmw dec 267 if aao != -2123
eri inc -857 if um != -137
um inc -651 if eri != -1896
j dec -122 if a >= 1473
umr dec 177 if gk == -1753
mmw inc -16 if t > 2911
eri dec 502 if um <= -785
hg inc 134 if x != -2775
lx dec 263 if kg <= 2978
hg dec 83 if es != -1235
mmw dec -837 if umr <= 693
dy inc 148 if um < -792
gk inc -13 if j > -247
x dec 749 if yk >= -568
lbf inc 606 if is != 2489
x inc 588 if dy >= 2345
dy dec 243 if yk <= -574
umr dec 1 if es == -1233
f dec 104 if t == 2903
aao dec 32 if es != -1224
x inc 882 if j < -245
hg inc -998 if uy == 890
dy dec -605 if dy <= 2115
hg inc 45 if gk != -1769
lbf inc -521 if t > 2894
umr inc -115 if a != 1473
lx dec -795 if x == -2194
t inc 143 if f < -1154
es dec 629 if is > 2494
lbf inc 195 if fk <= -263
fk inc 926 if aao <= -2153
um inc 351 if es != -1230
t dec -541 if lx != 316
mmw inc -329 if mmw != 4178
dy inc 708 if is > 2481
j inc 386 if t != 3050
hg dec 253 if umr == 568
um inc 236 if mmw >= 4172
fk inc -874 if hg != 1328
lbf dec -499 if um != -202
lbf dec 999 if gk > -1774
gk dec 474 if fk > -219
mmw dec -598 if yk > -585
fk inc -508 if t == 3046
mmw inc -638 if x == -2193
f dec 756 if a == 1477
mmw dec -339 if aao > -2161
um inc 109 if lbf <= -578
fk dec -421 if lx < 321
is inc -725 if ada >= -1226
fk dec -458 if ada >= -1226
uy dec -588 if aao <= -2160
ada inc 404 if dy != 3420
x inc 788 if f <= -1910
kg dec -520 if is == 1754
es dec 895 if lbf < -568
fk dec -999 if lbf == -578
kg dec -38 if lbf != -574
uy inc 343 if lbf != -579
is dec -176 if es <= -2125
lbf dec -680 if lbf < -573
eri inc 562 if uy != 1823
x inc 87 if fk >= 1158
umr dec -850 if eri > -1843
um inc -978 if eri <= -1849
x dec 389 if gk < -2241
f inc -288 if a != 1486
kg dec -484 if uy < 1826
lx dec -328 if lbf != 97
um inc -998 if gk <= -2240
yk inc 314 if mmw <= 5120
t dec -884 if es == -2128
uy dec 190 if f <= -2199
lx dec 128 if umr > 1425
eri inc 807 if a > 1485
ada inc 272 if umr < 1422
hg inc 630 if is == 1937
um dec 143 if ada >= -949
eri dec -334 if lx != 637
fk dec 147 if umr < 1426
gk dec 309 if uy == 1631
aao dec 233 if hg == 1336
is dec 825 if yk > -271
lbf dec -498 if umr <= 1413
kg dec 473 if es > -2131
mmw dec -728 if hg != 1327
dy dec 309 if hg <= 1341
dy inc -863 if kg >= 3023
x inc -465 if lx <= 647
a inc 253 if x >= -1793
kg inc -184 if eri < -1500
um inc -527 if lx != 652
j inc -455 if hg > 1328
eri inc 866 if yk != -263
aao inc -47 if gk > -2553
gk inc 228 if gk < -2554
gk inc -493 if fk <= 1006
mmw inc 800 if x == -1784
lbf inc -351 if umr < 1426
a inc -903 if ada > -958
umr inc 942 if es != -2128
dy inc 600 if a < 830
j dec -247 if lx < 646
gk dec -922 if t >= 3930
mmw inc -114 if lx != 654
fk dec 415 if um > -1764
t inc -763 if lbf < -246
ada inc 818 if is > 1108
uy inc -839 if t != 3171
fk inc -335 if is > 1106
fk dec -335 if yk == -263
fk inc -291 if dy == 3711
lx dec -665 if yk != -263
es dec -772 if uy != 792
umr dec -528 if um != -1764
t dec -95 if es < -2137
es inc -800 if yk >= -261
kg inc 150 if j >= -70
f dec -118 if mmw < 6536
a inc 595 if uy > 794
is inc 927 if lx > 636
eri dec -61 if x != -1785
hg inc -878 if yk != -260
gk inc -727 if fk <= 305
mmw dec -945 if a <= 833
aao inc -101 if x >= -1792
hg dec 567 if es > -2131
gk inc -689 if mmw < 7484
ada inc -644 if eri > -1452
yk inc -810 if yk > -265
um dec 655 if aao < -2533
t dec 179 if umr != 1943
gk inc 833 if hg >= -110
fk dec 998 if fk < 315
a dec -558 if aao > -2543
x inc 426 if lbf == -249
uy inc 892 if yk > -1075
umr inc 250 if es <= -2127
mmw inc -727 if umr >= 2193
kg dec 111 if es == -2128
dy dec 898 if fk != -693
yk dec 168 if umr >= 2191
uy dec 113 if dy <= 3711
mmw inc -752 if yk == -1241
yk inc -181 if t > 2989
mmw dec -636 if t < 2995
a inc -424 if hg == -109
j dec -762 if ada > -780
lx dec 565 if uy <= 1577
aao dec 858 if j == 697
fk inc -383 if a < 969
eri inc -51 if lx <= 85
aao inc 666 if j > 690
t dec 234 if a == 964
aao inc -69 if fk > -1085
es inc -721 if gk >= -2215
is inc -185 if lbf > -251
mmw dec 411 if es == -2849
f dec -214 if gk == -2210
yk inc 904 if aao >= -2804
es inc 883 if mmw != 6210
x dec 6 if ada != -774
aao inc -776 if um != -2419
j inc -653 if yk == -344
gk dec 338 if fk != -1072
yk inc -13 if x >= -1360
lbf inc 201 if dy < 3716
yk dec -904 if aao != -3575
f dec 922 if j == 697
uy dec -562 if lbf != -53
gk dec 50 if lbf <= -47
t inc -670 if mmw > 6222
lx inc 515 if uy == 2133
yk inc 261 if dy > 3704
x dec -854 if uy == 2133
kg inc 66 if umr == 2196
kg dec -83 if j != 706
ada inc 739 if gk > -2590
eri dec 379 if eri == -1497
dy inc 638 if aao >= -3583
a dec 130 if is > 1851
mmw dec 399 if uy == 2133
eri inc -195 if f > -2801
j dec 885 if dy > 4339
eri inc -544 if aao == -3587
kg inc 895 if t != 2984
yk inc 258 if dy <= 4350
es dec 660 if dy == 4342
umr inc -92 if gk < -2592
eri inc 361 if x == -504
um dec -298 if gk != -2588
fk dec 532 if j < -184
uy inc 31 if f < -2791
aao dec 31 if j != -182
ada inc 448 if um <= -2113
fk inc -13 if eri <= -1703
t inc -59 if es >= -1971
gk dec -909 if x == -510
es inc 805 if hg >= -112
j dec 734 if kg >= 3919
um inc 369 if aao != -3606
yk inc -548 if dy > 4348
gk inc 934 if j < -182
x dec 346 if hg <= -107
lbf dec -379 if eri != -1718
lbf inc -921 if f >= -2802
mmw inc -191 if eri <= -1703
umr inc 252 if lx != 600
mmw dec 410 if ada >= -330
gk inc 558 if a != 828
mmw dec 320 if um <= -1744
ada dec 517 if t < 2933
is dec -616 if ada > -835
yk dec -406 if j <= -185
yk inc -526 if lbf <= -586
ada inc 368 if j == -188
kg inc -89 if f <= -2791
kg dec -531 if lbf == -590
mmw inc -252 if f < -2787
is inc 293 if eri > -1713
lbf inc 509 if kg <= 4367
eri inc 607 if fk > -1620
f dec -313 if j > -194
ada inc -582 if aao >= -3611
a inc 373 if x == -850
eri dec 668 if ada != -1057
um dec 112 if lbf <= -72
lx inc 91 if t > 2919
a inc 157 if is > 2139
fk inc -207 if a != 1371
um inc 108 if t <= 2929
aao inc 80 if lx >= 681
fk inc 437 if lbf == -81
umr inc 473 if lbf <= -75
eri inc 509 if umr != 2822
a dec -7 if is >= 2146
fk inc -10 if t != 2920
is dec 235 if a > 1358
ada inc -655 if eri == -1201
kg dec 983 if f >= -2486
es dec 640 if t <= 2938
eri dec -700 if is < 1919
ada inc -213 if fk == -1401
hg dec -846 if kg != 3381
f dec 584 if a <= 1361
aao inc 731 if gk != -1107
t inc 823 if kg == 3377
es dec 382 if j > -195
fk inc -83 if ada < -1916
umr inc 948 if eri > -511
a inc -765 if eri == -501
a inc 114 if f > -2478
aao inc 343 if aao == -2798
t inc -172 if eri < -498
fk inc 905 if x < -840
dy dec -731 if a > 597
lx inc 410 if um <= -1744
eri inc -859 if lbf <= -90
fk dec 820 if ada < -1916
yk dec 14 if dy != 5078
aao inc -89 if lbf != -81
umr dec 242 if aao > -2457
f inc -563 if lx <= 1100
uy dec 967 if uy <= 2166
eri dec 984 if lx > 1086
hg dec 816 if mmw <= 4653
hg dec -413 if um == -1753
dy dec -410 if mmw > 4643
uy dec -298 if lx >= 1094
mmw dec -611 if dy > 5483
t dec 471 if is != 1915
fk inc 505 if aao >= -2463
gk dec -947 if fk == -894
es inc -556 if umr >= 3532
es inc 768 if x >= -853
yk dec -865 if aao == -2455
hg inc -481 if a != 609
ada inc 904 if es == -1971
hg dec -518 if um < -1750
yk dec -744 if fk != -889
a inc 410 if f > -3047
dy inc 522 if is >= 1913
um inc 882 if is < 1915
es inc -950 if fk > -889
is dec -211 if is == 1911
kg inc -160 if um == -871
a inc 315 if j == -188
umr inc 840 if eri <= -1479
kg inc -805 if ada <= -1013
um inc 701 if x == -850
a inc 735 if umr == 4375
um inc -413 if lbf != -76
dy inc 310 if mmw <= 5268
lbf inc -210 if dy != 5800
um dec -489 if lx == 1095
fk dec -743 if mmw <= 5258
lx inc 332 if mmw > 5249
hg dec 396 if mmw >= 5251
yk inc -672 if fk > -896
a inc -872 if t >= 3114
a inc 22 if umr >= 4370
es inc 374 if um > -98
uy inc 609 if lx <= 1434
a dec 580 if is >= 2118
hg dec -809 if lx >= 1424
fk dec 451 if aao != -2446
mmw dec -339 if gk < -156
hg inc 566 if gk < -153
hg inc -629 if uy >= 2100
lx dec 314 if a > 1503
lbf dec 173 if lx >= 1109
t dec 107 if ada == -1021
dy inc 421 if mmw <= 5607
is dec 751 if hg != 731
hg inc 844 if hg != 730
eri inc -44 if a == 1505
uy dec 230 if t <= 3002
uy inc -450 if eri < -1521
kg dec 353 if j == -188
lbf inc -100 if mmw >= 5592
umr dec -946 if f >= -3045
t inc 893 if j == -188
lbf dec -263 if hg <= 1572
j inc 22 if umr == 5313
eri dec 598 if aao >= -2463
umr dec -591 if eri > -2130
t dec 489 if dy <= 6230
ada dec -547 if a != 1505
eri dec -38 if dy > 6220
ada inc 895 if is == 1371
is inc -303 if mmw < 5599
uy dec -217 if a <= 1513
a dec -366 if x <= -851
um dec 570 if t < 3411
uy inc -560 if mmw <= 5599
um dec -234 if gk != -152
fk dec 305 if um == -430
lx dec -553 if a > 1505
yk dec -923 if yk < 1335
yk dec 137 if es < -1590
hg dec 737 if es > -1605
yk dec 607 if eri < -2080
um dec -588 if eri != -2097
aao inc -230 if aao != -2455
fk inc -654 if t >= 3398
umr dec 525 if kg != 2064
mmw inc -242 if lbf < -90
lbf dec 682 if aao >= -2462
yk inc -971 if t >= 3402
t dec -403 if fk <= -2296
ada dec 404 if kg == 2059
dy inc 95 if yk < 542
lbf inc 427 if j <= -182
j inc 10 if j <= -179
x dec 524 if f <= -3051
lx dec 326 if gk != -163
umr dec 176 if lx >= 789
um dec 264 if eri == -2089
t inc 197 if eri == -2084
dy dec 574 if es > -1605
lx inc -898 if um >= -110
es dec -845 if um >= -113
es inc -731 if yk < 537
lx dec 424 if f >= -3053
a inc 525 if lx != -535
uy dec 692 if yk > 531
a inc -591 if fk >= -2309
fk dec -204 if aao != -2459
mmw dec -420 if fk <= -2110
yk inc 166 if j < -168
umr inc 535 if gk < -158
eri dec 417 if yk >= 695
umr inc 230 if mmw != 5363
umr inc -36 if lbf < -348
f dec -763 if aao < -2450
uy inc -841 if es >= -1490
is dec -381 if gk >= -167
x dec 981 if hg == 828
f inc 682 if ada == -530
fk inc 268 if uy != -450
dy dec 891 if ada < -529
uy dec 943 if hg != 828
ada dec -496 if a < 907
is dec 380 if gk == -159
aao dec 772 if eri < -2505
umr dec -646 if umr > 6151
dy dec 978 if t == 3809
kg inc -768 if fk > -1834
lbf dec -107 if x <= -1828
lx dec 822 if yk <= 709
umr inc -504 if ada > -533
aao dec -710 if es == -1483
uy inc 17 if hg >= 838
fk dec -48 if a == 914
fk inc -80 if j >= -182
gk inc 339 if um < -113
lbf inc 224 if f != -1603
lbf inc 553 if kg == 1291
umr dec -384 if ada > -535
lx dec -618 if t == 3809
aao dec -291 if ada >= -534
lx dec -385 if f <= -1591
lbf inc -918 if is <= 1069
kg inc 807 if dy != 3871
a dec -120 if eri >= -2509
fk dec 886 if uy == -452
is inc 668 if f == -1600
ada dec 281 if dy >= 3872
aao inc 952 if j > -182
eri inc -279 if kg >= 2098
gk inc -357 if gk <= -153
lbf inc -255 if um == -106
es inc -509 if um < -105
j dec 929 if umr < 6681
is inc 906 if um != -114
ada dec 951 if gk >= -523
aao dec 80 if kg > 2089
t inc 811 if hg < 832
yk inc 303 if f > -1601
gk inc 180 if mmw <= 5351
is dec -639 if umr < 6672
mmw dec -142 if kg <= 2103
fk dec -275 if is != 2643
ada inc 568 if x <= -1822
a dec 677 if yk != 1005
yk inc 111 if es <= -1990
eri inc -17 if eri >= -2793
lbf inc 974 if gk == -516
hg inc -723 if lbf == 337
mmw dec 408 if dy <= 3877
t dec 142 if mmw < 5084
gk dec 53 if yk != 1111
lbf dec -434 if aao != -1344
kg dec -837 if f >= -1593
f inc 513 if eri <= -2804
fk dec -925 if fk >= -2756
t inc 280 if kg != 2100
lx dec 328 if dy < 3880
t inc -359 if j < -1103
es inc 289 if ada < -1203
x dec -414 if gk >= -574
aao dec 710 if dy == 3873
es dec -70 if ada <= -1187
ada dec 883 if j == -1110
is dec -635 if um != -105
is inc 627 if a == 1034
um inc -348 if ada > -1190
mmw dec -270 if uy >= -454
ada dec 362 if is > 3900
eri dec -504 if t != 4541
uy inc 910 if eri >= -2804
es dec 261 if fk < -1821
uy dec -430 if uy >= 456
yk dec -841 if um >= -107
j dec -287 if fk >= -1834
a dec 90 if uy <= 897
lx inc 867 if hg < 819
yk dec 265 if fk >= -1820
is inc -444 if umr >= 6676
kg inc 586 if f == -1600
es dec -298 if uy != 889
mmw inc -896 if gk >= -576
a dec -320 if t >= 4538
t dec -722 if hg >= 819
mmw inc -778 if ada < -1553
um dec -914 if j != -826
kg inc -964 if f < -1605
yk inc -51 if umr >= 6670
um dec 219 if j == -820
dy inc 727 if a == 1264
a dec -817 if kg <= 2692
um dec 99 if fk == -1826
kg dec 302 if uy != 892
j dec -696 if lx <= -688
uy inc -626 if t <= 5268
a dec 961 if hg <= 837
yk inc -803 if a != 1119
mmw dec 678 if lx < -680
lbf inc 862 if fk < -1825
kg inc -786 if t <= 5259
aao dec 91 if x == -1407
uy dec -548 if t == 5263
aao inc 638 if is != 3463
hg dec 244 if uy > 807
f inc 58 if lbf >= 765
fk inc 581 if is != 3455
hg dec -692 if fk >= -1247
um inc -752 if aao < -1424
lbf dec 14 if lbf != 783
t dec 270 if f == -1542
uy inc 70 if hg <= 1277
is inc 676 if lx == -682
is inc 230 if um >= -163
gk dec 799 if yk > 1107
ada dec -20 if eri != -2804
lx dec -278 if umr == 6678
gk inc 83 if umr <= 6686
lbf inc 265 if a >= 1118
is dec 476 if j != -820
eri dec 509 if lx > -413
is dec -486 if dy < 4606
kg dec 989 if is > 4847
lx inc 996 if dy >= 4591
is inc -371 if eri > -3303
kg dec 209 if f != -1542
kg dec -21 if kg < 1394
uy dec -34 if x == -1417
mmw inc -753 if hg != 1285
gk dec 862 if kg > 1408
ada dec 346 if is < 4856
umr inc 262 if es > -1888
lx inc -842 if umr < 6948
f inc 557 if yk != 1103
dy inc -323 if lbf >= 1030
kg dec 610 if ada >= -1883
f dec 727 if f != -1544
es dec -922 if aao > -1435
kg inc -628 if f == -2269
eri inc -762 if lx < -245
a dec 246 if a <= 1118
aao dec 51 if kg >= 181
is dec 761 if x >= -1417
j inc 359 if x == -1417
mmw dec 562 if ada < -1880
lbf dec 955 if aao != -1426
umr dec -851 if x == -1417
t dec -845 if is <= 4101
lbf inc -666 if hg > 1272
um dec -105 if f >= -2274
gk inc 191 if umr != 7781
dy dec -399 if eri <= -4072
is inc 681 if t != 5835
mmw inc -731 if ada > -1883
x inc -603 if yk < 1111
j inc 860 if fk <= -1239
t dec -480 if kg > 175
eri inc 308 if mmw > 957
hg inc 37 if gk >= -1163
eri inc 868 if kg >= 172
gk inc 381 if f > -2276
ada inc -231 if fk < -1234
uy dec -404 if gk >= -781
es inc -33 if yk != 1105
j inc -210 if um != -66
umr dec -783 if kg == 176
a inc 287 if hg < 1322
es inc 794 if f >= -2270
f inc 816 if a < 1417
eri inc -136 if fk <= -1235
j dec 421 if lbf < 362
kg dec -889 if fk > -1248
um inc 701 if yk <= 1110
x dec -487 if fk < -1243
aao dec 623 if umr <= 8582
mmw dec -307 if eri > -3038
t inc 803 if f == -1453
kg dec 980 if a < 1404
dy inc -974 if gk < -772
yk inc 221 if eri < -3040
gk inc -421 if aao > -2059
mmw dec -751 if f <= -1445
kg dec 422 if lx <= -250
dy dec 191 if x <= -1535
um inc -318 if gk != -1195
mmw inc 870 if kg != 651
j dec -865 if t < 7131
um dec 886 if t < 7124
ada inc 171 if eri < -3030
x dec -755 if es == -202
fk inc -325 if hg >= 1313
t dec 984 if t != 7130
j dec 55 if aao == -2056
fk dec 80 if x <= -773
dy dec 852 if lx != -256
is inc 295 if a >= 1408
uy dec 733 if hg < 1318
x inc 868 if um <= -560
t dec -532 if t != 6128
aao inc -530 if x == 90
is dec 374 if lbf == 358
aao inc 93 if t == 6673
uy inc -657 if hg != 1317
fk inc -670 if umr > 8568
x inc 791 if j != 634
mmw dec -872 if uy >= -73
yk inc -771 if eri <= -3034
umr dec -125 if kg < 645
mmw inc -617 if aao > -2581
mmw dec -90 if mmw != 3145
es dec 182 if aao <= -2574
kg dec 903 if ada >= -1934
um inc 319 if lbf == 358
uy inc -958 if f <= -1447
ada dec -965 if eri == -3033
fk dec 750 if es >= -393
hg inc -488 if hg >= 1307
lx inc 742 if umr != 8703
uy inc 378 if kg != 643
lx dec -584 if um != -233
kg dec -654 if ada >= -986
is dec 181 if f == -1453
eri inc 302 if lx < 1080
uy inc -907 if kg != 1289
yk dec 652 if is < 4223
lbf inc -147 if hg != 823
fk dec -584 if kg < 1300
fk dec -593 if f <= -1449
dy dec -83 if gk < -1189
a dec -568 if es <= -377
aao inc -742 if gk <= -1193
kg dec -560 if hg <= 831
es dec -871 if fk > -1899
lx inc 239 if kg != 1855
uy dec 696 if ada >= -984
kg dec -899 if yk >= 452
x inc -303 if is <= 4223
um inc -207 if lbf != 211
eri dec 520 if eri >= -2731
is dec -251 if t < 6675
umr inc 19 if kg == 1857
lbf dec -365 if uy != -2632
yk dec 192 if fk < -1883
dy dec 451 if hg > 820
j dec -789 if lx <= 1320
um dec -577 if lx > 1309
es dec 954 if dy != 2800
aao dec 798 if f <= -1446
mmw dec -339 if mmw >= 3143
j inc 126 if yk == 259
ada inc -898 if umr != 8718
kg inc -365 if eri == -3251
aao dec 718 if lx > 1307
x inc -872 if kg <= 1495
j dec -862 if is != 4464
mmw dec -785 if is == 4469
t dec 355 if uy != -2627
ada dec -528 if ada == -977
yk dec -139 if hg >= 823
mmw dec -97 if is == 4469
j dec -454 if is == 4469
yk dec -151 if kg < 1500
lbf inc -19 if lbf != 576
yk inc 281 if umr == 8718
gk dec 59 if mmw <= 4374
umr dec 266 if hg < 828
fk inc -54 if is <= 4477
is inc 468 if is >= 4477
mmw inc -749 if ada != -442
is inc 22 if mmw > 3608
uy inc -436 if ada != -449
umr dec -545 if gk == -1256
mmw inc -716 if ada <= -447
fk dec -470 if f >= -1450
ada inc -429 if uy != -2633
aao inc -28 if a < 1984
umr inc -826 if aao >= -4867
lbf dec 141 if kg < 1493
lbf inc 307 if eri == -3251
um dec -120 if um == 335
j inc -674 if fk == -1956
mmw inc -784 if lx == 1315
x inc -524 if dy == 2805
mmw dec 911 if kg == 1492
gk inc 260 if mmw >= 1200
es inc 638 if hg > 819
mmw dec 276 if ada == -449
eri dec -682 if kg != 1489
um inc 790 if t > 6321
a inc 288 if eri >= -2560
eri dec -477 if lbf >= 747
kg inc 922 if kg > 1489
ada dec -65 if uy >= -2634
ada dec -106 if umr >= 8170
is dec -609 if aao >= -4866
t dec -598 if mmw == 930
gk dec 89 if t != 6912
t dec -500 if f < -1456
is dec -169 if es == 171
f dec -633 if f <= -1453
aao dec -191 if t > 6905
a dec -772 if eri > -2574
x inc -272 if x >= -818
es dec 135 if j <= 2862
uy inc 950 if aao == -4674
ada dec 380 if aao != -4676
aao inc 111 if kg < 2415
lx inc -339 if umr == 8171
yk dec 63 if ada <= -653
yk inc -894 if j > 2863
f dec -590 if eri != -2560
hg inc -281 if gk == -996
lx inc -529 if hg >= 539
ada dec -133 if es != 163
f dec -510 if t != 6912
uy inc -761 if um != 465
a inc -466 if um > 452
f dec 811 if lbf <= 747
umr dec 206 if umr >= 8170
x dec -606 if dy <= 2814
t dec 823 if hg <= 553
yk inc 130 if um != 453
aao inc 984 if fk > -1948
x dec -152 if um > 447
fk dec -958 if kg > 2418
eri dec 996 if a < 2290
aao inc 702 if x != -330
lbf dec -8 if aao > -2872
mmw inc 346 if hg != 554
is dec -255 if fk == -1946
gk dec -139 if x >= -335
j dec -238 if x != -332
lbf inc 649 if a < 2283
lx inc 702 if es < 178
fk dec -918 if j > 2858
lbf inc 971 if hg == 544
f dec -807 if a < 2283
eri dec -263 if dy != 2814
fk dec 128 if kg == 2414
hg dec 541 if mmw > 1270
uy inc -144 if um <= 458
um dec 362 if mmw == 1276
yk inc -346 if mmw == 1276
mmw inc -543 if yk <= -340
hg inc -358 if mmw == 733
es dec -652 if f >= -232
uy dec 401 if ada == -525
x inc 736 if kg >= 2412
uy inc -489 if mmw == 733
yk inc 134 if is > 5522
lbf dec 531 if uy != -3470
f inc 472 if umr >= 7960
f dec -410 if lbf >= 1836
eri inc 522 if gk == -857
um inc -672 if es != 178
fk dec -774 if j <= 2871
f inc 825 if kg != 2414
j dec -713 if es <= 178
um inc 769 if t <= 6079
lx inc 995 if dy > 2797
is dec 359 if es < 180
a inc -680 if es < 177
eri inc -102 if mmw < 736
ada inc 39 if eri != -2889
lx dec -935 if lx != 2145
hg inc 741 if es >= 165
kg dec -156 if lbf <= 1835
f dec 376 if eri > -2892
aao inc 570 if j == 3577
dy inc 708 if is > 5162
a dec 737 if aao == -2307
x inc 936 if hg == 391
aao inc -405 if j > 3576
mmw inc -42 if kg > 2561
j dec 295 if um != -588
yk dec -641 if j <= 3282
umr inc -633 if gk != -864
dy inc -202 if gk < -858
aao inc -244 if gk != -861
uy inc -97 if kg == 2573
mmw dec -889 if ada < -482
es inc -166 if fk == -382
eri dec -962 if eri >= -2889
umr dec 201 if t >= 6086
gk dec -700 if mmw == 1580
ada inc -158 if gk < -159
t inc 650 if es < -2
lbf dec 870 if aao > -2966
uy dec 727 if j <= 3289
umr inc 483 if lbf < 971
hg dec -283 if fk != -379
kg dec 202 if t < 6090
eri inc 607 if a >= 864
lbf dec 282 if lx > 3074
yk dec 490 if mmw >= 1573
uy dec -536 if aao >= -2959
uy dec -306 if lx > 3071
fk dec 982 if lx == 3069
aao dec 431 if aao < -2947
mmw inc 145 if t < 6093
is inc -222 if es <= 11
mmw inc -953 if fk < -372
a inc 588 if x != 406
gk dec 464 if lx <= 3080
mmw dec -655 if a > 1448
mmw dec 251 if aao < -3394
t inc 582 if dy < 3508
lbf dec 816 if ada < -492
uy inc 374 if a >= 1445
f inc 98 if f >= -129
gk dec -206 if gk == -621
lbf dec -368 if fk != -382
mmw dec -16 if um == -579
dy dec 522 if umr == 7614
fk inc -645 if dy != 2998
hg dec 829 if lbf > 676
aao dec 472 if t != 6098
kg inc 926 if aao >= -3868
x dec -485 if j <= 3284
x dec 987 if mmw > 1433
yk dec -933 if aao != -3859
fk inc -446 if lx <= 3080
kg dec 573 if f != -129
hg dec 231 if dy <= 2992
eri dec -162 if es < 14
t dec 975 if lx > 3086
dy dec -144 if f < -147
lx dec 122 if lbf < 682
mmw inc -438 if umr == 7614
j inc 149 if mmw < 1009
t inc 749 if lx > 2947
um inc -970 if hg >= -400
kg inc 368 if kg != 2721
aao dec 845 if kg == 2721
eri dec -521 if yk > -59
gk dec -200 if ada >= -495
hg inc 462 if um == -1549
eri dec -54 if mmw >= 998
hg dec -268 if a >= 1450
j dec 86 if t != 6840
a dec -394 if a == 1452
aao inc 166 if kg >= 2720
x inc -146 if is == 4943
es inc 496 if kg < 2723
t dec -949 if uy <= -2989"""

print(and_or_trick(puzzle_input))