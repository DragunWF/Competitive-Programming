// https://www.codewars.com/kata/5a4e3782880385ba68000018

class Kata
{
    public static string BalancedNumber(int number)
    {
        int leftSum = 0, rightSum = 0;
        string strNum = number.ToString();
        bool isEven = strNum.Length % 2 == 0;
        int middle = strNum.Length / 2;
        for (int i = 0; i < (isEven ? middle - 1 : middle); i++)
        {
            leftSum += GetNum(strNum[i]);
        }
        for (int i = strNum.Length - 1; i > middle; i--)
        {
            rightSum += GetNum(strNum[i]);
        }
        return leftSum == rightSum ? "Balanced" : "Not Balanced";
    }

    private static int GetNum(char num)
    {
        return int.Parse(num.ToString());
    }
}