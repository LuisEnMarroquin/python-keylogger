array=($(ls *.py))

echo ""

for var in "${array[@]}"; do
  echo " ---" $var
  pylint $var
done
