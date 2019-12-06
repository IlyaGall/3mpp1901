/*Вторая программа, показывает, является ли строка палиндромом*/
public class Palindrome
{
    public static void main(String[] args)
    {
        for (int i = 0; i < args.length; i++)// цикл в котором, ведётся перебор входных аргументов
        {// java E:\javaProcet\Palindrome.java java Palindrome madam racecar apple kayak song noon
            String s = args[i];//локальная переменная string в которую записывается значание аргумента. Можно и на пряму отправлять в метод isPalindrome, но в примере написано так, так что не буду изменять
            System.out.println( s +" - " + isPalindrome(s));// вывод(true/false) является ли аргумент палиндром.
        }
    }
    /* метод переворачивает слова задом на перёд принимает на вход слово типа String возрашает тип String, но уже перевёнутое задом на перёд*/
    public static String reverseString(String stringWord)
    {
        String reverseWord="";// локадьная 
        for(int count=stringWord.length()-1;   count > -1;    count--) // создан цикл, который вставляет буквы задом на перёд
        {
            reverseWord+=stringWord.charAt(count);// записывает всё перевёрнутые буквы
        }
        return reverseWord; //возращает перевёрнутое слово
    }
    // метод проверки аргумената на палиндром
    // принимает на вход аргумент
    // возращает true or false
    public static boolean isPalindrome(String s)
    {
        String   reverseWord    = reverseString(s);// используется метод reverseString для "переворота слова"
        return reverseWord.equals(s);// сравниевает исходный аргумент с аргументом("перевёрнутым") из метода reverseString
    }
}
