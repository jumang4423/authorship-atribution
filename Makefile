# resolve dependencies
install:
	pip3 install -r requirements.txt

# to predict who write a given text by pipeline
run:
	python3 main.py

# show coverage of correctness
test:
	python3 main.test.py