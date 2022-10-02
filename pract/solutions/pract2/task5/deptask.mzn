int: ROOT=0;
set of int: menu = {100,110,120,130,140,150};
set of int: dropdown = {180,200,210,220,230};
set of int: icons = {100,200};

var int: menuitem;
var int: dropdownitem;
var int: iconsitem;

constraint forall (m in menu, d in dropdown, i in icons) (
  menuitem>=110 /\
  menuitem<=150 /\
  dropdownitem>=200 /\
  dropdownitem<=230 /\
  iconsitem=200
);

solve maximize menuitem+dropdownitem+iconsitem;
