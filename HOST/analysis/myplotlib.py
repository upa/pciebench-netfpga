

marker_index = 0
marker_list = [ "o", "x", "s", "+", "v", "h", "^", "d" ]
color_index = 0
color_list = [ "#009e73",
               "#56b4e9",
               "#707070",
               "#e54e40",
               "#0072b2",
               "#e69f00", 
               "#000000",
               "#1a1a1a" ,
]

def get_marker():
    global marker_index
    global maker_list
    m = marker_list[marker_index]
    marker_index = (marker_index + 1) % len(marker_list)
    return m

def get_color():
    global color_index
    global color_list
    c = color_list[color_index]
    color_index = (color_index + 1) % len(color_list)
    return c

def change_aspect_ratio(p, ratio):
    aspect = ((1/ratio) *
              (p.get_xlim()[1] - p.get_xlim()[0]) /
              (p.get_ylim()[1] - p.get_ylim()[0]))
    p.set_aspect(aspect)
    return

