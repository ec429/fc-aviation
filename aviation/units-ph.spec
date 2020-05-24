
[spec]

; Format and options of this spec file:
options = "+Freeciv-3.0-spec"

[info]

; Aviation Tileset placeholders created by ec429

artists = "
    ec429
"

[file]
gfx = "aviation/placeholders"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 64
dy = 48
pixel_border = 1

tiles = { "row", "column", "tag"
  0,  1, "u.ph-PP" ; Pioneer, Passenger
  0,  2, "u.ph-R1" ; Early Recon
  0,  3, "u.ph-R2" ; Recon / Light Bomber
  0,  4, "u.ph-LE" ; Light Bomber, Early
  0,  5, "u.ph-L1" ; Biplane Light Bomber
  0,  6, "u.ph-L2" ; Light Bomber, 20s
  0,  7, "u.ph-L3" ; Light Bomber, 30s
  0,  8, "u.ph-LT" ; Light Bomber, Twin
  0,  9, "u.ph-SA" ; Scout, Armed
  0, 10, "u.ph-SM" ; Scout, Monoplane
  0, 11, "u.ph-SP" ; Scout, Pusher
  0, 12, "u.ph-SS" ; Scout, Sesquiplane
  0, 13, "u.ph-ST" ; Scout, Triplane
  0, 14, "u.ph-SB" ; Scout, Biplane
  0, 15, "u.ph-S2" ; Scout, 20s
  0, 16, "u.ph-S3" ; Scout, 30s
  0, 17, "u.ph-FE" ; Fighter, Early Monoplane
  0, 18, "u.ph-FM" ; Fighter, Monoplane
  0, 19, "u.ph-FC" ; Fighter, Cannon
  1,  0, "u.ph-FF" ; Superprop Fighter
  1,  1, "u.ph-F1" ; Fighter, First-gen Jet
  1,  2, "u.ph-FV" ; First-gen Light Fighter
  1,  3, "u.ph-FW" ; Fighter, Swept Wing
  1,  4, "u.ph-FI" ; Supersonic Interceptor
  1,  5, "u.ph-FA" ; Fighter, Air-superiority, Supersonic
  1,  6, "u.ph-FL" ; Fighter, Light, Transonic
  1, 10, "u.ph-FP" ; Fighter, Pusher
  1, 11, "u.ph-FS" ; Fighter, Strutter
  1, 12, "u.ph-FB" ; Fighter, Biplane
  1, 13, "u.ph-F3" ; Fighter, 30s
  1, 14, "u.ph-FT" ; Fighter, Turret
  1, 18, "u.ph-RJ" ; Recon Jet
  1, 19, "u.ph-RS" ; Recon, Supersonic
  2,  0, "u.ph-TF" ; Trench Fighter
  2,  1, "u.ph-A2" ; Attacker, 20s
  2,  2, "u.ph-A3" ; Attacker, 30s
  2,  3, "u.ph-AK" ; Attacker
  2,  4, "u.ph-A1" ; Attacker, First-gen Jet
  2,  5, "u.ph-AJ" ; Attack Jet
  2,  6, "u.ph-AS" ; Attacker, Supersonic
  2, 10, "u.ph-EF" ; Early Heavy Fighter / Escort Fighter
  2, 11, "u.ph-FH" ; Fighter, Heavy
  2, 12, "u.ph-JA" ; Jet Fighter, All Weather
  3,  0, "u.ph-SF" ; Shipboard Fighter
  3,  1, "u.ph-N2" ; Naval Fighter, 20s
  3,  2, "u.ph-N3" ; Naval Fighter, 30s
  3,  3, "u.ph-NM" ; Naval Fighter, Monoplane
  3,  4, "u.ph-NS" ; Naval Fighter, Strike
  3,  5, "u.ph-ND" ; Naval Dogfighter
  3,  6, "u.ph-NC" ; Naval Fighter, Cannon
  3,  7, "u.ph-NP" ; Naval Fighter, Super Prop
  3,  8, "u.ph-NA" ; Naval Attacker
  3,  9, "u.ph-NJ" ; Naval Jet, Early
  3, 10, "u.ph-NF" ; Naval Fighter, Swept Wing
  3, 11, "u.ph-AN" ; Attacker, Naval Jet
  4,  0, "u.ph-HV" ; Hydravion
  4,  1, "u.ph-HS" ; Floatplane Scout
  4,  2, "u.ph-HA" ; Floatplane, Armed
  4,  3, "u.ph-HF" ; Floatplane Fighter
  4,  4, "u.ph-HT" ; Floatplane, Torpedo
  4,  5, "u.ph-HL" ; Floatplane, Torpedo, Large
  4,  6, "u.ph-HC" ; Floatplane, Coastal
  4, 10, "u.ph-PE" ; Flying-boat, Early
  4, 11, "u.ph-PB" ; Patrol Boat
  4, 12, "u.ph-P2" ; Flying-boat, 20s
  4, 13, "u.ph-P3" ; Flying-boat, 30s
  4, 14, "u.ph-PH" ; Flying-boat, Heavy
  4, 15, "u.ph-PJ" ; Flying-boat, Jet
  5,  0, "u.ph-TE" ; Torpedo Bomber, Early
  5,  1, "u.ph-T2" ; Torpedo Bomber, 20s
  5,  2, "u.ph-T3" ; Torpedo Bomber, 30s
  5,  3, "u.ph-TM" ; Torpedo Bomber, Monoplane
  5,  4, "u.ph-TB" ; Torpedo Bomber
  5, 10, "u.ph-D2" ; Dive Bomber, 20s
  5, 11, "u.ph-D3" ; Dive Bomber, 30s
  5, 12, "u.ph-DB" ; Dive Bomber
  6,  0, "u.ph-M2" ; Medium Bomber, 20s
  6,  1, "u.ph-M3" ; Medium Bomber, 30s
  6,  2, "u.ph-MB" ; Medium Bomber
  6,  3, "u.ph-M1" ; Medium Bomber, Jet, Prototype
  6,  4, "u.ph-MJ" ; Medium Bomber, Jet, Small
  6, 10, "u.ph-BE" ; Bomber, Early
  6, 11, "u.ph-BT" ; Bomber, Triplane
  6, 12, "u.ph-BB" ; Bomber, Biplane
  6, 13, "u.ph-B2" ; Bomber, 20s
  6, 14, "u.ph-B3" ; Bomber, 30s
  6, 15, "u.ph-B4" ; Bomber, Four-engine
  6, 16, "u.ph-BH" ; Bomber, Heavy
  6, 17, "u.ph-BS" ; Bomber, Heavy, Superprop
  6, 18, "u.ph-B1" ; Bomber, Jet, Early
  6, 19, "u.ph-BJ" ; Bomber, Heavy, Jet
  7,  0, "u.ph-C2" ; Cargo, 20s
  7,  1, "u.ph-C3" ; Cargo, 30s
  7,  2, "u.ph-CM" ; Cargo, Monoplane
  7,  3, "u.ph-CS" ; Cargo, Strategic
  7,  4, "u.ph-CT" ; Cargo, Turboprop
  7,  5, "u.ph-CJ" ; Cargo, Jet
  7,  8, "u.ph-GG" ; Glider
  7,  9, "u.ph-GH" ; Glider, Heavy
  7, 10, "u.ph-ZS" ; Zeppelin Scout
  7, 11, "u.ph-ZB" ; Zeppelin Bomber
  7, 12, "u.ph-ZC" ; Blimp, Coastal
  7, 17, "u.ph-BC" ; Bomber, Heavy, Supersonic
}
