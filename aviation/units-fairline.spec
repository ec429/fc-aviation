
[spec]

; Format and options of this spec file:
options = "Freeciv-3.0-spec Freeciv-spec-Devel-2019-Jul-03"

[info]

; Aviation unit tiles by the Civ2 Scenario League on forums.civfanatics.com
; Modified for freeciv (mainly transparency) by ec429
; Used with permission.

; Includes images from Fairline's WW2 unit compilations (from
; https://forums.civfanatics.com/threads/ww2-unit-graphics.409277/page-43)
; which may include some by other artists
; Crediting generally based on signature logos in the source images
; Images credited ec429 are mostly kitbashed from Fairline originals
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
; 1,  6, "u.demon"       ; F3 Thirties Fighter (Hawker Demon) [EC]: kitbashed hart [GB]
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
  3,  7, "u.zeppeliner"  ; LZ Zeppelin Liner [GB]
  3,  8, "u.heyford"     ; B3 Thirties Bomber (Handley Page Heyford) [T]
  3,  9, "u.faireyiii"   ; HC Coastal Seaplane (Fairey IIIF) [T]
  3, 10, "u.demon"       ; F3 Thirties Fighter (Hawker Demon) [T]
  3, 11, "u.buccaneer"   ; AN Naval Attack Jet (Blackburn Buccaneer) [T]
  3, 12, "u.thunderjet"  ; A1 First-gen Jet Attacker (Republic F-84 Thunderjet) [T]
  3, 13, "u.thunderstreak";AJ Attack Jet (Republic F-84F Thunderstreak) [T]
  3, 14, "u.harrier"     ; AV VTOL Attack Jet (Hawker Siddeley Harrier GR.3) [GB]
  3, 15, "u.phantom"     ; AF Jet Fighter-Bomber (McDD F-4 Phantom II) [GB]
  3, 16, "u.sukhoi15"    ; FJ Jet Fighter (Sukhoi Su-15) [T]
  3, 17, "u.g91"         ; FL Transonic Light Fighter (Fiat G91) [T]
  3, 18, "u.f5"          ; F5 Supersonic Light Fighter (Northrop F-5 Freedom Fighter) [T]
  3, 19, "u.f8crusader"  ; NI Supersonic Naval Fighter (Vought F8U Crusader) [T]
  4,  0, "u.p47"         ; AP Superprop Attacker (Republic P-47D Thunderbolt) [GB]
  4,  1, "u.banshee"     ; N1 Naval Jet Attacker (McDonnell F2H-2 Banshee) [GB]
  4,  2, "u.skymaster"   ; CS Strategic Transport (Consolidated B-24J Liberator) [GB], gun turrets removed by [EC] to turn it into a C-87 Liberator Express
  4,  3, "u.bulldog"     ; S2 Twenties Scout (Bristol Bulldog) [EC]
  4,  4, "u.liberty"     ; MS Merchant Ship (Liberty Ship) [GB]
  4,  5, "u.albatrosw"   ; HW Fighter Seaplane (Albatros C.III) [GB], kitbashed by [EC] to add floats from u.schneider
  4,  6, "u.flycatcher"  ; N2 Twenties Naval Fighter (Fairey Flycatcher) [EC]
  4,  7, "u.floatcatcher"; H2 Twenties Floatplane (Fairey Flycatcher) [EC]
  4,  8, "u.cuckoo"      ; TE Early Torpedo Bomber (Martinsyde G.100, standing in for a Sopwith Cuckoo) [GB], torp added by [EC]
  4,  9, "u.f8c"         ; D2 Twenties Dive Bomber (Polikarpov I-15, which is a fighter but I needed something to put here) [GB]
  4, 10, "u.whitley"     ; BW Early Heavy Bomber (Armstrong-Whitworth Whitley) [T]
  4, 11, "u.audacity"    ; CVE Escort Carrier (possibly HMS Audacity) [GB]
  4, 12, "u.rufe"        ; HM Monoplane Float Fighter (Nakajima A6M2-N "Rufe") [GB]
  4, 13, "u.cant"        ; HB Floatplane Bomber (CANT Z.506 Airone) [T]
  4, 14, "u.he51w"       ; H3 Thirties Seaplane (Heinkel He 51 W) [GB], floats added by [EC]
  4, 15, "u.virginia"    ; B2 Twenties Bomber (Vickers Virginia) [EC]: kitbashed from Vickers Vimy [GB]
  4, 16, "u.judy"        ; KA Kamikaze (Yokosuka D4Y4 Suisei/"Judy") [GB]
  4, 17, "u.aggregat"    ; V2 Artillery Rocket (Thiel A4 Aggregat) [GB]
  4, 18, "u.truck"       ; Radar Van (Bedford QLT 3t) [GB]
  4, 19, "u.short81"     ; HA Armed Floatplane (Short Type 81 Folder) [EC]: kitbashed from Sopwith Schneider [GB]
  5,  0, "u.short184"    ; HT Torpedo Floatplane (Short Type 184 Folder) [EC]: derived from u.short81
  5,  1, "u.baby"        ; HF Floatplane Fighter (Hanriot D.1) [T], floats added by [EC]
  5,  2, "u.short320"    ; HL Large Torpedo Floatplane (Short Type 320 Folder) [EC]: derived from u.short184
  5,  3, "u.dart"        ; T2 Twenties Torpedo Bomber ("Breguet", maybe a 14?) [GB]
}
