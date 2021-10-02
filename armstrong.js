function power(x, y)
{
    if( y == 0)
        return 1;
    if (y % 2 == 0)
        return power(x, parseInt(y / 2, 10)) *
               power(x, parseInt(y / 2, 10));
                  
    return x * power(x, parseInt(y / 2, 10)) *
               power(x, parseInt(y / 2, 10));
}

// Function to calculate
// order of the number
function order(x)
{
    let n = 0;
    while (x != 0)
    {
        n++;
        x = parseInt(x / 10, 10);
    }
    return n;
}

// Function to check whether the
// given number is Armstrong number
// or not
function isArmstrong(x)
{
       
    // Calling order function
    let n = order(x);
    let temp = x, sum = 0;
    while (temp != 0)
    {
        let r = temp % 10;
        sum = sum + power(r, n);
        temp = parseInt(temp / 10, 10);
    }

    // If satisfies Armstrong condition
    return (sum == x);
}
 
let x = 153;
if(isArmstrong(x))
{
    document.write("True" + "</br>");
}
else{
    document.write("False" + "</br>");
}
x = 1253;
if(isArmstrong(x))
{
    document.write("True");
}
else{
    document.write("False");
}

