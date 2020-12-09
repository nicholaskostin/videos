import three;
import labelpath3;
import graph3;

defaultpen(fontsize(8pt));

size(6cm,0);

currentprojection=perspective(2*(6,-6,3), up=Z);

real innerangle = radians(60);
real outerangle = radians(70);
real midangle = radians(0);

path brace(pair a, pair b, real amplitude = 0.14*length(b-a)) {
    transform t = identity();
    real length = length(b-a);
    real sign = 1;
    if (amplitude < 0) {
        sign=-1;
    }
    path brace = (0,0){expi(sign*outerangle)} :: {expi(sign*midangle)} (length/4, amplitude/2) :: {expi(sign*innerangle)} (length/2, amplitude) {expi(-sign*innerangle)} :: {expi(-sign*midangle)}(3*length/4, amplitude/2) :: {expi(-sign*outerangle)} (length,0);
    real angle = degrees(atan2((b-a).y, (b-a).x));
    t = rotate(angle)*t;
    t = shift(a)*t;
    return t*brace;	
}

// draw coordinate axis
draw(-8X -- 8X, arrow=Arrow3(TeXHead2), L=Label("$x$", position=EndPoint));
draw(-8Y -- 8Y, arrow=Arrow3(TeXHead2), L=Label("$y$", position=EndPoint));
draw(-7Z -- 10Z, arrow=Arrow3(TeXHead2), L=Label("$z$", position=EndPoint, align=N));

// draw sphere
surface sphere = scale3(6.0)*unitsphere;
draw(sphere, palegray+opacity(.4));

// draw big R
draw(O -- (6*sin(pi/6)*cos(pi/4),6*sin(pi/6)*sin(pi/4),6*cos(pi/6)), black, L=Label("$R$", position=0.5, black+fontsize(8pt)));

// draw R*sin(theta)
draw((0,0,6*cos(pi/6)) -- (6*sin(pi/6)*cos(pi/4),6*sin(pi/6)*sin(pi/4),6*cos(pi/6)), black, L=Label("$R\sin{\theta}$", position=0.5, align=N, black+fontsize(4pt)));

// draw R*cos(theta)
draw((-0.1,-0.1,6*cos(pi/6)) -- (-0.1,-0.1,0), black, arrow=Arrows3(TeXHead2), L=Label(rotate(90, Y)*rotate(180, Z)*"$R\cos{\theta}$", position=0.5, filltype=Fill(white), align=N, black+fontsize(4pt)));

// draw theta arc
draw(arc(c=O, (1*sin(pi/6)*cos(pi/4),1*sin(pi/6)*sin(pi/4),1*cos(pi/6)), Z), black, L=Label("$\theta$", position=0.5, align=N));

// draw vector r
draw((6*sin(pi/6)*cos(pi/4),6*sin(pi/6)*sin(pi/4),6*cos(pi/6)) -- (0,0,9), arrow=Arrow3(), L=Label("$\vec{r}$", position=0.5, align=NE));

// label z
// draw((-0.4,-0.4,0) -- (-0.4,-0.4,9), L=Label("$z$", align=E, position=0.5, filltype=Fill(white)), arrow=Arrows3(TeXHead2));
transform3 T = rotate(90, X);
transform3 S = rotate(90, Y);
path3 brace = T*S*path3(brace((0,0), (0,9)));
draw(brace);
label("$z$", position=midpoint(brace), align=W);
