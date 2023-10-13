# LANGUAGE SYNTAX

# Comment Lines (both in-line and block)
    -:<comment-body>:-

# Import Statements
## Module import
    "<module-name>"
## Class import
    "<module-name.class-name>"
## Function import
    "<module-name.function-name>"
## Class Function import
    "<module-name.class-name.function-name>"

# Data Types
## Non-Empty
Includes integers, non-integers, complex, quaternions, ...  
1, 1.5, 1+i, 1+i+j+k, 1+e0+e1+e2+e01+e02+e12+e012, ...
## Undefined
basically everything else; strings, character, class, functions, modules
## Empty
basically, None, void, [], {}, anything which is empty.  
"Empty" is always mutable, since something defined empty can have a value or element assigned to it at a later point during execution.

# Variable declaration
    <variable-name>
Whenever a variable is declared, it, by default is assigned an empty type. Writing explicitly, <variable-name\> <- Empty is also a valid implementation. 
# Varaible assignment
    <variable-name> <- <value>
# Varaible Scope
Same as the variable scopes in other languages

# Operators
## Addition
    +
## Subtraction
    -
## Multiplication
    *
## Division
### Float Division
    /
### Integer Division
    
## Assingment
    <-
## Return
    ->

# Function Def
```
<function-name> <- {
    [parameter-list]
    <function-body>
    -> [return-parameters]
}
```

# Class Def
```
<class-name> <- {
    [class-varibales]
    <class-name> <- {
        [instance-variables]
        <contructor-body>
    }
    <function-name> <- {
        [parameter-list]
        <function-body>
        -> [return-parameters]
    }
}
```