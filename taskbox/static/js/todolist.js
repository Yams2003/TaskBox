function displayProgress(id, progress) {
  // Why was I sending a GET request every time I needed to make the progress bar visible/invisible? I really don't know.
  /*$.ajax({
      type: "GET",
      url: "/progress/"+id,
      contentType: "text/plain",
      dataType: 'json' 
    });*/

  const progressBar = document.getElementById("progress"+id);
  
  // Toggles progress bar visibility
  if (progressBar.style.display === "none") {
    progressBar.style.display = "table-row";

    // Sets the bar element to correspond with the percentage of progress
    document.getElementById("progressBar"+id).style.width = progress + '%';

  } else {
    progressBar.style.display = "none";
  }
}