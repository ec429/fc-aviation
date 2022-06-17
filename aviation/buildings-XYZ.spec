
[spec]

; Format and options of this spec file:
options = "Freeciv-3.0-spec Freeciv-spec-Devel-2019-Jul-03"

[info]

; Additional Aviation tiles, modified by Sketlux (XYZ).

artists = "
    Sketlux
"

[file]
gfx = "aviation/buildings-xyz"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 64
dy = 48
pixel_border = 1

tiles = { "row", "column", "tag"
  0,  0, "b.aero_lib"    ; Aeronautical Library
  0,  1, "b.school"      ; Flying School
}
