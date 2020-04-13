
[spec]

; Format and options of this spec file:
options = "+Freeciv-2.6-spec"

[info]

; Aviation unit tiles by Fairline (of the Civ2 Scenario League on forums.civfanatics.com)
; Modified for freeciv (mainly transparency) by ec429
; Used with permission.

; Fairline's WW2 unit compilations (from
; https://forums.civfanatics.com/threads/ww2-unit-graphics.409277/page-43)
; include work by other artists; I don't know which sprites are theirs so
; credit them here in case.
artists = "
    Fairline [GB]
    Tanelorn
    Broken Erika
"

[file]
gfx = "aviation/fairlined"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 64
dy = 48
pixel_border = 1

tiles = { "row", "column", "tag"
  0,  0, "u.2pdr"        ; Assault Gun
  0,  1, "u.be2"         ; R1 Early Recon
  0,  2, "u.tabloid"     ; R2 Recon/Light Bomber (RAF R.E.8, standing in for an R.E.7)
  0,  3, "u.dh4"         ; LE Early Light Bomber (Airco DH.4)
  0,  4, "u.dh9a"        ; L1 Biplane Light Bomber (Airco DH.9)
  0,  5, "u.hart"        ; L2 Twenties Light Bomber (Hawker Hart)
  0,  6, "u.battle"      ; L3 Thirties Light Bomber (Fairey Battle)
  0,  7, "u.blenheim"    ; LT Light Bomber Twin (Bristol Blenheim I)
  0,  8, "u.scout"       ; SA Armed Scout (Sopwith Scout (Pup), standing in for a Bristol Scout)
  0,  9, "u.eindecker"   ; SM Monoplane Scout (Fokker E.III)
  0, 10, "u.dh2"         ; SP Pusher Scout (Airco DH.2)
  0, 11, "u.nieuport"    ; SS Sesquiplane Scout (Nieuport 17)
  0, 12, "u.triplane"    ; ST Triplane Scout (Sopwith Triplane)
  0, 13, "u.camel"       ; SB Biplane Scout (Sopwith Camel)
  0, 14, "u.fury"        ; S3 Thirties Scout (Hawker Fury I)
  0, 15, "u.hurricane"   ; FE Early Monoplane Fighter (Hawker Hurricane I)
  0, 16, "u.spitfire"    ; FM Monoplane Fighter (Supermarine Spitfire II)
  0, 17, "u.spitix"      ; FC Cannon Fighter (Supermarine Spitfire IX)
  0, 18, "u.me262"       ; F1 First-gen Jet Fighter (Messerschmitt Me 262A)
  0, 19, "u.vampire"     ; FV First-gen Light Fighter (de Havilland Vampire)
}
