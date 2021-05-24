# `montyhall`

More code from  my own adventures trying to teach myself
how to write Python code.

I was interested in doing this in C and C++ not too long
ago, but as I'm sure you'll probably figure by looking
through the README files for my other projects... I haven't
gotten to that yet.

Anyway, the Monty Hall problem is a gameshow where you have
3 doors with a prize behind one of them (a car, probably)
and a goat or whatever behind the other two doors. The
point of the game is that you want the car. You select one
of the doors. Then host then opens another door,
revealing a goat. At this stage, do you switch doors? Or do
you stick with the same door? Let's find out what gives you
the best chance of success by simulating this scenario like
1000 times.

# Implementation

If you stick with the same door, you basically have a 1 in
3 chance of getting the right door, regardless of whether
another door is opened or not, so I just pick a random
door to put the prize and and pick another random door as
the door selection and see if the door numbers match.

If you switch doors, this means that there must be a random
selection for the prize door and the selection door. A
random number is selected until that number doesn't match
the prize door and doesn't match your selection, meaning
that it will lead to opening the door with the goat that
you haven't selected yet. You then keep selecting a random
door until it's not the door that was opened and not the
door that was your original selection, meaning that you
switch to the other unopened door. This is checked with the
prize door to see if they match.

Just as a curiosity experiment, I have 2 functions that run
the simulation. I call them in two different ways: firstly
by using a polymorphic programming paradigm, whereby the
the same door and switching door tests are called by using
two different subclasses. The other way is functional,
whereby the two test functions are passed as arguments to a
separate `run_function` that just calls the argument.

# Usage

Requires Python3.

``` shell
git clone https://github.com/caojohnny/montyhall.git
cd montyhall
python3 montyhall.py
```

# Demo

```
Using PolymorphicMontyHallTester...
Same Door Success Pct = 0.355
Change Door Success Pct = 0.674

Using FunctionalMontyHallTester...
Same Door Success Pct = 0.356
Change Door Success Pct = 0.683
```

The tests come up with the right numbers so I must have
done *something* right.

# Credits

Built with [PyCharm](https://www.jetbrains.com/pycharm/)
