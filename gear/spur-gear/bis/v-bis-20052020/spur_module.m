%algorithm: Finds module of spur gear from preferred series by iteration
%author: Atharv Darekar
clear;
clc;
mi=[1,1.125,1.25,1.375,1.5,1.75,2,2.25,2.5,2.75,3,3.5,4,4.5,5,5.5,6,6.5,7,8,9,10,11,12,14,16,18,20,22,25,28,32,36,40,45,50]; %specified values of module
Sutp=input("Enter ultimate tensile strength of pinion N.mm^-2\n"); %ultimate tensile strength of pinion N.mm^-2
Sutg=input("Enter ultimate tensile strength of gear N.mm^-2\n"); %ultimate tensile strength of gear N.mm^-2
Ep=input("Enter modulus of elasticity of pinion N.mm^-2\n"); %modulus of elasticity of pinion N.mm^-2
Eg=input("Enter modulus of elasticity of gear N.mm^-2\n"); %modulus of elasticity of gear N.mm^-2
zp=input("Enter pinion teeth\n"); %pinion teeth
zg=input("Enter gear teeth\n"); %gear teeth
for i=1:12 
  fprintf("For Grade %d Enter %d\n",i,i);
endfor
grade=input("Enter grade of gear\n"); %grade of gear
fprintf("Enter 1 for 14.5 degree full depth involute tooth\n");
fprintf("Enter 2 for 20 degree full depth involute tooth\n");
fprintf("Enter 3 for 20 degree stub involute tooth\n");
y=input("Select type of gear\n"); %Lewis form factor
P=input("Enter power transmitted by gear W\n"); %power transmitted by gear W
Np=input("Enter speed of pinion rpm\n"); %speed of pinion rpm
Q=input("Enter 1 for internal gearing\nEnter 2 for external gearing\n"); %type of gearing
switch (Q)
  case 1
  Q=(2*(zg/zp))/((zg/zp)-1);
  case 2
  Q=(2*(zg/zp))/((zg/zp)+1);
endswitch
FOSr=input("Enter factor of safety\n"); %factor of safety required
cs=input("Enter service factor\n"); %service factor
sigmabp=1/3*Sutp; %allowable bendig stress of pinion N.mm^-2
sigmabg=1/3*Sutg; %allowable bendig stress of gear N.mm^-2
switch (y) 
  case 1
    yp=0.124-(0.684/zp); 
    yg=0.124-(0.684/zg);
    alpha=14.5; %pressure angle degree
    k=0.107;
  case 2
    yp=0.154-(0.912/zp);
    yg=0.154-(0.912/zg);
    alpha=20; %pressure angle degree
    k=0.111;
  case 3
    yp=0.175-(0.95/zp);
    yg=0.175-(0.95/zg);
    alpha=20; %pressure angle degree
    k=0.115;
endswitch
c=k/((1/Ep)+(1/Eg));
FOS=0; %factor of safety available
i=1; %counter variable for module row matrix 
while (FOSr>=FOS)
  [Fap, Fag, FOS, Fd]=spur_load(mi(i),sigmabp,sigmabg,yp,yg,zp,zg,Np,P,grade,c,cs); %function call to calculate bendig load and effective load iteratively for each module in preferred series
  i++;
endwhile
[Fap, Fag, FOS, Fd]=spur_load(mi(i-1),sigmabp,sigmabg,yp,yg,zp,zg,Np,P,grade,c,cs); %function call to calculate bendig load and effective load for the required module
Fw=Fd*FOSr;
sigmab=sqrt((Fw/(10*zp*(mi(i-1)^2)*Q))*(1.4/(sind(alpha)*cosd(alpha)*((1/Ep)+(1/Eg)))));
BHN=sigmab/2.65;
fprintf("The Effective Load on gear pair is %d N\n",Fd);
fprintf("The Bending Load Capacity of pinion is %d N\n",Fap);
fprintf("The Bending Load Capacity of gear is %d N\n",Fag);
fprintf("The Wear Load Capacity of gears is %d N\n",Fw);
fprintf("The required case hardening of gears is %d BHN\n",BHN);
fprintf("The module of gears is %d mm\n",mi(i-1));
fprintf("Available factor of safety is %d\n",FOS);