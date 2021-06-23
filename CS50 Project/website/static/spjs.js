$(document).ready(function() {
  
    // checks how many checkboxes are on page (I plan to use this for different pages of a site, so having this to check length makes it easier to duplicate without having to change to many details)
    var count = 0;
    var checked = 0;
    function countBoxes() { 
      count = $("input[type='checkbox']").length;
      console.log(count);
    }
    
    countBoxes();
    $(":checkbox").click(countBoxes);
    
   //Check Counts
    
    function countChecked() {
      checked = $("input:checked").length;
      
      var percentage = parseInt(((checked / count) * 100),10);
      $(".progressbar-bar").progressbar({
              value: percentage
          });
      $(".percentPacked").text(percentage + "% Packed");
    }
    
    countChecked();
    $(":checkbox").click(countChecked);
  });
  
  