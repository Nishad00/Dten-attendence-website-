$(document).ready(function()
{
   $("#attedancediv").show();
   $("#editattenddiv").hide();
       

   $( "#editattendbutton").click(function() 
   {
    $("#attedancediv").hide(1000);
    $("#editattenddiv").show(1000);
    });


    $( "#canceleditdiv").click(function() 
    {
     $("#editattenddiv").hide(1000);
     $("#attedancediv").show(1000);
    });

       
});  