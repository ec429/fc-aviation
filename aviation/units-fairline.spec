
[spec]

; Format and options of this spec file:
options = "+Freeciv-2.6-spec"

[info]

; Aviation unit tiles by Fairline (of the Civ2 Scenario League on forums.civfanatics.com)
; Modified for freeciv (mainly transparency) by ec429
; Used with permission.

; Includes images from Fairline's WW2 unit compilations (from
; https://forums.civfanatics.com/threads/ww2-unit-graphics.409277/page-43)
; which may include some by other artists
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
  2,  0, "u.seafire"     ; ND Naval Dogfighter (Supermarine Seafire I) [GB], cannons removed by [EC]
  2,  1, "u.bearcat"     ; NC Naval Cannon Fighter (Grumman F-8F Bearcat) [GB]
  2,  2, "u.seafury"     ; NP Naval Superprop (Hawker Sea Fury) [GB]
  2,  3, "u.panther"     ; NJ Early Naval Jet (Grumman F-9F Panther) [GB]
  2,  4, "u.schneider"   ; HS Floatplane Scout (Sopwith Schneider) [GB]
  2,  5, "u.sunderland"  ; PH Heavy Flying Boat (Short Sunderland) [GB]
  2,  6, "u.swordfish"   ; T3 Thirties Torpedo Bomber (Fairey Swordfish) [GB]
  2,  7, "u.devastator"  ; TM Torpedo Monoplane (Douglas TBD Devastator) [GB]
  2,  8, "u.avenger"     ; TB Torpedo Bomber (Grumman TBF Avenger) [GB]
  2,  9, "u.sbchell"     ; D3 Thirties Dive Bomber (Curtiss SBC-4 Helldiver) [GB]
  2, 10, "u.stuka"       ; DB Dive Bomber (Junkers Ju 87B "Stuka") [GB]
  2, 11, "u.anson"       ; M3 Thirties Medium Bomber (Avro Anson) [T] & [GB]
  2, 12, "u.wellington"  ; MB Medium Bomber (Vickers Wellington) [GB]
  2, 13, "u.arado"       ; M1 Prototype Jet Bomber (Arado Ar 234) [GB]
  2, 14, "u.canberra"    ; MJ Small Jet Bomber (English Electric Canberra B.2) [GB]
  2, 15, "u.o400"        ; BE Early Bomber (Handley Page O/400) [GB]
  2, 16, "u.gotha"       ; BB Biplane Bomber (Gotha G.IV) [GB]
  2, 17, "u.stirling"    ; B4 Four-engine Bomber (Short Stirling) [GB]
  2, 18, "u.lancaster"   ; BH Heavy Bomber (Avro Lancaster) [GB]
  2, 19, "u.b29"         ; BS Superprop Bomber (Boeing B-29 Superfortress) [GB]
  3,  0, "u.vulcan"      ; BJ Jet Bomber (Avro Vulcan) [GB]
  3,  1, "u.ju52"        ; CM Monoplane Transport (Junkers Ju 52) [GB]
  3,  2, "u.dfs"         ; GG Assault Glider (DFS 230) [GB]
  3,  3, "u.seaplane-tender" ; Seaplane Tender (Auxiliary ship of some sort) [GB]
  3,  4, "u.cvl"         ; CVL Early Aircraft Carrier (HMS Furious) [GB]
  3,  5, "u.cv"          ; CV Aircraft Carrier (HMS Ark Royal) [GB]
  3,  6, "u.lcmboat"     ; Landing Craft (LCM) [GB]
}