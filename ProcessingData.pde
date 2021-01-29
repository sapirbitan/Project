import shapes3d.*;
import shapes3d.contour.*;
import shapes3d.org.apache.commons.math.*;
import shapes3d.org.apache.commons.math.geometry.*;
import shapes3d.path.*;
import shapes3d.utils.*;

String[] lines;
ArrayList<SphereLoc > spheres;
HashMap hm = new HashMap(); 
int index = 0;
int x,y,id,pid,i=0;
int z=25;
int r,g,b;

void setup() 
{
  background(255);
  size(1000, 1000,P3D);
  frameRate(50);
  lines = loadStrings("positions1.txt");
  spheres = new ArrayList<SphereLoc>();
  noStroke();
}

void draw() 
{
  lights();
  if (index < lines.length)
  {
    String[] pieces1 = split(lines[index], '\t');
    index = index + 1;
    if (pieces1.length == 4)
    {
      x = int(pieces1[0]) ;
      y = int(pieces1[1]) ;
      id=int(pieces1[2]);
      pid=int(pieces1[3]);
      if (!hm.containsKey(pid))
       {
          update();
          hm.put(pid,1);
       } 
       for (int i = 0; i <spheres.size(); i++) 
       { 
         if(spheres.get(i).pid==pid)
         {
           if(spheres.get(i).id==0||spheres.get(i).id==1||spheres.get(i).id==2||spheres.get(i).id==3)
           {
             print("x: ",spheres.get(i).x=x );
             print(" y: ",spheres.get(i).y=y );
             print("\n");
             spheres.get(i).move();
           }
           print("x: ",spheres.get(i).x=x );
           print(" y: ",spheres.get(i).y=y );
           print("\n");
         }
         spheres.get(i).render();
       }
    }
  }
}

void update()
{
  if(id==0)
  {
    spheres.add(new SphereLoc(x,y,id,85,211,247,pid,z));
  }
   else if(id==1)
   {
     spheres.add(new SphereLoc(x,y,id,247,242,85,pid,z));
   }
   else if(id==2)
   {
     spheres.add(new SphereLoc(x,y,id,28,131,53,pid,z));
   }
   else if(id==3)
   {
     spheres.add(new SphereLoc(x,y,id,232,86,70,pid,z));
   }
   else if(id==4)
   {
     spheres.add(new SphereLoc(x,y,id,114,233,245,pid,z));
   }
   else
   {
     spheres.add(new SphereLoc(x,y,id,21,61,203,pid,10));
   }
}

class SphereLoc  
{  
  float x, y ,z;
  int r,g,b,id,pid;
  SphereLoc(float x_,float y_,int id_, int r_, int g_, int b_,int pid_, int z_)
  {
    x=x_;
    y=y_;
    id=id_;
    r=r_;
    g=g_;
    b=b_;
    pid=pid_;
    z=z_;
  }
  
  void move()
  {
    if(spheres.get(i).x!=x && spheres.get(i).y!=y)
    {
      spheres.get(i).x=x;
      spheres.get(i).y=y;
    }
  }
  void render()
  {
    translate(x, y, 0);
    fill(r,g,b);
    sphere(z);
    translate(-x, -y, 0);
  }
}
