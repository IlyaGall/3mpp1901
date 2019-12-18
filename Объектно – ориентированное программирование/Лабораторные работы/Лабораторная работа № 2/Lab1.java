public class Lab1
{
    public static void main(String[] args)
    {
        Point3d point3dOne=new Point3d(1,1,0);  // создание 3-х точек в пространстве
        Point3d point3dTwo=new Point3d(-2 ,4,0);
        Point3d point3dThree=new Point3d(-2,-2,0);


        System.out.println( "S= "+   computeArea(point3dOne,point3dTwo,point3dThree));//передача данных для расчёта площади треугольника

    }
    /*статичный медот для подсчёта S трёхмнерного треугольника
    * на вход получает три метода Point3d с координатами
    * возрашает S-дь */
    public  static double computeArea(Point3d onePoint,Point3d twoPoint, Point3d threePoint)
    {
        if((onePoint.getX()==twoPoint.getX()||onePoint.getX()==threePoint.getX()||twoPoint.getX()==threePoint.getX())
        &  (onePoint.getY()==twoPoint.getY()||onePoint.getY()==threePoint.getY()||twoPoint.getY()==threePoint.getY())
        &  (onePoint.getZ()==twoPoint.getZ()||onePoint.getZ()==threePoint.getZ()||twoPoint.getZ()==threePoint.getZ()))// проверка на одинаковые точнки в пространстве
        {
            System.out.print("одна из точек равна другой, поэтому S=");
            return 0;
        }
        //Чтобы удобнее читать и легче понимать код сделал так:
       double a= onePoint.distanceTo(twoPoint);
       double b= twoPoint.distanceTo(threePoint);
       double c= threePoint.distanceTo((onePoint));
       double P=(a+b+c)/2;
       double s=Math.sqrt(P*(P-a)*(P-b)*(P-c));
       //альтернативный вариант выглядит так:  double s=Math.sqrt(P*(P-onePoint.distanceTo(twoPoint))*(P-twoPoint.distanceTo(threePoint))*(P-threePoint.distanceTo((onePoint))));
       return  s;
    }
}
