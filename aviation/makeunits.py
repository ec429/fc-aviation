#!/usr/bin/python2
import sys
import re

getvs = re.compile(r'_?\(?"([^"]+)"\)?')

class Unit(object):
    def __init__(self, key):
        self.key = key
        self.tech = None
        self.flags = None
        self.ph = None
        self.rest = dict()
    def __getitem__(self, key):
        return self.rest[key]
    def get(self, key, default=None):
        return self.rest.get(key, default)
    def __setitem__(self, key, value):
        self.rest[key] = value
    def __delitem__(self, key):
        del self.rest[key]
    def process(self):
        if self.get('no_veteran'):
            # This unit has no veteran levels (level name is never displayed)
            del self['no_veteran']
            self['veteran_names'] = '_("green")'
            self['veteran_base_raise_chance'] = '0'
            self['veteran_work_raise_chance'] = '0'
            self['veteran_power_fact'] = '100'
            self['veteran_move_bonus'] = '0'
        if self.get('slow_veteran'):
            # Ground/sea units don't get acespeed, but can still achieve
            # veteran levels for combat purposes.
            del self['slow_veteran']
            self['veteran_names'] = '_("green"), _("veteran"), _("ace"), _("elite")'
            self['veteran_base_raise_chance'] = '30, 15, 10, 0'
            self['veteran_work_raise_chance'] = '0, 0, 0, 0'
            self['veteran_power_fact'] = '100, 150, 160, 200'
            self['veteran_move_bonus'] = '0, 0, 0, 0'
        targets = set(str.split(self.get('targets', ''), ','))
        if '"AntiGround"' in self.flags:
            targets.add('"Land"')
            targets.add('"Assault"')
        if '"AntiSea"' in self.flags:
            targets.add('"Sea"')
        if '"AntiAir"' in self.flags:
            targets.add('"Air"')
            targets.add('"Carrier-borne"')
            targets.add('"Missile"')
            targets.add('"Seaplane"')
            targets.add('"Glider"')
            targets.add('"Helicopter"')
        targets.discard('')
        if targets:
            self['targets'] = ', '.join(list(targets))
        upkeep = self['uk_base']
        del self['uk_base']
        self['uk_shield'] = upkeep
        self['uk_gold'] = upkeep
    def writekey(self, f, k, v):
        f.write('%s = %s\n' % (k.ljust(16), v))
    def write(self, f):
        f.write('\n')
        f.write(self.key+'\n')
        self.writekey(f, 'tech_req', '"%s"' % (self.tech.name if self.tech else None,))
        self.writekey(f, 'flags', self.flags)
        if self.ph is not None:
            f.write(';phcode=%s\n' % (self.ph,))
        for k in sorted(self.rest):
            self.writekey(f, k, self.rest[k])

def getunits(f, techs):
    curr = None
    units = {}
    raw = []
    cont = None

    for line in f.readlines():
        line = line.rstrip()
        if cont:
            line = cont + line
        if line and line[-1] == '\\':
            cont = line[:-1]
            continue
        cont = None
        if line.startswith('[unit_'):
            if curr:
                units[curr.key] = curr
            curr = Unit(line)
            continue
        if not curr:
            raw.append(line)
            continue
        if '=' not in line:
            continue
        key, _, value = line.partition('=')
        key = key.strip()
        value = value.strip()
        m = getvs.match(value)
        vs = m.group(1) if m else None
        if key == 'tech_req':
            curr.tech = techs[vs]
        elif key == 'flags':
            curr.flags = value
        elif key == ';phcode':
            curr.ph = value
        else:
            curr.rest[key] = value
    if curr:
        units[curr.key] = curr
    return units, raw

def procunits(units):
    for u in units.values():
        u.process()

def sortunits(units):
    def nreqs(u):
        if units[u].tech:
            return 1 + len(units[u].tech.allreqs)
        return 0
    return sorted(units, key=nreqs)

class Tech(object):
    def __init__(self):
        self.name = None
        self.preqs = []
    @property
    def allreqs(self):
        r = []
        for p in self.preqs:
            r.append(p)
            r.extend(p.allreqs)
        return set(r)

def gettechs(f):
    curr = None
    techs = {'None': None}
    for line in f.readlines():
        line = line.rstrip()
        if line.startswith('[advance_'):
            if curr:
                techs[curr.name] = curr
            curr = Tech()
            continue
        if not curr:
            continue
        if '=' not in line:
            continue
        key, _, value = line.partition('=')
        key = key.strip()
        value = value.strip()
        m = getvs.match(value)
        vs = m.group(1) if m else None
        if key == 'name':
            curr.name = vs
        elif key in ('req1', 'req2'):
            if vs != 'None':
                curr.preqs.append(techs[vs])
    if curr:
        techs[curr.name] = curr
    return techs

def main(f):
    techs = gettechs(open('techs.ruleset', 'r'))
    units, raw = getunits(f, techs)
    procunits(units)
    for r in raw:
        print r
    for u in sortunits(units):
        units[u].write(sys.stdout)

if __name__ == '__main__':
    main(sys.stdin)
