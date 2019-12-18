

public class Point3d
{
    private  double point3dX;
    private  double point3dY;
    private  double point3dZ;


    public static void main(String[] args)
    {
        /* пример работы метода для поиска расстояния м-у 2-мя точками
        Point3d point3dOne=new Point3d(3,8,7);
        Point3d point3dTwo=new Point3d(1,2,3);
        Point3d point3dThree=new Point3d(3,8,7);
        point3dOne. distanceTo(point3dTwo);
        */
    }
    /** добавление данных в не статистический метод **/
    public Point3d(double x,double y,double z)
    {
        point3dX=x;
        point3dY=y;
        point3dZ=z;
    }
    /** Конструктор по умолчанию.  Если юзер забыл добавить данные**/
    public Point3d()
    {
        this(0,0,0);
    }


    /** Возвращение координаты X **/
    public double getX ()
    {
        return point3dX;
    }
    /** Возвращение координаты Y **/
    public double getY ()
    {
        return point3dY;
    }
    /** Возвращение координаты Z **/
    public double getZ ()
    {
        return point3dZ;
    }

    /** Установка значения координаты X. **/
    public void setX ( double newVal)
    {
        point3dX = newVal;
    }
    /** Установка значения координаты Y. **/
    public void setY ( double newVal)
    {
        point3dY = newVal;
    }
    /** Установка значения координаты X. **/
    public void setZ ( double newVal)
    {
        point3dZ = newVal;
    }
    /** Поиск расстояния между точками.**/
    public  double distanceTo(Point3d two)
    {// чтобы получить значение из point3dOne надо использовать this, например   this.getX(),  для метода  point3dOne. distanceTo(point3dTwo), а для передоваемого просто обращатся на прямую, например two.getX();
        double distance=Math.sqrt(  (Math.pow(two.getX()- this.getX(),2)+Math.pow(two.getY()-this.getY(),2 ) + Math.pow(two.getZ()-this.getZ(),2)) );
        distance=Math.round(distance*100);// умножаем на 100, а потом делим для того чтобы округлить значение
        distance=distance/100;
        return distance;
    }
}
