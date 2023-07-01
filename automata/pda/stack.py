#!/usr/bin/env python3
"""Classes and methods for working with PDA stacks."""

import collections


class PDAStack(collections.namedtuple('PDAStack', ['stack'])):
    """A PDA stack."""

    def __new__(cls, *elements):
        """Create the new PDA stack."""
        stack = tuple(elements[0]) if len(elements) == 1 else elements
        return super(PDAStack, cls).__new__(cls, stack)

    def top(self):
        """Return the symbol at the top of the stack."""
        return self.stack[-1] if self.stack else ''

    def pop(self):
        """
        Pop the stack top from the stack.

        Return a new PDAStack with the new content.
        """
        stack_contents = list(self.stack)
        stack_contents.pop()
        return self.__class__(stack_contents)

    def replace(self, symbols):
        """
        Replace the top of the stack with the given symbols.

        Return a new PDAStack with the new content.
        The first symbol in the given sequence becomes the new stack top.
        """
        stack_contents = list(self.stack)
        stack_contents.pop()
        stack_contents.extend(reversed(symbols))
        return self.__class__(stack_contents)

    def __len__(self):
        """Return the number of symbols on the stack."""
        return len(self.stack)

    def __iter__(self):
        """Return an interator for the stack."""
        return iter(self.stack)

    def __repr__(self):
        """Return a string representation of the stack."""
        return f'{self.__class__.__name__}{self.stack}'
