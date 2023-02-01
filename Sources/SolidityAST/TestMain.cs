// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT license.
namespace SolidityAST
{
    using System;
    using System.IO;
    using Microsoft.Extensions.Logging;

    class TestMain
    {
        public static void Main(string[] args)
        {
         if (args.Length < 1 || args.Length > 2)
            {
                Console.WriteLine("Usage: Test [<YourContract.sol>]");
            }
            
            DirectoryInfo debugDirectoryInfo = Directory.GetParent(Directory.GetCurrentDirectory());
            string workingDirectory = debugDirectoryInfo.Parent.Parent.Parent.Parent.FullName;
            Console.WriteLine($"workingDirectory = {workingDirectory}");
            string solcPath = workingDirectory + "\\Tool\\solc.exe";  
            Console.WriteLine($"solcPath = {solcPath}");       
            string testDir = workingDirectory + "\\Test\\regressions";
            Console.WriteLine($"testDir = {testDir}");

            ILoggerFactory loggerFactory = LoggerFactory.Create(builder => builder.AddConsole()); // .AddConsole(LogLevel.Information);
            ILogger logger = loggerFactory.CreateLogger("SolidityAST.RegressionExecutor");

            RegressionExecutor executor = new RegressionExecutor(solcPath, testDir, logger);
            executor.BatchExecute();
            Console.ReadLine();
        }

        // Legacy entry point for testing
        private static void LegacyMain(string[] args)
        {
            //at root dir
            DirectoryInfo debugDirectoryInfo = Directory.GetParent(Directory.GetCurrentDirectory());
            string workingDirectory = debugDirectoryInfo.Parent.Parent.Parent.Parent.FullName;
            string filename = args[0];
            string solcPath = workingDirectory + "\\Tool\\solc.exe";
            Console.WriteLine($"solcPath = {solcPath}");
           // Path.GetDirectoryName(solidityFilePath);
            string filePath = workingDirectory + "\\Test\\regressions\\" + filename;
            SolidityCompiler compiler = new SolidityCompiler();
            CompilerOutput compilerOutput = compiler.Compile(solcPath, filePath);
            AST ast = new AST(compilerOutput);

            Console.WriteLine(ast.GetSourceUnits());
            Console.ReadLine();
        }
    }
}
