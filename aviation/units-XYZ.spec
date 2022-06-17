
[spec]

; Format and options of this spec file:
options = "Freeciv-3.0-spec Freeciv-spec-Devel-2019-Jul-03"

[info]

; Additional Aviation tiles, collected by XYZ.  Unit associations by ec429

artists = "
    XYZ
    GriffonSpade
    Ngunjaca
    VladimirSlavik
"

[file]
gfx = "aviation/XYZamplio"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 64
dy = 48
pixel_border = 1

tiles = { "row", "column", "tag"
  0,  0, "u.falcon"      ; A2
  0,  1, "u.victoria"    ; C2.  Mirrored and slightly tweaked.
  0,  2, "u.dornierx"    ; P3
  0,  3, "u.p51h"        ; FF
; 0,  4, "u.stuka"       ; DB
; 0,  5, "u.b17"         ; B4.  Probably a B17E or F (which would strictly be BH but I want a Lancaster dammit).
; 0,  6, "u.c47"         ; CM
; 0,  7, "u.mig15"       ; FW
  0,  8, "u.c135"        ; CJ.  It might be meant as a B-52 (but again, I want a Vulcan in that slot).
  0,  9, "u.eurofighter" ; currently unused
  0, 10, "u.b707"        ; LJ
  0, 11, "u.warthog"     ; currently unused
; 0, 12, "u.thunderchief"; AS
  0, 13, "u.b2spirit"    ; currently unused
  0, 14, "u.skyhawk"     ; currently unused (was AN)
  0, 18, "u.dblimp"      ; ZD.  Was probably intended as a Zeppelin, but it's a late model (teardrop/icthyoid hull); ZS and ZB are straight-sided
  0, 19, "u.e3dsentry"   ; currently unused
  1,  0, "u.hoverfly"    ; UE Early Helicopter
  1,  1, "u.chinook"     ; UT Twin Rotor
  1,  2, "u.huey"        ; UH Helicopter
  1, 14, "u.fatman"      ; X1 Atomic Bomb
}
