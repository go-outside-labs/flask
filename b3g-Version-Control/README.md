b3g Version Control
===================

This is my own git-like version control.


[Based in the (git parable from Tom Preson)](http://tom.preston-werner.com/2009/05/19/the-git-parable.html].)



```

Usage: ./b3g [OPTION] <ARGUMENT>

Options:

      config <WORKFOLDER>:
                  Set the configuration file (in the root).
                  <WORKFOLDER> is where is the root of your project.
                  Should be called when starting a project.

      snapshot <TAG>:
                  Create a snapshot. Works with ss too.
                  <TAG> is optional, and it will be written in the HEAD file.

      current:
                  Show the current snapshot.

      checkout <SNAPSHOT>:
                  Checkout a snapshot. Works with co too.
                  <SNAPSHOT> is a number, or l for the latest.

      log:
                  Show snapshot logs.

      diff <SNAPSHOT1> <SNAPSHOT2>:
                  Show the difference between 2 snapshots.

      rm:
                  Terminate project, removing config files.
