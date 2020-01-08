/**двумерный класс точки.  **/

public class Point2d {

/** координата X **/
    private double xCoord;
/** координата Y **/
    private double yCoord;

/** Конструктор инициализации **/
    public Point2d ( double x, double y) {
        xCoord = x;
        yCoord = y;
    }

/** Конструктор по умолчанию. **/
    public Point2d () {
//Вызовите конструктор с двумя параметрами и определите источник.
        this(0, 0);
    }

/** Возвращение координаты X **/
    public double getX () {
        return xCoord;
    }

/** Возвращение координаты Y **/

    public double getY () {
        return yCoord;
    }

/** Установка значения координаты X. **/
    public void setX ( double val) {
        xCoord = val;
    }

/** Установка значения координаты Y. **/
    public void setY ( double val) {
        yCoord = val;
    }
    public static void main(String[] args) {
        Point2d myPoint = new Point2d();
        Point2d myOtherPoint = new Point2d(5,3);
        Point2d aThirdPoint = new Point2d();

        // сравнение 2 - точек в пространстве
        if (myOtherPoint.equals(aThirdPoint)){
            System.out.println("Point one = Point Two");
        }
        else{
            System.out.println("Point One not= point Two");

        }

    }
    //метод сравнивает точки м\у друг другом
    // возращает true-то точки равны, false не равны
    public boolean equals(Object obj)
    {
        Point2d tmp =(Point2d)obj;
        if(tmp.getX() == getX() && tmp.getY() == getY())
            return true;
        else
            return false;
    }
}