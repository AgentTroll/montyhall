import random as r

NUM_ROUNDS = 1000
NUM_DOORS = 3


def same_door():
    successes = 0
    for i in range(0, NUM_ROUNDS):
        prize_door = r.randint(1, NUM_DOORS)
        selection_door = r.randint(1, NUM_DOORS)

        if prize_door == selection_door:
            successes += 1

    print("Same Door Success Pct = " + str(successes / NUM_ROUNDS))


def change_door():
    successes = 0
    for i in range(0, NUM_ROUNDS):
        prize_door = r.randint(1, NUM_DOORS)
        selection_door = r.randint(1, NUM_DOORS)

        while True:
            opened_door = r.randint(1, NUM_DOORS)
            if opened_door != prize_door and opened_door != selection_door:
                break

        while True:
            new_selection = r.randint(1, NUM_DOORS)
            if new_selection != selection_door and new_selection != opened_door:
                selection_door = new_selection
                break

        if prize_door == selection_door:
            successes += 1

    print("Change Door Success Pct = " + str(successes / NUM_ROUNDS))


def run_function(function):
    function()


class MontyHallTester:
    def test(self):
        raise NotImplementedError("Unsupported operation")


class PolymorphicMontyHallTester(MontyHallTester):
    class SameDoorTester(MontyHallTester):
        def test(self):
            same_door()

    class ChangeDoorTester(MontyHallTester):
        def test(self):
            change_door()

    def test(self):
        same_door_tester = PolymorphicMontyHallTester.SameDoorTester()
        same_door_tester.test()

        change_door_tester = PolymorphicMontyHallTester.ChangeDoorTester()
        change_door_tester.test()


class FunctionalMontyHallTester(MontyHallTester):
    def test(self):
        run_function(same_door)
        run_function(change_door)


print("Using PolymorphicMontyHallTester...")
polymorphic_monty_hall_tester = PolymorphicMontyHallTester()
polymorphic_monty_hall_tester.test()

print("")

print("Using FunctionalMontyHallTester...")
functional_monty_hall_tester = FunctionalMontyHallTester()
functional_monty_hall_tester.test()
