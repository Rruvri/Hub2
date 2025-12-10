Hello! 
This is the second version of RaviHUB, a life managing central space that I am building alongside my Python learning!
The previous version had item management for stuff at home, memos and goals, reminders to buy e.g. groceries
[!] is To-Do, [->] completed or in progress


=== CURRENT FEATURES ===

== Completed:
+ Time-based tracking, day periods for routines etc.
+ Save system with Pickle
+ Basic Daily goals tracking
    + Archive function
    + View function
    + Dynamic updating for next day


== Now working on:

+ Fix saves bug
    + Fixed, error was due to a trial 'reset class' function and global variable scoping
        -> finish new reset option

-> Error Handling
    -> Tied with general collection listing + index no.s, add a handle that stops out of range inputs

-> Daily goals tracking
    + Complete/ edit goals
        -> If completed, move up next goals
        
        + If deleted and not main/sec. clear field
            -> Realistically, whole thing needs a reformat
    
    ! Add a 'set tomorrow's goals' early

    ! Move dict interactions to a general function for DRY reuse

    ! Decorator for while true menu holding
        -> Basic version implemented but not universally applied nor very efficient
        
    -> Implementing comparison between previous login and current date
        + if daily goals set yesterday and today is after yesterday, update goals
            -> this is done, but could be cleaner

-> Memos
    -> Started basic implementation
        + There's a bug with view fn, check about changing class methods
            -> It's menu_hold was missing, but this feels messy so have a look

    ! Add a 'shorthand' toggle for collections such as grocery lists, that would never need additional notes

    ! add a sublist/ extended notes feature that would align with e.g. translating this README into a memos (task) list






=== ROADMAPish... ===
! Implement Item tracking  
    ! Either copy across old structure from Hub1, or start fresh (with GUI in mind)

! Implement GUI
