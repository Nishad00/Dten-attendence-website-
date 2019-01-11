$(document).ready(function()
{
   $("#addsubjectdiv").hide();
   $("#adddivisiondiv").hide();
   $("#addeddivisiondiv").hide();
   $("#batchoption").hide();     
   $("#tpracticales").hide();     
  

   $( "#addsubjectbutton" ).click(function() 
   {
    $("#addsubjectdiv").show(1000);
    });
    $( "#cancelsubeject").click(function() 
    {
     $("#addsubjectdiv").hide(1000);
     });
 
     $( "#adddivbutton" ).click(function() 
     {
      $("#adddivisiondiv").show(1000);
      });
      $( "#canceldiv").click(function() 
      {
       $("#adddivisiondiv").hide(1000);
       });
  
       $( "#divadded" ).click(function() 
       {
        $("#addeddivisiondiv").show(1000);
        $("#adddivisiondiv").hide(1000);
        $("#adddivbutton").hide(1000);
         });
        
        $( "#deletediv").click(function() 
        {
         $("#addeddivisiondiv").hide(1000);
         $("#adddivbutton").show(1000);
        });
        
   $("#type").change(function() 
  {
      if(this.value == "theory") {
        $("#batchoption").hide(1000);     
        $("#tpracticales").hide(1000); 
        $("#lectureinput").val("");          
        $("#tlectures").show(1000);
        $("#practicalinput").val(1);     
      }
      else{
        $("#tlectures").hide(1000);
        $("#batchoption").show(1000);     
        $("#practicalinput").val("");     
        $("#tpracticales").show(1000);     
        $("#lectureinput").val(1);     
             }
   });

       
});  