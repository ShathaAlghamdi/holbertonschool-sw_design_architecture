#!/usr/bin/env python3
"""Decorator pattern example with a caramel wrapper."""


class Beverage:
    """Base beverage interface."""

    def cost(self):
        """Return the beverage cost."""
        raise NotImplementedError

    def description(self):
        """Return the beverage description."""
        raise NotImplementedError


class Coffee(Beverage):
    """A basic coffee."""

    def cost(self):
        """Return the base coffee cost."""
        return 50

    def description(self):
        """Return the base coffee description."""
        return "Coffee"


class MilkDecorator(Beverage):
    """Add milk to a beverage."""

    def __init__(self, inner):
        self._inner = inner

    def cost(self):
        """Add the milk cost."""
        return self._inner.cost() + 10

    def description(self):
        """Add milk to the description."""
        return self._inner.description() + " + milk"


class SugarDecorator(Beverage):
    """Add sugar to a beverage."""

    def __init__(self, inner):
        self._inner = inner

    def cost(self):
        """Add the sugar cost."""
        return self._inner.cost() + 5

    def description(self):
        """Add sugar to the description."""
        return self._inner.description() + " + sugar"


class CaramelDecorator(Beverage):
    """Add caramel to a beverage."""

    def __init__(self, inner):
        self._inner = inner

    def cost(self):
        """Add the caramel cost."""
        return self._inner.cost() + 15

    def description(self):
        """Add caramel to the description."""
        return self._inner.description() + " + caramel"


def main():
    """Run the Decorator example."""
    coffee_with_milk = MilkDecorator(Coffee())
    print(coffee_with_milk.description(), coffee_with_milk.cost())

    coffee_with_sugar_and_milk = MilkDecorator(SugarDecorator(Coffee()))
    print(
        coffee_with_sugar_and_milk.description(),
        coffee_with_sugar_and_milk.cost()
    )

    coffee_with_caramel = CaramelDecorator(
        MilkDecorator(SugarDecorator(Coffee()))
    )
    print(coffee_with_caramel.description(), coffee_with_caramel.cost())


if __name__ == "__main__":
    main()
