#!bash/bin

myfile=$1
permission=0
shift
for i in "$@"
do 
  if [ "$i" == "read" ]
  then
    permission=$(($permission + 100))
  fi

  if [ "$i" == "write" ]
  then
    permission=$(($permission + 200))
  fi

  if [ "$i" == "execute" ]
  then
   permission=$(($permission + 400))
  fi
done

chmod $permission $myfile




