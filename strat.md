# Aviation Strategy Notes

## Conventions and general notes

Every unit has a "ph-code", which is a two-character abbreviation
(usually derived from the unit's name).  These started out as the tags
for placeholder sprites (which are just large forms of those characters),
but can still be seen on e.g. the recognition charts.  Throughout this
guide, units are frequently referred to by their ph-code; on the first
mention of a unit we will usually give both the code and the full name
(e.g. "M2 Twenties Medium Bomber").  ph-codes in uppercase are aircraft
of one sort or another, whereas ground and sea units use lowercase.

"AP" and "DP" are Attack and Defence Power, computed as AP = A * FP * HP
and DP = D * FP * HP.  To a first approximation, these govern to-the-death
combats.  For OneAttack units with a CR (Combat Rounds) limit, however,
we also must consider Bombing Power, BP = FP * CR.  (CR rarely matters
for air-to-air combat, since _usually_ the fighter's HP runs out before
the fuel.)  "WR" or "winrate" is the probability of being the survivor in
a fight that continues to the death; if the attacker has CR, this will
usually only happen if it has multiattack and chooses to keep fighting.
This may also be called "Pk" (for "probability of kill"), but that
term may also be used for bombing (by which I mean anything OneAttack)
to mean the probability that the defender will die within the CR.
From the perspective of the defender, this is "Pd" ("probability of
death"), while the chance that the bomber will be shot down is Pk; the
sum of these is at most 100% but may be less owing to CR limits.  I also
have matchup tables showing two numbers: expected number of bombers to
kill, and expected damage to each; I don't have snappy names for those.
Some of these terms conflict with ph-codes: FirePower clashes with FP
Pusher Fighter, while Attack Power collides with AP Superprop Attacker
and Bombing Power with BP Intercontinental Bomber.
Hopefully it's always clear which one is meant here.

We often compare combat power of various kinds to build cost, either
between an aircraft and its upgrade or across categories within a given
year's tech.  Strictly speaking this is not always accurate, as the
upkeep costs (in shields and unhappiness) tend to remain fixed and will
therefore favour the more expensive aircraft.  So for instance if an
upgrade makes the unit 50% more powerful but also 50% more expensive,
it is still worth having as it has effectively cut upkeep by 33%.
Where the break-even point lies depends on how long you expect the
unit to live, how much of that time it will spend outside your borders,
and how difficult unhappiness is for you to deal with.  Also, note that
Longturn games generally run with `shieldbox 60`, magnifying the
importance of upkeep relative to build cost.

"lcmboat" means the Landing Craft, while "tender" is shorthand for
the Seaplane Tender, and "lphboat" is the Helicopter Assault Carrier.
"Merchies" and "subs" are Merchant Ships and Submersibles; CAM is the
Catapult Armed Merchantman.  A "cb" is a Seabees (worker).  The ph-codes
for carriers — cl, cv, ce and cn — correspond to the hull codes
CVL, CV, CVE and CVN which we use here; the actual unit names are Light
Aircraft Carrier, Aircraft Carrier, Escort Carrier and Nuclear Aircraft
Carrier.  The carrier family as a whole are also called "flattops".
A "torper" is any plane with CRtb (i.e. TB and HB families).  For that
matter, "TB" can refer either to torpedo bombers as a family, or TB
Torpedo Bomber specifically (similarly for "DB", "BB", "HB", and perhaps
"MB").  "Scout" is a blurry term; sometimes it means a single-seat fighter
(with "fighter" initially reserved for two-seaters), but sometimes
it refers to reconnaissance machines (or, as a verb, to the act of
reconnoitring).  For that matter, "Recon" (capitalised) usually means
the ability to Investigate City, whereas "reconnaissance" or "scouting"
can just mean flying around to explore the map or lift the fog of war.

Aircraft can be divided into 'fast' (fuel=1) and 'slow' (fuel>1).
Fast aircraft will never end a turn outside of a base, so are less
likely to be attacked.  Speed and range are quoted with M and F numbers;
"7M3F" means a move_rate of 7 and fuel for 3 turns.  OneAttack aircraft
(always Slow) don't get full use out of an odd-number fuel, since the
last turn doesn't increase their radius of action (e.g. although 7×3=21,
our hypothetical 7M3F can't bomb a target 10 tiles away, because bombing
halfway through the second turn 'wastes' its remaining four move);
it does however allow them to loiter (e.g. on ocean patrol) or bomb on
two consecutive turns (if they have enough HP left to do so safely).
It also increases their 'ferry range' (the distance they can cover on a
one-way journey between two friendly bases).  Multiattack aircraft lose
some effectiveness when operating at the limits of their range, as they
can spare fuel for only a few rounds of combat before they must turn
for home.  Don't forget that Ace or Elite aircraft have an additional
movement point, which can allow them to strike at longer range, or (for
multiattack) get in more hits per turn, than you might be counting on.
This is a big deal early on, when for instance the difference between a
Veteran ST (6 move) and an Ace (7 move) could be 50% more combat rounds
in an interception; it's less likely to matter for jets with 20+ move.

Airbases and buoys can increase the area over which your aircraft can
operate.  However, bases you build could be captured by the enemy, who
might then use them to land troop transports and cause you some major
headaches!  Tenders and carriers don't have this risk, but obviously
are restricted to the oceans; there is also the danger that the enemy
will sink your carrier, leaving your planes far out at sea with no base
within range.

"Interception" refers to a fighter attacking a bomber (or other slow
aircraft), whereas a "scramble" is when a fighter (or potentially any
other aircraft with nonzero defence) in a city (or base) defends against
a bomber.  When a fighter attacks a fighter in a city, technically
that's both an interception and a scramble, but we generally call it a
"fighter duel".
While bombers and other non-fighter aircraft can scramble against bomber
attack, they suffer a penalty that reduces their defence by a factor of 3.
In this guide, we do not discuss their performance in such scrambles, as
it's generally awful; all most of them can do is use up the bomber's BP.
Note that this penalty does not apply when attacked by Attackers
(including naval attackers and the Jet Flying Boat), since some of those
have AntiAir capability and could thus intercept them in flight (and we
have no way at present to distinguish the two cases in ruleset bonuses).
It also doesn't apply when naval aircraft are attacked by a torper (which
for non-fighters can only happen on a buoy), since in that case there is
instead a 2x defence _bonus_ for the seagoing fighters to counteract the
torper's strong attack / CR 18.

## Pre-war era

You aren't going to be doing much fighting — or at least, if somehow
you do, it won't involve air attack.  So the main thing of interest
is exploring the map and finding (a) locations to found cities and (b)
other civs.
The main options for this are reconnaissance aircraft (P0/PP/R1),
airships (ZS), floatplanes (HV/HS), and — perhaps surprising, this
one — merchant ships.

P0 has a pathetic range, and barely enables you to look beyond your city
borders; its main use is to be upgraded (or to let you start building
early, and upgrade the production when you get Passenger Carrying).
There is some benefit to building P0, though, in that it's Veteran, which
while totally irrelevant for the powerless Pioneer, can be handy once it
gets upgraded (so maybe you'd want to build a corps of P0s ready to turn
them into light bombers in 1915).
PP and then R1 are just about sufficient to let you scout out ahead of
your Settlers, but not much else; they take at least _slightly_ longer to
shoot down since they have 1 defence (but 0 firepower; they don't shoot
back).  However, unlike P0 they have the ability to **Spot** for your
artillery, turning your non-fatal bombarders into the most powerful
offensive land unit in the game.  (Spotting ends the plane's turn, but
that's not a problem if the enemy hasn't invented fighters yet.)

Merchant ships have 3 move and no need to refuel, and are cheap to build.
So they can map out the world's oceans and coasts pretty effectively;
in particular, this is a good way to find other civs.  (And when you do,
the merchie can enter the marketplace and pay for itself.)  However, they
of course can't explore inland, so they aren't great city placement scouts
(beyond finding empty islands you might want to send settler-boats to).

HV and HS basically extend the vision range of a Seaplane Tender.
Tenders have the same move speed as merchies, but cost nearly three times
as much.  However, the seaplanes on board can look inland, and the tender
can deploy them to locations far from your cities.  Thus, the combination
has perhaps the highest addressable area (if the continents aren't too
broad, it might technically be able to reach every tile on the map).
On the other hand, it's rather slow, as the tender can't make its full
speed without shortening the seaplane's reach.  This is particularly
bad for HV, which can only just keep up with a tender at full steam;
realistically HV should be treated much like P0, as a stepping stone.
(On the other hand, the infrastructure — a tender, possibly several
— will be useful later.)  HS has nonzero defence, which could matter
if you run into some very primitive fighters, and it can Spot for
Artillery inshore.
Seaplanes can also operate from the Line-of-Battle Ship, which at this
point is mainly of use to spot enemy submarines and manœuvre the ship to
deny them the initiative (against a battleship, subs' 4:1 attack/defence
ratio becomes 10:1 thanks to their hefty attack bonuses).  Also, HS gains
the ability to Spot for Naval Gunfire, which at sea gives battleships a
25% attack bonus.
Beware however
that carrying an aircraft slightly reduces a battleship's defence against
any attacks that _do_ slip through.

The Zeppelin Scout is by far the longest-ranged aircraft in the era,
with a 9-tile radius of action.  It can scout out good sites for cities,
discover neighbouring islands, and likely make first contact with rivals
while you're still out of their scouting range.  On the down-side, it's
slow, it doesn't have an upgrade path, and the tech branch will become a
dead end before long.  Also, if it _does_ make contact with other civs,
and they choose hostility and have _any_ fighters, it can't defend itself
and 30 shields will go down in flames.

At sea, you could attempt _guerre de course_ with Submersibles if you find
the enemy's shipping lanes.  A sub only needs to sink two merchies to turn
a profit (or better still, _one_ lcmboat carrying a settler), and until
the HA comes along in ~1914, the only things that can even attack it are
another sub or a battleship (the latter being very expensive and itself
somewhat vulnerable to submarine attack).
OTOH, once you start sinking them, merchies will just stop
putting to sea; but at least you're denying trade to the enemy (probably
they'll switch to building Export, which yields less gold and no science).
Subs' submerged endurance is very short — they can only spend two turns
underwater before coming up for air — but at this point there's nothing
with r²>2 vision to hide from, so they only need to submerge to attack.
If the merchies are sailing singly (rather than in convoy), you can even
take them as prizes, meaning you get the gold and bulbs for yourself
rather than merely denying them to the enemy; the sub needs to be on the
surface for this, but at this point in time that's not really a problem.
There's no ASW aircraft to spot and sink you, and if you're capturing
instead of attacking, the surfaced sub's lower Attack strength isn't
relevant either.

It might be possible to threaten undefended cities with Marines from
lcmboats, but typically they'll see you coming and have time to buy
some soldiers.  Even if all they can afford are Marines, the advantage
of being forted up in a city will probably enable them to hold you off.
On the other hand, fire support from a Line-of-Battle Ship (which has a
two-tile bombardment range and plenty of firepower) may tip the balance.
Dreadnoughts (circa 1910) bring increased mobility, but the additional
combat power is overkill against anything but another battlefleet and the
cost rises by a third.

If you find yourself with a land border, and want to invade, neither
Troops nor Marines will be much use on attack; you will need plenty
of Artillery to reduce the defenders.  Each volley will knock about
6HP off each defender, so three arty units should suffice to fatally
weaken them; with a fourth you'll be less susceptible to bad die rolls.
Troops have 40 AP for 30 shields; Marines have 24 AP for 24 shields; so
even ignoring the defence power, Troops are preferable for administering
the coup de grace.  The lowest you can reduce units in a city with arty
is 20% health, in which case Troops will have 4 HP and thus 24 DP; Marines
get 54% Pk whereas Troops get 86%.  (And you can't Spot units in a city.)
Either can clean up CBs in the field, but Marines
will struggle with Settlers (20 DP), with about a ⅓ chance of losing.
The best defence against an arty-and-troops stack at this point is to
put arty of your own in the city, allowing you to weaken the troops that
are defending the arty.  Then, attack them with Troops or Marines —
spread out across multiple tiles, so they can't arty the whole stack.
And since fortifying gives the troops a 15% bombard limit (so 3HP / 18DP
Troops or 2HP / 3DP Marines), it's easy to end up in trench warfare.
Fortresses double this to 30%; Troops will be reduced to 6 HP (36 DP if
fortified) which is probably proof against Marines (77% WR) but not Troops
(38% WR) and definitely not spotted Artillery (25% WR), while Marines at
4 HP (6 DP) won't fight off anything.
If the city has a Concrete Bunker, the limit is 50%, meaning Troops can
retain 10 HP and thus 60 DP, at which point attacking Troops have only a
1-in-6 win chance; it will likely take two units (at least one of them
Troops) to kill each defender.
The slow movement of ground units means that the defender can probably
be ready in time to repel the invasion, especially if they have enough
recon to see the attack forming up before it crosses the border.  Spotted
artillery is an effective attacker, but is susceptible to bombardment
itself, and your reach is limited by the short range of the spotters.

The Troop Ship can be useful for deploying defensive troops or artillery
between your existing cities, allowing you to quickly reinforce an island
outpost or a beachhead surrounded by the enemy; but it is vulnerable and
fairly expensive, and it can't unload without a city so isn't able to
deliver the initial invasion force to capture that first port.

Perhaps the most important fruit of the early tech tree is not a unit
but a building, the Flying Club.  Keeping your cities happy as they
grow is always a challenge for Democracies, and it rarely takes long
for the additional content citizen to pay for the 30 shield build cost
with their economic and material output.  As for the other buildings,
you are not likely to be in any hurry to build Flying Schools, as
there are at this stage few or no military aircraft to benefit from
the veterancy they provide.  Veteran PP or R1 have slightly more chance
to evade early scouts or fighters until they run low on fuel, maybe
letting them get home, but if the enemy has two scouts they'll still
die.
(An Ace unit gains an extra point of move, which would be useful even for
recon aircraft, but it is difficult to advance a unit to Ace when it is
not capable of combat!)
You might choose
to build them later when you start producing a meaningful air force;
or you might not; it's unclear whether the extra combat power is worth
it, as (thanks to CRs and multiattack) most aircraft won't take long to
experience the three or so battles it on average takes to earn Veteran.
Barracks may be worthwhile if you feel the need to have Veteran Troops
defending your cities or Artillery to go on the offensive,
and similarly Shipyards can provide a boost to
the effectiveness of Submersibles, but neither is really indicated at
this stage: a single green Troops will be enough to hold off most threats
until the big bombers show up, while subs' attack (4) is so far ahead of
the defence (1) of the potential targets that they're limited more by CR
than anything veterancy can help with (although it does have more effect
on a _surfaced_ sub, whose attack is 2; a veteran can more reliably sink
merchies without submerging).  The exception is if there's a naval arms
race of battleships, in which case veteran subs can really ruin some poor
Admiral's day.  (Conversely, veteran battleships are better at surviving
a wolfpack.)
Single-turn repair for land or sea units
could also have its uses in front-line cities.  I suppose it's possible
you might want to move your HQ around, but in Democracy there's little
reason to (corruption doesn't vary with distance).

The Lumber Yard will take a long time to pay for itself; like the later
factories (with which its effect doesn't stack) it's a rare city that'll
find it worthwhile.  Power Station (Steam Turbines) is a little more
expensive to build for the same 25% gain, but stacks with factories, so
has more enduring value.
On the other hand, the Aeronautical Library is
useful for research.  Balloon Rides create 3 lux, helping to keep a
growing city happy, but will become obsolete shortly after WWI.

Concrete Bunker boosts a city's defensibility against attacks with large
artillery support by a factor of 2.5, which might be important now if
someone's trying a ground invasion, but also can prove valuable later
against swarms of gliderborne artillery which might otherwise cause you a
lot of trouble.  (Basically, arty enough to hit the cap is a 5× force
multiplier, and the Bunker reduces this to 2×.)

There are a small number of Wonders available in this period.  War
College, with no tech prereq, will give an edge to the ground units
of its builder in a long war, as they will more rapidly rise up the
veterancy scale; unless you anticipate early war you don't want to tie
up resources by building it _now_, but having been the first to build
it will be advantageous later when war _does_ arrive.  Then again, later
wars will probably be decided by air battles, and too quickly for ground
troops to level up; attackers in particular will mostly be marching
into cities whose defenders have already been bombed into oblivion.
Defenders, though, might gain experience from living through the first
few bombing raids, and this is where the War College will be most useful.
The Yasukuni Shrine also has no tech prereq, but can only be built by
(and only provides benefits to) Fascist governments.  The additional
content citizen in every city is nice, but the main value of the Shrine
is the Kamikazes it will unlock far in the future.
Communists instead get to build the KGB Headquarters, which grants any
tech that at least two other players have researched; this means they can
avoid falling too far behind in tech despite their own poor science.
Lloyd's of London, a smallwonder, boosts one city's gold output, an
effect that only lasts until Twenties Airlift, but its real value is the
12½% boost to merchie revenue (which can be a big deal for a maritime
economy).
The smallwonder Statue of the Generals (Dirigible Balloons) loosens the
happiness constraints on one city's growth, by giving three extra content
citizens; but beware that its effect expires when anyone on the planet
discovers Bombers 1917, which might leave you struggling to keep that
city functioning until you can unlock General Aviation.
Kitty Hawk Monument is a _very_ small smallwonder, just producing a
constant 4 gold per turn until General Aviation.  Aeronautical Institute
roughly trebles the effect of one city's Aeronautical Library, but is
obsoleted by Aerodynamics Research.  In a large game, Jane's All The
World's Aircraft can be a real prize, allowing you to cut back on science
funding or just forge ahead with one branch of technology while neglecting
others, secure in the knowledge that Jane's will backfill for you.
The combination of Jane's and KGB is especially powerful, as it gives any
tech researched by a single other player.  (On the other hand, Communism's
40% science penalty makes it harder to develop the things you want if
no-one else happens to be researching them for you to steal from.)

## First World War era

Development in the 1914-1917 range is very rapid, as the skies militarise.
Compare, for example, the Armed Scout to the Biplane Scout.  Though
costing the same number of shields, an SB has over _six times_ the combat
power of an SA!  (The next sixfold improvement will take until the
arrival of jets with air-to-air missiles.)
The things you might do militarily with aircraft are:

* Reconnaissance.
* Attack enemy troops in the field or in cities.
* Attack the enemy's merchant shipping and sea transports.
* Hunt enemy submarines.
* Attack enemy aircraft.

### Reconnaissance

For recon, your tools are basically the same as in the pre-war era;
while a few longer-ranged aircraft become available, being military
they will cause unhappiness when outside your borders.  Still, a PE
Early Flying Boat in a Seaplane Tender can see a **lot** further than an
HS Floatplane Scout (though it can't spot for gunfire like HS can).
And as a battleship's sub-spotter it's longer-legged than an HS or even
the new HA/HT, though unlike those two it cannot attack the subs itself.
The ZB's gain over ZS is much less, and probably not worth the unhappies
(although it _does_ have the ability to transport units around, which
might be useful for logistics, along with its primary bombing rôle);
ZC Coastal Blimp actually has a _shorter_ range, although a higher
speed and a lower build cost (and *no shield upkeep*, though it does
cause unhappiness).  On the other hand, it can moor at a battleship,
which ZS can't, making it an interesting option.
However,
your old recon aircraft are now in danger from fighters, since neither ZS
nor R1 can shoot back.  HS has a little defence, but at only 6 DP,
anything but the earliest scouts can defeat it with ease.  Even the newer
R2 Recon / Light Bomber has a feeble 16 DP (although its vision range is
increased), and LE Early Light Bomber only has 18 — likely to fall to
even 1915 fighters.  The 1917-vintage L1 Biplane Light Bomber is rather
better, with 24 DP, but while likely enough to survive against a single
SM or SP, an FS or SS will probably beat it;
against FB, ST or its contemporary SB it stands little chance.
On the other hand, its 5M3F range may come in handy.

In summary: there aren't really any good options for contested recon, so
try to just keep your old ZS or HS exploring empty or friendly regions
of the map, and maybe re-equip your tender with a PE to do the same.
Artillery-spotting light bombers are likely to become 'Fokker fodder'.
Other aircraft should treat recon as very much a secondary rôle, rather
than their reason for being built.

### Anti-Ground

You have a few options to harass enemy ground units, but mostly they're
not hugely effective.  HA Armed Floatplane and R2 Recon / Light Bomber
are the earliest, each with 8 AP and 8 BP.  (R2 has the advantage of 16
DP; HA is defenceless.)  This is
not enough to kill even a cb; two aircraft _might_ do it if they roll
slightly better than average.  (If you catch an arty on its own, a single
lucky plane might suffice.)  Around about the same timeframe is the ZB
Zeppelin Bomber, with 36 AP and 8 BP (and enough fuel that it might be
able to strike again on the next turn).  In two turns it can expect to
kill a cb (92% Pk); but it only has 12 DP,
so even an FP can ruin its day, and R2's 16 DP aren't much better, with
even FP getting 35% Pk and SM getting 53%.
None of them really look worthwhile, until you consider the possibility of
using them in _combination_ with artillery on the ground.  For instance,
if a city's Troops have been reduced to 4 HP by an artillery barrage, then
a ZB gets 26% Pk and even R2 gets 2% (but 29% Pd).
Against Marines (bombarded down to 3 HP), R2/HA gets 68%-2% while ZB gets
an impressive 98% Pk.  While the ZB costs
more than the Troops you might otherwise use, the Troops are more likely
to have their own hitpoints attrited on their way to the battle than the
swifter-moving zeppelin.
As a tactical light bomber, R2 doesn't have the BadDefender flag, and thus
(unlike most aircraft) stands at least a little chance against ground unit
attack, getting 1% WR against Troops and 18% against Marines.  It's
actually a better defender than Marines, so might be a good choice to park
on a threatened airbase — or beachhead city — to hold it until you can
walk some Troops there.
It also has the ability to Spot for artillery, which HA and ZB don't.

Contemporanous with the R2 is the HR Reconnaissance Floatplane, to which
both HS and HA upgrade (and it's interconvertible with HT).  As a light
bomber it's comparable to R2, with 9 AP and 9 DP (thus slightly stronger
on attack but much weaker on defence); it can Spot for artillery or naval
gunfire, but despite the name does not have the Recon flag, so cannot
Investigate City.
It's 20% more expensive than R2 or HA, mainly justified by the greater
offensive strength of its HT alter ago.

1916 options are the LE, PE and BE.  LE and PE are similar, with 8 BP,
18 AP, and 18 (resp 9) DP; PE is more expensive, and really
shouldn't be deployed in the core theatre — it's meant for causing
trouble in far-flung outposts where only seaplanes can reach.  A swarm
of LE might be useful for taking out cbs, Marines or even Settlers;
but since on average it takes a single SP to bring an LE down,
they're probably only suitable for use within your own territory,
where enemy scouts will be short on fuel (killing a single LE will take
an SM 5 combats, and an SP 6.  Even an SS or ST will take about three).
So if the enemy comes a-marching with Troops and Artillery, LEs might be
good for finishing them off after a barrage from your arty weakens them.
If you use them in conjunction with arty against an enemy city, against a
4-hitpoint Troops the LE gets 11% Pk (a pair of LEs get almost 60%), which
is far more cost-effective than the ZB (though much shorter-ranged).
Another advantage of LE is that it has the FieldRepair flag, allowing it
to repair faster on airbases, which may combine well with its continuing
avoidance of BadDefender (though its DP are still not huge, getting 25% WR
against Marines).
BE Early Bomber is the first of the big boys, with 120 AP and 20 BP; it
can kill cbs and Marines without breaking a sweat, and even has an 11%
chance to knock out Settlers (more likely it'll just heavily damage
them, and you'll want something like an LE or PE to finish the job).
Against Troops in the open, both sides can expect to lose about half their
HP; so it accomplishes about as much as four LEs, at a much lower price.
Even in a city with a Concrete Bunker, artillery-reduced Troops (10 HP)
will fall to its bombs 37% of the time.
The downside is that it only has 30 DP; an SS will kill it 47% of the time
(and FB gets 71%),
though it does have a significant edge over an SM or SP.  An FS has the
same 47% Pk, but it would take about four combats to do it,
which is basically all its fuel.  One situation in which the BE _can_
win is if it catches the scouts on the ground (i.e. if it bombs a city
with only scouts, and no Troops, inside); there, it will expect to win
handily against anything up to at least SB (it even ought to beat S2 or S3
more often than not).  But that's a very situational capability, so most
of the time it may just not make sense to try to bomb cities at this stage.

In 1917 you get a wide variety of choices.  The LE upgrades to L1, with
36 AP and 24 DP (but still only 8 BP) as well as an extra point of fuel
(giving it 15 range, though still only 6 radius as bombing ends the turn);
it still needs to operate in swarms to accomplish much of anything, but
is at least that little bit better at picking off damaged units.  (Its
offensive capabilities are equivalent to the old ZB, at ¾ the cost and with
double the survivability, as well as a slightly higher speed, though of
course it still can't match the Zeppelin's long range.)  It now gets 50% WR
defending against Marines, and still has the FieldRepair flag.  It is
also carrier-capable, which might be helpful for going after undefended
islands or mounting a surprise attack against the soft underbelly.  But to
be honest its only really effective mission continues to be Spotting.
At sea the HN Large Reconnaissance Floatplane has somewhat weaker combat
stats — 20 AP, 10 DP — but the same 5M3F range and Spotting capability;
it's slightly more expensive at 32 shields (to L1's 30), but can convert
to HL for greater AntiSea firepower.
The PB is similar to the L1, with 36 AP and just 12 DP (although its 20-
tile range is among the best); really it is meant for the Anti-Sea rôle,
with its Anti-Ground capability serving only to provide flexibility
in an emergency.  And unlike the light bombers it can't Spot.
The heavy bomber line brings the BB Biplane Bomber,
which is much more resilient at 64 DP, though the offensive gains are more
modest at 160 AP and still 20 BP.  Still, as a bomber with the edge over a
single contemporary fighter (SB=40 AP), it just might be able to win you
a city if you can build enough; following up arty against a bunkered Troops
(10 HP), it gets 51% Pk.  It's actually more defensible (per shield) than
the light bomber, which is unusual.  Just watch out for FBs and STs (48 AP).
And speaking of triplanes, there's the alternative heavy bomber, the BT
Triplane Bomber.  It's arguable whether this should even be listed under
1917, since you can get to it _before_ even the 1916 bombers.  It has a
record 216 AP (20 BP), but it's vulnerable at only 36 DP.  If you don't
have to worry about enemy fighters, it's the most cost-effective of the
WWI bombers; but if a single SS shows up it's in trouble (39% Pk), and against
an ST or FB it's probably dead (65% Pk).  But there's also something
completely new: the TF Trench Fighter is the first _attacker_ in the tree.
Its 30 AP might not look that exciting, but it has multiattack, so it
can strafe a target until its HP is low and then turn for home, without
giving enemy fighters a chance to catch it.  It can kill a cb or Marines
fairly easily, and _would_ be able to take out a Settlers except that
doing so would take seven attacks which is basically all of its fuel.
(But it can fly out again next turn for another strike.)  Fuel also
means its radius of action isn't great; it can attack targets at most
four tiles from base (move three, shoot twice, move three back).  Thus,
it's primarily a defensive weapon, for use when enemy Troops or Marines
are marching into your territory.  At this task, though, it's far more
effective than an L1, and can do ⅔ the work of a BB for ⅓ the price.  In
three attacks against an arty-reduced fortified Troops (3 HP), it can get
82% Pk, which is better than Marines and almost as good as Troops, while
its 25-shield build cost lies between the two (and it has the advantage of
reach, and the ability to disengage if it's losing).

The overall picture is that ground invasions are even harder than
they were in the pre-war era, because TFs do more for defence against
slow-moving troop/arty stacks than BBs or BTs do for reducing the
defenders.  However, if you can get some Marines in on an lcmboat, they
might be able to walk into a city you've flattened with heavy bombers
— this still isn't _easy_, but it's a bit more feasible than ground
invasions even absent TFs.  (On the other hand, Marines can't hold a
city for long, so you'd better build or buy some Troops there faster
than the enemy's ground forces can get there to recapture it, or else
have a Troop Ship parked offshore ready to unload in the city.)
And if you _do_ manage to get some artillery in position at the enemy's
gates, bombers can deploy quickly to capitalise on that force-multiplier,
instead of you needing to guess at the size of a Troops stack sufficient
to both defend the arty and kill their victims when the ground force
first sets off.
Against a coastal city a battleship is a highly effective if expensive way
to deliver the artillery barrage, and at this stage isn't at great risk
from the air.

### Anti-Sea

The very first anti-shipping aircraft is the HA Armed Floatplane.
With 8 AP and 8 BP, it's distressingly feeble, taking two planes to
sink a sub and _four_ planes to sink an lcmboat.  Even a merchie will
survive six times out of seven.  What's more, it can't Spot for naval
gunfire like the HS can.  And it has
zero defence.  Only build it if you're desperate for a plane that can
hunt subs **and** mildly annoy ground units.
1915 tech brings the HR Reconnaissance Floatplane, which is only a minor
increment (9 AP, and cost is 20% up), but at least now it can Spot,
increasing the effectiveness of your battleships, and has an admittedly
meagre 9 DP to hold off the fighters.  It's interconvertible with the
other new unit, HT Torpedo Floatplane, which is defenceless like HA but
about 50% stronger on attack
(20 AP, 9 BP); on average it takes one raid to sink a merchie (65%
chance), 1⅓ to sink a sub (one time in seven the first raid will
do it), and 2½ to sink an lcmboat.
If your enemy's shipping lanes run through somewhere you can get a
tender without him noticing, and beyond the reach of his fighters,
you may be able to wreak havoc on his sea trade (though as always, the
likely effect is that you'll blockade him, rather than him obligingly
building more merchies and sending them out for you to kill.  Still,
this can stunt his economy in a way that is not to be sniffed at).
If he wants to force the issue, he'll likely need to build a tender of
his own and bring an HF to the party; you would need at least four HTs
to stand a decent chance of sinking his tender, so the economics now
tilt in his favour.  But if he hasn't developed seaplanes at all, he
can't do this, meaning his only option is to hunt your tender with subs;
in this case, the economics favour you, since as soon as the sub shows
up and attacks, you can retaliate with the HT.  He would need a large
and expensive wolfpack (three subs) to sink you first.  One important
thing to note about torpedo bombers (including the carrier-borne ones
when those come along) is that they **cannot** attack ships in port;
any aircraft with CR 9 or 18 may only attack into oceanic tiles.
Against battleships, torpedo floatplanes get shredded — they're simply
too flimsy and vulnerable to face the wall of flak a large warship can
put up to stop them.  Even a veteran HT will deal a mere 2.4 hitpoints on
average to a b0 Line-of-Battle Ship, with only a ⅐ chance to survive.

The first heavy bomber, 1916's BE Early Bomber, also has the ability
to attack ships at sea.  With 120 AP and 20 BP, it can easily take out
merchies or subs, just about sink an lcmboat (68% chance), or severely
damage a tender.  (Even if it wins every round it will leave the tender
with a single hitpoint.)  It also has a long loiter time, at least at
short ranges, which helps to mount continuous patrols over the ocean.
If the enemy's sea trade runs close to your shores, a BE can choke it off
quite effectively.  Again, his main defence will be floatplane fighters;
but the BE is more than a match for the HF (though two may bring it
down) and has decent odds against an HW (19% Pk).  (Of course, if the strait in
question is also close to _his_ shores, then his landplane fighters may
be able to spoil your fun.)  An important bonus is the vision range,
which is the same as the light bombers (r²≤4), helping you to find
targets even if your position reports are a bit stale; one effect of this
is that subs now have reason to submerge even when not mounting an attack,
in order to hide from a bomber passing two tiles away.
Heavy bombers have some capability against battleships, with 1% Pk-17% Pd
against the old Line-of-Battle Ship (the same attack performance, in
fact, as another battleship); on average two BEs (costing 120 shields)
are enough to sink a 150-shield b0, assuming they can get there without
being caught by fighters.
The bd Dreadnought is a tougher nut, but three bombers will do the job
(albeit with a 30% Pd) and still come out slightly ahead economically
(180 shields to 200).
Also arriving
in 1916 is the ZC Coastal Blimp, which is a fairly cheap airship
with a reasonable loiter capability and an ability to attack ships.
But it's very weak, with just 6 AP (though it does have multiattack,
which fixed-wing AntiSea won't get until the Fifties), which gives it
only coin-toss odds against a merchie and under 30% WR against a sub.
Since the blimp actually costs more than the merchie to build, this is not
a good trade; but you can disengage after every four CR (yay multiattack),
which in particular means you can damage a sub enough to potentially spoil
its attack plans and protect a battleship that might be carrying the
blimp.  (Subs' Pd is very sensitive to even slight damage, since attacking
a battleship will usually leave them on very low HP.)
More importantly, ZC is suited to scouting the oceans to find targets for
other craft, allowing you to employ your planes or subs more efficiently.
One good thing about the ZC is that it has no shield upkeep (although
it does still cause unhappiness when outside your borders), making it
cheaper in the long run than other ocean patrol options.  Beware its
zero defence, though; and note that unlike some other seaplane options it
can't Spot for naval gunfire.

At 1917 tech, a few more options appear.  The HT's upgrade is the HL
Large Torpedo Floatplane, now able handily to sink both merchies and subs
with its 32 AP and 18 BP.  It can sink an lcmboat (14% Pk-<1% Pd);
a pair will handily dispatch a tender or troopship.  Sadly, it still has
zero defence, and (like all FP2 torpers) scrambling fighters get double
defence against it (so e.g. 14% Pk-14% Pd vs HW, or 17%-83% vs H2).
Its light-bomber conversion, HN Large Reconnaissance Floatplane, is much
weaker at 20 AP and 8 BP (although its 10 DP _might_ serve some purpose),
but can Spot for your battleships' guns, and its 3 fuel gives it a loiter
capability, spending more time on-task and less time flying home to refuel
than the old HR.  When bombing a sub it gets 4% Pk, though if it attacks
again on the next turn it achieves 95% with only 1½% Pd.  Against a
merchie Pk is 47% on the first turn, 99% (1% Pd) on the second.
The other seaplane option is the PB Patrol Boat, which
unlike PE can now attack ships; it has 36 AP but only 8 BP, meaning it
can just about one-shot merchies (68% chance) and maybe subs (10% Pk).
Against a scrambling HW it will draw but with the advantage in damage
dealt; if the HW then attacks with its remaining hitpoints there's a
decent chance the PB will survive.  (E.g. HW@5 vs PB@9 the PB wins 45%.)
With its long range / loiter capability (5M4F), PB can also be effective
at finding targets
for other forces (planes or subs) to converge on.  12 DP leaves it fairly
vulnerable — an HF will bring it down handily (61% Pk), as will pretty
much any
fighter except for SA and FP — so you'll want to restrict it to areas
where the enemy can't get air cover (e.g. the middle of the ocean if he
doesn't have seaplanes).  New heavy bombers retain their anti-shipping
capability; BB and BT both have better odds to one-shot an lcmboat (78%
and 84% respectively), but as with the BE it will take two planes to sink
a tender.  The BT is probably a poor choice for this job, as its extra
Attack point makes little difference against D=1 ships; it's expensive,
slow, and vulnerable.  Far better to use the BB, which can survive
contemporary fighters and maybe even a lone S2 or S3.
It also has the same 5M4F range as the PB.  Of course, heavy bombers
aren't cheap, but if you're building a force of them anyway (perhaps for
some usage against land targets...) they can be very effective in any
anti-sea opportunities that may arise.
And they're both quite effective against battleships, where BT's Attack
actually matters and gives it 5½% Pk-1% Pd on b0 (BB gets 3%-9½%).
There is one other new type, the
TE Early Torpedo Bomber, which is basically a landplane equivalent of the
old HT, with a similar 9 BP.  Its advantages are 27 AP, slightly longer
range, and 9 DP, which is enough to fight off SA but not much else.
(An SP at long range might not have enough fuel to finish the job, and
against an HF it does at least have a 20% chance.)  On the other hand,
the TE is carrier-capable, and its upgrade path will get a _lot_ better,
so it's a stepping-stone.  It's slightly cheaper than the seaplanes, at
27 shields, but it doesn't have the hard-hitting capability of the HL; it
would take ten of them on average to sink a dreadnought, each standing
only a 7% chance of surviving the bombing run.  And it can't convert to a
spotter like HL can.

The summary here is that apart from BE/BB in your home waters (perhaps
to sink an invasion fleet of lcmboats?), none of this is much good if
the enemy has HFs (or SFs).  If he doesn't, then PBs and ZCs are good
sub-hunters and HT/HL can interdict merchant shipping or troopships.
Meanwhile battleships and dreadnoughts remain 'queen of the seas', at
least as long as the submarine threat is suppressed, and HR/HN provide
them with a useful force-multiplier (e.g. raising a dreadnought's WR in
pitched battle with another dread from 27% to 45%).

### Anti-Air

Aerial Weapons, the 1914 tech, gives two extremely primitive lash-ups, SA
Armed Scout and FP Pusher Fighter, with 6 and 12 AP (and DP) respectively.
These are almost completely useless against anything that can defend
itself (the best figures are FP's 86% winrate against HS), but are of
course entirely adequate for destroying defenceless R1/R2, ZS/ZC, am,
LZ, or even HL.  So if your enemy's spotters are _really_ annoying you,
or a swarm of ZBs are giving your cbs headaches, you might want to build
one; but apart from that rather improbable scenario, the only use for
either is as a stepping-stone to upgrade to something decent ASAP.
(And FP has quite a while to wait for its upgrade.)

1915 brings a spread of choices.  SM Monoplane Scout and SP Pusher Scout
are very similar — SM has 16 AP and 16 DP, while SP has 18 AP and 9 DP.
So you'd think SP is slightly stronger on attack; but SM having 2 FP gives
it effectively double the CR, so when operating at range, SP might not
have enough fuel to make full use of its extra hitpoint.  Also, of course,
in a scramble (scout on base defending against bomber) SM will be nearly
twice as strong.  So SM is better in most cases, but SP has a slight edge
when shooting at a bomber parked just outside the city (e.g. on its way
home after bombing) which in some cases _is_ the most likely scenario.
SP's FieldRepair flag may help if it's defending an airbase from bombers.
And Engines 1915 (for SP) is quicker to research than Interrupter Gear
(for SM).  At the end of the day, it doesn't make that much difference
which one you choose, because they both have the same upgrade path (to
SS, which requires both of those techs to reach); if you are in a hurry
to get any of the things that depends on Engines 1915 (HF, HT, ZB, R2)
then you may as well take that route and get the SP, whereas if you're
under heavy bombardment and need the best scramble scout immediately
then you'll prefer SM.  Once you have both techs, you can then research
Effective Scouts, which unlocks the FS Two-seat Scout.  This costs 50%
more to build, but with 32 AP and 16 DP (and a mere 6 move) it's a strong
if situational interceptor.  One advantage is that you save on upkeep, so if
all you need is AP then FS might be better.  (Also, its upgrade is good,
at least for a little while.)  In a scramble, FS merely matches the
performance of the cheaper SM.
We must also consider the HF Floatplane Fighter, which in
itself (14 AP, 6 DP, 7 move) is inferior to the SP that precedes it,
but as a seaplane can be deployed on a tender to protect shipping, or on
a battleship to provide air cover to the fleet.
In this rôle, it is likely to be facing weaker opposition such as
floatplane bombers (zero defence up to HL, and even HC will fall 74%
of the time) and flying-boats (HF has an 80% win against PE and a 61%
against PB).  Against the scouts it wins 93% vs HS, 80% vs HR and 74% vs
HN, all entirely adequate to interdict enemy spotters.
In a scramble it has 38% Pd against HT and 6% Pk-94% Pd
against HL; PB will kill it 37% of the time.  Against HA it will likely
draw in the scramble, with <1% Pk-3½% Pd.
If it's the only fighter you can get into the theatre, it's better than
nothing; but its weak defence means a concerted assault on the tender can
chew it up cheaply.

The breadth of choices continues in 1916, as the main Scouts tech gives
the option of SS Sesquiplane Scout or FB Fighter Biplane.  With 32 AP
and 16 DP, SS is a solid improvement over the previous single-seaters,
fully adequate to intercept contemporary bombers (47% WR against BE,
81% against LE, 39% against BT), though in a scramble it's no better
than SM.  As usual for a two-seater, FB is about 50% stronger on
interception with 48 AP, but in a scramble it really shines with 32 DP.
That's potentially enough to shoot down an LE or PE (36% chance), or
deal 25% damage to a
BE; by comparison, an SS has only 9% chance to down LE or PE and will
scarcely scratch a BE.  FB also has the FieldRepair flag, which SS
doesn't.
Set against that are its 50% extra cost and its 7 move (one
less than the SS), and its lack of an upgrade path (until the ’30s);
building FBs only makes sense if you need the _best_ scramble defence
_right now_.  There is also another option, through the Triplanes tech
which unlocks ST Triplane Scout.  This has 48 AP (same as the FB) but 16
DP (same as the SS), with a price tag equal to the SS.  That makes for an
effective interceptor, but there are two downsides: it only has 6 move
(so may not have enough fuel to finish off the target) and it doesn't
upgrade until the Twenties, which can leave you with a scramble gap.
Its FieldRepair flag may help it when forward-based on airfields to catch
slow heavy bombers on their way in, a tactic that could help make up for
its short range.
One last point about the ST is that Triplanes is a prerequisite for
Triplane Bombers, so if you want to operate BTs you might well develop
STs before Scouts 1916 and thus end up using them.

The headline fighter of 1917 is the SB Biplane Scout.  With 40 AP and
40 DP, it's a solid all-rounder, with interception almost as good as
FB/ST coupled with better scramble than anything before it (and still
with the 20-shield price tag).  It pretty much knocks everything before
it into a cocked hat, and once you have it you're unlikely to build
any other landplane fighters.  Its only slight downside is its lack of
FieldRepair.
At sea, you have two choices: the HW
Fighter Seaplane, an upgraded floatplane with 20 AP and 20 DP, and the
new option of carrier aviation in the form of the SF Shipboard Fighter.
Though navalisation leaves it slightly weaker than the SB, at 32 AP 32
DP it's distinctly stronger than an HW (and is slightly cheaper to build,
at 20 shields against the HW's 27).  Set against that, of course, is the
fact that a CVL is over twice the price of a tender, so while SF makes
sense as the air defence for a carrier task force, if all you want is to
get fighter cover over some ships that don't already include a flattop,
the seaplane solution is much cheaper overall.  In a scramble, the HW is
more likely to survive, but the SF will do more damage to the bomber.

To sum up, through most of the era there's a confusing panoply of options
(should you go single-seat or two-seat?  What about triplanes?) but
progress is so rapid that whatever you choose will be obsolete
pretty soon, so unless you're fighting off an air armada and need to
micro-optimise, the simple SP→SM→SS→SB progression is probably
the way to go.

### Naval Aviation

Gathering together the strands from the various sections above, seaplanes
are an effective low-cost way to go after merchies and subs, or to
defend your ships from enemy aircraft, but they're not much use in the
shore strike rôle.  Carrier aviation isn't greatly useful when it first
arrives in 1917: TE is little more than an HT; L1 is just not all that
powerful (on average it will take two of them just to kill a Marines,
or 1⅔ to kill a cb; an intercepting HW will kill it 33% of the time,
and SB 85%); SF is good as far as it goes but it's not clear how it
can justify the cost of a CVL when you could just run HWs and tenders.
And while L1's decent-ranged Recon capability might be useful in
conjunction with other forces, it's hard to _bring_ those other forces
into the kind of battlespace it needs a flattop to reach.
So really, operating a carrier at this techlevel makes little sense;
the only reason to start building one is if you think you will want it
later when you get better planes for it.  A CVL can be sunk by an average
of 1.8 BEs, costing only 20% more than the carrier; alternatively 2⅔ HLs
will do the same for 85 shields (slightly less than the CVL, but probably
also needing a 50-shield Tender to get them into position),
though of course the HLs have zero defence and in fact — thanks to their
weak 8 HP — may not even survive attacking (2% Pd).
A pair of subs each attacking twice will have a solid 54% Pk-22% Pd
(if they're veteran this jumps to 89%-6%), so
make sure you have decent ASW active.  It would probably take about
*five* TEs to sink it (120 shields), which further underscores how feeble
they are.  (4× TE gets 26% Pk, 5× gets 86%, and Pd is just 0.03%.)
The best excuse I can think of for operating TEs is to earn veteran
levels that can be carried across an upgrade, which is rather a thin
justification.

Naval fighters scrambling from tenders or carriers are fairly effective,
particularly against torpers — for instance, an HW scrambling against an
HL gets 14% Pk-14% Pd; against L1 both will survive (facing two L1s it
suffers 53% Pd), though a BB will blow it away (96% Pd).  Against TE it
gets <1% Pk with no Pd.
SF beats an attacking HL nearly 83% of the time, and gets 5% Pk-1⅔% Pd
against L1 or 27%-7% against TE, but BB still blasts it (99% Pd, <1% Pk).
Generally this means that you want to use level-bombers to sweep up the
ship's CAP before sending in the torpers to sink the ship itself.

For battleship aviation, the main choices are to embark air cover in the
form of HF/HW (highly unlikely to scramble when the ship itself is so
powerful, so mostly acting as an interceptor), to bring a ZC or PB for
ASW (either is adequate, but ZC is probably preferable simply because of
its cheapness, unless you're in a situation where you need killing power
against the subs rather than merely locating them), or to get naval
gunfire spotting from an HR or HN.
There's not a lot of
reason to carry HT/HL on a battleship since the ship's own guns are much
more effective against other boats, and the ranged strike of a tender or
flattop is little more than a nuisance to a battleship.
What you choose to carry will depend on the enemy forces, as either heavy
bombers or submarines could pose a threat to a battleship without the
corresponding defence, while in the absence of either you might prefer the
attack bonus from spotting.
The ASW options are very good at what they do;
the fighters less so (simply because heavy bombers' defence is actually
pretty good and floatplane fighters even in 1917 only get one FirePower),
except for retaliating against a bomber that's already been severely
damaged by the battleship's own flak.  On the other hand, they do go some
way towards discouraging the enemy from using BTs or spotters of his own.

Alternatively, you can convert your old Line-of-Battle Ships into CVLs;
unlike upgrading them to Dreadnoughts this doesn't cost gold, but it does
mean sitting in dock for three turns doing nothing useful.  And as
mentioned it will take a little while to get decent planes to put on it
(except for the SF, which is a much more effective air defence for your
battlefleet than HW, though this gap will narrow post-war).

### Civil Aviation

It's not all about the fighting, as two new utility aircraft arrive
in 1917.  The Ambassador is a moderate-ranged (4M4F) unit with the sole
purpose of establishing embassies in foreign cities, allowing you to keep
tabs on what your near neighbours are up to.  Slightly shorter-ranged
(3M4F), and a large investment at 60 shields, the LZ Zeppelin Liner allows
you to establish trade routes, highly lucrative over the long term.
Of course both are entirely defenceless should they find themselves
in the company of unfriendly aircraft, but across borders where peace
reigns they can do much for international peace and co-operation.

### Buildings

1914 techs unlock a few buildings.  Recruiting Office (Aerial Weapons)
allows you to save two shields of unit upkeep; costing 50 shields to
build, it thus takes 25 turns to pay for itself at a zero discount rate.
But if you have nothing better to build, it may be a good long-term
investment.  Of course, gold-paying governments (which includes the
starting Constitutional Monarchy) gain nothing from it.
Technical College (Aircraft Industry) is the next step for
the science economy, boosting the city's research by another third.
Repair Sheds (Aircraft Industry) and Aircraft Slipways
(Military Seaplanes) provide single-turn repair to landplane and seaplane
units respectively; when war comes you'll want at least a scattering
of repair depots for such aircraft types as you field, to ensure you
can sustain your combat-ready strength after the initial engagements.
Also under Military Seaplanes is the wonder Naval College, which does for
ships, seaplanes and carrier-capable aircraft what the War College does
for ground troops.  As mentioned earlier in connection with the Shipyard,
veterancy doesn't do much for sub attacks anyway, so the main benefit for
ships is likely to be in _defending_ themselves, either from subs or from
air attack.  Veteran seaplanes will be that much more effective at their
usual tasks of raiding shipping or protecting your merchies from enemy
subs and planes (for instance, veterancy more than _doubles_ an HT's
Pk against a sub, or an HL's Pk against an lcmboat).  Later, this
may prove useful in making carriers and their air wings more powerful.
(And note that dive-bombers and many light bombers, being carrier-capable,
come under the Naval College's rubric even if you only ever operate them
from land bases.)
And of course if the world builds battleships, suddenly veterancy for subs
and dreadnoughts becomes a big deal, as ship-to-ship combat on vaguely
even terms is possible.

1915's Zeppelin unlocks the Airship Company, which slightly boosts luxury
(but goes obsolete with General Aviation).  Significantly, for civs with
0% luxrate, Balloon Rides's 3 lux only gives one happy citizen, but
Airship Company lifts this to 4 lux and thus a second happy citizen.
Early Blimp in 1916 gives
access to Barrage Balloons, but since those are for defence against
dive-bombers — which aren't invented until the Twenties — you're
unlikely to need it just yet.  When they do arrive, it'll be a handy
little bonus if your opponent happens to use a diver armada (largely
nullifying their BP advantage over heavy bombers), but if they favour a
different mode of attack (or choose one after noticing you've built
balloons) it may just be a waste of shields and gold.

There are a couple more buildings that arrive with 1917 techs.  War
Memorial (Bombers 1917) is useful for a Democracy fighting offensive
or maritime wars where aircraft will often end their turn outside its
borders; it's less important if your war effort consists chiefly of
putting up fighters against enemy bombers over your own territory, and
of course it's irrelevant for Fascists and Communists.  Flak Battery
(Anti-Air Artillery) gives a small boost to a city's AA defence, but
given you could build another Troops for the same price (albeit with
shield instead of gold upkeep), it's probably only worthwhile for a
city which is going to hold a large stack of units.  It will, however,
become more useful later when Proximity Fuse is invented, more than
doubling its effect.  Mooring Mast (Effective Airships) is required
to build Zeppelin Liners, and lets a city access a second trade route
(without it, a city can only _receive_ one LZ from elsewhere).

### Other Tech

The Escape Parachutes technology, which is roughly 1916 and depends on
the lighter-than-air line (Early Blimp), gives the fairly minor benefit
of a 10% increase in veterancy chance.
This is most useful for units that can expect to live through many
combats, either because they have multiattack (scouts/fighters,
attackers) or because they are strong enough defensively to survive
interception (BB).
It's pretty weaksauce, but it's also fairly cheap to research, so might
be worth getting towards the end of the era (or in the Twenties).

## Inter-war era

Without the pressures of a World War to drive it, the pace of improvement
in aircraft performance slows down; instead, the key developments of
the ’twenties and ’thirties are qualitative in nature, as the new
technologies are put to peacetime use and as new theories are formed about
how to fight the next air war.  The biggest innovation is a whole new
application of air power, in various forms of airborne troop transport and
logistics; but there are also new ideas of how to fulfil existing rôles.

### Reconnaissance

All the old recon platforms see upgrades in the ’Twenties.  Airships get
the ZD Twenties Blimp, which has better range (5M4F) than the old ZC,
though remains defenceless.  It still has zero shield upkeep, which
is nice.
HC Coastal Seaplane _finally_ brings Recon to the floatplane line, and
has a little defence (10 DP, enough to _maybe_ survive an HF (74% Pd)),
but the range is no better than HN and it's still its other capabilities,
rather than Recon, that must justify its price tag.  However, at least
now it combines Spotting and torpedo-bombing in one unit, rather than
needing to Convert back and forth.
P2 Twenties Flying Boat
(still not capital-R Recon) gains additional speed and vision (r²≤4),
as well as beefing up its survivability to 28 DP (still not great,
an interception by HW has 20% Pk and H2 will win three times out
of five), so it can do a good job of scouring the oceans for targets
(against merchies or subs it will likely just operate as AntiSea and
sink them itself, but if it spots an enemy carrier it'll be glad to
call in assistance).  L2 Twenties Light Bomber, similarly, is faster
(6M3F) than L1, and has better defence (45 DP, giving it a fighting
chance against enemy scouts).  Really, you might choose any of these,
depending on what you want to achieve — ZD or P2 for ocean patrol,
L2 for city Recon, or HC for the same if there's no ships around for it
to AntiSea on.  But note that ZD doesn't have an upgrade path.

In the ’Thirties, only the flying-boats and light bombers see upgrades.
P3 Thirties Flying Boat is faster (9M3F) and better-defended (54 DP) than
its predecessor, but it's still fairly vulnerable (contemporary fighters,
even the H3, threaten it cheaply).  The L3 Thirties Light Bomber is
also fast (10M2F) and defensible (60 DP), as well as having slightly
longer vision (r²≤5), but doesn't have an upgrade path (which will be
Bad News once fighters improve).  Still, that speed should allow it to
get in and out (Investigate City doesn't end your turn, and nor does
Spotting once you've got Radio) quickly enough
to avoid fighter interception, at least on cities close to the border.

1935 tech brings a few more aircraft.  HB Floatplane Bomber replaces HC,
with increased range (7M3F) and defence (15 DP, which still isn't great);
while it does have Recon, it's really meant more for AntiSea duties.
PH Heavy Flying Boat is also primarily an AntiSea (and like all the
flying-boats it _doesn't_ have Recon), but its long range (10M3F)
makes it great for ocean patrol, and its 75 DP enables it to survive
against at least the previous generation of fighters (which includes
the H3, that doesn't have a 1935 upgrade).  On the other hand, at 80
shields it's expensive to build.  LT Light Bomber Twin is one notch
faster than L3, and has 80 DP, but isn't carrier-capable, and costs
50 shields (and as mentioned, you can't upgrade your L3s to it).  It
also loses the ability to Spot for artillery.
All three of these options are rather expensive for pure recon usage;
if all you want to do is Investigate hostile cities I'd stick with L3,
while the most cost-efficient way to search the oceans (separately from
attacking whatever you might find there) is probably still the old ZD.
The biggest problem is that if FE and FT start showing up, none of these
have much chance of survival.

Overall, the interwar period is not too bad for recon, but it runs out
of steam towards the end.

### Anti-Ground

Whole new categories of bomber appear in the ’Twenties.  Dive bombing
is highly accurate and gives the D2 Twenties Dive Bomber 40 AP (12 BP)
in an inexpensive package (especially for Fascist nations, which pay no
upkeep on any iteration of the dive-bomber line).  It has a 68% chance
to take out cbs, but it's vulnerable at only 16 DP (WW1 scouts can kill
it with ease), and short-ranged at 6M2F.  It's carrier-capable, though,
giving naval aviation a meaningful onshore strike capability, which is
something that the L2 Twenties Light Bomber (the other carrier-borne
option) fails to provide.  L2 has 45 AP and 45 DP but only 8 BP, so while
it's rather more survivable, you'll need a lot of them to deal damage
quickly (typically twice as many L2s as D2s).  Both are rather cheap
at 30 shields.
With its decent defence and no BadDefender flag, the L2 is the first
unit to have a good winrate (63%) when attacked by Troops; that may make
it useful for defending an airbase (possibly combined with a fighter such
as S2 to deter bombers, which would otherwise make short work of the L2),
especially as it still has the FieldRepair flag.
The other new category, medium bombers lie between the
lights and heavies, with a balance of offensive and defensive capability.
The M2 Twenties Medium Bomber has 105 AP, 63 DP and 12 BP (this last is
the same as the D2), but costs 60 shields.  Its range and speed (8M2F)
are quite good — it can go almost as far as a heavy, and can do it
more often, though its ferry range is actually slightly inferior to
the L2's (6M3F).  If you're not sure whether you'll be facing strong
or weak fighter defences, M2 can be a good way to hedge your bets.
It also has r²≤4 vision.  The new flying-boat, P2, also gets 12 BP,
but only 42 AP and 28 DP; land-side bombing is not what it's good at
(though its 6M4F range is state-of-the-art).  Heavy bomber improvements
are a minor increment, with the B2 Twenties Bomber having 216 AP, 72
DP and 20 BP, but costing 90 shields.  In a single turn it's likely to
deal only about the same damage as a pair of D2s, but it is much more
likely to survive to try again.  It also gains a transport capability
(see the section on Airborne Assault below), so can simultaneously bomb
the defenders out of a city and deliver the troops to occupy it.  Lastly,
the trench fighter line continues with the A2 Twenties Attacker, a minor
improvement with 20% more HP (36 AP and 12 DP) and one point more speed
(9M1F) than the TF.  It continues to be a good way to finish off damaged
units without exposing a slow bomber, but with its short range and low
CR (4) it can't do much per turn on the offensive.  On the plus side,
being in control of when it engages means it's easier than a bomber
to level up the veterancy ladder (getting that sweet acespeed and thus
another four CR per turn).  Any of these aircraft (except possibly P2)
can have a place in your terrestrial strike forces; the mix you choose
will depend on many factors like the expected level of fighter opposition,
the value to you of secondary rôles like glider towing, paradropping or
Recon, and whether you need to hitch a ride on a flattop.  In order from
L2→M2→B2→D2, each has more offensive capability, but less defensive
resilience, per shield to build; remember though that they all cost the
same 1 shield per turn of upkeep and 1 unhappiness when deployed outside
your borders, factors which (for Democracies, at least) favour a smaller
number of heavies over a swarm of lights.  And as always, don't forget to
consider which types you'll be happiest upgrading to in a few years' time.

Speaking of those upgrades, the ’Thirties bring one for each of
the abovementioned types.  The L3 Thirties Light Bomber is one of the
first types to benefit from the monoplane transition, gaining speed
and radius of action (10M2F), but the growth in its combat capabilities
(60 AP, 60 DP, still 8 BP) at best matches the higher cost (40 shields)
of the new metal structures, and it's not upgradeable.  Moreover, it loses
the FieldRepair flag, in a knock to its vaunted airfield ground-defence
capabilities; but at least it can still Spot for artillery.
Equally fast
(and with equal cost growth, proportionally, at 80 shields) is the M3
Thirties Medium Bomber, which sees even more modest offensive gains
(120 AP, 12 BP) but a distinctly more healthy survivability boost at 96
DP (giving it 95% WR against intercepting S3, instead of M2's 77% versus
S2).
It also gains AntiSea as an ancillary capability.
The new heavy bomber, B3 Thirties Bomber, is still
slow and lumbering (6M4F, one point faster than the B2) and while it's
much tougher (108 DP), it's still only the same 20 BP despite the 20%
rise in build cost.  The D3 Thirties Dive Bomber also gains a point of
speed/range, and its hitpoints increase by slightly more than its cost,
giving it 50 AP and 20 DP (the BP, of course, stay the same at 12); this
isn't much of a capability gain as these DP still aren't enough to survive
most fighters, but at least it means it's less likely (7½%) than the
D2 (41%) to be shot down when trying to bomb Troops with flak support
(without flak, but still fortified, the figures are 4% resp 29½%).
P3 Thirties Flying Boat is inferior to medium bombers, having 54 AP and
54 DP for its 60 shield cost, and a 9M3F range is not really suited to
raiding land targets; but at least it is starting to stand some chance
of survival against contemporary fighters.  A3 Thirties Attacker gets
a significant advance in ruggedness, reaching 48 AP and 16 DP, as well
as another point of speed, making it almost as deadly at short range
as a heavy bomber, though still without anything like the same power
projection capability.  It also has the FieldRepair flag, so may be able
to usefully forward-base.  There is an upgrade lacuna coming up, though.
Overall the balance is much the same as in the previous decade, but with
the A3 pulling ahead relative to the bombers whose progress is frankly
a little disappointing, unless the geography of the front line happens
to make the extra range highly relevant to you or the survivability
boost of the medium and heavy are important.

In the rearmament period (1935-38), the new light bomber is the LT
Light Bomber Twin; unlike previous lights (which can't upgrade to it)
it's not carrier-capable and can't Spot, but can attack sea targets.
Its 80 AP and 80
DP marginally justify its 50 shield build cost (25% more than the L3,
for 33% more combat strength shackled to the same old 8 BP), but it does
gain another point of speed.  Weirdly, its best use may be to join
a stack of heavier bombers as an escort, soaking up fighter damage,
as a cheap way to buy DP with more than one fuel (and bringing Recon to
the party, too).
The MB Medium
Bomber is handily improved, with 150 AP and 125 DP along with a two-point
jump in speed to 12M2F, while the cost sees only a modest increase to 90
shields.  It continues to be a good balance of attack and defence,
particularly if lifetimes are long enough for upkeep to be a consideration
(though sadly its lineage ends here, with no further upgrades).
Heavy bombers gain little combat power,
with the BW Early Heavy Bomber having only an extra point of speed and
a few extra hitpoints to
show for its 11% cost increase; on the other hand there are some nice
upgrades coming up which you might want to position yourself for.  DB Dive
Bomber gains AntiSea capability, a point of move and significant combat
power, with 72 AP and 36 DP, but at the cost of a 25% price increase.
It's a cheap source of BP and at least a bit more survivable than previous
divers, but (like MB) it lacks an upgrade path.  On the water, the PH
Heavy Flying Boat adds a point of speed, but its gain in AP and DP
(both 75) is offset by the 33% rise in build cost, and the new monoplane
fighters will find it easy to shoot down.  As mentioned above, there's no
new attacker this time; but the A3 is still good enough at what it does to
remain relevant.  Out of all of these, the DB is probably the strongest
performer for making war in the near-term; but if you have an eye on the
future you will likely be investing in heavies (and maybe a few LTs as
escorts), for reasons which will become clear when we get to the next era.

Across the interwar era as a whole, the range of choices is broad
(much like with fighters in the previous era), as designers experiment
with new ideas which at least in the short term seem like good ones.
Dive bombers are consistently effective in the opening stages of a
blitzkrieg campaign, but lack staying power (loss rates will be heavy)
which can lead a protracted war to turn against you if you fail to get
a knockout blow early on.  Medium bombers may seem like the unloved
middle child, but they have the advantage of being the cheapest glider
tugs (see the airborne assault section), which may be reason enough to
include them in your air force.  Heavy bombers start out a strong option,
but gradually fall behind.  In all cases, there is negligible growth in
offensive Pks — in fact no growth at all from the ’Twenties to the
’Thirties — instead, the improvements are mostly in DP and range.
The increasing ranges not only deepen the front line but also mean
that your bombers may be able to be based slightly back from it, rather
than all piled in one vulnerable stack in the city nearest the enemy.
Thanks to dive-bombing, carrier groups can now include a meaningful
onshore strike wing, contributing to power projection on land rather than
merely controlling the sea, and thereby increasing the feasibility of an
amphibious attack to capture an isolated island colony (which then in
turn becomes a valuable airbase for further sea control, or maybe even
island-hopping towards the enemy mainland).  Near the end of the era,
Electronics 1935 brings a significant improvement as beam-bombing adds 20%
to all bombers' attack strengths against cities; among other things, this
reduces the risk to DBs from scrambling fighters.  Looked at another way,
it cancels out the effect of a Flak Battery.  One other thing to consider
is that thanks to airborne assault, the nature of the land battles the
air war will be supporting have changed; rather than being able to catch
armies as they march slowly across the border, you will have to deal with
troops suddenly appearing alongside your cities.  Bombing raids will be
directed mostly against those cities, and destroying enemy fighters on
the ground will be a major part of their objectives.  Front lines will
move more fluidly as cities can fall rapidly and unexpectedly, possibly
even behind the apparent front.

### Anti-Sea

The ’Twenties bring new versions of all your favourite ocean strike
options.  ZD Twenties Blimp (12 AP) is an effective antisubmarine
patroller, with about 3-in-4 odds of sinking a Submersible, and a useful
speed/range increment to 5M4F.  Operating a few of these (perhaps from
tenders) is a cheap and effective way to protect your merchant fleets from
the underwater menace, unless the enemy brings air cover in which case the
defenceless blimps will be quickly eradicated.  An HC Coastal Seaplane
can deal plenty of damage (40 AP, 18 BP), while taking at least _some_
effort to shoot down, though its 10 DP isn't safe against anything more
advanced than 1915 (for instance, the HF, dating back to 1915's Effective
Seaplanes, has nearly a 74% Pk).  It matches the HN's range of 5M3F, while
carrying torpedoes, whose weight previously reduced HL to 5M2F; though of
course the third fuel doesn't do much to stretch radius of action.
P2 Twenties Flying Boat, with its 12 BP, can now more reliably (Pk=84%) kill
submarines (and 6M4F makes it good at finding them), but is rather too
weak to be cost-efficient against lcmboats or tenders; as with previous
flying-boats, it's better at finding them for other planes to strike.
Its 28 DP is nothing to write home about, despite being more than double
that of the PB; per shield it's much more defensible than the HC, yet
contemporary fighters will still mess it up (H2 gets 60% Pk, N2 gets 77%).
But as a long-range ASW patrol it really is unsurpassed at its techlevel.
(Note, however, that its additional vision range doesn't help against
submarines, which can't be seen from a distance, except when they surface.)
Lengthened torpedoes
give the T2 Twenties Torpedo Bomber the ability to do serious damage to
ships with its 48 AP and 18 BP.  It can be confident of killing a merchie
or sub straight off, and if it rolls luckily (14% chance) it can even
one-shot an lcmboat.  Its performance against battleships is marginal, with
six T2s (costing 192 shields) having a 52% Pk on a 200-shield dreadnought,
but a 91% Pd on the initial bombing run.
It has 12 DP, little more than the HC.  With the same cost as
that seaplane, its speed is one notch higher and its upgrade
prospects are better (but of course a flattop costs more than a tender;
also it doesn't have the floatplane's loiter/ferry range).
Beware that, like HL and HC, T2 (and subsequent LongTorp landplanes)
suffers against scrambling fighters, which get double defence against it.
The fully land-based B2 Twenties Bomber has basically the same offensive
capabilities as the old BT; its 216 AP and 20 BP will allow it to kill
anything up to an lcmboat, but tenders and carriers can still only be
heavily damaged by the first attack.  With 72 DP, it will withstand
most contemporary naval fighters (e.g. H2 has only 7% Pk against it).
But at 90 shields it's a lot more expensive than the alternatives; for
example, you could get a P2 _and_ a T2 for that price, providing a total
of 30 BP (though only 90 AP and 40 DP, and the T2's range is shorter;
still, against most naval targets other than battleships, the P2+T2 combo
deals slightly more damage than the B2).
So it's not likely to be worthwhile building B2s purely for naval work;
if they do it at all it's likely to be on secondment from a land-bombing
force that doesn't need them right now.  Instead, you probably want P2s
(or ZDs, but they lack upgrades) for ASW, and T2s for your fleet air
arm or to repel seaborne invasions.  HC is probably only worth it if
you already have tenders.
Meanwhile, the Marine Diesels tech allows for a new generation of subs;
the uu U-Boat is little stronger than the su in itself (just one
additional hitpoint, giving 12½% extra AP/DP for 10% more build cost),
but its speed when surfaced is higher (5 MP), helping it to get into
position for an ambush.  It also has significantly more underwater
endurance than the old Submersible, improving its odds of hiding from the
new long-vision ASW aircraft.

There are no ’Thirties upgrades of blimps or floatplanes, but there
is the P3 Thirties Flying Boat.  With 9M3F its ferry range is increased
but its radius and loiter time reduced.  The 20% rise in build cost
earns a decent HP increase, taking AP to 54, but DP jumps to (also) 54,
making interception by the fighters of the day almost a fair fight.
Of course the BP remains stuck at 12, but that's enough for ASW, with a
65% Pk against U-boats.
T3 Thirties Torpedo Bomber nearly doubles its AP, to 84, in return
for its 12½% price increase; against hard targets like carriers (or,
especially, scrambling fighters) this can make a noticeable difference
(e.g. 33% Pk-18% Pd against H3, whereas T2 got 35%-65% vs H2),
and its Pk against lcmboats is up at 30%,
but it's still vulnerable with a mere 14 DP.
Significantly, for the first time the T3 has the economic edge against
dreadnoughts, taking an average of just under 140 shields' worth of
torpedo-bomber to sink the 200-shield battlewagon, and with only a 54%
Pd to boot.  A CV full of T3s will get a 94% Pk on the dread, with an
average of just 73 shields being shot down in the attack, but if there's
any enemy fighter cover then the rest of the torpers won't be coming home
either.  (And of course the CV itself ain't free.)
A new
option is the M3 Thirties Medium Bomber, which while really meant for
supporting the fight on land, can now deploy its 12 BP against shipping
as well.  Against subs (96% Pk) and merchies it's effective (although at
10M2F it can't search too widely for them or loiter in the area) and it
doesn't need to have much fear of fighters (especially naval fighters)
thanks to its 96 DP.  However, at 80 shields it's not cheap (that's 33%
more than the P3), so only really makes sense in this rôle if there are
enough fighters around to make life too dangerous for a flying-boat.
B3 Thirties Bomber is just a hitpoint and range upgrade; that extra
range (6M4F) could be useful for ocean patrol, but the price is once
again a turn-off.  It's getting a bit expensive for use against
dreadnoughts, but unlike previous heavies can guarantee it won't die in
the attack, so in the absence of enemy fighters a force of B3s can smash
sortieing warships when not busy bombing ground targets.
On balance I think the optima are M3 for hunting
subs and merchies off your coast, P3 for the same out in the open ocean
(especially with support from tenders or buoys), and T3 to discourage
enemy lcmboats, carriers or battleships.

Come 1935, the option space broadens even further.  The larger,
multiengined HB Floatplane Bomber has an offensive capability similar
to the T3, and while 15 DP is not impressive its range (7M3F) is much
better than previous floatplanes.  If unmolested by fighters, it can
sink a lot of merchies and subs, but if it goes after carriers it is
likely to be a suicide mission (even SF gets 91% Pk against it; the
contemporary NM gets 99.96%).  Still, it's cheap at 40 shields, meaning
a pair of these, with 37½% Pk on a CVL, costs less than the carrier.
(But scrambling fighters will hurt it badly, as usual for torpers.)
It's the first floatplane to pose
an economically viable counter to battleships; but it's also the _last_
floatplane bomber, with no upgrade path.
The other seaplane
option is the PH Heavy Flying Boat; its extra point of range and large
growth in hitpoints are set against its 33% growth in cost, and do
nothing to improve its Pks (against the new CAM it only gets 61%).
Its 75 DP enable it to likely survive against an H3 (5.5% Pd),
though an NM will kill it one time in three; really it's too
expensive to risk in contested skies.  It works best in situations
like the historical Battle of the Atlantic, where there's a very large
ocean to scour for subs but the enemy has no carriers or islands to
base fighters on; if that's where you find yourself, then PH is great,
especially since it gets a 2x attack bonus against subs (giving it 98% Pk
on su and 92% on uu).
TM Torpedo Monoplane has a solid 120 AP to go with its 18 BP, giving it
better Pks than T3 (it can reliably one-shot a CVE or CAM, and gets 44%
on an lcmboat) with less risk of death against hard targets.
The cost rises only slightly, to 40 shields, while defence is 7% up at
15 DP (but that's still not enough to fight off anything postwar, with
the possible exception of the H2 at 91% Pk), and the speed/range extends
to 7M2F.  Against dreadnoughts it's stronger than ever, deploying an
average of 121 shields per soaking admiral but with an 86% chance to come
home in one piece, distinctly better than the T3's 46%.
But torpers are no longer the only carrier-borne AntiSea units,
as DB Dive Bomber also has that capability.  With 72 AP but only 12 BP,
it deals less damage on average than TM but it's more predictable in the
damage it does do, and it reaches slightly
further with 8M2F.  It's a little more expensive at 45 shields, but its
76% Pk against CVE (93% vs CAM,
basically 100% vs merchie) is largely adequate.  While its 36 DP is poor
by landplane standards, compared to the torpers it looks rather robust.
However, it's slightly less effective than TM against scrambling fighters
(although there's really very little to choose between them).
190 shields' worth of DBs sinks a dreadnought, with 79% Pd; this is just
economically viable (the dread cost 200), but of course the torpers do
better in that matchup.
The real reason to use it, though, is its versatility; a carrier air
group with DBs in is prepared to strike at both land and sea targets,
whereas a wing of TMs is capable only of the latter (and a mixture of
TMs and L3s is less efficient, because often part of the force will be
standing idle with nothing to do).  Land-based bombers can also play their
part, including (for the first time) a light, the LT Light Bomber Twin
(which unlike previous lights is not carrier-capable).  It has an 80%
Pk against merchies but only 39% against subs (it has to win all eight
combat rounds, though it *does* get a 2x attack bonus against them; and
it doesn't have the BP to one-shot a U-Boat but it'll do enough damage to
mission-kill them)
and 26% vs CAM; however, it's fast (11M2F) and resilient
(80 DP) for its 50 shield build cost.  Its long vision range (r²≤5)
also helps it to find targets (unless they're underwater, in which
case like everyone else it needs to be adjacent).  It's not the most
efficient Anti-Sea unit, but plinking merchies makes a useful side gig
when it's not busy on land; and if (say) there's a carrier nearby that
your torpers just didn't _quite_ manage to sink this turn, maybe you can
re-task an LT to go and finish it off before it slips away to repair.
The MB Medium Bomber is rather more capable, reliably sinking merchies
(93% of CAMs will succumb) and subs (98% Pk) as well as having rather
good odds (76%) against a CVE.  A pair of them are enough for an lcmboat,
or have a decent chance (54% Pk) against a tender.  What's more, with 125
DP it's difficult for a naval fighter to bring it down (e.g. NM has 3%
Pk), although FE will still do it 22% of the time and of course a pair of
fighters working together can still overwhelm it.  Its reach is 12M2F,
one notch further than the LT.  The price tag of 90 shields is hefty
(more than a PH; the same as _two_ DBs) but, as usual with mediums,
it's a sound
compromise between effectiveness on attack and resilience on defence.
BW Early Heavy Bomber extends its speed/range to 7M4F, but is otherwise
little better than the B3 (just a few extra hitpoints);
I wouldn't risk them on commerce warfare, but
if an enemy invasion fleet is approaching your homeland then your BWs
can play a rôle.  So can something rather different, the KA Kamikaze.
Buildable only by a Fascist nation with the Yasukuni Shrine smallwonder,
KAs are highly deadly with 24 BP and 120 AP, but they act as missile
units and cost not only 20 shields but also _one population_ to build.
But when desperate times call for desperate measures, a few kamikazes
into the enemy's carriers and dreadnoughts can save the day.  (It takes
an average of 2.5 KAs to kill either a CV or a dread; in shield terms
that's a bargain, but the economic hit of the lost pop may be severe.)
Frankly the biggest problem
for all the bombers in 1935 is that FE and NM are just a lot stronger
than earlier fighters, so even LT and MB have to fight hard to survive,
not having improved by nearly as much.

Overall, none of the AntiSea lines are really satisfactory throughout
the entire interwar period.  Flying-boats are the best at ASW, but if the
skies are contested they're too expensive and vulnerable.  Torpers (and
DB) can be devastatingly effective on attack but their survivability
is almost nonexistent.  Conventional landplane bombers can hunt subs
even in the face of enemy fighter cover, but tie up a lot of shields
that could otherwise be employed elsewhere.  And, as already mentioned,
everything gets left behind by the jump in fighter performance in 1935
(a situation that will only get worse in 1939).

### Anti-Air

After the confusion of WWI, fighters in the ’Twenties are refreshingly
simple.  There is just one land-based fighter, the S2 Twenties Scout,
with 20% more hitpoints (48 AP, 48 DP) and 25% more move (12) than the SB.
However, for the first time in the single-seater line, the build cost
rises by 25%, to 25 shields.  A single S2 will bring down a D2 (98%
Pk) or maybe L2 (51% Pk), but M2 is trickier (23% Pk) as is B2
(21% Pk).  In a scramble, it will likely lose to a B2 (92% Pd),
but against an M2 both will survive (2% Pd) and it may well defeat
a D2 (46% Pk-2% Pd).  S2 also gets the FieldRepair flag, which main-line
scouts have previously lacked.
Fighters at sea are playing catch-up, with the H2
Twenties Floatplane getting its second FP to attain 32 AP and 32 DP —
20% weaker than an SB, but 60% stronger than the old HW — and 9 move,
at a cost of 32 shields.  This is enough to intercept naval bombers (98% Pk
vs HC, 96½% vs T2, 60% vs P2),
but you'll likely need at least two fighters to
bring down, say, a B2 or M2; and in a scramble it will likely lose to a
B2 (99% Pd) and has only a small edge over a P2 (16%-44%).
The N2 Twenties Naval Fighter is both cheaper (25 shields)
and more capable (40 AP, 40 DP; same Pks as an SB), but of course its
carrier is more expensive.  Scrambling against a T2 (65% Pk-14½% Pd) or
P2 (16% Pk-8% Pd) it does well,
though a B2 will obliterate it (98% Pd).
It also has the FieldRepair flag, should it hop off its carrier and onto
a terrestrial airfield; with its 10 HP that sees very favourable rounding,
_quadrupling_ its repair rate.
Which of these aircraft you use will be determined largely
by what platforms you choose for other reasons; they're all adequate
for their respective rôles.

The S3 Thirties Scout is a modest upgrade, gaining only additional speed
(12 move).  Against the new generation of bombers, it can struggle to
do the business (3% Pk vs B3, 5% vs M3, 31% vs L3); small wonder that
Baldwin believed "the bomber will always get through".  (On the other
hand, those bombers have risen significantly in price.)  It's still able
to hack down dive-bombers with ease (96% Pk vs D3).
It still has FieldRepair.
Two-seaters are
also back, with the F3 Thirties Fighter; it's better at interception
(66 AP) but weaker in a scramble (44 DP) and has only 10 move, largely
failing to justify its 36 shield build cost.
Still, if you have any old FBs lying around it's worth upgrading them; it
keeps the FieldRepair flag.
And of course it's upkeep-efficient; after 5 turns of shield upkeep it's
a slightly cheaper source of AP than the S3.
The new seaplane, H3 Thirties Floatplane, is a solid upgrade that closes
the gap with other fighters, having the same 40 AP/40 DP as the SB or
N2, and a speed of 11.  This keeps pace with torpers on intercept (98% Pk
vs T3), but not
with level bombers (1½% vs B3), nor with flying-boats (26% Pk vs P3);
it still struggles in a scramble (18% Pk-33% Pd vs T3, 29% Pd vs M3,
1½%-8% vs P3), and it has a while to wait for its next upgrade.  On the
flattops we have the N3 Thirties Naval Fighter, a modest improvement (one
more hitpoint, two more move, taking both to 11) that brings it closer
to its land-based brethren.  Again, it falls behind many of its targets
(3% Pk vs M3, 33% vs P3), but the most important threat to carriers is
probably T3 which it deals with handily (99% Pk).  Scramble survivability
is also up (92% Pd vs B3, 10% vs M3, 13% vs T3), but it's not likely
to shoot the bomber down (except in the case of T3, with 18% Pk).  It
keeps FieldRepair.
One change in all these lines, which might be significant,
is that they now have CR 5 (instead of 3).  On the plus side, that means
they're less likely to have insufficient fuel to down a target if they
can reach it at all; on the minus, re-engaging for one more battle when
low on HP is that much more risky.

The monoplane transition reaches fighters in 1935, starting a period of
rapid increase in strength.  Chief among these is the FE Early Monoplane
Fighter, which at 96 AP / 96 DP is twice as powerful as an S3, yet only
44% more expensive.  It also has 16 move.  The change to 3 FP does mean
more cases where rounding works against you (e.g. to down a 16 HP bomber
you need six hits, of which ⅔ of the last is wasted), but that's a
small detail that doesn't stop your Pks from leaping up — 31% against
BW, 22% vs MB, 64% vs LT.  Even in a scramble, your Pd against BW is only
53%, while you have slight Pks against MB (<0.1%) and LT (0.3%).  And its
FieldRepair sees favourable rounding, regaining *six* hitpoints per turn
parked on an airfield.
There is also a new two-seater, the FT
Turret Fighter.  It's pricey at 48 shields, but it has 132 AP / 99 DP
and 12 move, making it a _slightly_ more cost-effective interceptor than
the FE, though not so great in a scramble.  Also, it loses FieldRepair
and has no upgrade path.
A new concept is the EF Early Heavy Fighter, which has
the distinction of being able to loiter (12M2F), allowing it to escort
bombers over the target.  With 99 AP for 50 shields, it's inferior as
an interceptor (it would take over 400 turns of shield upkeep for it to
overtake FE), but its 99 DP is better than the similarly-priced LT
which can also perform the escort rôle.
However, the LT has a bombing capability, as well as Recon, so you might
prefer to use that; the main situations in
which the EF makes sense are (a) you really need that extra point of
escort range, or (b) you aren't sure how many interceptors or escorts
you need and EF gives you something that can be both.  (Future upgrades
aren't a concern, because the upgrades FH and LM are the same airframe
and can be converted to one another.)  At sea, there is no new floatplane,
but the carriers get the NM Monoplane Naval Fighter.  The speed rises to
15, but the 64 AP / 64 DP is only about in line with the price increase
(36 shields, same as the FE).  That does give some solid Pks (7% vs BW,
3% vs MB, 30% vs LT, 31% vs PH, 90% vs DB, >99% vs TM) in the intercept,
and adequate scramble (53% Pd vs BW, draw vs MB or LT, 5% Pk vs DB,
2% Pk-2% Pd vs TM) except against KA (84% Pd).  Like the FE, it has
FieldRepair with favourable rounding (though again this makes less
difference for a plane that will spend most of its time on a boat).
All of these fighters also have r²≤4 vision.

So what generalisations can we make about this era?  The main one is that
two-seat scouts are underwhelming; another is that the early ’Thirties
are a bad time for air defence but the late ’Thirties are much better;
yet another is that floatplanes can't keep up.  The likely conclusion
is to build S2→S3→FE on land, and flattops with NMs if you want a
fleet air arm.

### Airborne Assault

In the ’Twenties it becomes possible to move Assault-class units around
by air.  (Technically the ZB could do that back in 1914, but it was slow
and vulnerable and could only carry a single unit.)
Initially this just covers Settlers, Seabees and Marines, but
through the Glider Assault and Parachute Dropping techs you gain access to
the Assault Troops and Paratroops units, with decent Attack values
(40 AP each), as well as the Assault Gun (an airliftable artillery
unit with a bombardment attack).  Marines are as cheap a source of AP as
Assault Troops, but the latter have much better defence, important
for holding onto your gains, and are more upkeep-efficient.
The most straightforward means of
transporting these units is in the C2 Twenties Transport, which for 36
shields can carry up to two units at a time over its 6M2F range.  However,
it's basically defenceless (while it can evade a little, contemporary
fighters will likely down it in two or three combats).
Two other units, B2 Twenties Bomber and P2
Twenties Flying Boat, each have the ability to carry one unit; B2 is much
more expensive, but does have the better defence (72 DP for 90 shields,
versus the P2's 28 DP for 50 shields).  But while Paratroops can drop
from these transports anywhere, the other assault units need somewhere
to unload; so while transports can quickly move them around friendly
cities and airbases (or buoys in the case of P2), delivering them to the
outskirts of an enemy city for a lightning attack requires something else.
At this point in time, that something else is the GG Glider, a 12-shield
disposable vehicle that can carry two units.  Either the B2 or the M2
Twenties Medium Bomber can tow it into position; after dropping the
glider, they can still bomb the city as well.  The M2 generally makes a
better tug, thanks to its higher speed and proportionally stronger defence
(63 DP for 60 shields).  So the optimal glider-enabled attack on a city
probably consists of a couple of gliders each with an Assault Gun and an
Assault Troops, towed by M2s; drop the gliders, shell with the Guns, use
the M2s and as many more bombers as you need to finish off the defenders,
then capture the city with the Assault Troops.  Move in some fighters
to help defend the city while it builds some Troops.  If the enemy is
unlikely to get a counterattack together in time, then you can replace
the Assault Troops and the second glider with a Paratroops carried in a
B2 or C2; it will save you the cost of a glider, but Paratroops are very
weak defenders, and they cost 8 shields more than Assault Troops in
the first place, so the total amount saved is rather slender (although
if you use them again later, you come out further ahead as compared to
having to build another glider for the next assault).
One difference is that the C2's speed/range is shorter than the
M2's; the B2's radius of action is longer still (and the P2 even beats
that), but it takes twice as long to get there.  An interesting note is
that a P2 carrying Paratroops can operate from a Seaplane Tender, thus
allowing you to launch an assault arbitrarily far from friendly bases,
more effectively than with the slow and vulnerable lcmboat.  There are,
by comparison, no carrier-capable aircraft that can either drop paras
or tow gliders, so flattops can't deliver troops ashore (a situation
that will only change with the arrival of helicopters in the late ’40s).

The ’Thirties bring incremental improvements, mainly in speed and
range.  C3 Thirties Transport has two extra points of move (8M2F),
and can take slightly more hits,
but is otherwise unchanged and costs 11% more.  M3 is now faster, at
a pacey 10M2F, allowing gliders to reach further; its DP grows to 96,
outpacing the rising cost (80 shields).  B3 sees similar
gains (6M4F, 108 DP for 108 shields).  P3's speed jumps but the radius of
action isn't up so far as it goes to 9M3F, although if it is operating
from a moving tender then radius is not necessarily the right metric
(e.g. in the three turns it takes to go out 18 tiles and back 9, the
tender could cover the remaining 9 and be in position to refuel it);
also, if you're only dropping paras and not bombing then you don't have
to end your turn to do so and can thus use all your range.
Its defence improves considerably, though is still not great, being
proportionally slightly more vulnerable than a heavy.
On the whole it makes amphibious airborne assault reasonably practical,
if you have a strong carrier-borne force to do the bombing.  Meanwhile,
mediums are still the best glider tug.

In 1935 still not much changes.  CM Monoplane Transport is noticeably
faster at 10M2F, but costs 25% more.  Its improved evasion will keep it
alive slightly longer against old scouts but an FE will down it in
rather short order.  MB sees a similar speed gain (to 12M2F), as
well as a 30% defence improvement, and only sees its price rise 12½%.
BW's extra point of speed could help bring a target into range, but
otherwise it's uninspiring.  PH adds one move (10M3F), and gets 40% more
defence (75 DP), but also costs 33% more at 80 shields; while the idea of
paratroopers jumping from Sunderlands to capture a city is delightfully
batty, it's not really economical.

Basically, throughout the period, the mainline options are mediums towing
gliders and C-transports dropping paras.  Other variations are _possible_,
but only advantageous in unusual circumstances.  Transports get noticeably
more expensive to build but extend their reach significantly.
The important part is that wars can now be won from the air, rather than
air power merely serving to support battles on land and sea.

### Naval Aviation

Carrier-borne aircraft gain real capability in the interwar period,
mirroring the way historically aircraft carriers gradually replaced
dreadnoughts as the capital ships of Great Power navies.  The six-unit
complement of a CV can include meaningful shore strike (dive bombers),
anti-ship (torpedo bombers) and air defence (naval fighters) capability,
and the ship itself has a chunky 120 DP.  Unfortunately, the same
improvements that make _your_ torpers more useful also mean _enemy_
torpers can threaten your carrier; the price in shields of the expected
number of torpers to sink a CV (assuming each makes only a single attack)
goes from 178 (5.56 T2s) to 160 (4.44 T3s) to 156 (3.89 TMs),
all slightly more than the 150 shields the CV cost to build, but with
zero Pd in the bombing-run, which makes them pretty good if something
else deals with the fighters so they can get home.
(Against CVL they do even better; 85 (2.67 T2s) to 80 (2.22 T3s or 2 TMs)
as compared to the 90 shields the CVL cost.)
On the
other hand, the range of these aircraft is enough that you may be able
to launch strikes without your carrier being located, especially since
the CV's 5 move (6 with Shipping Forecast)
allows the launch and recovery to be widely separated;
and the defending fighters are highly effective against torpers (getting
double defence in that situation), though level bombers and dive bombers
can attrit them to open the way for torpers to sink the carrier.
Kamikazes are very powerful; three of them will get 94% Pk on a CV, at a
cost of 60 shields — and three pop!  While they might stop the invasion
now, their builder will be weakened for the future.
The CVE that's developed in 1935, carrying a single air unit at a cost
of just 30 shields, is a cheap but slow and vulnerable platform; it can
provide meagre air cover to a merchant convoy, but trying to use several
as a basis for an attack force will founder on the upkeep (the same 1
shield 1 unhappy as a full-sized CV).

Seaplanes, on the other hand, are not as viable as they once were.
While flying-boats can search further than ever, and transport a small
quantity of troops (or cbs), they become expensive and are vulnerable to
the growing strength (and range) of land-based fighters.  Floatplanes,
meanwhile, are flimsy and cannot match the performance of wheeled
equivalents, though the fighters may still be adequate against torpers.

Battleships probably want to carry a ZD for ASW patrol, or better still
operate in conjunction with a CV and keep the flammable petrol off their
own decks; in most cases the battlewagons' job is now to protect the
carriers from enemy battleships that get too close or from bombers that
get through the CAP, rather than to sortie on their own.  While they
could carry an HC to spot for the guns, again a carrier-based L2 or L3 is
noticeably superior and avoids the fire risk.  Come 1935 you _might_ want
to carry an HB for battleship engagements; if it finds the enemy dread it
can deal a few damage, maybe slowing them down enough to let your dread
catch them, at which point the HB can provide spotting too and turn the
odds in your favour (which normally they aren't because battleships are
better at defence than attack).  But a setup like this, operating without
carrier support, is just asking for someone to show up with a CVL full of
TMs and send you to the bottom.  (But at least the HB is useful for ASW.)

If you're using subs, then at some point in this era you'll want to
research Autogyro, increasing the vision range of surfaced subs and thus
enabling them to more easily spot targets and get in position before
submerging to spring an ambush.  However, air cover can spot _you_
more easily when surfaced.

Catapult Armed Merchantmen, available from 1935, have the chance to
occasionally survive, or at least inflict a bit of extra damage on their
assailants, but in most cases it's not a huge difference — even 18
DP is just too weak to survive much of anything.  And of course they're
just as vulnerable to subs as regular merchies.  Still, they may be worth
the extra 6 shields if the enemy is bombing them a lot (especially if
he's using LTs, old HCs, or even older HNs — against HN a CAMboat's Pd
is just 5% in the first round, and if the HN attacks again then CAM gets
a 40% WR).

### Civil Aviation

In the ’Twenties, heavier-than-air craft become adequate for passenger
travel and freight transport, with the LL Airliner providing a new
way to create trade routes.  It goes further and faster than the LZ,
at 5M3F, and is also slightly cheaper (45 shields); on the other hand,
it can only be built in a city with a Commercial Airstrip.  So you might
initially be reluctant to use it, when most of the time you have plenty
of gold and thus don't need that building's main effect.  This is fine,
until 1935 when the development of the LD Monoplane Airliner
obsoletes the Mooring Mast.  This represents the public turning away
from zeppelin travel after the series of airship disasters culminating
in the loss of the Hindenburg.  After this point, you will need to build
airports if you want to keep adding to your trade network.
The LD itself has slightly lengthened range (9M2F), which may bring one
or two extra cities within reach.  However, it is a smidgen more
expensive, at 50 shields.

### Flight Refuelling

New in the ’Thirties is K3 Tanker Biplane, which can extend another
aircraft's range by carrying it for the first 5 tiles of its journey,
then picking it back up on the way home again.  Besides allowing your
bombers to strike at distant targets, it can also speed up a heavy's
travel to the target, e.g. a K3+B3 stack can cover 11 tiles in one turn,
allowing it to make an attack slightly further away than M3 can manage
without the slow B3's usual risk of being intercepted before it can bomb.
But the stack costs about as much as a pair of M3s, which together deal
about as much damage as the B3 while being much more resilient against
fighter attack (and the K3 is especially vulnerable, having 0FP), so the
benefit is unclear.
More significant is the K3's ability to stretch civil aviation, letting
LL reach cities 20 tiles away (or 25 if you expend the tanker) and thus
expand global trade; it may also help you get Ambassadors into civs you
couldn't otherwise reach.

### Buildings

The ’Twenties bring the biggest collection of buildings and wonders
in the game.  General Aviation is a key technology; besides its own
buildings it also doubles the effect of Flying Club, making it easier to
keep your citizens happy.  On the other hand, it does obsolete several
early buildings.  Air Tours boosts lux, also useful if you're trying
to grow your cities bigger.  FAA Branch reduces corruption — which
for Democracies doesn't vary with distance, so you'll want this in big
trading cities rather than cities far from the capital — and adds
one more content citizen.  Crop Dusting enables the extra food output
from farmland, which might allow you to grow a city bigger, or might
just allow you to have more of its citizens on shield-producing tiles
like coal mines.  Finally it brings the de Havilland smallwonder, which
boosts trade output in the city that has it.  Mass Production brings
three more buildings; Tramways are likely to be needed in your bigger
cities to deal with pollution, despite their two gold per turn upkeep.
Marshalling Yard brings extra trade in a city with lots of railways around
it (it should synergise particularly well with de Havilland), but costs
two upkeep so is only worth it in big cities with lots of land tiles
to work.  Engine Factory allows you to churn out production much faster,
but three upkeep and a 100-shield build cost make it rarely worth it.
Display Team (Twenties Fighters) is a smallwonder that gives you a happy
citizen in _every_ city; for Democracies this is likely to be a must-have
just to reduce the amount of lux you need (especially if you're trying
to celebrate).  RAF College Cranwell (Twenties Fighters) is the staff
college for landplanes, which (unless carriers are a big deal) makes it
typically the most important of the three — having your air force get
quickly to ace/elite can give you a distinct edge.  Air Races (Twenties
Seaplanes) gets you another two content citizens, albeit at upkeep 2.
Wind Tunnel (Aerodynamics Research) boosts the city's science output;
finally, Commercial Airstrip (Twenties Airlift) does the same for tax,
and also allows building Airliners in the city (and unlocks the second
trade route, if you didn't already build a Mooring Mast).  Every one
of these buildings is potentially useful if you're trying to create a
burgeoning metropolis with all the economic force-multipliers you can
squeeze in; perhaps less useful if you're still able to grow out (into
empty land) rather than up.

S.B.A.C. Airshow (Engines 1930) is a valuable smallwonder, as it lets
you upgrade your units more cheaply; with the accelerating technological
change through WWII this will come in very handy indeed.  Schneider Trophy
(Thirties Seaplanes), a greatwonder which can only be built in a city
with Air Races, grants a tech; that's a rather small gain for the cost
of building it, but I guess you get bragging rights?  National Airline
(Thirties Airlift) requires a Commercial Airstrip in the city, and doubles
the effect of all your airstrips, potentially providing an appreciable
boost to tax revenue if you've built a lot of them (which you may have
done just for the airliners).  It's only a smallwonder, so everyone
can have one.  Broadcasting Corporation (Radio) is of limited use —
diplomatic contact with everyone isn't a huge deal, and AIs are so sessile
that it makes little difference whether they choose war or peace with you.
The other smallwonder in Radio, though, is Shipping Forecast, which grants
a valuable speed boost to your sea units; this can for instance make your
merchies more efficient (fewer turns of upkeep paid en route) or, if you
have it and an enemy doesn't, improve the effectiveness of your subs at
hunting down their ships.

Aircraft Factory (Military-Industrial Complex) stacks another production
boost on top of Engine Factory, but it's even more expensive (in both
shields and upkeep) so even fewer cities are likely to justify it.  (And
those which do will probably run into serious pollution problems.)
R.D.F. brings both a building, Radar Station, and a smallwonder,
Chain Home.  Both give four tiles of vision, Radar Station to the city
and Chain Home to all cities on the continent.  There's also the Radar
Van unit, which after driving out to the desired location can convert to
a Radar Tower with three tiles of vision.  Radar stations can be
useful on the extremities of your empire to spot slower-moving forces
like lcmboats or early heavy bombers before they can attack, but most
airborne threats move too quickly for radar to make a huge difference.
Fundamentally, it's quite situational.  Electrification (Electronics
1935) helps to limit pollution from high-production cities (such as
those with factories); it's expensive, but so is losing output because
your hinterland is all covered in muck.
If your cities grow very large, they may need Travel Agent (Airlift 1935),
to boost luxury output and keep your citizens happy.
Concrete Runway (Large Monoplanes) doesn't do much immediately, just
increasing repair rates in the absence of Repair Sheds from ⅓ to ½ per
turn, but come 1939 the four-engined heavy bombers will need it to repair
at all after combat; you might want to start laying some ahead of time.

### Other Tech

Radio, in the 20s, allows light bombers to Spot without ending their turn;
thus a target that was previously on the limit of an LE's range can be
Spotted by an L3 that runs straight back home again out of harm's way.
(But of course by this point Artillery in the field are at severe risk
from aerial attack, so the usefulness of this capability is unclear.)

## Second World War era

War once again spurs development, particularly through more powerful
engines.  Great bomber fleets mount long and gruelling campaigns to
decide the fates of nations.  The 'superprop' techs of 1944-45 are a
dead end, but have more to offer in the short term than the earliest
postwar jets will, and avoid the need to build new runways for the
latter.

### Reconnaissance

There is not much new recon in 1939.  Blimps have long since ceased to
develop, and now floatplanes and flying-boats are running out of steam
as well.  Even light bombers have a gap; so the only fresh arrival is
the UE Early Helicopter.  With a short range (6M2F) and the same zero
defence as the ZD, really its only
advantages are being able to use more types of carriers, and (crucially)
the extended (r²≤5) detection range for subs.

1942 brings something rather better: the paired FH Heavy Fighter and
LM Light-Medium Bomber, which can be converted to each other.  LM has a
slightly longer vision range (r²≤5); while its speed/range of 13M2F
is a distinct improvement over the LT, FH beats it by one.  Both are
fairly strong on defence, but FH is the stronger, with 120 DP to LM's 100.
So mostly when doing pure recon (rather than mixing it with bombing)
you'll want to operate these as FH.  Either way, they cost 20% more than
the old LT to build, but are definitely worth the increase.

Circa 1943 the ASV-equipped PL Ocean Patrol is one notch faster than the
old PH, and has r²≤5 vision, but is a landplane (so can't use buoys and
tenders), and its defence is a little weaker at 60 DP.  Like PH it doesn't
have capital-R Recon; but its 33-tile ferry range makes it the best
sub-hunter yet; between these and LM, U-boats will want to stay submerged
as much as possible to reduce their risk of being found.

And that's it for the era.  Once you've got FHs, they'll probably meet
your recon needs quite handily, but contemporary fighters will cause
trouble if they catch them — e.g. 50-50 odds in a duel with an FM,
⅓ chance to survive an FC or FF.

### Anti-Ground

Most of the lighter bombers stop developing once WW2 kicks off;
the only new bomber in 1939 is the B4 Four-engine Bomber.  This is a
significant upgrade, with 480 AP and 180 DP, as well as increased speed
(though a slight reduction in radius of action) at 10M3F.  The cost
rise is comparatively modest, but this is from a rather high baseline
and thus reaches 150 shields.
Moreover, it's the first bomber with the 'heavy' flag, which means it
can only be repaired in a city with the Concrete Runway improvement;
thus you will likely need to spend the 45 shields (and 1 gold/turn
upkeep) to build these in the cities housing your bomber groups.
Still stuck at 20 BP, B4 is not likely to one-shot
even an unfortified Troops (1.7% Pk) but will do significant damage.
Against either fortified or unfortified Troops, B4 can expect to get
around 0.7 more hits than BW would have.  A pair of B4s has 81% Pk
against fortified Troops, as opposed to 59% for BWs.  Attackers also
improve, with the AK Attacker jumping to 64 AP (a 33% gain) for only
a 20% increase in cost (36 shields).  Speed stays the same at 10M1F,
but it now has CR 6 so can fight for longer at the limits of its range.
Against Troops (and with enough fuel) it can do nearly as much damage
as a B4, but if an FM scrambles against it it'll probably only be able
to knock a few HP off, whereas B4 has a 36% Pk (and near-zero Pd)
assuming flak in the city.  (Attackers are best against targets with high
HP and low FP — where bombers' CR limits hold them back — whereas
against targets with higher FP the attacker is more likely to run out
of HP than the bomber is to run out of CR.)  It loses the FieldRepair
flag, though, which might be a shame if you're trying to use forward
basing to make up for the short range.
The fleet air arm gets an
attacker of its own, in the form of the NS Naval Strike Fighter, which
combines reasonable ground-attack strength (48 AP, same as the A3) with
a mediocre air-to-air capability, at the same 36-shield price as an AK.
It's slightly longer-legged at 12 move, but has a slightly lower 5 CR since
it's categorised as a fighter.  It's not likely to be a carrier wing's
major damage dealer, but it should be good at cleaning up targets after
the bombers have weakened them, and its versatility might be attractive.
Do be aware, though, that its upgrade path, into pure naval attackers,
loses the ability to engage air targets.

1942 brings a couple of new bombers.  The LM Light-Medium Bomber is
broadly speaking a cheaper MB, with the same 12 BP and decent combat stats
of 100 AP and 120 DP, at ⅔ the price.  It also has Recon and r²≤5 vision,
and an extra point of move (13M2F).  Its CR 12 fits the 'medium' standard,
but it upgrades from the LT.  It's also
convertible to the FH, increasing its versatility (and explaining why
it's unlocked by the 'Fighters 1942' tech).  On the whole it's good
at what it does, but it'll still likely play only a supporting rôle.
The main work of wearing down the forces defending enemy cities will be
done by the BH Heavy Bomber.  It has an extra FirePower, taking it to 576
AP and 30 BP, along with 216 DP, and all at the same 150-shield price
as its predecessor.  (It does, however, lose the ability to carry troops,
though it can still tow a glider.)  Its 13M2F speed means it can finally
reach distant targets without having to spend multiple turns en route as
the older BWs did.  Against an unfortified Troops it has an impressive 56%
Pk; in the more likely case (beam-bombing against a fortified Troops with
proxy-fused flak) it's still about 20%.  The slightly lower HP means it's
at marginally greater risk than a B4 from a scrambling FM, FC or FF;
in either case it has much higher Pk than the B4, with less chance of a
draw.  Interception is more dangerous; FM gets 29% Pk (only slightly less
than vs B4) and FC is unchanged at 50%.
BH can also be converted to the BD Modified Heavy Bomber, which while
itself unable to attack (and more vulnerable at 180 DP), can carry the XT
Penetrator Bomb.  XT's 240 AP and 20 BP aren't spectacular (an unconverted
BH would do more damage, without needing to throw away a 40-shield bomb),
but its ability to perform a Precision Strike, reliably destroying a
selected building in the target city, can prove very useful.
(For instance, it could take out a Flak Battery or even SAM Battery,
weakening the defences against following bombers; or destroy a Concrete
Runway or Air Base that's maintaining the enemy's units.  Or something
really expensive like an Aircraft Factory that cost over three times as
many shields to build.)  Moreover, the BD's turn isn't ended by dropping
the bomb, so it can run some distance away, perhaps evading the fighters —
although the BD's move, at 10M2F, is rather less than the plain BH.
In a way the BH is what the heavy-bomber line has
been building up to since the start: high destructive potential that
renders Troops inadequate as a defence.  LM is distinctly more cost-
effective on defence, but can't match the offensive power of BH; its main
value may be to clean up damaged units for whom it's not worth committing
an expensive BH (and where attackers haven't got the legs).
As always, the best choice depends on what you're facing.

If you go down the superprop line, 1944 has another heavy bomber to offer,
in the BS Superprop Bomber.  With 900 AP and 360 DP it easily justifies
its 20% higher build cost, noticeably increasing its Pks and bolstering
its survivability against interceptors.  It also reaches further than ever
with 14M2F, and gains r²≤5 vision.  It does however lose the ability
to tow gliders — it's a pure bomber, with no ancillary rôles left.
The BS dominates the LM on all axes (it's tied on DP/bc but upkeep puts it
in front immediately), so apart from Recon there's no reason to keep
building LMs (although FH are still well ahead on defence).
Again, there's a Modified variant, the BU, with slightly worse stats (300
DP, 12M2F) but able to carry specialist bombs, which by now may also
include the X1 Atomic Bomb.  You can only have one Atomic Bomb at once,
but its awesome destructive power allows it to wipe any stack.  On the
other hand, deploying it expends not only the 100 shields to build the
bomb, but also the carrier aircraft, which is unable to escape the massive
nuclear explosion.
The AP Superprop Attacker has 90 AP and 14 move, but cost is only up 33%
to 48 shields; once again, it can do almost as much as a BS to unfortified
Troops (64% Pk to BS's 69%), but it falls behind when facing proxy-fused
flak or scrambling fighters, so it remains best suited to the traditional
attacker rôles of harrassing armies in the field and finishing off
damaged garrisons after bombardment.  Its 36 DP should only matter when
it's being bombed on the runway; it's more than double what the old
AK had.  The fleet gets a carrier-borne version, the NA Naval Attacker,
slightly weaker at 72 AP (and costing a marginally-higher 50 shields)
but with r²≤4 vision and 54 DP.  Unlike the NS which upgrades to it,
it doesn't have AntiAir (so it doesn't get to use those DP in carrier
scrambles, not being coded as a Naval Fighter).

Overall, WWII is the era of the four-engined heavy bomber, and
specifically the BH which finally puts the lineage back in the leading
position it last occupied in WWI, as the weapon that deals damage like
nothing else.  Battles will probably hinge on whether you have enough
of them to finish the job before the fighters can retaliate (and if not,
whether you have enough escorting FH).  If wars go nuclear, the amount of
death will be limited by the production rate of the unique Atomic Bomb
units, but it still won't be pretty.

### Anti-Sea

There's no specifically naval bomber that arrives in 1939/40, so the only
new AntiSea aeroplane at that tech is the B4.  It will very reliably kill
a sub (taking no damage ⅝ of the time) and has 91% Pk on an lcmboat;
but its 20 BP aren't enough to finish off a carrier or even a tender.
On average it will take three of them to kill a CV.  Its 10M3F range is
the same as the PH, useful either for searching a wider swath of ocean,
or bombing the same target on consecutive turns (in which case it has
e.g. 99% Pk against a CVL), assuming it doesn't get brought down by
fighters in the meantime.  Instead of a blimp, the latest antisubmarine
patroller is the UE Early Helicopter.  Its combat stats are basically the
same as the ZD, but with CR 8, and it's shorter-ranged but slightly faster
at 6M2F.
Its main advantage is the extended (r²≤5) vision range against submerged
units, coupled with doubled attack strength against submarines whether on
the surface or below it (giving it a 97% WR on subs or 95½% on U-boats).
Also, it can use regular aircraft carriers (blimps
are coded as seaplanes, so can only use tenders and CVLs), as well as
its dedicated Helicopter Assault Carrier (which is slightly cheaper and
more resilient than a tender, but only carries two helis (rather than the
three seaplanes of a tender)).  And it can capture merchies, too, although the opportunity isn't all that likely to arise.

1942 brings the final evolution of the torper line, in the TB Torpedo
Bomber.  Its BP are the same old 18, but with 150 AP and 30 DP,
and an extra point of speed, it's noticeably less flimsy than the TM.
If intercepted by an NM it has nearly 5% chance of survival,
although the ND will mince it 99½% of the time
and against the contemporary NC its survival odds are under 0.2%.
When scrambled against, its Pk-Pds are 4%-1% (NM), 17%-61%
(ND), 17%-83% (NC).
The cost is 12½% up, at 45 shields, but it's worth it
for the doubled defence and the improved performance against dreads
(three planes, or 135 shields, gets 76½% Pk with 8% Pd on the first one).
LM Light-Medium Bomber has a longer
reach at 13M2F, and a much higher DP (120) along with a decent 100 AP,
but its 12 BP are lower
than the TB.  They're still enough, though, to get over 99% Pk on subs
or 98% on uu (like LT and helis, it gets double attack against them) or
67% on CVEs.  It's pricier than the TB, yet is probably a marginally
better choice in heavily contested skies (or to burn through carried
fighters); but it's not carrier-capable.  Attacking dreadnoughts it does
rather less damage than a torper (on average it'll take nearly four LMs,
which together cost more than the ship), but Pd is only 10%.
Last but by no means least, the BH Heavy Bomber can bring its 30 BP
and 576 AP to the naval theatre, with over a 2 in 3 chance to sink a
CVL straight off; a pair of BHs together have a 71% Pk against a CV.
In uncontested skies a gaggle of TBs is a slightly more cost-effective
attack, but if there are any fighters on the carrier
the BH will stand a distinctly better chance.  So if an enemy carrier
group approaches your homeland, it's likely worthwhile sending your
heavies against them.
Converted BDs can drop the XT, which has triple attack against
battleships, dealing more damage on average than a BH but with a slightly
lower Pk (34% rather than 38%) as it only has 20 BP.  If the battleship
is even slightly damaged then XT's Pk overtakes BH's.  And it may be
preferable to expend a 40-shield bomb than to take potentially quite
heavy damage to a 150-shield bomber.

1943's A.S.V. tech (behind Heavy Bombers) brings the PL Ocean Patrol,
which should really be compared to the old flying-boats; it's the same 80
shield price as PH, with longer reach (11M3F) and slightly higher attack
(80 AP) but weaker defence (60 DP).  It has r²≤5 vision, and it's simply
the longest-ranged aircraft of its era.  Its Pk on subs is 99% and on uu
it gets 96%.  Unlike flying-boats, this heavy landplane needs Concrete
Runways to operate at peak effectiveness.

There's only one AntiSea superprop in WW2, the BS Superprop Bomber.  It's
noticeably stronger with 900 AP and 360 DP, and longer-legged at 15M2F,
but the price is up another 20% and it's still at risk if intercepted by
contemporary fighters (which by now have a much larger radius of action
— another carrier as far as eight or nine tiles away could send over
NPs with a useful fuel margin and an 11% Pk).
It absolutely wallops dreadnoughts, with a 52% Pk and no Pd (in fact it
takes an average of just 27½% damage), although it does cost almost as
much as the ship.

Throughout the era, PH remains largely adequate for hunting submarines,
and the price that looked so hefty before is now modest next to the
big bombers; for new build you might turn to the PL, since it has an
upgrade path ahead of it.
Torpers continue to be an effective if vulnerable way to
strike the enemy fleet from your carriers, though they're still far
inferior to landplane level-bombers at attriting the CAP fighters.

### Anti-Air

Fighters take a major leap in 1939 with the FM Monoplane Fighter (for
which note the tech dependency on Thirties Seaplanes).  AP and DP are both
50% up at 144, and the speed of 18 is marginally better, all for the same
36 shield price as the FE.  Its interception Pks are pretty good (31% vs
B4, 58% vs MB, 90% vs LT) though it's not devastating in a scramble (~0%
Pk-46% Pd vs B4, 1% Pk vs MB, 61% Pk vs DB).  One slight downside of the
new stressed-skin construction is the loss of FieldRepair bonuses; but
it's fast enough that it can probably operate from your cities anyway.
At sea, the last gasp of
the floatplanes is the HM Monoplane Float Fighter, which is enough to turn
the tables against the PH (55% Pk; or 1½% Pk with zero Pd in a scramble),
but its 84 AP / 84 DP are a bit weak for taking on modern landplanes
(e.g. 6% Pk intercepting B4, 15% vs MB), especially scrambling from
its tender (<1% Pk vs MB, 35% Pk vs DB, 50% Pk-9% Pd vs TM, ~0% Pk-88%
Pd vs B4).  14 move is also sub-par in this era.  At least its 36 shield
cost is no higher than its land-based brethren.  The main carrier-borne
fighter, the ND Naval Dogfighter, is a much more capable unit, with 108
AP / 108 DP and 18 move (the latter being the same as the FM, which it's
basically a navalised variant of).  It's still a little more fragile than
the landplanes (intercepting a B4 it gets 15% Pk, while in a scramble it
has 89% Pd vs B4, 73% Pk-10% Pd against a TM, and 61%-<1% vs DB) and it's
a tad more expensive at 40 shields, but it should give pause to anyone
going after your carriers.  Like the similar FM, it loses FieldRepair,
but carrier-borne aircraft rarely care about that anyway.
There's also the NS Naval Strike Fighter,
which in addition to its attacker rôle can deploy its 48 AP and 32 DP
as a very limited air-to-air fighter (78% Pk intercepting DB, <1% vs MB,
~0% vs B4, ~100% vs TM; in a scramble it will draw with DB or MB, but has
2% Pd against TM, and B4 will kill it over ⅔ of the time).
Along with
its 12 move it's really not strong as a fighter; it's definitely built
for ground-attack, with AntiAir a distinctly secondary capability, but the
combination is pretty good.  (The upgrade will lose AntiAir, though, and
not get it back until VTOL.)

In 1942 the FC Cannon Fighter adds another point of FirePower to reach
192 AP and 192 DP, slightly outdoing the gains in the new heavy bombers
(50% Pk intercept, 3% Pk-89% Pd scramble vs BH) and making life hard
for the new lights (85% Pk in intercept, 49% Pk scrambling against LM).
Even with the slight price rise to 40 shields, and no advance on 18 move,
this is a strong unit.  There's a new escort in the FH Heavy Fighter,
with 160 AP & DP, enough to give it 65% winrate against the old FM and
a 49% chance against an FC.  At 60 shields, it's of course inferior for
home defence, but it's by far the best way to improve a bomber formation's
defence (at 2⅔ DP per shield, it's a more efficient defender than the BH,
as well as the LM to which it converts).  Its speed/range of 14M2F is fully
adequate to escort even the longest of raids; it's a really valuable
upgrade over the EF and at least for now makes escorting worthwhile.
Aircraft carriers get the NC Naval Cannon Fighter, with the same FirePower
boost as the FC for 144 AP/DP, but a reduced speed at
16 move (still probably plenty).  Against its most likely opponent (TB),
it has 99.8% Pk on intercept and 83% Pk-17% Pd in a scramble; a pair of TBs
with the initiative will still only be enough to kill it 59% of the time.
Thus it puts carrier defence in a strong position, performing as well
against TB as ND did against the old TM.

Superprops offer only slight improvements.  1944's FF Superprop Fighter
is faster, at 21 move, but otherwise has identical stats to the FC (thus
e.g. 14% Pk intercepting BS, <1% Pk-94% Pd in scramble).  Meanwhile,
the NP Naval Superprop (Carrier Aviation 1945) gains a little interception
strength at 192 AP, though defence remains at 144 DP,
and the price rises to 45 shields; its advantage is the 25% speed
boost to 20 move.  So as an interceptor it's rather good, retaliating
on bombers across a big chunk of ocean, but in a scramble it's not ideal.
The importance of superprops, though, is that they let you eke out the
last gasp of capability without having to build Air Bases to support jets.

Overall, fighters gain ground in the early and mid war years, but then
the superprops are disappointing and may be worth skipping (but then the
early jets won't be that great either).  Also of note is the Airborne
Radar tech which gives all AntiAir units +20% attack; this isn't a huge
bonus so it probably makes sense to prioritise the new fighter techs,
at least up to 1942.

### Airborne Assault

Not much changes for troop transport in 1939.  The only new aircraft
with cargo is the B4 Four-engine Bomber, which can ferry assault troops
or gliders over a record 30 tiles but whose radius of action if it wants
to bomb as well is only 10 tiles, the same as the CM (for paras) and
inferior to the MB (for gliders).
Still, it may be
worth having a bomber fleet bring along their own paras to take a city
rather than needing dedicated transports.  (Just make sure to unload
them before you bomb, in case a scrambling fighter shoots you down!)

1942 sees rather more change.  BH Heavy Bomber loses the ability to
transport assault units directly, but can still tow gliders (and at 13M2F
has one notch longer legs than MB).  Those gliders may now include GH
Heavy Glider, which carries four units — twice as much as the GG, but
at 150% the cost (18 shields), meaning that (apart from economising on
tugs) it's only cheaper if fully loaded.  Its main advantage is that it
can deploy the new ac Light Tank, with 33% more DP-per-shield than
Assault Troops, helping you to hang onto your gains.
And for when you need to move a lot of men around, there's now
the CS Strategic Transport, with a cargo of 4 assault units and a brisk
15M2F speed/range.  It, too, can carry the Light Tank (though of course
it needs a city or airfield to unload at).
However, at 80 shields it's quite a high-value asset,
so you might be reluctant to send it into the front line with a load of
paratroops, lest the enemy take advantage of its lack of defensive
armament; its 16 hitpoints won't last more than a couple of passes from
cannon-armed fighters.

Note that if you upgrade your BHs in 1945 to BS Superprop Bomber, they
will no longer be able to tow gliders.

None of this stuff is hugely exciting, but at least airlifting large
stacks is now slightly more efficient, and Tetrarchs are nice.

### Naval Aviation

The balance of airpower at sea swings in favour of the defence, as the
upgrade from NM through ND and NC to NP is much greater (a trebling of
AP, and 2.25× DP)
than that from TM to TB (doubled DP, 25% more AP,
and no gain in BP at all).
On the other hand, the latter can sometimes survive an attack from the
mixed-rôle NS; and it's that bit better against battleships (average to
sink a dreadnought is now 117 shields).
Both NS and NA are reasonably useful ground-attackers,
weaker than their land-based equivalents but delivering more effective BP
at short range than carrier-capable bombers like DB or L3;
NS also makes a useful contribution to the defence of the carrier.
The only carrier-capable aircraft that's actually reasonably effective
against a scrambling NC/NP is the old KA, with a 47% Pk, but 1 pop is a
lot to spend to achieve that.
Apart from that, only land-based heavies pose a serious threat to a
carrier with cannon-armed CAP.
The old DB is alright, with an average of two DBs to kill each NP (both
units costing 45 shields, so defence still has better economics).

Seaplanes hang in there with HM, just about strong enough to hunt TBs
and PHs or PLs but not stunning against anything else.

There's no upgrades to the old DB; and while the UE is new it's unclear
whether its sonobuoys and doubled ASW attack are worth more than the ZD's
longer loiter.

### Flight Refuelling

In 1944, KM Tanker Monoplane adds a couple of tiles of move, and improves
evasion (though not enough to keep pace with progress in fighters, which
have advanced a _lot_ since the K3's day).  This brings the range gain
with refuelling back up to 50% for the latest heavy bombers; KM's Heavy
flag is not likely to be an issue since hopefully the need to repair
won't ever arise.  A single KM can keep _two_ PS continually airborne and
on-task by staggering their refuellings two turns apart, magnifying their
sub-hunting efficiency.  KM+LD is the first extension of airliner range
since 1935; the next won't come until the Fifties.
Set against this is the cost increase; 75 shields is quite a lot (it's
half a BH, just as K3 cost about half a B3).  Though as a non-combatant
unit it should have a longer life expectancy than the bombers, at least
if used correctly, so it should be easy to maintain the capability once
you've built it up.

### Buildings

Heavy Airlift unlocks the building Waterbombers, which increases the
economic output of forest tiles.  It's reasonably cheap at 80 shields,
so for a city working several such tiles it's a worthwhile investment.
In the same tech is the greatwonder ICAO; the benefit to the owner is
fairly limited (see all cities on the map), the most important effect
being that everyone gets an additional trade route per city.  So building
it first is mostly just for bragging rights, but getting it built at
all is helpful to a large trading empire.

Tracking Radar unlocks a building (Sector Control) and a greatwonder
(Dowding System) with the fairly weak effect of increasing fighter
defence in cities by 30%.  At 80 shields to build and 2 gold upkeep,
Sector Control costs about the same as a pair of FCs, and even a six-stack
of fighters with the bonus is weaker than the eight fighters you could get
otherwise.  Probably not worth bothering with.

Proximity Fuse doesn't unlock a new building, but does boost the effect
of the existing Flak Battery; this can be useful in frontline cities.
For example, a BH with beam-bombing has a 42% Pk on a plain fortified
Troops, flak alone brings this down to 31%, but proxy-fused flak takes
it below 20%.  Looked at another way: two Troops and a proxy-fused
Flak Battery has the same DP as three Troops and no flak, costs the
same shields to build, but upkeep is 2 shields and 1 gold, rather than
3 shields.

Nuclear Weapons unlocks the Manhattan Project greatwonder, which allows
**all** civs (with the selfsame tech) to build nukes.  You only want that
if you have both a fleet of heavy bombers to carry them, and a big enough
lead to give you the edge in a nuclear war.

## Postwar era

The jet engine and air-to-air missiles quickly obsolete the wartime air
fleets, but the replacements are increasingly expensive, and require new
infrastructure to support them.  Strategic nuclear bombing continues to
rely on the old propeller technology.

### Reconnaissance

The superprop PS Maritime Reconnaissance, replacing the PL, _finally_
brings capital-R Recon to maritime patrol, and its 10M4F range won't be
surpassed until supersonic bombers in the Sixties (and they can't loiter
like propellers can), but its 60 DP really won't do much (FV gets 91% Pk)
and the cost is up a little at 90 shields.

In first-gen jets, the M1 Prototype Jet Bomber gains the Recon ability,
which older MBs didn't have, and at 15M2F it's fast.  However, it
only has r²≤4 vision, and at 100 shields it's much more expensive
than the LM/FH.  Its 216 DP are pretty okay — the old FC has 39%
Pk intercepting, it as does F1, and even cheap little FV has 11%.
Meanwhile, the UH Helicopter is still fairly short-ranged (9M2F) and,
while it does now have
some defence, it's only 8 DP (approximately anything will shoot it down),
so using it for city recon would be an odd choice.  Its main selling
point remains the ASW capabilities (sonobuoys and attack bonus).

The late ’40s bring the first really practical jets, among which is the
RJ Recon Jet — the first purpose-built pure reconnaisance aircraft since
before WW1.  It costs 75 shields and is basically defenceless, but with
some evasive capability (14 defence but 0 FirePower means fighters may
take a few rounds to bring it down); it has
16M2F speed/range, r²≤5 vision, and can cross borders in peacetime
— allowing you to keep an eye on friendly nations whom you perhaps
don't trust to stay friendly.  MJ Small Jet Bomber matches it for speed
and vision, and is pretty resilient with 350 DP, but does cost a hefty
120 shields to build; if you've built some for bombing, it's useful to
have the recon capability there, but it'd be odd to build one purely to
use for that.

### Anti-Ground

The earliest jets are too fuel-hungry for heavy bombers, so the M1
Prototype Jet Bomber is a medium, with the same old 12 BP.  Its 15M2F
speed is a 25% improvement on the MB, but AP is only slightly
improved to 189 (a 26% gain), while the
cost is up 11% at 100 shields.  DP is up to 216 (73% more than MB);
however, fighters have improved
an awful lot since the MB's day, and e.g. an F1 will shoot it down quite
often (Pk=39%).  Apart from Recon, it's hard to see why you'd bother
with it when e.g. a BS can do so much more than a pair of M1s (unless
you're eyeing the upgrades).  There are several attacker options, of
which the most obvious is A1 First-gen Jet Attacker.  Unlike previous
attackers, it has 2 FirePower, giving it 120 AP and 72 DP.  However,
its AP growth over the AP Superprop Attacker is matched by the rising
cost (64 shields), meaning that its real advantages (apart from being
slightly more upkeep-efficient) are its r²≤4 vision and (especially)
its 18 move, which gives it the range to strike well into enemy territory.
With the same combat stats, the PJ Jet Flying Boat is the last gasp of
seaplane strike; it's slightly slower at 16 move, and costs a hefty 80
shields, but also brings an AntiAir rôle to the table and might have
its uses in amphibious warfare.  So too might the N1 Naval Jet Attacker,
operating from aircraft carriers with its 100 AP/60 DP.  It has the same
18 move as the A1, and is very slightly cheaper at 60 shields, but doesn't
hit quite as hard.  Still, it's the best shore strike option the carriers
have, dealing slightly more damage per shield than the old DB and without
the risk of fighter interception.  Off on a branch of its own, the V2
Artillery Rocket (Rocketry) is a missile (i.e. destroyed after attacking)
with a range of 12 tiles.  It deals slightly more damage than an M1,
and is pretty cheap at 20 shields, but whether it's worth expending
missiles rather than using bombers that you can _re_-use is unclear.
The situation where it makes most sense is if there are enough enemy
fighters swarming around that you wouldn't get your bombers back _either_.
(But then, it's quite weak against scrambling fighters since they're
far more likely than 1-FirePower Troops to burn through its HP before
it finishes its CRs.)  In such a situation, the other option would be
attackers, which don't deal as much damage relative to cost, but _do_
generally come home again.  To be honest, none of 1946's AntiGround
options are that great, so you might choose to just stick with the old
BS until the next generation comes along.
If you spend the large amount of bulbs to research Thermonuclear Weapons,
you gain access to the Thermonuclear Bomb, functionally similar to the
Atomic Bomb but non-unique (so you can build up a nuclear stockpile) and
slightly cheaper at 90 shields.  A strange game; the only winning move is
not to play.

That next generation, Bombers 1949, brings something impressive in the
form of the MJ Small Jet Bomber.  Costing 120 shields (the same as a
pre-war heavy), its 2 FirePower yields 24 BP, 300 AP and 350 DP, which
if it gets really lucky can occasionally one-shot Troops.  At 16M2F it
can reach as far as a heavy.  Such a heavy can be built for 160 shields
in the form of the B1 Early Jet Bomber; with 720 AP, 450 DP and 30 BP,
it's slightly less devastating than the BS (though defends better),
and has marginally less BP per shield than MJ, so its main draw is
the better upgrade path.
The BP Intercontinental Bomber (with its six turnin' and four burnin')
stretches the range of nuclear delivery slightly with its 14M2F (two more
move than a BU), but costs 10% more at 200 shields, is no better on
defence (meaning the contemporary FW gets 63% Pk), and can't perform the
conventional-bombing rôle.  (So beware that if you upgrade your BUs to it
they won't be able to convert to BS any more.)
Over in the
attacker line we have the AJ Attack Jet, 25% stronger than the A1 (150
AP, 90 DP) and slightly faster (20 move) for an unchanged price; within
their range attackers are by now distinctly more effective than bombers,
simply because they are so much cheaper.  The AN Naval Attack Jet sees
this too, with the same combat stats as the AJ but slightly pricier at
70 shields.  (For that extra cost, you get not only carrier capability
but also AntiSea.)

Heavy jet bombers come into their own in the Fifties, with the BJ Jet
Bomber delivering 1152 AP and 576 DP over a long 18M2F range; against
fortified Troops with all the modifiers (beam-bombing versus proxy-fused
flak) it has a 42% Pk, and even a scrambling FI will lose 86% of the time,
with just under a 1% chance to down the bomber.
On the other hand, the same fighter intercepting (it will have the
Airborne Radar bonus) will get a 51% Pk, and
the bomber is expensive at 200 shields.
The BJ can also convert to the BN Jet Bomber (Nuclear), which for the
first time loses no DP or range compared to its conventional cousin.  As
well as penetrator bombs and free-fall nukes, it can carry the XS
Stand-Off Bomb, which while slightly more expensive at 120 shields (and
requiring an Air Base to build), can fly up to 4 tiles from the bomber,
thus finally letting you avoid catching your own bomber in the explosion.
For those who haven't built Air Bases everywhere, the BR Turboprop Bomber
provides a decent upgrade to the superprops, with 16M2F range, 990 AP and
360 DP.  (It can carry free-fall bombs but not stand-off missiles.)
Meanwhile, the AS Supersonic
Attacker can almost match it for range, with its 30 move, and packs a
decent punch (192 AP, 96 DP) for its 80 shields.  While it doesn't deal
as much damage as the bomber, avoiding the risk of interception (and
the upkeep of unhappiness) may well make it the preferred strike option.

In summary, the immediate postwar era is a bit of a weird period as
strike aircraft begin to usurp the bombers' traditional rôle.  If the
enemy is denuded of fighters, or just technologically inferior, bombers
remain the quickest way to collapse his resistance in a lightning war,
but in heavily contested airspace the attackers with their lower loss
rates are distinctly more economical in the long term.  And of course
heavy bombers are the only ones that can carry nukes; a V-force of BN
Jet Bomber (Nuclear) carrying XS makes for a hell of a deterrent, as long
as their bases are spread widely enough to survive a first strike.

### Anti-Sea

The PS Maritime Reconnaissance is great at ASW, with 98% Pk on U-boats
and an incredible 10M4F range.  It gets a solid 88% Pk on CAM boats and
68% on CVE, but its 12 BP aren't enough to sink landing-craft, tenders
etc. (it'll deal an average of 10 damage and take 2), and as for full CVs
it should stick to finding them and let someone else make the attacks.

The M1 Prototype Jet Bomber deals only marginally more damage to shipping
that the old MB could; its advantages are higher speed (15M2F) and
having more HP left over in case of interception.  In most cases it's
less effective in the rôle than torpers.  The UH Helicopter has a solid
99% Pk against subs, and even 54% versus lcmboats, but it'd take quite
a swarm of them to do anything meaningful to a carrier, and it still
only ranges 9M2F; its real job is not AntiSea (apart from ASW, with
sonobuoys to spot the subs) but airlanding infantry.
Really, if you're trying to sink anything big you're best off sticking
with your existing TBs and heavy bombers at this point.

In 1949/50, the rather good MJ Small Jet Bomber has a 3% chance to
one-shot a CVL, while a pair of MJs has a 6% chance to sink a CV.
With a third MJ, it's 94%, while four have a 42% chance against a CVN.
Of course, at 120 shields each, MJs aren't cheap — you could get over
twice as many TBs, which would be much more destructive — but the
MJ's defence is far stronger (only 41% Pd to an intercepting NF, or 53%
if the fighter has airborne radar).  And unlike TBs, MJ is guaranteed to
survive
attacking a dreadnought (if there are any still around), dealing over 10
HP of damage on average (and with a 2½% chance to sink it outright).
There's also the B1 Early Jet Bomber, which can comfortably kill a CVL
(68% Pk); a pair of them can do the same to a CV (71% Pk) and three can
even sink a CVN (58% Pk).  It's rather less vulnerable to fighters
(35% Pd to a radar-equipped NF).  Since three
B1s cost the same as four MJs, the B1 is slightly more cost-effective
at destroying carriers, so long as it can manage not to get shot down.
B1 is also better against a scrambling fighter, with e.g. 98½% Pk-1½% Pd on
NF (whereas MJ has 79%-21%).  On the other hand, for everything except
beating off interception or operating at the absolute limits of range,
BS is better still (though a tad pricier).  Torpers are finally replaced
by the AN Naval Attack Jet, a carrier-capable attacker (150 AP) with 20
move that can target ships.  A single AN, costing just 70 shields, has
a three-in-four chance to sink a CV; a pair will sink a CVN four times
out of five.  However, ANs can be blunted by fighters; a scrambling NF
will beat an AN 63% of the time (an NC or NP gets 45%, NJ gets 35%), and
perhaps more importantly has a 40% chance to kill it in the first combat,
before the AN can disengage.
So ideally you want to use bombers to blow up the fighters, and then ANs
to sink the carriers they were on, but that could be hard to arrange.
ANs should also be useful for sub-hunting, as they can one-shot a U-boat
(74% Pk; the rest of the time a second shot is basically always enough)
and then carry on moving to look for another one.  Sinking dreadnoughts
takes an average of about two ANs, which is viable (especially since, as
an attacker, AN is likely to gain veteran levels easily).

The main new AntiSea aircraft in the Fifties is the BJ Jet Bomber;
it hits slightly harder than the B1 (63% Pk vs dreads; 84% Pk vs CVL;
99% Pk-0.1% Pd vs scrambling NI where B1 gets 97%-3%)
and is more likely to survive the fighter response
(18% Pd vs intercepting NI).
In a hot nuclear war, a single XS from its BN persona could wipe an entire
CVN and its aircraft complement in one go — if you know where to find it.
Also, with 18M2F it can reach further than ever.  But it does cost 200
shields to build, a major investment.
Cities without an Air Base instead get to build the BR Turboprop Bomber,
which is only fractionally stronger than BS with its 990 AP and the same
360 DP, but 16M2F extends its reach appreciably.  Against dreadnoughts
its Pk is up to 58%; on CVL it gets 81%.  But it is vulnerable to the
latest fighters, NI getting 52% on interception, and it costs the same
200 shields as the BJ.

The Fifties also see the development of the nu SSN, a more powerful
underwater attacker that for the first time doesn't need to surface to
recharge thanks to its nuclear propulsion.  This may help it to hide from
PS and other fixed-wing ASW, but not from UH's sonobuoys (nor from other
SSNs, which have the best hydrophones in the business).

Overall, the most important AntiSea development in the era is the AN,
but MJ and BJ also have their moments, while PS makes trouble for subs.

### Anti-Air

The jet fighters of 1945 are faster, but no stronger, than the props
they replace.  F1 First-gen Jet Fighter has the same 192 AP as an FC or
FF, but only 144 DP (same as an FM), and it costs a chunky 50 shields.
Its main selling-point is its 25 move, allowing it to cover quite a
wide area.  Alternatively, the FV First-gen Light Fighter is cheap at
32 shields, but with only 120 AP and 90 DP it's limited in what it can
do — although it is quite effective against an M1, and has the same 25
move as the F1.  The two are pretty closely matched for cost-efficiency,
but in the long run F1 pulls ahead because of upkeep.  FV's main selling-
point is that it doesn't need an Air Base to build or repair, making it
ideal for deployment in far-flung outposts.  It even gets the FieldRepair
flag, so can more readily be dispersed to airfields outside your cities.
Jet fighters also
find their way onto the carriers, with the NJ Early Naval Jet.  At 24
move it's slightly slower than the other two, and it's also a little
weaker than an F1, having 160 AP and 120 DP, while being rather more
expensive at 60 shields.  Apart from the extra speed it's inferior to an
NC or NP, and even defends worse than ND.
All these early jets are just something you have
to get through to reach the good stuff; but if they're strong enough to
do the job (and against some older bombers they will be) then being able
to reach a couple of tiles further could come in handy.  There's also PJ
Jet Flying Boat, with 120 AP and 72 DP for the high price of 80 shields
(and only 16 move); it's also an AntiGround attacker, but even combining
those two capabilities with the option to use tenders and buoys it looks
unlikely to be worth building unless you have a bunch of tenders and want
to build an onshore strike force for them (in which case being able to
combine the strike and air-defence rôles in a single airframe might well
be preferable to a mixture of PH and HM).  Unlike most jets, the flying
boat doesn't need an Air Base to support it, which might also be a point
in its favour (since e.g. an NJ can't repair at sea whereas PJ can).

1950 brings the second generation jet fighters, armed with air-to-air
missiles which give them a FirePower of 5.  Thus the FW Swept-wing Fighter
has 375 AP, well worth its 60 shield cost; intercepting an MJ it has
61% Pk.  However, things aren't so good in a scramble (it has 225 DP),
where an MJ will kill it 63% of the time.  Fortunately, its 28 move means
it can be based a long way back from the front line and still be able to
make interceptions.  The FL Transonic Light Fighter, though requiring an
extra tech to reach, is equally cost-efficient, having 280 AP and
168 DP for just 45 shields, though only 25 move; like FV, its ability to
operate from unprepared bases (FieldRepair flag, no Jet flag) makes up
for its poorer upkeep efficiency,
but if you already have Air Bases (e.g. to support jet bombers) then the
FW is probably preferable.
Going the other way,
there's now a jet heavy fighter in the JA All-Weather Jet Fighter; it has
360 AP, making it a decently powerful interceptor but not enough so
to justify its 75 shield cost.  Rather, its value comes from its loiter
(15M2F) allowing it to escort bombers with its 240 DP — it's a marginally
cheaper source of DP than either MJ or B1, though of course it can't bomb
like they can.  It also has r²≤5 vision, the first fighter to do so.  On
balance it's doubtful whether it'll be worth building escorts (rather than
just having a bigger stack of bombers), but it's certainly worth upgrading
any old FH for the 50% DP boost (and more than doubled AP) if you have the
Air Bases to support it.
Aircraft carriers get the NF Swept-wing
Naval Fighter, which is not quite as good as the landlubbers — 300 AP,
180 DP, 26 move, for 70 shields — but is a major upgrade over the NJ, and
slightly more cost-efficient on interception than the NP.  The main gain
though is that it can pack more combat power into the same amount of
hangar space on the carrier; neglecting that, it's still a worse scrambler
than the props.
All four of these fighters are good at what they do; it's just that
(apart from the FL) they're rather expensive for it.
Finally, there's the XA Surface-to-Air Missile, which is very powerful for
its cost at short-range interception, but as a missile is single-use, and
has no scramble capability; its rôle is to retaliate against a bomber
force that didn't manage to take the city it's in, but this in many cases
is better met by fighters in a nearby city.  One potential use for XA is
to embark it on an aircraft carrier; since units at sea can't repair as
rapidly as in cities, enemies are more likely to attempt attritional
bombing when they don't have the forces to take out the carrier-group in
one turn.  On the other hand, XAs take up a lot of hangar space.
Interestingly, XA can also launch from the nu SSN, potentially causing a
loitering PS to have a Very Bad Day (especially as the sub can see the PS
from further away than vice-versa).

In the Fifties the heavy-fighter concept merges into the main fighter line
to produce the FA Supersonic Fighter, with 20M2F allowing it to fly escort
missions (with its 240 DP) as well as using its 480 AP for interception.
The latter gives it 39% Pk against a BJ, while the former gives roughly
even odds against an FF or F1 — but another FA (with Airborne Radar)
will kill it 88% of the time.  Still, at 70 shields, it's a slightly more
useful escort than JA, and doesn't cause unhappiness when deployed.
Curiously, FW upgrades to it but JA doesn't.
For scrambling, your best bet is the FI
Supersonic Interceptor, with 320 DP and the same 480 AP, along with 30
move, at a price of 64 shields.  This has a tiny chance to beat an
attacking BJ (<1% Pk-92% Pd), or 56% against an MJ;
it is simply the most cost-efficient scrambler yet, finally outperforming
the props in this rôle even absent considerations of upkeep.  It's also
the best interceptor, being a smidge cheaper than FA.
At sea, the NI Supersonic Naval Fighter has the same 30
move but is weaker at 350 AP and 210 DP — only marginally better than
the NF, but at least the cost is the same at 70 shields.  All three of
these fighters have r²≤5 vision.  Since these fighters (particularly
FI) are so effective, enemies may be tempted to switch from bombers to
attackers, forcing you to fight in the scramble; alternatively, they
may just make heavy use of escorts.

Jet fighters as a whole are slow to get started, but once equipped with
missiles they firmly eclipse the old props with impressive interception
capabilities, though most struggle in the scramble.
Carrier-borne equivalents
are playing catch-up once again, with fewer hitpoints and higher prices
than their land-based cousins.

### Airborne Assault

In 1945, the UH Helicopter provides a new way to deploy assault units.
It can land anywhere, without all that tedious mucking about with gliders,
and it's pretty cheap at 32 shields, but it only has capacity for a single
unit, and its range is short at 9M2F.  While not completely defenceless,
it's still very vulnerable with just 8 DP.  Possibly the best use for it
is in conjunction with the Helicopter Assault Carrier, for more effective
amphibious invasions: an lphboat and two helis costs 104 shields, rather
than the 60 shields of a pair of lcmboats, but the lphboat is faster (3
move instead of 2) and can unload from a distance.  Also, helis can land
on a carrier at sea, but ground units can only board lcmboats in cities.
Besides the lphboat, helis can also use ordinary aircraft carriers,
so e.g. a CVN with a spare slot on its way to wipe out an island city's
garrison can bring along the soldiers to capture the city too.  They can
even ride on a dreadnought if there are any left.

Two new transports are developed in the Fifties.  The CT Turboprop
Transport has longer range (12M2F) than the old CM, and carries a
third unit (plus it can see r²≤5), while costing only marginally more at
60 shields.  CJ Jet Transport reaches much further and faster, at 18M2F,
with a cargo of up to five units; however, like the CS it replaces,
it's an expensive asset (100 shields!) which you might be reluctant to
risk in the front line.  The slight improvements to evasion don't help
much against jet fighters with plenty of move.

### Naval Aviation

Carrier-borne fighters take a while to advance past the old props,
except in the matter of speed, and become distinctly expensive to build.
There are no new torpers, but they finally get properly replaced in 1950
with the AN which can really ruin a carrier admiral's day.  The same
aircraft is responsible for shore strike, as strong as the AJ and only
slightly more expensive.  As for seaplanes, the PJ is just weird —
similar stats to the contemporaneous A1 attacker, but 25% more expensive,
and why do you still have tenders anyway?  Just use N1s on a _proper_
carrier.  (If the ability to repair at sea is important to you, NA is
very nearly as good, apart from the lack of AntiAir, and doesn't require
a by-now-rare dedicated platform.)

Carriers can also transport V2s, but they can't launch them from deck
so it's not clear what the point would be.

Carrier Aviation 1950 also unlocks the CVN, which has twice the capacity
of the old CV, twice the defence (240 DP), and a point more speed (6 move),
while only costing 80% more at 270 shields.  If you have any reason to
send a 12-stack of naval aircraft out in a single task force, it's a
cost-efficient way to do so; but if the enemy does manage to sink it
you'll probably be wishing you'd opted for the redundancy of a pair
of CVs.  A CVN loaded up with a full complement of NFs and ANs comes to
a total of 1,110 shields — that's a lot of eggs to put in one basket.
(Especially when a single nuke could crack the lot in one go.)
Then again, if you're the kind of economic hyperpower that can afford
several of these, then the USS Big Stick really is an unrivalled tool
for global power projection and bragging rights.  The only thing it
*can't* do is launch nuclear strikes.

If you have any spare slots on your carriers and can't afford the planes
to fill them, a handful of XAs may be a good idea to punish any bombers
that dare to attack your carrier group.  But enemies might well be using
ANs instead, in which case you don't get a chance to fire the XA at them.

### Civil Aviation

Fifties Airlift unlocks the LJ Jet Airliner, whose 12M3F range doubles
the reach of your trade routes, but costs 50% more to build than the old
LD.  If you don't have the Int'l Airport, you must instead rely on the
LV Turboprop Airliner, which at 11M2F should bring quite a few cities
into range, and is only 10% more expensive than LD.
However, note that researching this tech also
reduces the one-time revenue from new trade routes (and from merchant
ships!) by a third.  On the other hand, at this point ongoing trade
probably has more to offer (especially for a Democracy with lots of
economy buildings).

### Flight Refuelling

Fifties Tankers unlocks the KJ Tanker Jet, whose 11M2F allow it to add 11
tiles to the operational range of any aircraft.  For instance, it could
stretch the range of a BJ or BN by over 50%.  Two working together can even
keep aircraft (even 1-fuel fighters) on continuous airborne alert; this
may have its uses in ensuring your nuclear deterrent force survives an
enemy first strike.  (And when we fix transport nesting, you'll be able
to use Black Buck style tanker stacks to nearly double bomber range,
albeit expensively.)
If the world is big enough that there are cities even LJ can't reach, a
helping hand from a KJ can make trade routes just that bit longer; or it
can enable LV to make trips that otherwise would need LJ (and thus an
Int'l Airport in the source city).
KJ is a big improvement over KM (about 50% more range and ⅔ more evasion)
but the price tag, as always, rises too; at 120 shields it's 60% costlier
than the old KM.  And it needs an Air Base.

### Buildings

Air Base (Gas Turbine) is required to build or maintain jet aircraft
(with a few exceptions like light-fighters and PJ); with the weaknesses
of first-gen jets you might not be in a hurry to build it at first, but
when powerful weapons like FW, AN, MJ and BN+XS come along you'll want to
be ready to make use of them.

The smallwonder Supersonic Wind Tunnel (Supersonic Aerodynamics) doubles
the city's science output, though at 300 shields you'll need a hefty
trading city to justify it.  Sound Barrier (Rocketry) is a 300-shield
greatwonder that gives two immediate techs, which just might get you to
second-generation combat jets quicker than your rivals.  Space Flight
unlocks two greatwonders: Spy Satellites reveal the entire map and cities,
but not units (it's not clear how useful this is), while Human In Orbit
gives a very useful two happy citizens in every city (which could push
you into celebration in peacetime, or combat unhappiness from deployed
units when at war).  SAM Battery (Early Missiles) is a nice upgrade from
flak, doubling defence, but costs 90 shields to build and 2 gold per
turn to maintain.
Int'l Airport (Fifties Airlift) adds 50% to tax revenue;
this alone would struggle to justify its 2 gold upkeep, but it also lets
the city open an additional trade route, which is much more valuable, as
well as allowing the construction of LJ for global trade.

## Cold War era

We don't really have coverage of this period in the ruleset yet.
Mainly this is because historically by this time nuclear MAD with
ICBMs had rendered wars between Great Powers undesirable, so most of
the fighting ended up happening in proxy wars.  But there are no ICBMs
in the ruleset, and I need to figure out what the flavour of warfare
becomes in the presence of air-launched nukes.

### Reconnaissance

The RS Spy Plane is a significant upgrade from the RJ, largely because
of its speed — at 36M1F it no longer has to loiter over enemy territory
and risk interception, so it's basically a completely safe way to keep
tabs on enemies and friends alike.  Cost is 20% up at 90 shields.
MS Tactical Strike Jet also has Recon, and 21M2F is enough to look
fairly deeply in a single turn, but as always it's the bombing capability
that justifies its existence.

### Anti-Ground

In the Sixties, the BC Supersonic Bomber extends the speed/range of heavy
bombing out to 24M2F, but its combat stats are only slightly stronger at
1404 AP / 648 DP; its Pk (with beam) against Troops (fortified with SAM)
is 30%, and it gets 77½% vs scrambling FJ (63% with Sector Control).
An intercepting FJ gets 52½% Pk — F5 gets 29% — so you'll need some sort
of escort if you want your
expensive (240 shields!) asset to survive.  There's also a new medium
bomber, the MS Tactical Strike Jet.  Its 432 AP for 135 shields is
pretty good, although 24 BP is still rarely enough to kill Troops (18%
Pk, or 6% against fortified).  At 21M2F it can reach far across the
battlefield; however, 486 DP — while much more defensible for its price
than the heavy — still leaves interceptors troublesome, with FJ getting
66½% Pk and F5 getting 56%.
Attackers get a big boost with
the AF Jet Fighter-Bomber having 3 FirePower (and being able to target
all unit classes); it has 384 AP / 144 DP while still only costing 80
shields, so for targets within its 30M1F range it's hugely effective —
84% Pk vs Troops+SAM,
and 65% vs scrambling FJ which is vastly better than the
old AS.  The fleet air arm aren't left out either, with AV VTOL Attack
Jet — not quite as strong, but still 288 AP / 192 DP for a solid 64%
Pk on Troops, though only 13½% vs FJ (or 36% vs F5).  On the other hand,
being carrier-borne it has maybe more chance to surprise cities without
SAMs or flak, in which case Pk is 97% vs Troops and 48% vs FJ.  Do bear in
mind though that range is still limited, with just 20 move, and its price
rises to 80 shields.  Overall, the decade strongly favours attackers —
heavy bombers are just too vulnerable in this age of supersonic fighters,
and with guided munitions allowing a smaller aircraft to destroy a target,
there's much less justification for a big bomb-bay full of boom, outside
of the 'instant sunshine' nuclear delivery rôle.
Meanwhile, the attackers have also picked up AntiAir capabilities to make
them even more valuable and versatile.

### Anti-Sea

The same four aircraft provide the Sixties' Anti-Sea as Anti-Ground:
BC Supersonic Bomber, MS Tactical Strike Jet,
AF Jet Fighter-Bomber and AV VTOL Attack Jet.
BC is a slight improvement with better odds (80½%) to survive NI
interception thanks to its extra hitpoints, which also takes
it to 99½% Pk against a scramble; but its damage dealt to ships is little
changed ­— it's still only 30 BP, after all, and against a defence of
3 or 4, having an attack of 13 instead of 12 makes not much difference.
(There probably aren't still dreadnoughts around, but if there are then
Pk rises a little to 68%.)
Meanwhile, carriers are now likely to have more organic interception
capability by retasking their AVs — which despite a nominally lower AP
than NI have almost as good a Pk (7%) as NI (19%) suffers from rounding.
MS slightly improves its chances to sink a CVL, but against anything more
resilient it's limited by its 24 BP; its main gains are in survivability.
On the other hand,
a single AF can reliably take out a CV or even a CVN, although if it has
to grind through scrambling fighters first it could take a while; AV is
not quite as strong but still poses a potent threat to any carriers it
finds (Pk=70%).
So, much as with Anti-Ground, attackers in the Sixties
become a devastating weapon that gives offence the advantage over defence.

### Anti-Air

The new air-superiority fighter is the FJ Sixties Fighter, which with
560 AP / 320 DP is distinctly stronger, particularly in escort —
another FJ intercepting will only kill it 84% of the time.  Range is up
at 25M2F, enough to stay with a BC; but build cost is up at 80 shields.
F5 Supersonic Light Fighter is an inexpensive fast fighter — 450 AP /
225 DP for 50 shields, and almost as fast (28 move) as an FI.
It's the most cost-efficient interceptor yet, though its scramble is a
little behind FI; as usual for light fighters, it doesn't need an Air
Base to build and maintain it, but it no longer has the FieldRepair flag.
Attackers
in the Sixties gain air-to-air capability; AF Jet Fighter-Bomber has
19% Pk vs BC, though costs the same 80 shields
as an FJ (which has 46% more AP), and in a scramble its 144 DP are no
stronger than the old FM that cost less than half as much.
Similarly, the AV VTOL Attack Jet is
a fairly decent interceptor — 288 AP, 7% Pk vs BC — but with the defence
of an FF (192 DP) it'll get flattened in a scramble (94% Pd vs BC in
the open; even with SAM it's 77½%).  Still, it's useful that your
attack forces can now also contribute meaningfully to air defence —
yet another reason to prefer attackers to heavy bombers.
AF and AV should actually be stronger at AntiAir, as they ought to get
the bonus from Airborne Radar, but game engine limitations mean we can't
currently give them it without them also getting the bonus against ground
targets (which we don't want to give them).

### Airborne Assault

The new UT Twin Rotor helicopter is fully specialised for the cargo rôle, and can deliver up to two Light Tanks to any random field 10 tiles from home.  Its 28 DP won't last long against anything, though (even pre-war FE gets over 99% Pk) so make sure to have top cover from air-superiority fighters.  Also, the usefulness of this capability is unclear when even a pair of Light Tanks backed by a SAM battery aren't a match for the latest attack aircraft; fighters are a better defence in most cases.  Light Tanks are stronger when attacked by ground units, but that's not very likely to occur.  The real value may be that UT doubles the number of units that can squeeze onto an lphboat, dropping off one to capture each of several cities emptied of defenders by your air forces.

### Naval Aviation

With the AV VTOL Attack Jet being such a capable multi-rôle aircraft,
it's tempting to load your carriers up with nothing but AVs.  A 12-strong
wing on a CVN can chew up the enemy army or navy; but the stack costs
1,230 shields, and if the enemy is likely to find and attack your carrier
then you might still want to pack a few NIs to beef up the defences.
An attacking AF can eat through approximately 1⅚ NIs or 2 AVs);
the extra 10% of the NI (and slightly lower build cost)
may be worth it if it can make the difference
between the carrier surviving or not, but if the enemy force is strong
enough that finding you = sinking you then you may as well just carry
as much attack capability as possible and hope you can stay hidden while
you wreak havoc.
And of course neither AV nor NI can do much about a nuclear strike.
Two things that we probably ought to have for realism, but currently
don't, are harrier carriers / Through Deck Cruisers (should AV be coded
as a helicopter?) and heavy naval strike/patrol aircraft that can only
use CVNs (the US fly some pretty big stuff off their supercarriers).  As
it stands, there's not much reason to use a CVN rather than two CVs (just
a 10% shield saving and an extra point of move, in exchange for the extra
flexibility of being able to split the task force in two).

### Civil Aviation
### Flight Refuelling
### Buildings

Hub Airport (Sixties Airlift) is a useful smallwonder for your economy,
increasing tax output from 2x (airstrip + airport) to 3x, as well as
allowing additional trade routes (in theory two, but if ICAO has been
built then we hit the game's `MAX_TRADE_ROUTES=5` so only get one more).
This late in the game you're likely to have finished up the tech tree and
thus be running a mainly gold-generating economy, in which case the Hub
could end up yielding over 100 gold per turn, which buys a lot of units.
