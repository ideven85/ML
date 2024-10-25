t turns out that this is a good pattern to follow when designing a program from scratch. In test-first programming, you write the spec and the tests before you even write any code. The development of a single function proceeds in this order:

1) Spec: Write a specification for the function.
Test: Write tests that exercise the specification.
Implement: Write the implementation.
Systematic testing
Rather than exhaustive, haphazard, or randomized testing, we want to test systematically. Systematic testing means that we are choosing test cases in a principled way, with the goal of designing a test suite with three desirable properties:

Correct. A correct test suite is a legal client of the specification, and it accepts all legal implementations of the spec without complaint. This gives us the freedom to change how the module is implemented internally without necessarily having to change the test suite.

Thorough. A thorough test suite finds actual bugs in the implementation, caused by mistakes that programmers are likely to make.

Small. A small test suite, with few test cases, is faster to write in the first place, and easier to update if the specification evolves. Small test suites are also faster to run. You will be able to run your tests more frequently if your test suites are small and fast.