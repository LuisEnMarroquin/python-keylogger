rm -rf dist/
rm -rf build/
rm -rf __pycache__/

array=($(ls *.spec))
for var in "${array[@]}"
do rm $var
done
