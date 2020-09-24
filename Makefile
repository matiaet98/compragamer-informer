VERSION := $(shell git describe --abbrev=0 --tags)
ACCOUNT := matiaet98
APP := compragamer
IMAGE := $(ACCOUNT)/$(APP)

build:
	docker build -t $(IMAGE):$(VERSION) .
	docker tag $(IMAGE):$(VERSION) $(IMAGE):latest
