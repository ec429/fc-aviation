
[spec]

; Format and options of this spec file:
options = "+Freeciv-2.6-spec"

[info]

; Aviation unit tiles by Fairline (of the Civ2 Scenario League on forums.civfanatics.com)
; Modified for freeciv (mainly transparency) by ec429
; Used with permission.

; Fairline's WW2 unit compilations (from
; https://forums.civfanatics.com/threads/ww2-unit-graphics.409277/page-43)
; Images credited ec429 are kitbashed from Fairline originals
artists = "
    Fairline [GB]
    Tanelorn [T]
    Broken Erika
    ec429 [EC]
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
  0,  0, "u.2pdr"        ; Assault Gun [GB]
  0,  1, "u.be2"         ; R1 Early Recon [GB]
  0,  2, "u.tabloid"     ; R2 Recon/Light Bomber (RAF R.E.8, standing in for an R.E.7) [GB]
  0,  3, "u.dh4"         ; LE Early Light Bomber (Airco DH.4) [GB]
  0,  4, "u.dh9a"        ; L1 Biplane Light Bomber (Airco DH.9) [GB]
  0,  5, "u.hart"        ; L2 Twenties Light Bomber (Hawker Hart) [GB]
  0,  6, "u.battle"      ; L3 Thirties Light Bomber (Fairey Battle) [GB]
  0,  7, "u.blenheim"    ; LT Light Bomber Twin (Bristol Blenheim I) [GB]
  0,  8, "u.scout"       ; SA Armed Scout (Sopwith Scout (Pup), standing in for a Bristol Scout) [GB]
  0,  9, "u.eindecker"   ; SM Monoplane Scout (Fokker E.III) [GB]
  0, 10, "u.dh2"         ; SP Pusher Scout (Airco DH.2) [GB]
  0, 11, "u.nieuport"    ; SS Sesquiplane Scout (Nieuport 17) [GB]
  0, 12, "u.triplane"    ; ST Triplane Scout (Sopwith Triplane) [GB]
  0, 13, "u.camel"       ; SB Biplane Scout (Sopwith Camel) [GB]
  0, 14, "u.fury"        ; S3 Thirties Scout (Hawker Fury I) [GB]
  0, 15, "u.hurricane"   ; FE Early Monoplane Fighter (Hawker Hurricane I) [GB]
  0, 16, "u.spitfire"    ; FM Monoplane Fighter (Supermarine Spitfire II) [GB]
  0, 17, "u.spitix"      ; FC Cannon Fighter (Supermarine Spitfire IX) [GB]
  0, 18, "u.me262"       ; F1 First-gen Jet Fighter (Messerschmitt Me 262A) [GB]
  0, 19, "u.vampire"     ; FV First-gen Light Fighter (de Havilland Vampire) [GB]
  1,  0, "u.mig15"       ; FW Swept-wing Fighter (Mikoyan-Gurevich MiG 15) [GB]
  1,  1, "u.lightning"   ; FI Supersonic Interceptor (English Electric Lightning) [GB]
  1,  2, "u.f100"        ; FA Supersonic Fighter (North American F-100 Super Sabre) [GB]
  1,  3, "u.gunbus"      ; FP Pusher Fighter (RAF F.E.2b) [GB]
  1,  4, "u.strutter"    ; FS Two-seat Scout (Sopwith 1½ Strutter) [EC]: kitbashed brisfit [GB]
  1,  5, "u.brisfit"     ; FB Fighter Biplane (Bristol F.2 Fighter) [GB]
  1,  6, "u.demon"       ; F3 Thirties Fighter (Hawker Demon) [EC]: kitbashed hart [GB]
  1,  7, "u.defiant"     ; FT Turret Fighter (Boulton Paul Defiant) [T] & [GB]
  1,  8, "u.salamander"  ; TF Trench Fighter (Airco DH.5) [GB]
  1,  9, "u.potez25"     ; A2 Twenties Attacker (Potez 25) [GB]
  1, 10, "u.he51c"       ; A3 Thirties Attacker (Heinkel He 51C) [GB]
  1, 11, "u.il2"         ; AK Attacker (Ilyushin Il-2) [GB]
  1, 12, "u.thunderchief"; AS Supersonic Attacker (Republic F-105F/G Thunderchief) [GB]
  1, 13, "u.bf110"       ; EF Early Heavy Fighter (Messerschmitt Bf 110) [GB]
  1, 14, "u.mosquito"    ; FH Heavy Fighter (de Havilland Mosquito) [GB], lightly kitbashed by [EC] into a fighter version
  1, 15, "u.javelin"     ; JA All-Weather Jet Fighter (Gloster Javelin) [GB]
  1, 16, "u.shipcamel"   ; SF Shipboard Fighter (Sopwith Ship's Camel) [EC]: lightly kitbashed camel [GB]
  1, 17, "u.fifi"        ; N3 Thirties Naval Fighter (Grumman FF "Fifi") [GB]
  1, 18, "u.wildcat"     ; NM Monoplane Naval Fighter (Grumman F-4F Wildcat) [GB]
  1, 19, "u.firefly"     ; NS Naval Strike Fighter (Fairey Firefly) [GB]
}
