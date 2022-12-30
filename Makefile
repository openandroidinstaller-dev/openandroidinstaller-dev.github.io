install:
	poetry install

style:
	cd mybulma && npm run css-build
	ls
	cp ./mybulma/css/mystyles.css ./static/style.css
	
website:
	poetry run python build.py
