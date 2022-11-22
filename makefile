all:
	#run to download
	#array of bird files
	# ./input/bird_class
	python3 download_birds.py
	python3 data_aug.py
	bash move_dirs.sh
move:
	#move to the labelling directory
	rm -rf ../OpenLabeling-master/main/train
	rm -rf ../OpenLabeling-master/main/test
	rm -rf ../OpenLabeling-master/main/val
	cp -r ./train ../OpenLabeling-master/main/
	cp -r ./test ../OpenLabeling-master/main/
	cp -r ./val ../OpenLabeling-master/main/
	tree ../OpenLabeling-master/main/
