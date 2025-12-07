Console.Write("Input kata: ");
string word = Console.ReadLine();
string reversed = "";

for (int i = word.Length - 1; i >= 0; i--)
{
    reversed += word[i];
}

if (word.ToLower() == reversed.ToLower())
    Console.WriteLine("Palindrome");
else
    Console.WriteLine("Bukan palindrome");
