### Wheel


I call this repo the *wheel* repo, because I'm reinventing the wheel, ie, coding out implementations to major algorithms, to improve my programming skills.

#### MergeSort

There are two algorithms for mergesort to work. One is recursive, and goes like this:
1. if list is just one element long, then return the list
2. split the list given into two halves of equal (or as equal as possible) length
3. sort both using mergesort
4. merge the sorted algorithms


Then, we had the merge algorithm, which required some more gymnastics:
1. we take two lists
2. create an empty list, that'll be your finished, sorted product.
3. while both lists are not empty, compare the first elements of each list, Add whichever is smaller to the empty list, and remove it from the main list.
4. Once one list is empty, add the other one to the final list.


And that's how its done.
