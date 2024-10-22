C_NAME := new_publisher
C_CODE := src/pysv/c_package/$(C_NAME).c
bin := .venv/bin


install-dev:
	python3 -m venv .venv
	$(bin)/python -m pip install uv
	$(bin)/uv pip install -e .[dev]

.PHONY: build
build: $(C_CODE)
	cc -c $(C_CODE) -o $(C_NAME)

.PHONY: run
run:
	sudo PYSV_INTERFACE=$(iface) nice -n -20 .venv/bin/python -m pysv -debug

.PHONY: clean
clean: $(C_NAME)
	rm $(C_NAME)
