# Aviation Ruleset for freeciv-2.6

## Empire building in the Age of Flight

In this ruleset, there are only a handful of ground and sea unit types — but over a hundred air units!
As well as a 50-year span of technology (from the pioneer era to the early supersonic age), there are an efflorescence of different _categories_ of aeroplane, many with their own special rules.

Bombers, dive bombers, torpedo bombers and strike aircraft attack ground (or in some cases sea) units.  Ground units can make airborne assaults either by parachute or by glider.  Gliders are towed by bombers, and expended once dropped; paratroops jump from transport aircraft.  Sea units can transport either carrier-capable aeroplanes, seaplanes or ground units.  Airliners create trade routes between cities.  Reconnaissance planes watch the enemy to find out what he's up to...

... and Fighters try to shoot down everything else!

## Development Status

The rules all seem to be working, although we're a bit short on City Improvements and (especially) Wonders.  The tech-tree goes up to the 1950s, but will be extended up to the present day in later versions.  Balancing has been done by rule-of-thumb only — there has not been much playtesting yet, so some units might be useless while others are overpowered.

The main thing that's missing is tiles (and other art).  I made _one_ unit tile (the Pioneer), and it took a whole night; so I've decided to use a bunch of placeholders for now (units are two-letter codes, vaguely reminiscent of hull symbols, while buildings are just using vaguely-appropriate-looking classic building images) while I get the ruleset sorted out.

Also missing is governments.  I've stripped out everything except Democracy and Anarchy (which I've renamed _Revolution_), but I intend to add Communism back in and also add Fascism — since the 20th Century was militarily characterised by conflict between those three systems.

## Significant Rule Changes

* Ground units have been split into two classes, Land and Assault.  The difference is that Land units can't be transported, either by sea or by air, whereas Assault units can.
  - The idea is that Land units are defensive, and have heavy weapons (tanks, artillery), whereas Assault units can be brought rapidly into an attack but don't have as much equipment with them, making them weaker defenders.  Paratroops in particular will struggle to hold their gains unless quickly reinforced.
  - Neither the Airlift nor Paradrop actions are used.  Instead, units are loaded into specialised aircraft.
    + Assault units can load into Gliders, which in turn load into another aircraft (the tug: a medium or heavy bomber).  The tug flies to the drop zone, then the Glider unloads from the tug, then the Assault unit unloads from the Glider; the Glider is now stuck on the ground, so disband it.  (Unfortunately, it's possible to cheat by unloading from the Glider while it's still on tow.  I haven't figured out how to fix that yet.)
    + Assault units can load and unload from transport aircraft at cities and airbases.
    + Paratroops can unload from transport aircraft while in flight.
    + Some heavy bombers and flying-boats also have a small transport capacity.
* Aircraft can't typically attack all unit classes.  Most will be specialised to attack either other aircraft, ground units, or sea units — although a few types can attack two or even all three.
* Aircraft are split into four unit classes:
  - Air.  Ordinary landplanes refuel-at-cities-and-airbases, but can't use aircraft carriers.
  - Carrier-borne.  Can operate from aircraft carriers (but not the Seaplane Tender).
  - Seaplane.  Floatplanes and flying-boats can operate from the Seaplane Tender (also the Light Aircraft Carrier).
  - Glider.  See airlanding-assault rules above.  Note that Gliders cannot land in Mountains.
* Instead of providing vision, Buoys act as airbases for Seaplanes, allowing them to refuel on long overwater missions (but don't prevent stack death).
* Sea units can't attack at all; they're all support vessels.
  - An Aircraft Carrier unit, for example, represents a CVBG (Carrier Battle Group) — while there are many gun-toting warships escorting the carrier, they're all too _busy_ escorting the carrier to run off and shoot someone else's ships.  And no carrier Admiral is going to initiate a surface gun-range engagement with an enemy CVBG (unless he _wants_ to end his career).
* Land and sea units are very slow.  If you want to get anything done, you'll need to use planes to move stuff around.
  - Roads don't speed up movement at all, and Railroads only reduce movement cost to 2/3.
* Unit Hitpoints and Firepower vary a lot, as does Fuel; just looking at the A/D/M numbers won't give you an accurate picture of a unit's capabilities.
* Buildings (Improvements and Wonders) have been almost entirely replaced with a set of air-themed ones, some with effects which resemble classic ones — and some which don't.
* There is (currently) no Space Race victory.  You'll just have to conquer them!
* The tech tree includes a core of 'pure' research (the Engines series, and various aerodynamics techs), with branches for different aircraft categories tracking along.  This tends to make it especially inefficient to race ahead with one category while neglecting others.
  - Don't ignore the seaplanes branch — you can't develop World War II fighters without Thirties Seaplanes.  This is because, historically, the impetus for high-speed aerodynamics research came from the Schneider Trophy seaplane races (most famously in the case of Supermarine).
* There is no Diplomat or Spy unit.  Instead, some aircraft are capable of some of their actions:
  - Recon aircraft (including light bombers and some heavy fighters) can Investigate City; most (but not the very earliest ones) can survive it (unit flag "Spy").
    + However, game engine limitations mean that aircraft with Recon capability can't be ordered to attack units in a city (the dialogue box has no option for 'Attack').
    + Also, Spy flag requires Diplomat flag, meaning those aircraft will defend against enemy diplomatic actions.

### Insignificant Rule Changes

Mostly because the game starts in 1900, so quite a few things that would be reasonable for a Bronze Age civilisation to need to build should just already be ubiquitous.

* There is no Harbour building, but its effect is permanently applied.
* You start the game as a Democracy.
* The calendar turns by season (i.e. 4 turns per year).
* Newly founded cities have 2 population.
  - But settlers still only cost 1, so you can quickly spread across your continent.
* Unhappiness from units in the field is only 1, even under Democracy.
* Road bridges and railways are available from the start.  So is Farmland, even though the building to enable its effect (Crop Dusting) requires the technology General Aviation.
* Workers are called Seabees.
