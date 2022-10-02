set of int: target = {0,100,200};
set of int: shared = {0,100,200};
set of int: foo = {0,100,110};
set of int: left = {0,100};
set of int: right = {0,100};
int: root = 100;

var int: tar;
var int: sha;
var int: fo;
var int: lef;
var int: rig;

constraint (if sha = 100 then tar = 100 endif);
constraint (if rig = 100 then sha <=200 endif);
constraint (if lef = 100 then sha >=100 endif);
constraint (if fo = 110 then lef = 100 endif);
constraint (if fo = 110 then rig=100 endif);
constraint (fo = 100 /\ tar = 200);

solve satisfy;