
[spec]

; Format and options of this spec file:
options = "+Freeciv-2.6-spec"

[info]

; Aviation Tileset created by ec429

artists = "
    ec429
"

[file]
gfx = "aviation/units"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 64
dy = 48
pixel_border = 1

tiles = { "row", "column", "tag"
  0,  0, "u.wright3"     ; P0
  0,  1, "u.boxkite"     ; PP
  0, 17, "u.zeppscout"   ; ZS.  Based on Zeppelin from XYZ's collection
  0, 18, "u.zeppelin"    ; ZB.  Based on Zeppelin from XYZ's collection
  0, 19, "u.cblimp"      ; ZC.  Based on Zeppelin from XYZ's collection
  1,  6, "u.lph"         ; Helicopter assault carrier.  Based on Captain Nemo's amplio2 u.transport, with Chinook from XYZ's collection
  2,  5, "u.2pdr"        ; assault gun.  Based on Captain Nemo's amplio2 u.howitzer
}
