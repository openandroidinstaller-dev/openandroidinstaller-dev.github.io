install:
	poetry install

style:
	cd mybulma && npm run css-build
	ls
	cp ./mybulma/css/mystyles.css ./public/static/style.css
	
website:
	poetry run python build.py
