La monadologie
==============

A rough 'n ready introduction to monads in Python.

Refactoring to monads
---------------------

Monads can be confusing, despite being a relatively simple concept. This can be seen by
[the proliferation of monad tutorials](http://www.haskell.org/haskellwiki/Monad_tutorials_timeline),
employing florid metaphors from burritos to space suits.

Learning monads by studying the formal definition and monad laws can be intimidating, as
satirised by the famous saying:

> A monad is just a monoid in the category of endofunctors.
>
> What's the problem?

I think the best way to approach monads is by refactoring subtly repetitive code until monadic
abstractions naturally reveal themselves. In this repository is some Python code where I attempt
to do just that.

Formalities
-----------

Once the concept has taken root, here are the ingredients of a well-behaved monad that will
help you play nicely with existing functions and description:
* A constructor function that turns a regular value into a monadic one, usually called _unit_ or _return_.
* A function that applies a function to a monadic value returns a new monadic value, usually called _bind_.
* Conformance to [a couple of mathematical laws](http://www.haskell.org/haskellwiki/Monad_laws), which enables code that works with all monads.
* Nice syntax (optional).
