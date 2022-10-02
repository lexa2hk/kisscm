include "all_different.mzn";

set of int: DIGIT = 0..9;

var DIGIT: A;
var DIGIT: B;
var DIGIT: C;

var DIGIT: D;
var DIGIT: E;
var DIGIT: F;


array[1..6] of var DIGIT: digits = [A, B, C, D, E, F];

constraint A + B + C = D + E + F;

constraint all_different(digits);

solve minimize A+B+C;