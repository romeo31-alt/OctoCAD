%program: Input and outpute manager
%author: Atharv Darekar
clear;
clc;
load /home/ubuntu/.OctoCAD/spur-gear/user_input_design.txt; %loads the data collected by the Gui.py program into the memory
cd /home/ubuntu/OctoCAD/bis/gear/spur-gear/; %changes the current working directory to v-bis-20200602
[Fd, Fap, Fag, Fw, BHN, m, FOS, zp, zg] = spur_module (Sutp,Sutg,Ep,Eg,zp,zg,grade,y,P,Np,Q,FOSr,cs); %calls spur_module function
result_f=fopen("/home/ubuntu/.OctoCAD/spur-gear/result.txt","w"); %creates or overwrites the result.txt file
fprintf(result_f,"Fd=%d\nFap=%d\nFag=%d\nFw=%d\nBHN=%d\nm=%d\nFOS=%d\nzp=%d\nzg=%d",Fd,Fap,Fag,Fw,BHN,m,FOS,zp,zg); %prints the design data to the result file
fclose(result_f); %closes the result.txt file
