oldIFS=$IFS
IFS=$'\n'

course="vetcyb24p2"
seminar_date=${1}
file=${2}

teachers="(dbosk|masvanbe|elzen)@kth.se"

get_grade_data() {
  tail -n +2 ${file} \
    | grep -Ev "${teachers}" \
    | cut -d, -f 2,3,5 \
    > participation-seminar.csv

  for user in $(cat participation-seminar.csv | cut -d, -f 1 | sort -u)
  do
    echo -n "$user ";
    sum_minutes=0;
    for minutes in $(grep $user participation-seminar.csv | cut -d, -f 3)
    do
      sum_minutes=$(($sum_minutes + $minutes));
    done;
    echo $sum_minutes;
  done
}

open ${file} &
get_grade_data
read -p "Enter the limit in minutes: " limit_minutes

for result in $(get_grade_data)
do
  user=$(echo $result | cut -d ' ' -f 1);
  minutes=$(echo $result | cut -d ' ' -f 2);
  if [ $minutes -ge $limit_minutes ]
  then
    canvaslms grade -c ${course} -a "Live seminar ${seminar_date}" \
      -u $user -g complete
  else
    canvaslms grade -c ${course} -a "Live seminar ${seminar_date}" \
      -u $user -g incomplete \
      -m "You had $minutes minutes of participation out of more than $limit_minutes minutes."
  fi
done
