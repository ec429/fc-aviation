# Aviation Ruleset for freeciv21

## Empire building in the Age of Flight

In this ruleset, there are only a handful of ground and sea unit types — but over a hundred air units!
As well as a 60-year span of technology (from the pioneer era to the early supersonic age), there are an efflorescence of different _categories_ of aeroplane, many with their own special rules.

Bombers, dive bombers, torpedo bombers and strike aircraft attack ground (or in some cases sea) units.  Ground units can make airborne assaults either by parachute or by glider.  Gliders are towed by bombers, and expended once dropped; paratroops jump from transport aircraft.  Sea units can transport either carrier-capable aeroplanes, seaplanes or ground units.  Airliners create trade routes between cities.  Blimps and flying-boats patrol the seas, hunting submarines.  Reconnaissance planes watch the enemy to find out what he's up to...

... and Fighters try to shoot down everything else!

## Development Status

The rules all seem to be working, although we're a bit short on City Improvements and (especially) Wonders.  The tech-tree goes up to the 1960s, but will be extended up to the present day in later versions.  Balancing has been done by rule-of-thumb only — there has not been much playtesting yet, so some units might be useless while others are overpowered.

The main thing that's missing is tiles (and other art).  Making art takes a long time, and though Fairline kindly allowed me to use some of his unit sprites, there are a few gaps that I couldn't find anything suitable for; so I've decided to use a bunch of placeholders for now (units are two-letter codes, vaguely reminiscent of hull symbols, while buildings are just using vaguely-appropriate-looking classic building images) while I get the ruleset sorted out.

## Significant Rule Changes

* Ground units have been split into two classes, Land and Assault.  The difference is that Land units can't be transported, either by sea or by air, whereas Assault units can.
  - The idea is that Land units are defensive, and have heavy weapons (tanks, artillery), whereas Assault units can be brought rapidly into an attack but don't have as much equipment with them, making them weaker defenders.  Paratroops in particular will struggle to hold their gains unless quickly reinforced.
  - Neither the Airlift nor Paradrop actions are used.  Instead, units are loaded into specialised aircraft.
    + Assault units can load into Gliders, which in turn load into another aircraft (the tug: a medium or heavy bomber).  The tug flies to the drop zone, then the Glider unloads from the tug, then the Assault unit unloads from the Glider; the Glider is now stuck on the ground, so disband it.  (Unfortunately, it's possible to cheat by unloading from the Glider while it's still on tow.  I haven't figured out how to fix that yet.)
    + Assault units can load and unload from transport aircraft at cities and airbases, or from helicopters anywhere.
    + Paratroops can unload from transport aircraft while in flight.
    + Some heavy bombers and flying-boats also have a small transport capacity.
  - Marines, as an Assault-class unit with no tech requirement, allow invasions by landing-craft before the development of airlanding or paratroop units.  However, they're much weaker in combat, so are really only useful to prevent players from leaving their cities _completely_ undefended.
* Ground units cannot cross Mountain tiles.
* Aircraft can't typically attack all unit classes.  Most will be specialised to attack either other aircraft, ground units, or sea units — although a few types can attack two or even all three.
* Aircraft are split into six unit classes:
  - Air.  Ordinary landplanes refuel-at-cities-and-airbases, but can't use aircraft carriers.
  - Carrier-borne.  Can operate from aircraft carriers (but not the Seaplane Tender).
  - Helicopter.  Can operate from aircraft carriers and the Helicopter Assault Carrier.  Can load and unload units in the field (without an airbase).
  - Seaplane.  Floatplanes and flying-boats can operate from the Seaplane Tender (also the Light Aircraft Carrier).
  - Glider.  See airlanding-assault rules above.  Note that Gliders cannot land in Mountains, Forests or Jungles.
  - Missile.  Like Carrier-borne, except that the unit is destroyed after attacking.
* Instead of providing vision, Buoys act as airbases for Seaplanes, allowing them to refuel on long overwater missions (but don't prevent stack death).  They can only be built on coastlines (cardinally adjacent to land).
* Sea units can't attack at all; they're all support vessels.
  - An Aircraft Carrier unit, for example, represents a CVBG (Carrier Battle Group) — while there are many gun-toting warships escorting the carrier, they're all too _busy_ escorting the carrier to run off and shoot someone else's ships.  And no carrier Admiral is going to initiate a surface gun-range engagement with an enemy CVBG (unless he _wants_ to end his career).
  - The exception is the Submersible, which has a CR 9 torpedo attack.  Preventing subs from harassing your shipping is the main purpose of blimps (and to a lesser extent flying-boats).
* Land and sea units are very slow.  If you want to get anything done, you'll need to use planes to move stuff around.
  - Roads don't speed up movement at all, and Railroads only reduce movement cost to 1/2.
* Unit Hitpoints and Firepower vary a lot, as does Fuel; just looking at the A/D/M numbers won't give you an accurate picture of a unit's capabilities.
  - Also, combat-capable air units have a limited number of Combat Rounds; for example, an attacking medium bomber will only get 12 combat rounds, while a Monoplane Fighter gets just 5 (though attacking doesn't end the fighter's turn, so if it has fuel to spare it can engage again).  The number of Combat Rounds in any engagement is determined by the attacking unit.
    + Scout: CR 3.  Scouts and fighters up to the 1920s.
    + Fighter: CR 5.  Scouts, fighters, and heavy fighters from the 1930s onwards (including the Naval Strike Fighter).
    + Trench Fighter: CR 4.  Attack aircraft up to the early 1930s.
    + Attacker: CR 6.  Attack aircraft from the late 1930s onwards (including naval attackers and the Jet Flying Boat).
    + Light: CR 8.  Light bombers, dive bombers, airships, Armed Floatplane, Early Flying Boat and Patrol Boat.
    + Medium: CR 12.  Medium bombers, and flying boats from the 1920s to the Heavy Flying Boat.
    + Heavy: CR 10.  Heavy bombers (the names usually omit "Heavy", it's implicit).  Generally one step higher FirePower than other bombers, allowing them to do more damage than a (CR 12) medium.
    + Torpedo: CR 9.  Torpedo bombers and torpedo-carrying floatplanes.  These can only attack oceanic tiles (so no bombing cities or ships in port).
* Buildings (Improvements and Wonders) have been almost entirely replaced with a set of air-themed ones, some with effects which resemble classic ones — and some which don't.
* There is (currently) no Space Race victory.  You'll just have to conquer them!
* The tech tree includes a core of 'pure' research (the Engines series, and various aerodynamics techs), with branches for different aircraft categories tracking along.  This tends to make it especially inefficient to race ahead with one category while neglecting others.
  - Don't ignore the seaplanes branch — you can't develop World War II fighters without Thirties Seaplanes.  This is because, historically, the impetus for high-speed aerodynamics research came from the Schneider Trophy seaplane races (most famously in the case of Supermarine).
* There is no Diplomat or Spy unit.  Instead, some aircraft are capable of some of their actions:
  - Recon aircraft (including light bombers, some floatplanes, and some heavy fighters) can Investigate City.
  - The Ambassador (an air unit, despite its Diplomat sprite) can Establish Embassy.
* The available government types are Revolution (a renamed Anarchy), Constitutional Monarchy, Democracy, Communism and Fascism — since the 20th Century was militarily characterised by conflict between those three systems.
  - Constitutional Monarchy pays gold upkeep, can use martial law up to 2, has more corruption than either demo or commu, and unhappiness owing to empire size is quite severe.  It suffers unhappiness from military deployments.
  - Democracy has some corruption (unlike the classic ruleset), but it doesn't vary with distance.  It suffers unhappiness from military deployments; and it has a senate which may prevent aggressive wars.  It gets extra trade from tiles, and even more if the city is celebrating.
  - Communism has less corruption (varying with distance), but has waste of shields, is bad at science, and produces extra pollution.  It gets two additional content citizens per city.
  - Fascism has rampant corruption, but pays no upkeep for certain military units, and gold (instead of shields) for the rest.  It also gets two additional content citizens per city.
* There are a few units which can be obsoleted but not upgraded.  Generally this is to remove clutter from the city build dialogue when a unit is surpassed by something different enough from it that upgrading would be unrealistic.  In particular:
  - Zeppelin Bombers are obsolete once you can build Thirties Bombers.
  - Zeppelin Liners can't be built after the development of Monoplane Transport (Airlift 1935).  This represents the public turning away from Zeppelin travel after the series of airship disasters culminating in the loss of the Hindenburg; past this point you will need to build Commercial Airstrips so that you can produce Airliners instead.
  - Marines are obsoleted by Assault Troops (Glider Assault).
  - Dive Bombers are obsoleted by the Naval Attacker (Carrier Aviation 1945).  Note that the latter cannot target ships.
  - Torpedo Bombers are obsoleted by the Naval Attack Jet (Carrier Aviation 1950).

### Insignificant Rule Changes

Mostly because the game starts in 1900, so quite a few things that would be reasonable for a Bronze Age civilisation to need to build should just already be ubiquitous.

* There is no Harbour building, but its effect is permanently applied.
* A city retains 30% of its foodbox when changing size (there is no Granary building).
* You start the game as a Constitutional Monarchy.
* The calendar advances by two months per turn (i.e. 6 turns per year).
* Unhappiness from units in the field is only 1 under governments that have it (Monarchy and Democracy).
* Road bridges and railways are available from the start.  So is Farmland, even though the building to enable its effect (Crop Dusting) requires the technology General Aviation.
* Workers are called Seabees.  Improvement build times are around 0.6 of classic (so, somewhere in between Workers and Engineers).  Transform Terrain is unavailable.
* Chance to steal tech on city conquest is 60%.
* There is no land-based Caravan unit.  Instead, Airliners can open trade routes, while the inexpensive Merchant Ships can 'enter marketplace' to earn one-time revenue — they yield considerably more than building Export (coinage), so long as they don't get sunk on the way!
  - However, one-time revenue from trade between your own cities only yields Gold.  If you want to get Science as well, then you need to go international (which is easier for enemies to blockade).

## Aircraft category usage

There are a lot of different kinds of aircraft, and it's important to know how they're used.

### Level Bombers

Light, Medium and Heavy Bombers all attack ground units and (apart from Light bombers and the Twenties Medium Bomber) ships.  The larger bombers do progressively more damage, but are more vulnerable to fighters — attacking ends their movement for the turn, giving fighters a chance at them.  Try to 'use up' the enemy's fighters with sweeps before sending in your heavy bombers.

### Dive Bombers

These also attack ground units (and the Dive Bomber can attack ships), but are powerful for their size — dealing damage comparable to medium bombers.  However, they're short-ranged and _very_ vulnerable — even a Biplane Scout has a decent chance to shoot down a Dive Bomber.  If you have air superiority, though, dive-bombing can throw the enemy's ground forces into total disarray.

### Attackers and Strike Fighters

These attack ground units, but attacking does _not_ end their turn (they only have 1 fuel).  They can take out assault units in the field (especially if weakened by bombing), but are unlikely to do much damage to defensive Troops or units fortified in cities.  Some later models gain the ability to attack sea units, and in the 1960s they develop into multi-rôle combat aircraft that can also handle air-to-air fighting.

### Torpedo Bombers

These aircraft, which are carrier-capable (some are seaplanes) have one purpose only: sinking ships.  Most have a FirePower of 2 to go with their nine Combat Rounds, giving them almost as many potential hits as a heavy bomber.  However, they tend to be fairly vulnerable (some torpedo floatplanes even have zero defence).

After TBs become obsolete, the Naval Attack Jet can take on the same role (it can also operate as an Attacker).

### Flying Boats

The Early Flying Boat operates like a slightly longer-ranged light bomber, but the Patrol Boat and the Twenties, Thirties and Heavy Flying Boat can all attack ships.  Combined with their long endurance, this makes them great sub-hunters.  And (like all seaplanes) they can use Buoys and Seaplane Tenders as refuelling bases.

### Lighter Than Air

The Zeppelin Scout is pure recon, but the Zeppelin Bomber is a long-range (though slow) level bomber, while the blimps attack naval units, making them the _other_ great sub-hunters — much cheaper than flying-boats but not quite as powerful.  There's also the Zeppelin Liner, a non-military unit which acts as an early, slow Airliner for establishing trade routes.

### Transports

Transport aircraft are a fast way to move Assault-class units around, but can only land in cities or at prepared airbases.  (Getting some Seabees onto a beachhead and having them build an airbase can be an effective way to pour units into an invasion.)  Transports have no combat strength, so make sure to provide plenty of air cover!  Some bombers can transport a small number of units, as can some flying-boats — and the latter can unload units from a Buoy in coastal waters (which **might** be slightly safer than trying to build a base ashore).

Also, paratroopers can deploy from transports in flight.

Somewhat related, the Airliner is a non-military unit which can establish trade routes — it's a bit like the classic Caravan, except it flies.  The Ambassador is another non-military unit, which establishes embassies (it's not capable of other Diplomat actions, though, so no need to fear it).

### Gliders

When you need to land troops somewhere, and you don't have any airbases there, you can't land transports — but you _can_ land _gliders_.  You won't get them back, though; but hey, they're cheap to build, and if the invasion goes according to plan you'll only need them once.  They do need to be towed to the LZ, though, which is a good use for obsolescent bombers (and you _do_ get the bombers back.  Unless the enemy shoots them down).

### Helicopters

The Early Helicopter is just a short-ranged antisubmarine patroller (except that it can use its dedicated Heli Assault Carrier as well as regular aircraft carriers), but the Helicopter can also carry one Assault unit and — unlike transports — land it anywhere.  It's like gliders, only without the annoying "have to throw away the glider" and "need a tug" bits!

### Fighters

Fighters can be used to hack down enemy bombers — even if you're not quick enough to catch them before they bomb, they'll be stuck where they are for the rest of the turn so you've got plenty of time to attack them.

Fighters can also escort attackers on strike missions (since the strike doesn't end the attacker's turn): move the fighter next to the target, then move the attacker onto the same square.  After the strike, move the attacker home and then follow with the fighter.

#### Escort Fighters

These heavier fighters aren't quite as good in a dogfight as their single-engined brethren, but their big advantage is that they have 2 turns of fuel, meaning they can cover a bombing raid, staying with the bombers after the turn ends.

### Carrier Wing

An aircraft carrier's loadout will probably be some mix of TBs, DBs, attackers and fighters.  The TBs go after enemy carriers, the fighters (CAP, Combat Air Patrol) deal with any strikes the enemy carriers launched, and the DBs and attackers support operations on land.  (The fighters might also fly some escort missions.)  The proportions of the different types will depend on what you expect to be fighting against — if the enemy has a lot of carriers, you'll need sizeable TB and CAP contingents, but if the enemy's airpower is weak in the theatre of operations you might be able to fill up with strike aircraft instead.

Some of the Light Bombers are also carrier-capable.  The main value of this is reconnaisance, allowing you to Investigate City far from your homeland.

#### Kamikaze

A Fascist nation that has build the great wonder Yasukuni Shrine can construct Kamikaze units.  These are Missile-class units, quick to build and highly effective at attacking ships; but they also cost one population to build, and as missiles are destroyed after attacking.  Still, a Kamikaze swarm can be a useful way to take out enemy aircraft carriers when your homeland is threatened.  They are also carrier-capable.

## Known cheesy tricks

Seabees can build improvements while transported.  This is needed in order to allow building Buoys at all — from boats like the Landing-craft — but it also means that they can build them while on a plane.  So, a Twenties Flying Boat with a Seabees on board has essentially unlimited range over water: when fuel gets low, just drop a Buoy (it only takes one turn) then spend a turn moored at the Buoy to refuel.

Pulling the same trick with Airbases is a little harder, since they take two turns to build whereas transport aircraft only have two fuel (so can only loiter over the building site for one turn).  However, even the Twenties Transport has room to carry _two_ Seabees, who by working together can drop an Airbase out of the back of the plane in one turn.

So what about using this trick to land assault troops on an enemy island?  Well, unless you're very quick or have total air supremacy, the enemy will probably be able to get ground troops onto the airbase, denying it to you.  But assault troops can _also_ disembark from a seaplane moored at a Buoy, so if you drop one on the coast, you can use flying-boats to land an invasion force.  However, the assault units can't attack (or bombard) from offshore, so they will need an empty land tile to move onto.  Still, it could be a useful way to get extra value out of strong seaplane forces.

Because of how bombers work (OneAttack), they are highly susceptible to double-move shenanigans across TC (in and out before fighters can get the shot at them they're supposed to).  Use of unitwaittime in game settings is recommended in timed-turn games.  (This is not applicable to attackers, which under normal circumstances _never_ come under fighter attack while outside their bases.)
