mkdir train || echo "train exists"
mkdir test || echo "test exists."
mkdir val || echo "val exists."

for i in kea takahe tui kea_aug takahe_aug tui_aug ;
do 
    mv ./train/$i/* ./train/
    mv ./test/$i/* ./test/
    mv ./val/$i/* ./val/
    rmdir ./train/$i
    rmdir ./test/$i
    rmdir ./val/$i
done

mkdir ../label/main/train || echo "label train exists"
mkdir ../label/main/test || echo "label test exists"
mkdir ../label/main/val || echo "label val exists"
cp ./train/* ../label/main/train
cp ./test/* ../label/main/test
cp ./val/* ../label/main/val
