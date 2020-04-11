
[spec]

; Format and options of this spec file:
options = "+Freeciv-2.6-spec"

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
  0,  1, "u.boxkite"        ; PP: Pioneer, Passenger
  0,  2, "u.be2"            ; R1: Early Recon
  0,  3, "u.tabloid"        ; R2: Recon / Light Bomber
  0,  4, "u.dh4"            ; LE: Light Bomber, Early
  0,  5, "u.dh9a"           ; L1: Biplane Light Bomber
  0,  6, "u.hart"           ; L2: Light Bomber, 20s
  0,  7, "u.battle"         ; L3: Light Bomber, 30s
  0,  8, "u.blenheim"       ; LT: Light Bomber, Twin
  0,  9, "u.scout"          ; SA: Scout, Armed
  0, 10, "u.eindecker"      ; SM: Scout, Monoplane
  0, 11, "u.dh2"            ; SP: Scout, Pusher
  0, 12, "u.nieuport"       ; SS: Scout, Sesquiplane
  0, 13, "u.triplane"       ; ST: Scout, Triplane
  0, 14, "u.camel"          ; SB: Scout, Biplane
  0, 15, "u.bulldog"        ; S2: Scout, 20s
  0, 16, "u.fury"           ; S3: Scout, 30s
  0, 17, "u.hurricane"      ; FE: Fighter, Early Monoplane
  0, 18, "u.spitfire"       ; FM: Fighter, Monoplane
  0, 19, "u.spitix"         ; FC: Fighter, Cannon
  1,  0, "u.p51h"           ; FF: Superprop Fighter
  1,  1, "u.me262"          ; F1: Fighter, First-gen Jet
  1,  2, "u.vampire"        ; FV: First-gen Light Fighter
  1,  3, "u.mig15"          ; FW: Fighter, Swept Wing
  1,  4, "u.lightning"      ; FI: Supersonic Interceptor
  1,  5, "u.f100"           ; FA: Fighter, Air-superiority, Supersonic
  1,  6, "u.gnat"           ; FL: Fighter, Light, Transonic
  1, 10, "u.gunbus"         ; FP: Fighter, Pusher
  1, 11, "u.strutter"       ; FS: Fighter, Strutter
  1, 12, "u.brisfit"        ; FB: Fighter, Biplane
  1, 13, "u.demon"          ; F3: Fighter, 30s
  1, 14, "u.defiant"        ; FT: Fighter, Turret
  2,  0, "u.salamander"     ; TF: Trench Fighter
  2,  1, "u.falcon"         ; A2: Attacker, 20s
  2,  2, "u.curtiss"        ; A3: Attacker, 30s
  2,  3, "u.il2"            ; AK: Attacker
  2,  4, "u.thunderjet"     ; A1: Attacker, First-gen Jet
  2,  5, "u.thunderstreak"  ; AJ: Attack Jet
  2,  6, "u.thunderchief"   ; AS: Attacker, Supersonic
  2, 10, "u.bf110"          ; EF: Early Heavy Fighter / Escort Fighter
  2, 11, "u.mosquito"       ; FH: Fighter, Heavy
  2, 12, "u.javelin"        ; JA: Jet Fighter, All Weather
  3,  0, "u.shipcamel"      ; SF: Shipborne Fighter
  3,  1, "u.flycatcher"     ; N2: Naval Fighter, 20s
  3,  2, "u.nimrod"         ; N3: Naval Fighter, 30s
  3,  3, "u.wildcat"        ; NM: Naval Fighter, Monoplane
  3,  4, "u.firefly"        ; NS: Naval Fighter, Strike
  3,  5, "u.seafire"        ; ND: Naval Dogfighter
  3,  6, "u.bearcat"        ; NC: Naval Fighter, Cannon
  3,  7, "u.seafury"        ; NP: Naval Fighter, Super Prop
  3,  8, "u.skyraider"      ; NA: Naval Attacker
  3,  9, "u.attacker"       ; NJ: Naval Jet, Early
  3, 10, "u.venom"          ; NF: Naval Fighter, Swept Wing
  3, 11, "u.skyhawk"        ; AN: Attacker, Naval Jet
  4,  0, "u.hydravion"      ; HV: Hydravion
  4,  1, "u.short41"        ; HS: Floatplane Scout
  4,  2, "u.short81"        ; HA: Floatplane, Armed
  4,  3, "u.baby"           ; HF: Floatplane Fighter
  4,  4, "u.short184"       ; HT: Floatplane, Torpedo
  4,  5, "u.short320"       ; HL: Floatplane, Torpedo, Large
  4,  6, "u.velos"          ; HC: Floatplane, Coastal
  4, 10, "u.felix2a"        ; PE: Flying-boat, Early
  4, 11, "u.felix5"         ; PB: Patrol Boat
  4, 12, "u.southampton"    ; P2: Flying-boat, 20s
  4, 13, "u.singapore"      ; P3: Flying-boat, 30s
  4, 14, "u.sunderland"     ; PH: Flying-boat, Heavy
  4, 15, "u.sra1"           ; PJ: Flying-boat, Jet
  5,  0, "u.cuckoo"         ; TE: Torpedo Bomber, Early
  5,  1, "u.dart"           ; T2: Torpedo Bomber, 20s
  5,  2, "u.swordfish"      ; T3: Torpedo Bomber, 30s
  5,  3, "u.devastator"     ; TM: Torpedo Bomber, Monoplane
  5,  4, "u.avenger"        ; TB: Torpedo Bomber
  5, 10, "u.f8c"            ; D2: Dive Bomber, 20s
  5, 11, "u.hs123"          ; D3: Dive Bomber, 30s
  5, 12, "u.stuka"          ; DB: Dive Bomber
  6,  0, "u.sidestrand"     ; M2: Medium Bomber, 20s
  6,  1, "u.anson"          ; M3: Medium Bomber, 30s
  6,  2, "u.wellington"     ; MB: Medium Bomber
  6,  3, "u.arado"          ; M1: Medium Bomber, Jet, Prototype
  6,  4, "u.canberra"       ; MJ: Medium Bomber, Jet, Small
  6, 10, "u.caproni3"       ; BE: Bomber, Early
  6, 11, "u.caproni4"       ; BT: Bomber, Triplane
  6, 12, "u.vimy"           ; BB: Bomber, Biplane
  6, 13, "u.virginia"       ; B2: Bomber, 20s
  6, 14, "u.heyford"        ; B3: Bomber, 30s
  6, 15, "u.stirling"       ; B4: Bomber, Four-engine
  6, 16, "u.lancaster"      ; BH: Bomber, Heavy
  6, 17, "u.b29"            ; BS: Bomber, Heavy, Superprop
  6, 18, "u.valiant"        ; B1: Bomber, Jet, Early
  6, 19, "u.vulcan"         ; BJ: Bomber, Heavy, Jet
  7,  0, "u.victoria"       ; C2: Cargo, 20s
  7,  1, "u.valentia"       ; C3: Cargo, 30s
  7,  2, "u.ju52"           ; CM: Cargo, Monoplane
  7,  3, "u.skymaster"      ; CS: Cargo, Strategic
  7,  4, "u.hercules"       ; CT: Cargo, Turboprop
  7,  5, "u.c135"           ; CJ: Cargo, Jet
  7,  8, "u.dfs"            ; GG: Glider
  7,  9, "u.hamilcar"       ; GH: Glider, Heavy
  7, 10, "u.zeppscout"      ; ZS: Zeppelin Scout
  7, 11, "u.zeppelin"       ; ZB: Zeppelin Bomber
  7, 12, "u.cblimp"         ; ZC: Blimp, Coastal
}
