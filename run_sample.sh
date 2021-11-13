if [ ! -f $1 ]; then
    echo "File" $1 " not found!";exit
fi

if [ ! -f $2 ]; then
    echo "File" $2 " not found!";exit
fi

diamond blastx -d $1 -q $2 -k 1 -p 20 -o $3 -f 6 ; ./ecn_map.sh $3
