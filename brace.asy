import three;
import graph3;

size(6cm,0);

currentprojection=perspective(1*(2,2,2), up=Z);

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

transform3 T = rotate(45, Y);
transform3 S = rotate(45, Z);
transform3 R = rotate(45, X);
path3 brace = T*R*S*path3(brace((0,0), (0,5)));
draw(brace);

draw(-7X -- 7X, arrow=Arrow3(TeXHead2), L=Label("$x$", position=EndPoint, align=W));
draw(-7Y -- 7Y, arrow=Arrow3(TeXHead2), L=Label("$y$", position=EndPoint));
draw(-2Z -- 10Z, arrow=Arrow3(TeXHead2), L=Label("$z$", position=EndPoint));
