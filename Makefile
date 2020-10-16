# Top-level Makefile for aviation ruleset

VERSION := $(shell git describe --tags)

all: aviation

aviation: .FORCE
	make -C $@

release: aviation
	mkdir aviation-$(VERSION)
	cp -r aviation aviation-$(VERSION)/
	cp aviation.mpdl aviation.serv aviation.tilespec CREDITS LICENSE README.md aviation-$(VERSION)/
	tar -czvf aviation-$(VERSION).tgz aviation-$(VERSION)
	rm -r aviation-$(VERSION)

.FORCE:
