# Makefile for Doble Shortener Tool

# Default target
all: install

# Install dependencies
install:
	@echo "Installing dependencies..."
	@bash install.sh

# Run the tool
run:
	@echo "Running Doble Shortener..."
	@python3 main.py

# Clean the terminal screen
clear:
	@clear