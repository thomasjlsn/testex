PREFIX ?= /usr/local

install:
	@cp -v testex.py $(PREFIX)/bin/testex
	@chmod -v 555 $(PREFIX)/bin/testex

uninstall:
	@rm -v $(PREFIX)/bin/testex
