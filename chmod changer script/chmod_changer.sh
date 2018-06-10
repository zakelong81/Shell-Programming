#!bash/bin

echo "Enter the name of the file > "
read myfile
echo "Do you want to allow read permission? > "
read read_p
echo "Do you want to allow write permission? > "
read write_p
echo "Do you want to allow execute permission? > "
read execute_p

permission=0

  if [ "$read_p" == "yes" ]
  then
    permission=$(($permission + 100))
  fi

  if [ "$write_p" == "yes" ]
  then
    permission=$(($permission + 200))
  fi

  if [ "$execute_p" == "yes" ]
  then
   permission=$(($permission + 400))
  fi


chmod $permission $myfile




