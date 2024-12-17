all: install
install:
	@echo "Installing dependencies..."
	@bash install.sh
run:
	@echo "Running Doble Shortener..."
	@python3 main.py
clear:
	@clear