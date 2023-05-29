#! /usr/bin/bash

greeting=Hello
name=Tux

echo $greeting $name

expr 16 / 4
expr 20 - 10
expr 10 + 10

var=$(( 10 + 25 ))
echo $var

echo "scale=2; 22/7" | bc

echo "Enter a number"
read a
echo "Enter another number"
read b
echo "The sum of $a and $b is:"
sum=$(( $a + $b ))
echo $sum


read -p "Enter your name: " name
echo "Hello $name, welcome to my program"

read -p "Enter your age: " age
days=$[ $age * 365 ]
echo "That makes you over $days days old!"

if [ $age -ge 18 ]
then
    echo "You may go to the party."
elif [ $age -lt 18 ] && [ $age -gt 10 ]
then
    echo "You may go to the party but be back before midnight."
else
    echo "You may not go to the party."
fi

for i in {1..10}
do
    echo "Iteration number: $i"
done

for x in cyan magenta yellow black
do
    echo $x
done
