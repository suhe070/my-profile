// using System;
// using System.Collections.Generic;
// using Taskmanajer; 
// namespace dari TaskItem
// List<TaskItem> task = new ();
// int id = 1;
// bool running = true;

// while (running)
// { 
//     Console.WriteLine("1. Add | 2. List | 3. Comlete | 4. Exit");
//     string choice = Console.ReadLine();

//     switch (choice)
//     {
//         case "1":
//             Console.Write("Title: ");
//             tasks.Add(new TaskItem { Id = id++, Title = Console.ReadLine()});
//             break;
//         case "2":
//             foreach (var t in tasks)
//                 Console.WriteLine($"{t.Id}. {t.Title} - {(t.IsCompleted ? "Done" : "Pending")}");
//             break;
//         case "3":
//              Console.Write("Enter ID: ");
//              int markId = int.Parse(Console.ReadLine());
//              tasks.Find(t => t.Id == markId)?.MarkComplete();
//              break;
//         case "4" : running = false; break;

//     }
// }

using System;
using System.Collections.Generic;
using Taskmanajer; // namespace dari TaskItem

class Program
{
    static List<TaskItem> tasks = new List<TaskItem>();

    static void Main(string[] args)
    {
        while (true)
        {
            Console.WriteLine("\n=== Task Manager CLI ===");
            Console.WriteLine("1. Tambah Task");
            Console.WriteLine("2. Lihat Daftar Task");
            Console.WriteLine("3. Tandai Selesai");
            Console.WriteLine("4. Keluar");
            Console.Write("Pilih menu: ");

            string input = Console.ReadLine()!;
            switch (input)
            {
                case "1":
                    AddTask();
                    break;
                case "2":
                    ShowTasks();
                    break;
                case "3":
                    CompleteTask();
                    break;
                case "4":
                    return;
                default:
                    Console.WriteLine("Pilihan tidak valid.");
                    break;
            }
        }
    }

    static void AddTask()
    {
        Console.Write("Masukkan nama task: ");
        string title = Console.ReadLine()!;
        tasks.Add(new TaskItem(title));
        Console.WriteLine("Task ditambahkan!");
    }

    static void ShowTasks()
    {
        Console.WriteLine("\nDaftar Task:");
        if (tasks.Count == 0)
        {
            Console.WriteLine("Belum ada task.");
            return;
        }

        for (int i = 0; i < tasks.Count; i++)
        {
            string status = tasks[i].IsDone ? "" : "";
            Console.WriteLine($"{i + 1}. {tasks[i].Title} - {status}");
        }
    }

    static void CompleteTask()
    {
        Console.Write("Masukkan nomor task yang selesai: ");
        if (int.TryParse(Console.ReadLine(), out int index) &&
            index > 0 && index <= tasks.Count)
        {
            tasks[index - 1].IsDone = true;
            Console.WriteLine("Task ditandai selesai!");
        }
        else
        {
            Console.WriteLine("Nomor task tidak valid.");
        }
    }
}
