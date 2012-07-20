"""This module provides UTF-8 conversion into ISO-8859-x. It is
partially generated by the code executed when generated is set to
1. The module serves for compatibility with Python 1.5.2 only; Python
2 users should use the Unicode facilities instead. In fact, the tables
generated have to be generated with Python 2."""

# Generator part; activate by setting generate to 1 in this source code.
generate = 0
if generate:
    import codecs

    isocodes = []
    for i in range(1,20):
        try:
            name = "iso-8859-%d" % i
            codecs.lookup(name)
            isocodes.append(name)
        except LookupError:
            isocodes.append(None)

    print "code_to_uni=[None,"
    for code in isocodes:
        if code is None:
            print "None,"
            continue
        print '[',
        for char in range(128,256):
            print "%d," % ord(unicode(chr(char),code)),
        print "],"
    print "]"

class ConvertError(ValueError):
    pass

# Mapping table for unicode code points to iso-8859-x code points.
# Keys are encoding number (x), then the code point
uni_to_code=[None]*20

def utf8chr(c):
    if c < 0x800:
        return chr(0xc0 | (c>>6)) + chr(0x80 | (c & 0x3f))
    return chr(0xe0 | (c>>12)) + chr(0x80 | ((c>>6) & 0x3f)) + chr(0x80 | (c & 0x3f))

def code_to_utf8(encoding, c):
    """code_to_utf8(encoding, char) -> string
    Convert c from encoding to utf8; return UTF-8 string."""
    c = ord(c)
    if c<128:
        return chr(c)
    if code_to_uni[encoding] is None:
        raise ConvertError("unknown encoding ISO-8859-%d" % encoding)
    return utf8chr(code_to_uni[encoding][c-128])

def utf8_to_code(encoding, str):
    """utf8_to_code(encoding, str) -> char,rest
    Convert an UTF-8 string to encoding. Return the first char, and the
    remaining UTF-8 bytes."""
    if str == "":
        return str
    first = ord(str[0])
    if first<128:
        # Identity-map ASCII
        return str[0],str[1:]
    if uni_to_code[encoding] is None:
        # see whether we have reverse direction
        if code_to_uni[encoding] is None:
            raise ConvertError("unknown encoding ISO-8859-%d" % encoding)
        uni_to_code[encoding] = {}
        for code in range(128):
            uni = code_to_uni[encoding][code]
            uni_to_code[encoding][uni] = code+128
    if first<0xc0:
        # 10xxxxxx
        raise ConvertError("ill-formed UTF-8")
    if first<0xe0:
        # 110xxxxx 10xxxxxx
        val = ((first & 0x1f)<<6) | (ord(str[1]) & 0x3f)
        rest = str[2:]
    elif first < 0xf0:
        # 1110xxxx 10xxxxxx 10xxxxxx
        val = ((first & 0xf)<<12) | ((ord(str[1]) & 0x3f)<<6) | (ord(str[2]) & 0x3f)
        rest = str[3:]
    else:
        raise ConvertError("UTF-8 character outside BMP")
    try:
        return chr(uni_to_code[encoding][val]), rest
    except KeyError:
        raise ConvertError("Unicode character %x not supported in ISO-8859-%d"\
                           % (val, encoding))

############## GENERATED PART #########################
code_to_uni=[None,
[ 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, ],
[ 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 260, 728, 321, 164, 317, 346, 167, 168, 352, 350, 356, 377, 173, 381, 379, 176, 261, 731, 322, 180, 318, 347, 711, 184, 353, 351, 357, 378, 733, 382, 380, 340, 193, 194, 258, 196, 313, 262, 199, 268, 201, 280, 203, 282, 205, 206, 270, 272, 323, 327, 211, 212, 336, 214, 215, 344, 366, 218, 368, 220, 221, 354, 223, 341, 225, 226, 259, 228, 314, 263, 231, 269, 233, 281, 235, 283, 237, 238, 271, 273, 324, 328, 243, 244, 337, 246, 247, 345, 367, 250, 369, 252, 253, 355, 729, ],
[ 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 294, 728, 163, 164, 165, 292, 167, 168, 304, 350, 286, 308, 173, 174, 379, 176, 295, 178, 179, 180, 181, 293, 183, 184, 305, 351, 287, 309, 189, 190, 380, 192, 193, 194, 195, 196, 266, 264, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 288, 214, 215, 284, 217, 218, 219, 220, 364, 348, 223, 224, 225, 226, 227, 228, 267, 265, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 289, 246, 247, 285, 249, 250, 251, 252, 365, 349, 729, ],
[ 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 260, 312, 342, 164, 296, 315, 167, 168, 352, 274, 290, 358, 173, 381, 175, 176, 261, 731, 343, 180, 297, 316, 711, 184, 353, 275, 291, 359, 330, 382, 331, 256, 193, 194, 195, 196, 197, 198, 302, 268, 201, 280, 203, 278, 205, 206, 298, 272, 325, 332, 310, 212, 213, 214, 215, 216, 370, 218, 219, 220, 360, 362, 223, 257, 225, 226, 227, 228, 229, 230, 303, 269, 233, 281, 235, 279, 237, 238, 299, 273, 326, 333, 311, 244, 245, 246, 247, 248, 371, 250, 251, 252, 361, 363, 729, ],
[ 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 173, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 8470, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 167, 1118, 1119, ],
[ 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 1548, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 1563, 188, 189, 190, 1567, 192, 1569, 1570, 1571, 1572, 1573, 1574, 1575, 1576, 1577, 1578, 1579, 1580, 1581, 1582, 1583, 1584, 1585, 1586, 1587, 1588, 1589, 1590, 1591, 1592, 1593, 1594, 219, 220, 221, 222, 223, 1600, 1601, 1602, 1603, 1604, 1605, 1606, 1607, 1608, 1609, 1610, 1611, 1612, 1613, 1614, 1615, 1616, 1617, 1618, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, ],
[ 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 8216, 8217, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 8213, 176, 177, 178, 179, 900, 901, 902, 183, 904, 905, 906, 187, 908, 189, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 210, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 255, ],
[ 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 215, 171, 172, 173, 174, 8254, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 247, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 8215, 1488, 1489, 1490, 1491, 1492, 1493, 1494, 1495, 1496, 1497, 1498, 1499, 1500, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511, 1512, 1513, 1514, 251, 252, 253, 254, 255, ],
[ 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 286, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 304, 350, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 287, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 305, 351, 255, ],
[ 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 260, 274, 290, 298, 296, 310, 167, 315, 272, 352, 358, 381, 173, 362, 330, 176, 261, 275, 291, 299, 297, 311, 183, 316, 273, 353, 359, 382, 8213, 363, 331, 256, 193, 194, 195, 196, 197, 198, 302, 268, 201, 280, 203, 278, 205, 206, 207, 208, 325, 332, 211, 212, 213, 214, 360, 216, 370, 218, 219, 220, 221, 222, 223, 257, 225, 226, 227, 228, 229, 230, 303, 269, 233, 281, 235, 279, 237, 238, 239, 240, 326, 333, 243, 244, 245, 246, 361, 248, 371, 250, 251, 252, 253, 254, 312, ],
None,
None,
[ 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 8221, 162, 163, 164, 8222, 166, 167, 216, 169, 342, 171, 172, 173, 174, 198, 176, 177, 178, 179, 8220, 181, 182, 183, 248, 185, 343, 187, 188, 189, 190, 230, 260, 302, 256, 262, 196, 197, 280, 274, 268, 201, 377, 278, 290, 310, 298, 315, 352, 323, 325, 211, 332, 213, 214, 215, 370, 321, 346, 362, 220, 379, 381, 223, 261, 303, 257, 263, 228, 229, 281, 275, 269, 233, 378, 279, 291, 311, 299, 316, 353, 324, 326, 243, 333, 245, 246, 247, 371, 322, 347, 363, 252, 380, 382, 8217, ],
[ 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 7682, 7683, 163, 266, 267, 7690, 167, 7808, 169, 7810, 7691, 7922, 173, 174, 376, 7710, 7711, 288, 289, 7744, 7745, 182, 7766, 7809, 7767, 7811, 7776, 7923, 7812, 7813, 7777, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 372, 209, 210, 211, 212, 213, 214, 7786, 216, 217, 218, 219, 220, 221, 374, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 373, 241, 242, 243, 244, 245, 246, 7787, 248, 249, 250, 251, 252, 253, 375, 255, ],
[ 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 8364, 165, 352, 167, 353, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 381, 181, 182, 183, 382, 185, 186, 187, 338, 339, 376, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, ],
None,
None,
None,
None,
]
