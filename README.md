# stringCalculator

stringCalculator is my solution in response to 7shifts coding exercise for a developer intern position in Saskatoon. 

The stringCalculator will take a string of numbers seperated by a comma and will display the sum of those numbers. 
The calculator supports a custom delimiter where in the beginning of the string
will now contain a small control code that lets you set a custom delimiter in the format
“//[delimiter]\\[delimiter separated numbers].

Example: “//;\n1;3;4” - Result: 8

In the above you can see that following the double forward slash we set a
semicolon, followed by a new line. We then use that delimiter to split our
numbers.

Other examples

“//$\n1$2$3” - Result: 6

“//@\n2@3@8” - Result: 13

## Built With
* Python

## Installation
Please download the code and run in your own machine


## Usage

```python
from stringCalculator import Add

# returns 8
test = Add("1,2,5")

# returns 4
test = Add("1\n,2,1")
```

Numbers larger than 1000 are not supported and will be ignored. The calculator also allows multiple delimiters of arbitrary length.

```python
from stringCalculator import Add

# returns 19
test = Add("//$$,@@@,bbb,???\n5???2bbb1$$9@@@2")

# Please remove numbers [-3, -4]
test = Add("1,-3,-4")
```

## Contact

Raphael Pinto - raphael.pinto@usask.ca

Project Link: https://github.com/Raff29/stringCalculator
