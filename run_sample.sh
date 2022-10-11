while getopts i:o:d:p: flag
do
    case "${flag}" in
        i) input=${OPTARG};;
        o) output=${OPTARG};;
        d) database=${OPTARG};;
        p) threads=${OPTARG};;
    esac
done

threads=20

diamond blastx -d $database -q $input -k 1 -p $threads -o $output -f 6 ; sh ecn_map.sh $output
