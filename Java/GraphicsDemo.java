import java.applet.Applet;
import java.awt.*;

public class GraphicsDemo extends Applet
{
	public void paint(Graphics g)
	{  // set font color

		g.setColor(Color.red);
		g.drawString("W",50, 50); // display text
		g.drawLine(120,120,200,300); 		
		// draw and fill rectangle
		// draw a line
		g.drawRect(170,100,60,50);
		g.fillRect(170,100,60,50);
		// draw and fill rounded rectangle
		g.drawRoundRect(190, 10, 60, 50, 15, 15);
		g.fillRoundRect(190, 10, 60, 50, 15, 15);
		// draw and fill oval
		g.drawOval(70,200,50,50);
		g.setColor(Color.green);
		g.fillOval(170,200,50,50);
		// draw and fill arc
		g.drawArc(90,150,70,70,0,75);
		g.fillArc(270,150,70,70,0,75);
		// draw a polygon
		int xpoints[] = {30, 200, 30, 200, 30};
		int ypoints[] = {30, 30, 200, 200, 30};

		int num = 5;
		g.drawPolygon(xpoints, ypoints, num);
	}
}
