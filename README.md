**Fully automated T5-VeriSol Pipeline [2/22/2022]**

1. need to add boogie functionality
2. progam instatiating eith with inferred invariants

**Experiment Observations[2/20/2022]**

1. To make sure VeriSol compile properly on Windows, it's important to run `dotnet build VeriSol.sln` at the root folder where VeriSol.sln. If this command succeeds, we should notice aall debug files `.ddl` generated in usr/bin/Debug. This ensures all dependency files ara generated. Then we should use the developer command `dotnet %VERISOL_PATH%/bin/Debug/VeriSol.dll` on a contract to install z3 and corral. 

Based on multiple experiments, VeriSol doesn't seem to work on Mac, because solc compilable files are different on Mac v. on Windows. The path to compilables/the kind of compilables seems critical to VeriSol implementation. 

this is a research prototype of smart contract invariant inference
