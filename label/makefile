tr:
	rm -rf ./input || echo "input doesn't exist."
	mkdir input
	cp ./train/* ./input
	#may already have some labels
	cp ./train_out/* ./output/YOLO_darknet || echo "no labels"
	python3 main.py
	mv ./output/YOLO_darknet/* ./train_out
	tree ./train_out
te:
	rm -rf ./input || echo "input doesn't exist."
	mkdir ./input
	cp ./test/* ./input
	python3 main.py
	mv ./output/YOLO_darknet/* ./test_out
	tree ./test_out
v:
	rm -rf ./input || echo "input doesn't exist."
	mkdir ./input
	cp ./val/* ./input
	python3 main.py
	mv ./output/YOLO_darknet/* ./val_out
	tree ./val_out
