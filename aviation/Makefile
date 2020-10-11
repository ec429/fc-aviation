# Makefile for aviation ruleset

all: units.ruleset

units.ruleset: units.pre makeunits.py techs.ruleset
	./makeunits.py < $< > $@

