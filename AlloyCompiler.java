/** Running the Alloy Compiller.
  By Gail Terman
 */

import edu.mit.csail.sdg.alloy4.Err;
import edu.mit.csail.sdg.alloy4compiler.parser.CompUtil;
import edu.mit.csail.sdg.alloy4compiler.ast.Module;
import edu.mit.csail.sdg.alloy4compiler.ast.Command;
import edu.mit.csail.sdg.alloy4compiler.translator.A4Solution;
import edu.mit.csail.sdg.alloy4compiler.translator.A4Options;
import edu.mit.csail.sdg.alloy4compiler.translator.TranslateAlloyToKodkod;

/**
 * AlloyCompiler reads a file given as an argument, solves it, and places the output in out.xml.
 */
public class AlloyCompiler {
  public static void main (String[] args) throws Err{
    // Get the file from the argument list
    String filename = args[0];
    // parse the model of the world
    Module mod = CompUtil.parseEverything_fromFile(null, null, filename);

    // set basic options for Alloy solver
    A4Options opts = new A4Options();
    opts.solver = A4Options.SatSolver.SAT4J;

    // get the current working directory
    String cwd = System.getProperty("user.dir");

    // solve the model
    for (Command command: mod.getAllCommands()) {
      A4Solution ans = TranslateAlloyToKodkod.execute_command(null, mod.getAllReachableSigs(), command, opts);
      // if the model has a solution
      if (ans.satisfiable()) {
        // write it to the file
        ans.writeXML(cwd+"/out.xml");
       // otherwise print an inscrutable error that will make our code crash in horriffic ways
      }else System.out.println("Not satisfiable.");
    }
  }
}
