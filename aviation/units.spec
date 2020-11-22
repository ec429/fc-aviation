
[spec]

; Format and options of this spec file:
options = "Freeciv-3.0-spec Freeciv-spec-Devel-2019-Jul-03"

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
  0,  2, "u.hydravion"   ; HV
  0,  4, "u.caproni4"    ; BT Triplane Bomber (Caproni Ca 42 (Ca 4))
  0,  5, "u.submerged"   ; su Submersible (submerged).  Based on GoPostal's amplio2 u.submarine
  0,  7, "u.felix2a"     ; PE Early Flying Boat (Felixstowe F.2a)
  0,  8, "u.felix5"      ; PB Patrol Boat (Felixstowe F.5)
  0,  9, "u.sidestrand"  ; M2 Twenties Medium Bomber (Boulton Paul Sidestrand)
  0, 17, "u.zeppscout"   ; ZS.  Based on Zeppelin from XYZ's collection
  0, 18, "u.zeppelin"    ; ZB.  Based on Zeppelin from XYZ's collection
  0, 19, "u.cblimp"      ; ZC.  Based on Zeppelin from XYZ's collection
  1,  0, "u.old_settlers"; os Old Settlers.  Based on Captain Nemo's amplio2 u.settlers, with golden glow
  1,  6, "u.lph"         ; Helicopter assault carrier.  Based on Captain Nemo's amplio2 u.transport, with Chinook from XYZ's collection
; 2,  5, "u.2pdr"        ; assault gun.  Based on Captain Nemo's amplio2 u.howitzer
}
