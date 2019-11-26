"""
***************************************
knowledge_input_output.py

    Multiple Choice
        1. c
        2. b
        3. d
        4. b
        5. a
        6. c
        7. a
        8. b
        9. d
        10. a
        11. b
        12. d
        13. b
        14. a
        15. a
        16. c
        17. a
        18. b
        19. a
        20. b

    True or False
        1. False
        2. True
        3. False
        4. True
        5. False

knowledge_functions.py

    Multiple Choice
        1. c
        2. a
        3. d
        4. b
        5. a
        6. d
        7. b
        8. c
        9. a
        10. b
        11. d
        12. b

    True or False
        1. False
        2. True
        3. False
        4. False
        5. False
        6. True
        7. False
        8. False
        9. True
        10. False

knowledge_decision_structures.py

    Multiple Choice
        1. c
        2. b
        3. d
        4. a
        5. c
        6. b
        7. c
        8. b
        9. a
        10. b
        11. c
        12. a

    True or False
        1. False
        2. False
        3. False
        4. True
        5. True

knowledge_repetition_structures.py

    Multiple Choice
        1. b
        2. d
        3. d
        4. a
        5. c
        6. b
        7. d
        8. a
        9. b
        10. c
        11. d
        12. a

    True or False
        1. False
        2. True
        3. True
        4. False
        5. True
        6. False
        7. False

knowledge_files_and_exceptions.py

    Multiple Choice
        1. b
        2. a
        3. d
        4. c
        5. a
        6. b
        7. d
        8. c
        9. a
        10. d
        11. b
        12. a
        13. b
        14. c
        15. b

    True or False
        1. False
        2. True
        3. False
        4. True
        5. False
        6. False
        7. True
        8. False
        9. False

knowledge_lists_and_tuples.py

    Multiple Choice
        1. a
        2. b
        3. c
        4. d
        5. b
        6. c
        7. b
        8. d
        9. c
        10. b or c
        11. a
        12. b
        13. d
        14. d

    True or False
        1. False
        2. True
        3. True
        4. False
        5. False
        6. True
        7. True
        8. False

knowledge_strings.py

    Multiple Choice
        1. c
        2. d
        3. b
        4. c
        5. a
        6. c
        7. d
        8. a
        9. a
        10. b

    True or False
        1. True
        2. True
        3. False
        4. True
        5. False

knowledge_dicts_sets.py

    Multiple Choice
        1. b
        2. d
        3. b
        4. a
        5. c
        6. a
        7. d
        8. c
        9. b
        10. b
        11. c
        12. b
        13. a
        14. a
        15. c
        16. b
        17. d

    True or False
        1. False
        2. True
        3. True
        4. False
        5. False
        6. True
        7. False
        8. True
        9. False
        10. True

knowledge_classes_objects.py

    Multiple Choice
        1. b
        2. d
        3. c
        4. d
        5. b
        6. d
        7. c
        8. a
        9. a or b
        10. a
        11. d
        12. a

    True or False
        1. False
        2. True
        3. False
        4. False
        5. True
        6. False
        7. False
***************************************
"""
"""
Knowledge Classes Objects@@
    Multiple Choice:

        1. The ______________ programming practice is centered on creating functions that are
        separate from the data that they work on.
            >a. modular
            b. procedural
            c. functional
            d. object-oriented

        2. The ______________ programming practice is centered on creating objects.
            a. object-centric
            b. objective
            c. procedural
            >d. object-oriented

        3. A(n) ______________ is a component of a class that references data.
            a. method
            b. instance
            >c. data attribute
            d. module

        4. An object is a(n) ______________.
            a. blueprint
            b. cookie cutter
            >c. variable
            d. instance

        5. By doing this you can hide a class’s attribute from code outside the class.
            a. avoid using the self parameter to create the attribute
            b. begin the attribute’s name with two underscores
            >c. begin the name of the attribute with private__
            d. begin the name of the attribute with the @ symbol

        6. A(n) ______________ method gets the value of a data attribute but does not change
        it.
            a. retriever
            b. constructor
            c. mutator
            >d. accessor

        7. A(n) ______________ method stores a value in a data attribute or changes its value in
        some other way.
            a. modifier
            b. constructor
            >c. mutator
            d. accessor

        8. The ______________ method is automatically called when an object is created.
            >a. __init__
            b. init
            c. __str__
            d. __object__

        9. If a class has a method named __str__, which of these is a way to call the method?
            a. you call it like any other method: object.__str__()
            b. by passing an instance of the class to the built in str function
            c. the method is automatically called when the object is created
            ? you just call the object, so this I think....d. by passing an instance of the class to the built-in state function

        10. A set of standard diagrams for graphically depicting object-oriented systems is provided by ______________.
            >a. the Unified Modeling Language
            b. flowcharts
            c. pseudocode
            d. the Object Hierarchy System

        11. In one approach to identifying the classes in a problem, the programmer identifies the
        ______________ in a description of the problem domain.
        ?  a. verbs
            b. adjectives
            c. adverbs
            d. nouns

        12. In one approach to identifying a class’s data attributes and methods, the programmer
        identifies the class’s ______________.
            a. responsibilities
            b. name
            c. synonyms
        ?  d. nouns

    True or False:

        1. The practice of procedural programming is centered on the creation of objects.     F

        2. Object reusability has been a factor in the increased use of object-oriented programming.     T

        3. It is a common practice in object-oriented programming to make all of a class’s data attributes 
        accessible to statements outside the class.                                                           F

        4. A class method does not have to have a self parameter.              T

        5. Starting an attribute name with two underscores will hide the attribute from code outside the class.     T

        6. You cannot directly call the __str__ method.          T
        
        7. One way to find the classes needed for an object-oriented program is to identify all of
        the verbs in a description of the problem domain               T


Knowledge Decision Structure@@

    Multiple Choice
    1. A __________ structure can execute a set of statements only under certain circumstances.
        a. sequence
       > b. circumstantial
        c. decision
        d. Boolean

    2. A __________ structure provides one alternative path of execution.
        a. sequence
      >  b. single alternative decision
        c. one path alternative
        d. single execution decision

    3. A(n) __________ expression has a value of either true or false.
        a. binary
        b. decision
        c. unconditional
       > d. Boolean

    4. The symbols >, <, and == are all __________ operators.
        a. relational
        b. logical
        c. conditional
      >  d. ternary

    5. A(n) _________ structure tests a condition and then takes one path if the condition is
    true, or another path if the condition is false.
        a. if statement
        b. single alternative decision
      >  c. dual alternative decision
        d. sequence

    6. You use a(n) __________ statement to write a single alternative decision structure.
        a. test-jump
       > b. if
        c. if-else
        d. if-call

    7. You use a(n) __________ statement to write a dual alternative decision structure.
        a. test-jump
        b. if
       > c. if-else
        d. if-call

    8. and, or, and not are __________ operators.
        a. relational
       > b. logical
        c. conditional
        d. ternary

    9. A compound Boolean expression created with the __________ operator is true only if
    both of its subexpressions are true.
       > a. and
        b. or
        c. not
        d. both

    10. A compound Boolean expression created with the _________ operator is true if either
    of its subexpressions is true.
        a. and
       > b. or
        c. not
        d. either

    11. The ___________ operator takes a Boolean expression as its operand and reverses its
    logical value.
        a. and
        b. or
      >  c. not
        d. either

    12. A ___________ is a Boolean variable that signals when some condition exists in the
    program.
       ? a. flag
        b. signal
        c. sentinel
        d. siren

    True or False
    1. You can write any program using only sequence structures.  F?
    
    2. A program can be made of only one type of control structure. You cannot combine
    structures.                                                                          T?

    3. A single alternative decision structure tests a condition and then takes one path if the
    condition is true, or another path if the condition is false.                                   F

    4. A decision structure can be nested inside another decision structure.                       T

    5. A compound Boolean expression created with the and operator is true only when both
    subexpressions are true.                                                                       T
    

Knowledge Dicts Sets@@

        Multiple Choice:

        1. You can use the _________ operator to determine whether a key exists in a dictionary.
            a. &
        >  b. in
            c. ^
            d. ?

        2. You use _________ to delete an element from a dictionary.
            a. The remove method
            b. The erase method
        ? c. The delete method
            d. The del statement

        3. The _________ function returns the number of elements in a dictionary:
            a. size()
        > b. len()
            c. elements()
            d. count()

        4. You can use _________ to create an empty dictionary.
        > a. {}
            b. ()
            c. []
            d. empty()

        5. The _________ method returns a randomly selected key-value pair from a dictionary.
            a. pop()
        > b. random()
            c. popitem()
            d. rand_pop()

        6. The _________ method returns the value associated with a specified key, and removes
        that key-value pair from the dictionary.
        > a. pop()
            b. random()
            c. popitem()
            d. rand_pop()

        7. The _________ dictionary method returns the value associated with a specified key. If
        the key is not found, it returns a default value.
            a. pop()
            b. key()
            c. value()
        ? d. get()

        8. The _________ method returns all of a dictionary’s keys and their associated values as
        a sequence of tuples.
        ? a. keys_values()
            b. values()
            c. items()
            d. get()

        9. The following function returns the number of elements in a set:
            a. size()
        > b. len()
            c. elements()
            d. count()

        10. You can add one element to a set with this method.
        > a. append
            b. add
            c. update
            d. merge

        11. You can add a group of elements to a set with this method.
            a. append
            b. add
        > c. update
            d. merge

        12. This set method removes an element but does not raise an exception if the element is
        not found.
            a. remove
            b. discard
        > c. delete
            d. erase
            
        13. This set method removes an element and raises an exception if the element is not found.
        > a. remove
            b. discard
            c. delete
            d. erase

        14. This operator can be used to find the union of two sets.
        ? a. |
            b. &
            c. -
            d. ^

        15. This operator can be used to find the difference of two sets.
            a. |
        ? b. &
            c. -
            d. ^

        16. This operator can be used to find the intersection of two sets.
            a. |
            b. &
            c. -
        ? d. ^

        17. This operator can be used to find the symmetric difference of two sets.
            a. |
            b. &
        ? c. -
            d. ^

    True or False:

        1. The keys in a dictionary must be mutable objects.     T?

        2. Dictionaries are not sequences.                       F?

        3. A tuple can be a dictionary key.                      T

        4. A list can be a dictionary key.                       T

        5. The dictionary method popitem does not raise an exception if it is called on an empty
        dictionary.                                                                                 F

        6. The following statement creates an empty dictionary:
        mydct = {}                                                   T

        7. The following statement creates an empty set:
        myset = ()                                                   F

        8. Sets store their elements in an unordered fashion.        T

        9. You can store duplicate elements in a set.                F

        10. The remove method raises an exception if the specified element is not found in the
        set.                                                         T


Knowledge Files and Exceptions

    Multiple Choice:

        1. A file that data is written to is known as a(n)
            a. input file
          > b. output file
            c. sequential access file
            d. binary file

        2. A file that data is read from is known as a(n)
          > a. input file
            b. output file
            c. sequential access file
            d. binary file

        3. Before a file can be used by a program, it must be
            a. formatted
            b. encrypted
            c. closed
          > d. opened

        4. When a program is finished using a file, it should do this.
            a. erase the file
            b. open the file
        >  c. close the file
            d. encrypt the file

        5. The contents of this type of file can be viewed in an editor such as Notepad.
        >   a. text file
            b. binary file
            c. English file
            d. human-readable file
            
        6. This type of file contains data that has not been converted to text.
            a. text file
        >   b. binary file
            c. Unicode file
            d. symbolic file

        7. When working with this type of file, you access its data from the beginning of the file
        to the end of the file.
            a. ordered access
            b. binary access
            c. direct access
            d. sequential access

        8. When working with this type of file, you can jump directly to any piece of data in the
        file without reading the data that comes before it.
            a. ordered access
            b. binary access
            c. direct access
            d. sequential access

        9. This is a small “holding section” in memory that many systems write data to before
        writing the data to a file.
            a. buffer
            b. variable
            c. virtual file
            d. temporary file

        10. This marks the location of the next item that will be read from a file.
            a. input position
            b. delimiter
            c. pointer
            d. read position

        11. When a file is opened in this mode, data will be written at the end of the file’s existing
        contents.
            a. output mode
            b. append mode
            c. backup mode
            d. read-only mode

        12. This is a single piece of data within a record.
            a. field
            b. variable
            c. delimiter
            d. subrecord

        13. When an exception is generated, it is said to have been __________.
            a. built
            b. raised
            c. caught
            d. killedReview Questions 291

        14. This is a section of code that gracefully responds to exceptions.
            a. exception generator
            b. exception manipulator
            c. exception handler
            d. exception monitor

        15. You write this statement to respond to exceptions.
            a. run/handle
            b. try/except
            c. try/handle
            d. attempt/except

    True or False:

    1. When working with a sequential access file, you can jump directly to any piece of data
    in the file without reading the data that comes before it.

    2. When you open a file that file already exists on the disk using the 'w' mode, the contents 
    of the existing file will be erased.

    3. The process of opening a file is only necessary with input files. Output files are 
    automatically opened when data is written to them.

    4. When an input file is opened, its read position is initially set to the first item in the file.

    5. When a file that already exists is opened in append mode, the file’s existing contents
    are erased.

    6. If you do not handle an exception, it is ignored by the Python interpreter and the program 
    continues to execute.

    7. You can have more than one except clause in a try/except statement.

    8. The else suite in a try/except statement executes only if a statement in the try suite
    raises an exception.

    9. The finally suite in a try/except statement executes only if no exceptions are raised
    by statements in the try suite.


Knowledge Functions
        
    Multiple Choice

        1. A group of statements that exist within a program for the purpose of performing a specific task is a(n) __________.
            a. block
            b. parameter
            c. function
            d. expression

        2. A design technique that helps to reduce the duplication of code within a program and
        is a benefit of using functions is __________.
            a. code reuse
            b. divide and conquer
            c. debugging
            d. facilitation of teamwork

        3. The first line of a function definition is known as the __________.
            a. body
            b. introduction
            c. initialization
            d. header

        4. You __________ the function to execute it.
            a. define
            b. call
            c. import
            d. export

        5. A design technique that programmers use to break down an algorithm into functions
        is known as __________.
            a. top-down design
            b. code simplification
            c. code refactoring
            d. hierarchical subtasking

        6. A __________ is a diagram that gives a visual representation of the relationships
        between functions in a program.
            a. flowchart
            b. function relationship chart
            c. symbol chart
            d. hierarchy chart

        7. A __________ is a variable that is created inside a function.
            a. global variable
            b. local variable
            c. hidden variable
            d. none of the above; you cannot create a variable inside a function  
        
        8. A(n) __________ is the part of a program in which a variable may be accessed.
            a. declaration space
            b. area of visibility
            c. scope
            d. mode

        9. A(n) __________ is a piece of data that is sent into a function.
            a. argument
            b. parameter
            c. header
            d. packet    

        10. A(n) __________ is a special variable that receives a piece of data when a function is called.
            a. argument
            b. parameter
            c. header
            d. packet    

        11. A variable that is visible to every function in a program file is a __________.
            a. local variable
            b. universal variable
            c. program-wide variable
            d. global variable

        12. When possible, you should avoid using __________ variables in a program.
            a. local
            b. global
            c. reference
            d. parameter

    True or False

        1. The phrase “divide and conquer” means that all of the programmers on a team should
        be divided and work in isolation.

        2. Functions make it easier for programmers to work in teams.

        3. Function names should be as short as possible.

        4. Calling a function and defining a function mean the same thing.

        5. A flowchart shows the hierarchical relationships between functions in a program.

        6. A hierarchy chart does not show the steps that are taken inside a function.

        7. A statement in one function can access a local variable in another function.

        8. In Python you cannot write functions that accept multiple arguments.

        9. In Python, you can specify which parameter an argument should be passed into a function call.

        10. You cannot have both keyword arguments and non-keyword arguments in a function call.


Knowledge Input Output
    
    Multiple Choice

        1. A __________ error does not prevent the program from running, but causes it to
            produce incorrect results.
            a. syntax
            b. hardware
            c. logic
            d. fatal

        2. A __________ is a single function that the program must perform in order to satisfy the
            customer.
            a. task
            b. software requirement
            c. prerequisite
            d. predicate

        3. A(n) __________ is a set of well-defined logical steps that must be taken to perform a
            task.
            a. logarithm
            b. plan of action
            c. logic schedule
            d. algorithm       

        4. An informal language that has no syntax rules, and is not meant to be compiled or
        executed is called __________.
            a. faux code
            b. pseudocode
            c. Python
            d. a flowchart

        5. A __________ is a diagram that graphically depicts the steps that take place in a
        program.
            a. flowchart
            b. step chart
            c. code graph
            d. program graph    

        6. A __________ is a sequence of characters.
            a. char sequence
            b. character collection
            c. string
            d. text block

        7. A __________ is a name that references a value in the computer’s memory.
            a. variable
            b. register
            c. RAM slot
            d. byte   

        8. A __________ is any hypothetical person using a program and providing input for it.
            a. designer
            b. user
            c. guinea pig
            d. test subject
        
        9. A string literal in Python must be enclosed in
            a. parentheses
            b. single-quotes
            c. double-quotes
            d. either single-quotes or double-quotes

        10. Short notes placed in different parts of a program explaining how those parts of the
        program work are called __________.
            a. comments
            b. reference manuals
            c. tutorials
            d. external documentation

        11. A(n) __________ makes a variable reference a value in the computer’s memory.
            a. variable declaration
            b. assignment statement
            c. math expression
            d. string literal

        12. This symbol marks the beginning of a comment in Python.
            a. &
            b. *
            c. **
            d. #

        13. Which of the following statements will cause an error?
            a. x = 17
            b. 17 = x
            c. x = 99999
            d. x = '17'

        14. In the expression 12 + 7, the values on the right and left of the + symbol are
        called __________.
            a. operands
            b. operators
            c. arguments
            d. math expressions

        15. This operator performs integer division.
            a. //
            b. %
            c. **
            d. /

        16. This is an operator that raises a number to a power.
            a. %
            b. *
            c. **
            d. /

        17. This operator performs division, but instead of returning the quotient it returns the
        remainder.
            a. %
            b. *
            c. **
            d. /

        18. Suppose the following statement is in a program: price = 99.0. After this statement
        executes, the price variable will reference a value of this data type.
            a. int
            b. float
            c. currency
            d. str

        19. This built-in function can be used to read input that has been typed on the keyboard.
            a. input()
            b. get_input()
            c. read_input()
            d. keyboard()

        20. This built-in function can be used to convert an int value to a float.
            a. int_to_float()
            b. float()
            c. convert()
            d. int()

    True or False

        1. Programmers must be careful not to make syntax errors when writing pseudocode
        programs.

        2. In a math expression, multiplication and division takes place before addition and
        subtraction.

        3. Variable names can have spaces in them.

        4. In Python the first character of a variable name cannot be a number.

        5. If you print a variable that has not been assigned a value, the number 0 will be
        displayed.

        

Knowledge Lists and Tuples
    
    Multiple Choice
        1. This term refers to an individual item in a list.
            a. element
            b. bin
            c. cubby hole
            d. slot

        2. This is a number that identifies an item in a list.
            a. element
            b. index
            c. bookmark
            d. identifier

        3. This is the first index in a list.
            a. -1
            b. 1
            c. 0
            d. The size of the list minus one

        4. This is the last index in a list.
            a. 1
            b. 99
            c. 0
            d. The size of the list minus one

        5. This will happen if you try to use an index that is out of range for a list.
            a. a ValueError exception will occur
            b. an IndexError exception will occur
            c. The list will be erased and the program will continue to run.
            d. Nothing—the invalid index will be ignored

        6. This function returns the length of a list.
            a. length
            b. size
            c. len
            d. lengthof

        7. When the * operator’s left operand is a list and its right operand is an integer, the
        operator becomes this.
            a. The multiplication operator
            b. The repetition operator
            c. The initialization operator
            d. Nothing—the operator does not support those types of operands.
            
        8. This list method adds an item to the end of an existing list.
            a. add
            b. add_to
            c. increase
            d. append

        9. This removes an item at a specific index in a list.
            a. The remove method
            b. The delete method
            c. The del statement
            d. The kill method

        10. Assume the following statement appears in a program:
                mylist = []
        Which of the following statements would you use to add the string 'Labrador' to the
        list at index 0?
            a. mylist[0] = 'Labrador'
            b. mylist.insert(0, 'Labrador')
            c. mylist.append('Labrador')
            d. mylist.insert('Labrador', 0)

        11. If you call the index method to locate an item in a list and the item is not found, this
        happens.
            a. A ValueError exception is raised
            b. An InvalidIndex exception is raised
            c. The method returns -1
            d. Nothing happens. The program continues running at the next statement.

        12. This built-in function returns the highest value in a list.
            a. highest
            b. max
            c. greatest
            d. best_of

        13. This file object method returns a list containing the file’s contents.
            a. to_list
            b. getlist
            c. readline
            d. readlines

        14. Which of the following statements creates a tuple?
            a. values = [1, 2, 3, 4]
            b. values = {1, 2, 3, 4}
            c. values = (1)
            d. values = (1,)

    True or False:

        1. Lists in Python are immutable.

        2. Tuples in Python are immutable.

        3. The del statement deletes an item at a specified index in a list.

        4. Assume list1 references a list. After the following statement executes, list1 and
        list2 will reference two identical but separate lists in memory:
        list2 = list1

        5. A file object’s writelines method automatically writes a newline ('\n') after writing
        each list item to the file.

        6. You can use the + operator to concatenate two lists.

        7. A list can be an element in another list.

        8. You can remove an element from a tuple by calling the tuple’s remove method


Knowledge Repetition Structures
    
    Multiple Choice:

        1. A __________ -controlled loop uses a true/false condition to control the number of
        times that it repeats.
            a. Boolean
            b. condition
            c. decision
            d. count

        2. A __________ -controlled loop repeats a specific number of times.
            a. Boolean
            b. condition
            c. decision
            d. count

        3. Each repetition of a loop is known as a(n) __________.
            a. cycle
            b. revolution
            c. orbit
            d. iteration

        4. The while loop is a __________ type of loop.
            a. pretest
            b. no-test
            c. prequalified
            d. post-iterative

        5. A(n) __________ loop has no way of ending and repeats until the program is interrupted.
            a. indeterminate
            b. interminable
            c. infinite
            d. timeless

        6. The -= operator is an example of a(n) __________ operator.
            a. relational
            b. augmented assignment
            c. complex assignment
            d. reverse assignment

        7. A(n) __________ variable keeps a running total.
            a. sentinel
            b. sum
            c. total
            d. accumulator

        8. A(n) __________ is a special value that signals when there are no more items from a
        list of items to be processed. This value cannot be mistaken as an item from the list.
            a. sentinel
            b. flag
            c. signal
            d. accumulator
            
        9. GIGO stands for
            a. great input, great output
            b. garbage in, garbage out
            c. GIGahertz Output
            d. GIGabyte Operation

        10. The integrity of a program’s output is only as good as the integrity of the program’s
            a. compiler
            b. programming language
            c. input
            d. debugger

        11. The input operation that appears just before a validation loop is known as the
            a. prevalidation read
            b. primordial read
            c. initialization read
            d. priming read
        12. Validation loops are also known as
            a. error traps
            b. doomsday loops
            c. error avoidance loops
            d. defensive loops

    True or False:

        1. A condition-controlled loop always repeats a specific number of times.

        2. The while loop is a pretest loop.

        3. The following statement subtracts 1 from x: x = x - 1

        4. It is not necessary to initialize accumulator variables.

        5. In a nested loop, the inner loop goes through all of its iterations for every 
        single iteration of the outer loop.

        6. To calculate the total number of iterations of a nested loop, add the number of 
        iterations of all the loops.

        7. The process of input validation works as follows: when the user of a program enters
        invalid data, the program should ask the user “Are you sure you meant to enter that?”
        If the user answers “yes,” the program should accept the data.

Knowledge Strings
        
    Multiple Choice:

        1. This is the first index in a string.
            a. -1
            b. 1
            c. 0
            d. The size of the string minus one

        2. This is the last index in a string.
            a. 1
            b. 99
            c. 0
            d. The size of the string minus one

        3. This will happen if you try to use an index that is out of range for a string.
            a. a ValueError exception will occur
            b. an IndexError exception will occur
            c. The string will be erased and the program will continue to run.
            d. Nothing—the invalid index will be ignored

        4. This function returns the length of a string.
            a. length
            b. size
            c. len
            d. lengthof

        5. This string method returns a copy of the string with all leading whitespace characters
        removed.
            a. lstrip
            b. rstrip
            c. remove
            d. strip_leading

        6. This string method returns the lowest index in the string where a specified substring is
        found.
            a. first_index_of
            b. locate
            c. find
            d. index_of

        7. This operator determines whether one string is contained inside another string.
            a. contains
            b. is_in
            c. ==
            d. in

        8. This string method returns true if a string contains only alphabetic characters and is at
        least one character in length.
            a. The isalpha method
            b. The alpha method
            c. The alphabetic method
            d. The isletters method

        9. If you call the index method to locate an item in a list and the item is not found, this
        happens.
            a. A ValueError exception is raised
            b. An InvalidIndex exception is raised
            c. The method returns 1
            d. Nothing happens. The program continues running at the next statement.

        10. This string method returns a copy of the string with all leading and trailing whitespace
        characters removed.
            a. clean
            b. strip
            c. remove_whitespace
            d. rstrip

    True or False:

        1. Once a string is created, it cannot be changed.
        2. You can use the for loop to iterate over the individual characters in a string.
        3. The isupper method converts a string to all uppercase characters.
        4. The repetition operator (*) works with strings as well as with lists.
        5. When you call a string’s split method, the method divides the string into two substrings.


"""