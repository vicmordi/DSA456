  DSA456 – Lab 4: Sorting Algorithms – “Speed Is Found in the Minds of People”

Name: Victor Mordi


Part A – Questions
1. What sorting algorithm was the speaker trying to improve?

The speaker was trying to improve introsort, which is the sorting algorithm used in the C++ Standard Library (std::sort).
Introsort is a combination of three sorting algorithms: quicksort, heapsort, and insertion sort.
It starts with quicksort because it’s usually very fast, switches to heapsort when the data becomes hard to split, and finishes with insertion sort when only small sections are left to sort.
The goal was to make this mix work even faster on real computers.

2. At what partition size does Visual Studio use a simpler sort?

In Visual Studio’s version, when the part of the list being sorted becomes 32 elements or smaller, it switches from quicksort to insertion sort.
This is because quicksort is good for large data, but for very small lists, insertion sort is simpler and faster since it uses fewer steps and works well in memory.

3. At what partition size does GNU use a simpler sort?

In GNU’s version, the switch happens earlier at 16 elements.
So, when a part of the list has 16 or fewer items, it stops using quicksort and changes to insertion sort.
Both versions do this to save time when sorting small parts, because recursion and pivoting become slower when the list is small.

4. Why doesn’t binary search make insertion sort faster?

In theory, using binary search should help because it finds the right place to insert an element using fewer comparisons.
But in real life, it makes insertion sort slower.
Why? Because it adds more complicated if-else conditions, which confuse the CPU’s branch predictor.
The CPU can’t easily guess what happens next, so it wastes time fixing wrong guesses.
Also, insertion sort’s biggest cost isn’t finding the place to insert; it’s moving the elements to make space.
So binary search doesn’t actually help much.

5. What is branch prediction?

Branch prediction is how a CPU tries to guess which way a decision in the program will go.
For example, if the code says if (a > b):, the CPU tries to guess if that’s true or false before it actually checks.
If it guesses right, everything runs smoothly and fast.
If it guesses wrong, the CPU has to throw away some of the work it already did and restart that part, which slows everything down.
Good branch prediction = faster programs.
Bad prediction = wasted time.

6. What is informational entropy?

Informational entropy means how random or ordered your data is.
If the data is already sorted or almost sorted, it has low entropy — very predictable and easy for the CPU to handle.
If the data is completely mixed up, it has high entropy, and the CPU has to make more guesses about what comes next.
Higher entropy usually means more mistakes in prediction, so sorting takes longer.

7. What is unguarded_insertion_sort() and why is it faster?

Normally, insertion sort checks every time to make sure it doesn’t go past the start of the list.
unguarded_insertion_sort() removes that check because it knows that the smallest value is already at the beginning (called a “guard”).
Since it doesn’t need to keep checking boundaries, it avoids extra if statements.
That means fewer branch predictions and faster running code.
It’s called “unguarded” because it doesn’t guard itself with boundary checks anymore.

8. What does “incorporating conditionals into arithmetic” mean?

It means writing code that doesn’t use if statements, but instead uses math or logic to make decisions.
For example, instead of:

if a < b:
    swap(a, b)


You could use math tricks to swap without using if.
This helps the CPU because there are no “branches” to guess.
So, it just runs straight through the instructions, which is faster.

9. What was the bug in GNU’s version?

There was a small bug in the GNU version of the sort function.
It sometimes didn’t handle very small parts of the list correctly when switching from quicksort to insertion sort.
This caused some data to not be sorted properly or caused memory errors.
It showed how small mistakes in boundary conditions can create big problems in sorting algorithms.

10. Why can time go down even if moves and comparisons go up? What metric was missing?

The missing thing is branch misprediction rate.
Even if the algorithm does more moves and comparisons, it can still run faster if the CPU makes fewer mistakes guessing branches.
In other words, the number of operations doesn’t always tell the full story — how well the CPU predicts what happens next can matter even more.

11. What does “fast code is left-leaning” mean?

It means fast code has fewer conditionals and runs in a straight line.
In diagrams, branches usually go to the right — so fewer branches make the code “left-leaning.”
The fewer choices the CPU has to make, the easier it is for it to keep running smoothly.

12. What does “not mixing hot and cold code” mean?

“Hot code” is the part of a program that runs all the time, like the main loop.
“Cold code” only runs once in a while, like error handling.
If both are mixed together, the CPU’s memory cache can get confused and slow down.
Keeping hot and cold code separate makes it easier for the CPU to focus on the important parts and run them faster.

Part B – Reflection
1. What was hard to understand in the video?

The hardest part to understand was how CPU hardware affects the speed of sorting.
I didn’t know that something like branch prediction or cache memory could change how fast a sorting algorithm works.
It made me realize that writing fast code isn’t just about picking the best algorithm, but also about understanding how computers actually run the code.

2. What was most surprising to learn?

The most surprising thing was that doing more work can still be faster.
For example, some versions of sorting did more comparisons and swaps but still finished quicker because they had better branch prediction and cache use.
It showed me that the “number of steps” isn’t everything how the CPU processes those steps also matters a lot.

3. What ideas will you use to write faster code?

From this video, I learned a few practical lessons:

Try to write simple and straight code with fewer if statements.

Keep data organized so the CPU can read it in order (good for cache).

Think about real-world hardware, not just algorithms on paper.

And sometimes, even “weird” ideas like building a heap before insertion sort can actually make programs faster.