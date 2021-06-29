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

        static void Help()
        {
            Console.WriteLine("===============\nBurikoConverter\n===============\n");
            Console.WriteLine("Command format: \"BurikoConverter.exe subcommands C:\\file\\directory\"");
            Console.WriteLine("Subcommands:\n-d - Decode a script file\n-e - Encode a text file.");
        }
        public static void Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
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

        Encoding unicode = Encoding.Unicode;

        //List<(string, string, string)> lines = new List<(string, string, string)>();
        public async Task Decode(string path)
        {
            byte[] data = File.ReadAllBytes(path);
            script.Import(data);
            string[] lines = script.strings;

            File.Delete(path + ".txt");
            string line = "";
            using (StreamWriter sw = File.CreateText(path+".txt"))
            {
                for (int i = 0; i < lines.Length; i++)
                {
                    try
                    {
                        line = "<"+i.ToString()+">"+lines[i].Replace('\n'.ToString(), "\\n");
                        //Console.WriteLine(line);
                        await sw.WriteLineAsync(line);

                    }
                    catch (Exception e)
                    {
                        Console.WriteLine(e.Message);
                    }
                }
            }
            if (line != "")
                Console.WriteLine("[BC] Decoded : "+path);
        }
        public async Task Encode(string path)
        {
            script.Import(File.ReadAllBytes(path));
            string[] lines = script.strings;

            string[] new_lines = File.ReadAllLines(path+".txt");

            string new_path = Path.Combine(Path.GetDirectoryName(path), "encode");
            string new_file = Path.GetFileName(path);

            for (int i = 0; i < lines.Length; i++)
            {
                string tl = Regex.Replace(new_lines[i], @"\<\d*\>", "");
                script.strings[i] = tl;
            }

            byte[] scr_data = script.Export();
            Directory.CreateDirectory(new_path);
            using (FileStream fs = new FileStream(new_path+"\\"+new_file, FileMode.OpenOrCreate, FileAccess.Write))
            {
                try
                {
                    await fs.WriteAsync(scr_data, 0, scr_data.Length);
                    Console.WriteLine("[BC] Encoded : " + path);
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.Message);
                }
                
            }
        }
    }  

}
