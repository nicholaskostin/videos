import three;
import graph3;
// don't be a brainlet

defaultpen(fontsize(8pt));

size(6cm,0);

currentprojection=perspective(1.0*(1.5,-0.7,0.2), up=Z);

// draw the conducting sphere
surface conductor = scale3(3.0)*unitsphere;
draw(conductor, surfacepen=white+opacity(0.4));
draw((0,0,0) -- (3*sin(pi/4)*cos(pi/4),3*sin(pi/4)*sin(pi/4),3*cos(pi/4)), arrow=Arrow3, black, L=Label("$a$", position=0.8));

// draw slightly bent E field lines
real[] phi1 = {pi/4, 3*pi/4, 5*pi/4, 7*pi/4};
for (real phi : phi1)
{
    // draw((8*sin(7*pi/9)*cos(phi),8*sin(7*pi/9)*sin(phi),8*cos(7*pi/9)) .. (7*sin(7*pi/9)*cos(phi),7*sin(7*pi/9)*sin(phi),7*cos(7*pi/9)) .. (3*sin(pi/2)*cos(phi),3*sin(pi/2)*sin(phi),3*cos(pi/2)) .. (7*sin(2*pi/9)*cos(phi),7*sin(2*pi/9)*sin(phi),7*cos(2*pi/9)) .. (8*sin(2*pi/9)*cos(phi),8*sin(2*pi/9)*sin(phi),8*cos(2*pi/9)));
    draw((8*sin(7*pi/9)*cos(phi),8*sin(7*pi/9)*sin(phi),8*cos(7*pi/9)) .. (8*sin(7*pi/9)*cos(phi),8*sin(7*pi/9)*sin(phi),8*cos(7*pi/9)+1) .. (4*sin(pi/2)*cos(phi),4*sin(pi/2)*sin(phi),4*cos(pi/2)) .. (8*sin(2*pi/9)*cos(phi),8*sin(2*pi/9)*sin(phi),8*cos(2*pi/9)-1) .. (8*sin(2*pi/9)*cos(phi),8*sin(2*pi/9)*sin(phi),8*cos(2*pi/9)));
}

// draw not at all bent E field lines
real[] phi2 = {0, pi/2, pi, 3*pi/2};
//for (real phi : phi2)
//{
    //draw((12*sin(7*pi/9)*cos(phi),12*sin(7*pi/9)*sin(phi),12*cos(7*pi/9)) -- (12*sin(7*pi/9)*cos(phi),12*sin(7*pi/9)*sin(phi),12*cos(7*pi/9)+19));
//}

// draw heavily bent E field lines
real[] phi0 = {0, pi/2, pi, 3*pi/2};
for (real phi : phi0)
{
    draw((3.2*sin(7*pi/9)*cos(phi),3.2*sin(7*pi/9)*sin(phi),3.2*cos(7*pi/9)-3.5) .. (3.2*sin(7*pi/9)*cos(phi),3.2*sin(7*pi/9)*sin(phi),3.2*cos(7*pi/9)-2.5) .. (3*sin(7*pi/9)*cos(phi),3*sin(7*pi/9)*sin(phi),3*cos(7*pi/9)-1.2) .. (3*sin(17*pi/20)*cos(phi),3*sin(17*pi/20)*sin(phi),3*cos(17*pi/20)));

    draw((3*sin(3*pi/20)*cos(phi),3*sin(3*pi/20)*sin(phi),3*cos(3*pi/20)) .. (3*sin(2*pi/9)*cos(phi),3*sin(2*pi/9)*sin(phi),3*cos(2*pi/9)+1.2) .. (3.2*sin(2*pi/9)*cos(phi),3.2*sin(2*pi/9)*sin(phi),3.2*cos(2*pi/9)+2.5) .. (3.2*sin(2*pi/9)*cos(phi),3.2*sin(2*pi/9)*sin(phi),3.2*cos(2*pi/9)+3.5));
}
