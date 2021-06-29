using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Text.RegularExpressions;
using EthornellEditor;

namespace BurikoConverter
{
    class Program
    {
        public static System.Text.Encoding UTF8 { get; }

        static void Help()
        {
            Console.WriteLine("===============\nBurikoConverter\n===============\n");
            Console.WriteLine("Command format: \"BurikoConverter.exe subcommands C:\\file\\directory\"");
            Console.WriteLine("Subcommands:\n-d - Decode a script file\n-e - Encode a text file.");
        }
        public static void Main(string[] args)
        {
            if (args.Length >= 2)
            {
                MainAsync(args[0], args[1]).GetAwaiter().GetResult();
            }
            else
            {
                Help();
            }
        }
        private static async Task MainAsync(string sc, string f)
        {
            Encoder en = new Encoder();
            if (sc.StartsWith("-d"))
            {
                await en.Decode(f);
            }
            if (sc.StartsWith("-e"))
            {
                await en.Encode(f);
            }
        }
    }
    class Encoder
    {
        public BurikoScript script = new BurikoScript();

        //List<(string, string, string)> lines = new List<(string, string, string)>();
        public async Task Decode(string path)
        {
            byte[] data = File.ReadAllBytes(path);
            script.Import(data);
            string[] lines = script.strings;

            File.Delete(path + ".txt");
            using (StreamWriter sw = File.CreateText(path+".txt"))
            {
                Console.WriteLine("Decoding "+path);
                for (int i = 0; i < lines.Length; i++)
                {
                    try
                    {
                        await sw.WriteLineAsync(lines[i]);
                    }
                    catch
                    {
                        Console.WriteLine("Something went wrong!");
                    }
                }
            }
        }
        public async Task Encode(string path)
        {
            script.Import(File.ReadAllBytes(path));
            List<string> tl = File.ReadAllLines(path+".txt").ToList();
            List<string> scr = script.strings.ToList();
            //maybe for loop this or something
            //byte[] lines = script.Export();
            //Console.WriteLine(translation[0]);
            int diff = scr.Count - tl.Count;
            for (int i = 0; i < diff; i++) { tl.Add(""); }
            for (int i = 0; i < scr.Count; i++)
            {
                try
                {
                    if (String.IsNullOrEmpty(tl[i]) == true)
                    {
                        if (String.IsNullOrEmpty(scr[i]) != true)
                        {
                            tl.RemoveAt(i);
                        }
                    }
                }
                catch (Exception e)
                {
                    Console.WriteLine("{0} Exception caught.", e);
                }                
            }

            for (int i = 0; i < tl.Count; i++)
            {
                try
                {
                    script.strings[i] = tl[i];
                    Console.WriteLine(tl[i]);
                }
                catch (Exception e)
                {
                    Console.WriteLine("{0} Exception caught.", e);
                    break;
                }
            }

            byte[] scr_data = script.Export();

            using (FileStream fs = new FileStream(path+".new", FileMode.OpenOrCreate, FileAccess.Write))
            {
                await fs.WriteAsync(scr_data, 0, scr_data.Length);
            }
        }
    }  

}
