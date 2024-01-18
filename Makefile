.PHONY: help install style website

help:
	@echo "help - show this help"
	@echo "install - install dependencies"
	@echo "style - build css"
	@echo "website - build website"

install:
	poetry install

style:
	cd mybulma && npm run css-build
	ls
	cp ./mybulma/css/mystyles.css ./static/style.css
	
website:
	poetry run python build.py
