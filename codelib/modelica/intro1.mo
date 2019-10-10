model FirstOrderInitial "First order equation with initial value"
Real x "state variable";
initial equation
x = 2 "Used before simulation to compute intial values";
equation 
der(x) = 1-x "Drives value of x toward 1,0";
end FirstOrderInitial;